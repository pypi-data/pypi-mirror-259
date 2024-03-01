import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage

_MYSQL_DUMP_CONFIG_LOCATION  = getattr(settings, "MYSQL_DUMP_CONFIG_LOCATION")
MYSQL_DUMP_CONFIG_LOCATION  = os.path.normpath(_MYSQL_DUMP_CONFIG_LOCATION)

_MYSQL_DUMP_BINARY           = getattr(settings, "MYSQL_DUMP_BINARY", "mysqldump")
MYSQL_DUMP_BINARY           = os.path.normpath(_MYSQL_DUMP_BINARY)

_DUMP_LOCATION         = getattr(settings, "DUMP_LOCATION", "import_export")
DUMP_LOCATION         = os.path.normpath(_DUMP_LOCATION)

DUMP_CHUNK_SIZE       = getattr(settings, "DUMP_CHUNK_SIZE", 50 * 1024 * 1024)

DUMP_GET_TABLES        = getattr(settings, "DUMP_GET_TABLES", "import_export.funcs.mysql_get_tables")
DUMP_EXPORT_TABLE   = getattr(settings, "DUMP_EXPORT_TABLE", "import_export.funcs.mysql_dump_table")
DUMP_IMPORT_TABLE   = getattr(settings, "DUMP_IMPORT_TABLE", "import_export.funcs.mysql_exec_import_table")
DUMP_MUST_NOT_ENCRYPT = getattr(settings, "DUMP_MUST_NOT_ENCRYPT", True)

BACKUP_ROOT = getattr(settings, "BACKUP_ROOT", os.path.join(settings.BASE_DIR, 'backups'))
BACKUP_STORAGE = getattr(settings, "BACKUP_STORAGE", FileSystemStorage(location=BACKUP_ROOT))

EXCLUDED_EXPORT_TABLES = getattr(settings, "DUMP_EXCLUDED_EXPORT_TABLES", [
    "import_export_*",
    "django_*",
    "auth_*",
    # "accounts_*",
    "wagtailusers_*",
    "wagtailcore_groupapprovaltask",
    "wagtailcore_collectionviewrestriction",
    "wagtailcore_collectionviewrestriction_groups",
    "wagtailcore_groupapprovaltask",
    "wagtailcore_groupapprovaltask_groups",
    "wagtailcore_groupcollectionpermission",
    "wagtailcore_grouppagepermission",
    "wagtailcore_pageviewrestriction_groups",
    "wagtailcore_pageviewrestriction",
] if DUMP_MUST_NOT_ENCRYPT else []) # When encrypting; export everything
