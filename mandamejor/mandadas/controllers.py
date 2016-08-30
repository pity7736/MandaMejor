from .models import User


class CreateUserController:

    def __init__(self, email, first_name, last_name):
        assert email is not None, 'Email is obligatory'
        assert first_name is not None, 'First name is obligatory'
        assert last_name is not None, 'Last name is obligatory'
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def create_user(self):
        user = User.objects.create_user(
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name
        )
        return user
