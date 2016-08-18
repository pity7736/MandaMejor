from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(
        'primer nombre',
        max_length=30,
        blank=True
    )
    last_name = models.CharField(
        'segundo nombre',
        max_length=30,
        blank=True
    )
    email = models.EmailField(
        'email',
        blank=True,
        unique=True
    )
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        'activo',
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(
        'date sing up',
        auto_now_add=True
    )

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        if self.first_name or self.last_name:
            return self.get_full_name()
        return self.email

    def get_full_name(self):
        full_name = '{0} {1}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name


class Mandada(models.Model):
    user = models.ForeignKey(User, related_name='mandadas')
    when = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user
