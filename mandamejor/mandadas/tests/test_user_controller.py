from django.test import TestCase

from ..controllers import UserController, User

from doublex import Mock, Stub, ANY_ARG, assert_that, is_, verify
from hamcrest.core.core.isnone import not_none


class UserControllerTests(TestCase):

    def test_create_user(self):
        with Stub(User) as user_stub:
            user_stub.id = 1
            user_stub.email = 'test@test.com'
            user_stub.first_name = 'test first name'
            user_stub.last_name = 'test last name'

        with Mock(UserController) as user_mock:
            user_mock.create_user(ANY_ARG).returns(user_stub).times(1)

        user = user_mock.create_user(
            email='test@test.com',
            first_name='test first name',
            last_name='test last name'
        )

        assert_that(user_mock, verify())
        assert_that(user.id, not_none())
        assert_that(user.email, is_('test@test.com'))
        assert_that(user.first_name, is_('test first name'))
        assert_that(user.last_name, is_('test last name'))

    def test_create_user_with_email_none(self):
        with Mock(UserController) as user_mock:
            user_mock.create_user(ANY_ARG).raises(AssertionError)

        with self.assertRaises(AssertionError):
            user_mock.create_user(
                email=None,
                first_name='test first name',
                last_name='test last name'
            )

        assert_that(user_mock, verify())

    def test_create_user_with_firstname_none(self):
        with Mock(UserController) as user_mock:
            user_mock.create_user(ANY_ARG).raises(AssertionError)

        with self.assertRaises(AssertionError):
            user_mock.create_user(
                email='test@test.com',
                first_name=None,
                last_name='test last name'
            )

        assert_that(user_mock, verify())
