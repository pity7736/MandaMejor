from .models import User


class UserController:

    @staticmethod
    def create_user(email, first_name, last_name):
        user = User.objects.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        return user
