from django.test import TestCase

from ..controllers import UserController, User


class UserControllerTests(TestCase):

    def test_create_user(self):
        UserController.create_user(
            email='test@test.com',
            first_name='test first name',
            last_name='test last name'
        )

        user = User.objects.get(email='test@test.com')

        self.assertEqual(user.email, 'test@test.com')
        self.assertEqual(user.first_name, 'test first name')
        self.assertEqual(user.last_name, 'test last name')
