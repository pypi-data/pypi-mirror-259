try:
    from celery import shared_task
    from maintenance import modes
    from django.conf import settings
    import logging

    logger = logging.getLogger("import_export")

    @shared_task(name="import_export.backup_all_databases")
    def backup_all_databases():
        from . import util
        from .models import DatabaseDump
        from .wagtail_hooks import IMPORT_EXPORT_MAINTENANCE_MODE_KEY

        with modes.maintain(IMPORT_EXPORT_MAINTENANCE_MODE_KEY, lock_cache=True):

            databases = settings.DATABASES.keys()
            for database_name in databases:

                try:
                    dump = util.create_database_dump(
                        connection_name=database_name, 
                        skip_checks=True, 
                        path="maintenance/backups"
                    )
                except:
                    logger.exception("Failed to create database dump for database %s", database_name)
                    continue

                DatabaseDump.objects.log_dump(dump, DatabaseDump.TYPES.BACKUP)

except:
    pass