from django.db import connections, DEFAULT_DB_ALIAS
from django.conf import settings
from django.utils import timezone
from django.utils.module_loading import import_string
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from wagtail import hooks

import os
import zipfile

from typing import IO, Iterable

import logging

from .funcs import DumpedTable
from .models import DumpedDatabaseObject
from .settings import (
    DUMP_LOCATION,
    DUMP_GET_TABLES,
    DUMP_EXPORT_TABLE,
    DUMP_IMPORT_TABLE,
    EXCLUDED_EXPORT_TABLES,
    DUMP_MUST_NOT_ENCRYPT,
    BACKUP_STORAGE,
)

from . import crypto, multi_hooks

    
class DumpFailedException(Exception):
    pass

class MigrateFailedException(Exception):
    pass

class RestorationFailedException(Exception):
    pass

import_multi_hooks = multi_hooks.MultiHook("database_import", prefix="import_export.")
export_multi_hooks = multi_hooks.MultiHook("database_export", prefix="import_export.")

logger = logging.getLogger("import_export")


def table_is_allowed(table: str) -> bool:
    """Check if a table is excluded."""
    for pattern in EXCLUDED_EXPORT_TABLES:
        if pattern.endswith("*"):
            if table.startswith(pattern[:-1]):
                return False
        else:
            if table == pattern:
                return False
    return True


def get_tables(connection, skip_checks=False) -> list[str]:
    """Get a list of all tables in the database."""
    _get_tables = import_string(DUMP_GET_TABLES)
    tables = []
    for table in _get_tables(connection):
        if table_is_allowed(table) or skip_checks:
            tables.append(table)
    return tables


def get_database_name(database_name: str=DEFAULT_DB_ALIAS) -> str:
    """Get the name of the database."""
    return settings.DATABASES[database_name]["NAME"]


def _execute_dump_tables(database_name: str=DEFAULT_DB_ALIAS, tables: list[str]=None) -> Iterable[DumpedTable]:
    """Execute mysqldump and return an iterable of DumpedTable objects."""
    
    if tables is None:
        raise ValueError("Tables cannot be None.")
    
    _dump_table = import_string(DUMP_EXPORT_TABLE)

    for table in tables:
        yield _dump_table(database_name, table)
    

def open_dump(file: File, key: bytes=None, use_md5: bool=True) -> zipfile.ZipFile:
    """
        Open a database dump.
    """

    new = crypto.aes_decrypt_file(file, key=key, use_md5=use_md5)
    
    return zipfile.ZipFile(new, "r")

def create_database_dump(connection_name: str=DEFAULT_DB_ALIAS, tables=[], skip_checks=False, path="exports") -> DumpedDatabaseObject:
    """
        Execute mysqldump and return the media file location.
    """

    temp_zipfile = NamedTemporaryFile(suffix=".zip")

    try:
        database_name = get_database_name(connection_name)
    except KeyError:
        raise ValueError(f"Database {connection_name} does not exist.")

    if not tables:
        tables = get_tables(connections[connection_name], skip_checks=skip_checks)

    if not skip_checks:
        export_multi_hooks.before(connection_name=connection_name, tables=tables)

    with zipfile.ZipFile(temp_zipfile, "w") as zip_file:
        zip_file.comment = f"Database dump of {database_name} at {timezone.now().strftime('%Y-%m-%d %H:%M:%S')}".encode()
        for tmp in _execute_dump_tables(connection_name, tables):

            if not skip_checks:
                export_multi_hooks.during(connection_name=connection_name, table=tmp.tablename)

            filename = f"{database_name}.{tmp.tablename}.sql"
            zip_file.write(tmp.tempfile.name, arcname=filename)
            tmp.tempfile.close()

    if DUMP_MUST_NOT_ENCRYPT:
        media_filename = f"{database_name}.{timezone.now().strftime('%Y-%m-%d_%H-%M-%S')}.zip"
    else:
        media_filename = f"{timezone.now().strftime('%Y-%m-%d_%H-%M-%S')}.backup"

    media_file_path = os.path.join(DUMP_LOCATION, path, media_filename)
    media_file_path = os.path.normpath(media_file_path)

    file = File(temp_zipfile, name=media_file_path)
    file.seek(0)

    f = crypto.aes_encrypt_file(file)

    media_filename = BACKUP_STORAGE.save(media_file_path, f)
    file.close()
    f.close()

    obj = DumpedDatabaseObject(connection_name, tables, media_filename)

    if not skip_checks:
        export_multi_hooks.after(dump=obj, connection_name=connection_name, tables=tables)

    return obj

def import_database_table(connection_name: str=DEFAULT_DB_ALIAS, file: IO[bytes]=None) -> None:
    """
        Execute mysql on a file and import the database.
    """

    if file is None:
        raise ValueError("File cannot be None.")

    _import_table = import_string(DUMP_IMPORT_TABLE)
    _import_table(connection_name, file)


def import_database_dump(file: File, connection_name: str=DEFAULT_DB_ALIAS, recovery_db: bool = True, restoration_point: DumpedDatabaseObject = None) -> DumpedDatabaseObject:
    """
        Execute mysql on a file and import the database.
    """

    if recovery_db:
        restoration_point = create_database_dump(connection_name, skip_checks=True, path="maintenance/restore")
    else:
        restoration_point = None

    try:
        zip_file = crypto.aes_decrypt_file(file)
    except Exception as e:
        zip_file.close()
        raise crypto.CryptoFailedException(e) from e

    zip_file = zipfile.ZipFile(zip_file, "r")

    import_multi_hooks.before(zip_file=zip_file, connection_name=connection_name)

    for filename in zip_file.namelist():
        file = zip_file.open(filename)
        try:
            import_multi_hooks.during(file=file, connection_name=connection_name)

            import_database_table(connection_name, file)
        except Exception as e:
            if restoration_point is not None:
                try:
                    _restore_database(restoration_point, connection_name)
                except Exception as e:
                    raise RestorationFailedException(e)
            
            raise DumpFailedException(e)
        finally:
            file.close()

    import_multi_hooks.after(zip_file=zip_file, connection_name=connection_name)

    zip_file.close()

    try:
        _check_migrations(connection_name)
    except Exception as e:
        if restoration_point is not None:
            try:
                _restore_database(restoration_point, connection_name)
            except Exception as e:
                raise RestorationFailedException(e)
        raise MigrateFailedException(e)
    
    if restoration_point is not None:
        return DumpedDatabaseObject(connection_name, location=restoration_point.location)

    return DumpedDatabaseObject(connection_name)

def _restore_database(restoration_point: DumpedDatabaseObject, connection_name: str=DEFAULT_DB_ALIAS) -> None:
    """
        Restore the database to a previous point.
    """

    logger.info("Restoring database to previous point.")

    for hook in hooks.get_hooks(
            import_multi_hooks.scheme("before_database_restore", append_base=False)
        ):
        hook(restoration_point)

    try:
        file = restoration_point.file
        file = crypto.aes_decrypt_file(file)
    except Exception as e:
        file.close()
        # Shit is fucked.
        raise crypto.CryptoFailedException(e) from e

    with zipfile.ZipFile(file, "r") as zip_file:
        errors = []
        nl = zip_file.namelist()
        for filename in nl:
            file = zip_file.open(filename)
            try:
                import_database_table(connection_name, file)
            except:
                errors.append(f"Failed to import table from {filename}")
            finally:
                file.close()

        if len(errors) == len(nl):
            logger.critical("Failed to restore database %v", errors)
            raise RestorationFailedException(errors)
        
        elif len(errors) > 0:
            logger.critical("Failed to restore some tables in the database %v", errors)


def _check_migrations(connection_name: str=DEFAULT_DB_ALIAS) -> None:
    """
        Check if migrations are required.
    """

    from django.core.management import call_command

    # Check if migrations are required
    connection = connections[connection_name]

    try:
        connection.ensure_connection()
    except Exception as e:
        logger.critical("Failed to connect to database.")
        raise e
    
    if connection.is_usable():
        logger.info("Database is usable.")

    try:
        call_command("migrate", database=connection_name, interactive=False)
    except Exception as e:
        logger.critical("Failed to migrate database.")
        raise e
