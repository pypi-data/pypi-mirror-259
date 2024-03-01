from django.test import TransactionTestCase
from django.contrib.auth import get_user_model

import os

from .. import (
    settings as _settings,
    util as _util,
    crypto as _crypto,
)

User = get_user_model()

class TestDump(TransactionTestCase):
    def setUp(self) -> None:
        _settings.EXCLUDED_EXPORT_TABLES = []
        self.users = []
        self.ids = []
        for i in range(10):

            if User.USERNAME_FIELD == "email":
                user = User.objects.create_user(
                    email=f"user{i}@test.local",
                    password="password"
                )
            else:
                user = User.objects.create_user(
                    username=f"user{i}",
                    email=f"user{i}@test.local",
                    password="password"
                )

            self.users.append(user)
            self.ids.append(user.id)

    def test_recovery(self):
        dump = _util.create_database_dump(skip_checks=True, path="tests")

        for user in self.users:
            user.delete()

        if User.objects.filter(id__in=self.ids).exists():
            self.fail("Users were not deleted")

        _util.import_database_dump(dump.file, recovery_db=False)

        users = User.objects.filter(id__in=self.ids)
        if not users.exists():
            self.fail("Users were not restored")

        if not _crypto.is_valid_dump(dump.file):
            self.fail("Dump is not valid")

        dump.file.close()

        try: os.remove(dump.location)
        except: pass

        for i, user in enumerate(users):
            self.assertEqual(user.id, self.ids[i])
            self.assertEqual(user.email, self.users[i].email)
            self.assertEqual(user.username, self.users[i].username)
            self.assertTrue(user.check_password("password"))

        users.delete()

