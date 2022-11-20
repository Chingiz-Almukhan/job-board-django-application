from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import UserManager

ROLE = (('Employer', 'Работодатель'), ('Employee', 'Соискатель'))


class Profile(AbstractUser):
    email = models.EmailField(verbose_name='Электронная почта', unique=True, blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='avatars', verbose_name='Аватар',
                               default='/default_av.jpg')
    username = models.CharField(verbose_name='Имя пользователя', max_length=20, blank=True)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=20, blank=True)
    user_role = models.TextField(verbose_name='Роль', choices=ROLE, null=False, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.email} {self.username}'
