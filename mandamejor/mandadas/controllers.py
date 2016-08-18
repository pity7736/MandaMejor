from .models import User


class UserController:

    def create_user(self, email, first_name, last_name):
        assert email is not None, 'Email is obligatory'
        assert first_name is not None, 'First name is obligatory'
        assert last_name is not None, 'Last name is obligatory'
        user = User.objects.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        return user
