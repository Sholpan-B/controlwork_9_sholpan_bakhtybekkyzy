from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import UserManager


class Account(AbstractUser):
    username = models.CharField(unique=True, null=False, blank=False, verbose_name='Логин')
    email = models.EmailField(verbose_name='Электронная почта', unique=True, blank=True)
    favorites = models.ManyToManyField(to='picture.Photo', verbose_name='Избранное', related_name='user_favorites')
    commented_photos = models.ManyToManyField(verbose_name='Прокомментированные фото', to='picture.Photo',
                                              related_name='user_comments')
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    object = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
