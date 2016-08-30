import unittest

from doublex import Mock, Stub, assert_that, verify

from ..controllers.create_user_controller import CreateUserController
from ..models import User


class CreateUserControllerTests(unittest.TestCase):

    def test_create_user(self):
        user_stub = Stub(User)

        with Mock(CreateUserController) as user_mock:
            user_mock.create_user().returns(user_stub).times(1)

        user_mock.create_user()
        assert_that(user_mock, verify())

    def test_create_user_with_email_none(self):
        try:
            CreateUserController(
                email=None,
                first_name='test first name',
                last_name='test last name',
                password='123'
            )
        except AssertionError:
            pass
        else:
            self.fail('this should fail')

    def test_create_user_with_firstname_none(self):
        try:
            CreateUserController(
                email='test@test.com',
                first_name=None,
                last_name='test last name',
                password='123'
            )
        except AssertionError:
            pass
        else:
            self.fail('this should fail')
