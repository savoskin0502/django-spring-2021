from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class MainUser(AbstractUser):
    class Countries(models.TextChoices):
        KAZAKHSTAN = 'KZ', _('Kazakhstan')
        RUSSIA = 'RU', _('Russia')
        USA = 'USA', _('USA')

    bio = models.TextField(max_length=200, blank=True)
    location = models.CharField(max_length=3, choices=Countries.choices,
                                default=Countries.KAZAKHSTAN)

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
