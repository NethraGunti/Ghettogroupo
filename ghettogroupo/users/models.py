from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_('Email Address'), unique=True)
    username = models.CharField(max_length=20, unique=True)
    firstName = models.CharField(_("First Name"), max_length=20)
    lastName = models.CharField(_("Last Name"), max_length=20, blank=True, null=True)
    USERNAME = 'username'
    REQUIRED_FIELDS = ['email', 'firstName']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return self.username

    


