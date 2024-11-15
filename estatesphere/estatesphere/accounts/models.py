from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from estatesphere.accounts.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(to=UserModel, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    pofile_picture = models.URLField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def get_full_name(self):
        return f"{self.first_name or ''} {self.last_name or ''}".strip() or 'Anonymous'

