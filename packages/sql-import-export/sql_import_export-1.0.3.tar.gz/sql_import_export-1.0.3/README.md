import_export
=============

A package for importing and exporting your SQL database. It is by default configured for MySQL, but you can implement your own export functions without all too much effort.



Quick start
-----------

1. Add 'import_export' to your INSTALLED_APPS setting like this:

   ```
   INSTALLED_APPS = [
   	...,
   	'import_export',
   	'maintenance',
   	'celery',
   	'django_celery_beat',
   ]
   ```
2. Follow the install guide for the [maintenance](https://github.com/Nigel2392/wagtail-maintenance) package.
3. Follow the install guide for [Celery](https://github.com/celery/celery/).
4. Follow the install guide for [django_celery_beat](https://github.com/celery/django-celery-beat).


Settings
-----------


### MYSQL_DUMP_CONFIG_LOCATION



### MYSQL_DUMP_BINARY

This setting is only for people who stick to defaults and do not implement their own dump functions.

* Important for windows users to set this to where your `mysqldump.exe` is located.
* On unix it will try to execute the plain `mysqldump` binary. Make sure it is in your PATH or set the `MYSQL_DUMP_BINARY` to the full path of the binary.


### DUMP_LOCATION

Where to store the database dumps on the filesystem.

### DUMP_CHUNK_SIZE



### DUMP_GET_TABLES



### DUMP_EXPORT_TABLE



### DUMP_IMPORT_TABLE



### DUMP_MUST_NOT_ENCRYPT

Whether or not the database dump must be encrypted.
When the dump is encrypted it will also be signed.
The signature will be checked when importing the dump.

```python
# Default, do not encrypt the database dump.
# Accept unencrypted dumps.
# Accept encrypted dumps.
DUMP_MUST_NOT_ENCRYPT=True

# Encrypt the database dump.
# Do not accept unencrypted dumps.
DUMP_MUST_NOT_ENCRYPT=False
```


### BACKUP_ROOT

Where to store the backups.  
The default is `os.path.join(BASE_DIR, 'backups')`.

### DUMP_EXCLUDED_EXPORT_TABLES

Which tables do you want to exclude from the export?  
This will be a list or a tuple, where ending with a * will check for a partial match to the start of the table name.
   
```python
EXCLUDED_EXPORT_TABLES = getattr(settings, "DUMP_EXCLUDED_EXPORT_TABLES", [
    "import_export_*",
    "django_*",
    "auth_*",
    ...
] if DUMP_MUST_NOT_ENCRYPT else []) # When encrypting; export everything
```