from django.db import DEFAULT_DB_ALIAS, connections
from django.urls import reverse, path, include
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponseRedirect, JsonResponse, StreamingHttpResponse, HttpResponseForbidden
from django.conf import settings
from django.utils.html import format_html
from django.templatetags.static import static
from django.contrib.auth.models import Permission
from django.contrib import messages
from django.views import View

from wagtail.admin.menu import (
    SubmenuMenuItem,
    MenuItem,
    Menu,
)
from wagtail.admin.views.generic import WagtailAdminTemplateMixin
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.snippets.models import register_snippet
from wagtail import hooks

from maintenance import modes, keys
from typing import Any
import logging

from .models import DatabaseDumpSchedule
from . import util, crypto
from .forms import (
    DatabaseDumpScheduleForm,
    DatabaseDumpForm,
)
from .models import (
    DatabaseDump,
)



logger = logging.getLogger("import_export")



def file_iterator(file, chunk_size=8192):
    while True:
        chunk = file.read(chunk_size)
        if not chunk:
            break
        yield chunk


def _err(msg, status=400):
    return JsonResponse({
        'error': msg,
    }, status=status)


class ImportExportMenuItemMixin:
    permissions = None
    
    def __init__(self, *args, permissions=None, **kwargs):
        super().__init__(*args, **kwargs)

        if permissions and not isinstance(permissions, (list, tuple)):
            permissions = [permissions]

        if permissions and self.permissions:
            permissions = list(set(permissions + self.permissions))

        self.permissions = permissions

    def is_shown(self, request):
        if not self.permissions:
            return super().is_shown(request)
        
        return super().is_shown(request) and request.user.has_perms(self.permissions)

class ImportExportSubmenuMenuItem(ImportExportMenuItemMixin, SubmenuMenuItem):
    permissions = [
        "import_export.access_import_export_admin",
    ]

class ImportExportMenuItem(ImportExportMenuItemMixin, MenuItem):
    permissions = [
        "import_export.access_import_export_admin",
    ]


class PermissionViewMixin:
    permissions = []

    def dispatch(self, request, *args, **kwargs):
        if self.permissions and not request.user.has_perms(self.permissions):
            return HttpResponseForbidden()
        
        return super().dispatch(request, *args, **kwargs)

class BackupAdminView(PermissionViewMixin, WagtailAdminTemplateMixin, View):
    page_title = _("Backup")
    page_subtitle = _("Schedule a backup of the database.")
    template_name = 'import_export/task.html'
    header_icon = 'time'
    permissions = [
        'import_export.access_import_export_admin',
        'import_export.import_database',
    ]

    def dispatch(self, request, *args, **kwargs):
        self.schedule = DatabaseDumpSchedule.load(request_or_site=request)

        if request.method == 'POST':
            self.form = DatabaseDumpScheduleForm(
                request.POST, 
                for_user=request.user,
                instance=self.schedule,
            )
        else:
            self.form = DatabaseDumpScheduleForm(
                for_user=request.user,
                instance=self.schedule,
            )

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['task'] = self.schedule
        context['form'] = self.form
        return context
    
    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())
    
    def post(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseForbidden()
        
        if self.form.is_valid():
            dump_schedule = self.form.save()
            messages.success(request, _("Backup schedule updated."))
            return HttpResponseRedirect(reverse('import_export:backup'))
        
        return self.get(request, *args, **kwargs)

class ImportAdminView(PermissionViewMixin, WagtailAdminTemplateMixin, View):
    page_title = _("Import")
    page_subtitle = _("Import a database dump.")
    template_name = 'import_export/import.html'
    header_icon = 'download'
    permissions = [
        'import_export.access_import_export_admin',
        'import_export.import_database',
    ]

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseForbidden()
        
        database = request.GET.get('database', DEFAULT_DB_ALIAS)
        if database not in settings.DATABASES:
            database = DEFAULT_DB_ALIAS
    
        if request.method == 'POST':
        
            file = request.FILES.get('file')
            if not file:
                return _err("No file uploaded.")
            
            try:
                if not crypto.is_valid_dump(file, fail_silently=False):
                    return _err("Invalid zip file uploaded.")
            except (crypto.InvalidDumpException, crypto.CryptoFailedException) as e:
                return _err(str(e))

            dump = util.DumpedDatabaseObject(
                connection_name=database,
            )

            db_dump = DatabaseDump.objects.log_dump(
                dump=dump,
                dump_type=DatabaseDump.TYPES.IMPORT,
                file=file,
            )

            try:
                file.close()
            except:
                pass
    
            return JsonResponse({
                'filename': db_dump.file.name,
                'next_url': reverse('import_export:confirm_import', kwargs={'pk': db_dump.id}),
            })
        
        return _err("Invalid request method.", status=405)


class ExportAdminView(PermissionViewMixin, WagtailAdminTemplateMixin, View):
    page_title = _("Export")
    page_subtitle = _("Export a database dump.")
    template_name = 'import_export/export.html'
    header_icon = 'upload'
    permissions = [
        'import_export.access_import_export_admin',
        'import_export.export_database',
    ]

    def dispatch(self, request, *args, **kwargs):
        form_kwargs = {}
        if self.request.method == 'POST':
            form_kwargs["request"] = self.request

        self.selected_database_key = self.request.GET.get('database', DEFAULT_DB_ALIAS)
        if self.selected_database_key not in settings.DATABASES:
            self.selected_database_key = DEFAULT_DB_ALIAS

        self.selected_database = settings.DATABASES.get(self.selected_database_key)
        self.tables = util.get_tables(connection=connections[self.selected_database_key])
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        with modes.maintain(IMPORT_EXPORT_MAINTENANCE_MODE_KEY, lock_cache=True):

            dump = util.create_database_dump(
                self.selected_database_key,
                self.tables,
            )

            db_dump = DatabaseDump.objects.log_dump(dump, DatabaseDump.TYPES.EXPORT)

        return JsonResponse({
            'filename': db_dump.file.name,
            'url': reverse('import_export:download_file', kwargs={'pk': db_dump.id}),
            'recover_url': reverse('import_export:confirm_recover', kwargs={'pk': db_dump.id}),
            'edit_url': reverse('import_export_dumps:edit', kwargs={'pk': db_dump.id}),
            'tables': self.tables,
            'database': db_dump.database.upper(),
            'filesize': db_dump.filesize,
            'created': db_dump.created.strftime("%d/%m/%Y %H:%M:%S"),
        })

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        if len(settings.DATABASES) > 1:
            databases = [
                (alias, settings.DATABASES[alias]['NAME'])
                for alias in settings.DATABASES
            ]
            databases.sort(key=lambda x: x[1])

            context['databases'] = databases

        dumps = DatabaseDump.objects\
            .filter(type=DatabaseDump.TYPES.EXPORT)\
            .order_by('-created')[:5]
        context['dumps'] = dumps

        return context


class BaseImportConfirmAdminView(PermissionViewMixin, WagtailAdminTemplateMixin, View):
    ACTION = _('import')
    TYPE = DatabaseDump.TYPES.IMPORT
    page_title = _("Confirm Import")
    page_subtitle = _("Confirm the import of a database dump.")
    template_name = 'import_export/import_confirm.html'
    header_icon = 'warning'
    permissions = [
        'import_export.access_import_export_admin',
        'import_export.import_database',
    ]

    def dispatch(self, request, *args, **kwargs):
        type_kwargs = {}
        if self.TYPE is not None:
            type_kwargs['type'] = self.TYPE

        self.dump = get_object_or_404(DatabaseDump, pk=kwargs['pk'], **type_kwargs)
        self.dump_password_form = DatabaseDumpForm(
            user=request.user,
            data=request.POST if request.method == 'POST' else None,
        )

        return super().dispatch(request, *args, **kwargs)
    
    def get_view_icon(self):
        return "warning"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['dump'] = self.dump
        zf = util.open_dump(self.dump.file.file)
        context['file_count'] = len(zf.infolist())
        return context
    
    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):

        if not self.dump_password_form.is_valid():
            return _err(str(_("Invalid password.")))
        
        with modes.maintain(IMPORT_EXPORT_MAINTENANCE_MODE_KEY, lock_cache=True):
            try:
                util.import_database_dump(
                    file=self.dump.file.file,
                    connection_name=self.dump.settings_database,
                )

                new_dump = DatabaseDump(
                    settings_database=self.dump.settings_database,
                    database=self.dump.database,
                    tables=self.dump.tables,
                    type=DatabaseDump.TYPES.EXPORT,
                    file=self.dump.file.path,
                )

                self.dump.file.close()

                try:
                    self.dump.delete()
                except Exception as e:
                    logger.error(f"Error deleting dump: {e}")

                new_dump.save()

                return JsonResponse({
                    'next_url': reverse('import_export:import'),
                })
        
            except crypto.CryptoFailedException as e:
                return _err(str(_("An error occurred during the import process.")))

            except util.RestorationFailedException as e:
                return _err(str(_("An error occurred while restoring the database.")))

            except util.DumpFailedException as e:
                return _err(str(_("An error occurred while dumping the database.")))

            except util.MigrateFailedException as e:
                return _err(str(_("An error occurred while migrating to the new database.")))

            except:
                return _err(str(_("An error occurred during the import process.")))
        

class ImportConfirmAdminView(BaseImportConfirmAdminView):
    ACTION = _('import')
    ACTION_PLURAL = _('import')
    NAMESPACE = 'confirm_import'
    TYPE = DatabaseDump.TYPES.IMPORT
    page_title = _("Confirm Import")
    page_subtitle = _("Confirm the import of a database dump.")
    template_name = 'import_export/import_confirm.html'

class RecoverConfirmAdminView(BaseImportConfirmAdminView):
    ACTION = _('recover')
    ACTION_PLURAL = _('recover')
    NAMESPACE = 'confirm_recover'
    TYPE = None
    page_title = _("Confirm Recover")
    page_subtitle = _("Confirm the recovery of a database dump.")
    template_name = 'import_export/import_confirm.html'


def download_file(request, pk):
    if not request.user.has_perms([
        "import_export.access_import_export_admin",
        "import_export.download_dump",
    ]):
        return HttpResponseForbidden()

    dump = get_object_or_404(DatabaseDump, pk=pk)

    for hook in hooks.get_hooks('import_export.download_file'):
        hook(dump)

    response = StreamingHttpResponse(file_iterator(dump.file.file))
    response['Content-Length'] = dump.file.size
    response['Content-Disposition'] = f'attachment; filename="{dump.file.name}"'
    return response


class DatabaseDumpSnippetViewSet(SnippetViewSet):
    model = DatabaseDump
    icon = 'tasks'
    menu_order = 1000
    menu_label = _('Database Dumps')
    menu_icon = 'list-ul'
    list_display = ('database', 'type', 'created', 'filesize', 'file')
    list_filter = ('database', 'type')
    url_namespace = 'import_export_dumps'

register_snippet(DatabaseDump, DatabaseDumpSnippetViewSet)


class PriorityStatusClass(keys.Status):
    def maintaining(self):
        if self.request is None:
            return self.value
        
        if not self.value:
            return False
        
        invalid_path = any([
            self.request.path.startswith(path) 
            for path in [
                reverse("import_export_dumps:list"),
                reverse("import_export:import"),
                reverse("import_export:export"),
            ]
        ])

        return self.value and not invalid_path


class ImportExportKey(keys.Key):
    status_class = PriorityStatusClass


IMPORT_EXPORT_MAINTENANCE_MODE_KEY = ImportExportKey(
    "IMPORT_EXPORT.CACHE", 
    label=_("Import/Export Maintenance Mode"), 
    help_text=_("This will be automatically triggered when importing/exporting."), 
    timeout=modes.DAY,
)


@hooks.register('maintenance.register_key')
def register_maintenance_mode_key():
    return IMPORT_EXPORT_MAINTENANCE_MODE_KEY


@hooks.register('insert_global_admin_js')
def global_admin_js():
    return format_html(
        '<script src="{}"></script>',
        static('import_export/htmx.min.js')
    )


import_export_menu = Menu(
    register_hook_name="register_import_export_menu",
    construct_hook_name="construct_import_export_menu",
)

@hooks.register("register_import_export_menu")
def register_dump_menu_item(*args, **kwargs):
    return DatabaseDumpSnippetViewSet().get_menu_item(*args, **kwargs)

@hooks.register("register_import_export_menu")
def register_backup_menu_item():
    return ImportExportMenuItem(
        _("Backup"),
        name="backup",
        icon_name="time",
        url=reverse("import_export:backup"),
        order=100,
        permissions=[
            "import_export.access_import_export_admin",
            "import_export.schedule_backup",
        ]
    )

@hooks.register("register_import_export_menu")
def register_import_menu_item():
    return ImportExportMenuItem(
        _("Import"),
        name="import",
        icon_name="download",
        url=reverse("import_export:import"),
        order=200,
        permissions=[
            "import_export.access_import_export_admin",
            "import_export.import_database",
        ]
    )

@hooks.register("register_import_export_menu")
def register_export_menu_item():
    return ImportExportMenuItem(
        _("Export"),
        name="export",
        icon_name="upload",
        url=reverse("import_export:export"),
        order=300,
        permissions=[
            "import_export.access_import_export_admin",
            "import_export.export_database",
        ]
    )

@hooks.register('register_maintenance_menu_item')
def register_maintenance_menu_item():
    return ImportExportSubmenuMenuItem(
        _("Import/Export"),
        name="import_export",
        icon_name="database-check",
        menu=import_export_menu,
        order=-1,
        permissions=[
            "import_export.access_import_export_admin",
        ]
    )

urlpatterns = [
    path('import/', ImportAdminView.as_view(), name="import"),
    path('export/', ExportAdminView.as_view(), name="export"),
    path('backup/', BackupAdminView.as_view(), name="backup"),
    path('import/confirm/<int:pk>/', ImportConfirmAdminView.as_view(), name="confirm_import"),
    path('recover/confirm/<int:pk>/', RecoverConfirmAdminView.as_view(), name="confirm_recover"),
    path('download/<int:pk>/', download_file, name="download_file"),
]

@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        path('import-export/', include((urlpatterns, 'import_export'), namespace='import_export'), name='import_export'),
    ]

@hooks.register('register_permissions')
def register_permissions():
    return Permission.objects.filter(
        content_type__app_label='import_export',
        codename__in=[
            "access_import_export_admin",
            "schedule_backup",
            "import_database",
            "export_database",
            "download_dump",
        ]
    )


