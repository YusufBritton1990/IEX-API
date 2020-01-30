from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    name = models.CharField(max_length=30)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    # pass
    def __str__(self):
        return self.email

class Account(models.Model):
    user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    cash = models.FloatField(default=5000)

    def __str__(self):
        return self.user_id
