from django.test import TestCase
from users.tests.factories import UserFactory


class TestUserModel(TestCase):
    def test_create_user_object_successfully(self):
        self.user = UserFactory(username="new user name", email="new@gmail.com")
        self.assertEqual(self.user.email, "new@gmail.com")
        self.assertEqual(self.user.username, "new user name")
