from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as AbstractUserManager
from django.db import models


class UserManager(AbstractUserManager):
    pass


class User(AbstractUser):

    patronymic = models.CharField('Patronymic', max_length=150, default='', blank=True)
    phone = models.CharField('Phone', max_length=32, default='', blank=True)

    objects = UserManager()

    def __str__(self):
        return self.username

