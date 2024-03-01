from django.db import models
from django.conf import settings
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.files import File
from django.core import validators

from django_celery_beat.models import PeriodicTask, IntervalSchedule
from django_celery_beat.utils import make_aware

from wagtail.contrib.settings.models import BaseGenericSetting
from wagtail.admin.panels import (
    FieldPanel,
    FieldRowPanel,
    MultiFieldPanel,
)

import os

from wagtail_panels.panels import AnchorTag, ButtonPanel, DownloadButton

from .settings import DUMP_LOCATION, BACKUP_STORAGE

def get_import_file_path(instance, filename):
    return os.path.join(DUMP_LOCATION, "import", filename)

# Create your models here.

class DumpedDatabaseObject:
    def __init__(self, connection_name: str, tables: list[str] = None, location: str = None):
        self.connection_name:    str       = connection_name
        self._tables:            list[str] = tables
        self.location:           str       = location

    @property
    def database(self) -> str:
        return settings.DATABASES[self.connection_name]["NAME"]
    
    @property
    def tables(self) -> list[str]:
        if self._tables is None:
            return []
        return self._tables
    
    @property
    def filename(self) -> str:
        if self.location is None:
            raise ValueError("Location cannot be None to get the filename.")
        return os.path.basename(self.location)
    
    @property
    def filesize(self) -> int:
        if self.location is None:
            raise ValueError("Location cannot be None to get the filesize.")
        return BACKUP_STORAGE.size(self.location)
    
    @property
    def file(self) -> File:
        if self.location is None:
            raise ValueError("Location cannot be None to get the file.")
        return BACKUP_STORAGE.open(self.location)
    
class DumpedDatabaseManager(models.Manager):
    def log_dump(self, dump: DumpedDatabaseObject, dump_type, file=None) -> "DatabaseDump":
        return super().create(
            settings_database = dump.connection_name,
            database = dump.database,
            tables = dump.tables,
            file = file or dump.location,
            type = dump_type,
        )
    


class DatabaseDumpSchedule(BaseGenericSetting):
    class INTERVALS(models.TextChoices):
        HOURS = "hours", _("Hour(s)")
        DAYS = "days", _("Day(s)")
        WEEKS = "weeks", _("Week(s)")
        MONTHS = "months", _("Month(s)")
        YEARS = "years", _("Year(s)") 

    start_on = models.DateTimeField(
        verbose_name=_("Start On"),
        help_text=_("The date and time to start the schedule."),
        null=True,
        blank=False,
    )

    period = models.PositiveIntegerField(
        verbose_name=_("Period"),
        null=False,
        blank=False,
        default=1,
        #min_value=1,
        #max_value=365,
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(365),
        ],
    )

    interval = models.CharField(
        max_length=255,
        choices=INTERVALS.choices,
        verbose_name=_("Interval"),
        help_text=_("The interval to run the schedule."),
        null=True,
        blank=False,
    )

    task = models.ForeignKey(
        PeriodicTask,
        on_delete=models.CASCADE,
        verbose_name=_("Task"),
        help_text=_("The task to run."),
        null=True,
        blank=False,
    )

    panels = [
        FieldPanel("start_on"),
        FieldPanel("interval"),
    ]

    class Meta:
        verbose_name = _("Database Dump Schedule")
        verbose_name_plural = _("Database Dump Schedules")
        default_permissions = ()
        permissions = (
            ("schedule_backup", _("Schedule Backup")),
        )

    def __str__(self):
        if self.interval is None:
            return f"None ({self.pk})"
        
        return f"{self.interval.upper()} ({self.pk})"
    
    @property
    def next_backup(self):
        if self.task.last_run_at is None:
            return self.task.start_time
        
        if not self.interval:
            return None
        
        if self.interval == self.INTERVALS.HOURS:
            return self.task.last_run_at + timezone.timedelta(hours=(1 * self.period))

        elif self.interval == self.INTERVALS.DAYS:
            return self.task.last_run_at + timezone.timedelta(days=(1 * self.period))
        
        elif self.interval == self.INTERVALS.WEEKS:
            return self.task.last_run_at + timezone.timedelta(days=(7 * self.period))
        
        elif self.interval == self.INTERVALS.MONTHS:
            return self.task.last_run_at + timezone.timedelta(days=(30 * self.period))
        
        elif self.interval == self.INTERVALS.YEARS:
            return self.task.last_run_at + timezone.timedelta(days=(365 * self.period))

        else:
            raise ValueError(f"Interval {self.interval} is not valid.")
        
    def save(self, *args, **kwargs):
        if self.interval:
            if self.interval == self.INTERVALS.HOURS:
                interval, _ = IntervalSchedule.objects.get_or_create(
                    every=(1 * self.period),
                    period=IntervalSchedule.HOURS,
                )
            elif self.interval == self.INTERVALS.DAYS:
                interval, _ = IntervalSchedule.objects.get_or_create(
                    every=(1 * self.period),
                    period=IntervalSchedule.DAYS,
                )
            elif self.interval == self.INTERVALS.WEEKS:
                interval, _ = IntervalSchedule.objects.get_or_create(
                    every=(7 * self.period),
                    period=IntervalSchedule.DAYS,
                )
            elif self.interval == self.INTERVALS.MONTHS:
                interval, _ = IntervalSchedule.objects.get_or_create(
                    every=(30 * self.period),
                    period=IntervalSchedule.DAYS,
                )
            elif self.interval == self.INTERVALS.YEARS:
                interval, _ = IntervalSchedule.objects.get_or_create(
                    every=(365 * self.period),
                    period=IntervalSchedule.DAYS,
                )

            if getattr(self, "task_id"):
                self.task.interval = interval
                self.task.name = f"Database Dump ({self.interval.upper()})"
                self.task.task = "import_export.backup_all_databases"
                self.task.save()
            else:
                self.task, _ = PeriodicTask.objects.get_or_create(
                    interval = interval,
                    name = f"Database Dump ({self.interval.upper()})",
                    task = "import_export.backup_all_databases",
                )
            
            if self.start_on is not None and self.start_on != self.task.start_time:
                self.task.start_time = make_aware(self.start_on)
                self.task.save()
                
        else:
            if getattr(self, "task_id"):
                self.task.delete()
                self.task = None
        
        super().save(*args, **kwargs)


class DatabaseDump(models.Model):
    class TYPES(models.TextChoices):
        IMPORT = "import", _("Import")
        EXPORT = "export", _("Export")
        BACKUP = "backup", _("Backup")

    settings_database = models.CharField(
        max_length=255,
        choices=[(key, key.upper()) for key in settings.DATABASES.keys()],
        verbose_name=_("Settings Key"),
        help_text=_("The database as it appears in Django Settings."),
        null=False,
        blank=False,
    )
    database = models.CharField(
        max_length=255,
        verbose_name=_("Database Name"),
        help_text=_("The name of the database."),
    )
    tables = models.JSONField(
        verbose_name=_("Tables"),
        help_text=_("The tables that were dumped."),
        default=list,
    )
    type = models.CharField(
        max_length=255, 
        choices=TYPES.choices,
        verbose_name=_("Type"),
        help_text=_("The type of dump."),
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created"),
        help_text=_("The date and time the dump was created."),
    )
    file = models.FileField(
        verbose_name=_("File"),
        help_text=_("The file containing the dump."),
        upload_to=get_import_file_path,
        max_length=512,
        storage=BACKUP_STORAGE,
    )

    panels = [
        FieldRowPanel([
            FieldPanel("settings_database"),
            FieldPanel("database", read_only=True),
        ]),
        FieldPanel("type", read_only=True),
        MultiFieldPanel([
            FieldPanel("file", read_only=True),
            ButtonPanel([
                DownloadButton(
                    _("Download File"),
                    "file",
                    classname="button",
                ),
                AnchorTag(
                    _("Recover"),
                    lambda request, instance: \
                        reverse_lazy("import_export:confirm_recover", kwargs={"pk": instance.pk}),
                    classname="button no",
                    HIDE_ON_CREATE=True,
                )
            ]),
        ], heading=_("File")),

        FieldPanel("created", read_only=True),
        FieldPanel("tables", read_only=True),
    ]

    objects: DumpedDatabaseManager = DumpedDatabaseManager()

    class Meta:
        verbose_name = _("Database Dump")
        verbose_name_plural = _("Database Dumps")
        ordering = ["-created"]

    def __str__(self):
        return f"{self.database} ({self.type.upper()}/{self.pk})"
    
    @property
    def filesize(self) -> str:
        size = self.file.size
        if size < 1024:
            return f"{size} B"
        elif size < 1024**2:
            return f"{size/1024:.2f} KB"
        elif size < 1024**3:
            return f"{size/1024**2:.2f} MB"
        elif size < 1024**4:
            return f"{size/1024**3:.2f} GB"
        else:
            return f"{size/1024**4:.2f} TB"
    
    @property
    def dump(self) -> DumpedDatabaseObject:
        return DumpedDatabaseObject(
            connection_name = self.settings_database,
            tables = self.tables,
            location = self.file.path,
        )
    
    @dump.setter
    def dump(self, value: DumpedDatabaseObject):
        self.settings_database = value.connection_name
        self.database = value.database
        self.tables = value.tables
        self.file = value.location



class PermissionOnlyModel(models.Model):
    class Meta:
        verbose_name = _("Import/Export Permission Model")
        verbose_name_plural = _("Import/Export Permission Models")

        managed = False
        default_permissions = ()
        permissions = (
            ("access_import_export_admin", _("Access Import/Export Admin")),
            ("import_database", _("Import Database")),
            ("export_database", _("Export Database")),
            ("download_dump", _("Download Dump")),
        )
