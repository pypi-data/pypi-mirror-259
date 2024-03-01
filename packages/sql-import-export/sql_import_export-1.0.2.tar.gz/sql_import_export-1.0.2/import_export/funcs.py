from django.conf import settings
from django.core.files.temp import NamedTemporaryFile

import subprocess

from shlex import quote
from collections import namedtuple

from .settings import (
    MYSQL_DUMP_BINARY,
    MYSQL_DUMP_CONFIG_LOCATION,
)

from django.db import connections

from typing import IO

DATABASE_HOST = settings.DATABASES["default"]["HOST"]
DATABASE_PORT = settings.DATABASES["default"]["PORT"]

DumpedTable = namedtuple("DumpedTable", ["database_name", "tablename", "tempfile"])

def mysql_get_tables(connection):
    """Get a list of all tables in the database."""
    with connection.cursor() as cursor:
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
    return [table[0] for table in tables]


def mysql_exec_import_table(database_name: str, file: IO[bytes]):
    content = file.read()
    connection = connections[database_name]
    with connection.cursor() as cursor:
        cursor.execute(content)


def mysql_dump_table(database_name, tablename) -> DumpedTable:
    """Execute mysqldump on a single table and return a DumpedTable object."""
    command = MYSQL_DUMP_BINARY +\
        f" --defaults-file={MYSQL_DUMP_CONFIG_LOCATION}" +\
        " --protocol=tcp" +\
        " --skip-triggers" +\
        f" --host={quote(str(DATABASE_HOST))}" +\
        f" --port={quote(str(DATABASE_PORT))}" +\
        f" {settings.DATABASES[database_name]['NAME']}" +\
        f" {tablename}"
        # " --single-transaction" +\
        
    tmp = NamedTemporaryFile(suffix=".sql")
    process = subprocess.Popen(command, stdout=tmp, stderr=None, shell=True)
    process.wait()
    tmp.flush()
    tmp.seek(0)

    return DumpedTable(database_name, tablename, tmp)

