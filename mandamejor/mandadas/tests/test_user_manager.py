from django.test import TestCase

from ..models import User


class UserManagerTests(TestCase):

    def test_create_user(self):
        User.objects.create_user(
            email='test@comparamejor.com',
            password='123'
        )

        user = User.objects.get(email='test@comparamejor.com')

        self.assertEqual(user.email, 'test@comparamejor.com')
        self.assertEqual(user.check_password('123'), True)
        self.assertEqual(user.is_superuser, False)

    def test_create_user_with_email_none(self):
        try:
            User.objects.create_user(
                email=None,
                password='123'
            )
        except ValueError:
            pass
        else:
            self.fail('This should fail')

    def test_create_user_without_password(self):
        User.objects.create_user(
            email='testpass@comparamejor.com',
        )

        user = User.objects.get(email='testpass@comparamejor.com')

        self.assertEqual(user.email, 'testpass@comparamejor.com')
        self.assertEqual(user.has_usable_password(), False)
        self.assertEqual(user.is_superuser, False)

    def test_create_superuser(self):
        User.objects.create_superuser(
            email='super@test.com',
            password='123'
        )

        user = User.objects.get(email='super@test.com')

        self.assertEqual(user.email, 'super@test.com')
        self.assertEqual(user.is_superuser, True)
