import uuid

from django.utils.translation import ugettext_lazy as _
from django.db import models


class DeveloperKey(models.Model):
    user = models.OneToOneField("users.User", verbose_name=_("develeoper"), on_delete=models.CASCADE, unique=True)
    client_id = models.UUIDField(_("Client ID"), default=uuid.uuid4, editable=False)
    secret_key = models.UUIDField(_("Secret Key"), default=uuid.uuid4, editable=False)
    
    def __str__(self):
        self.user

    def __unicode__(self):
        self.user

    class Meta:
        verbose_name = 'DeveloperKey'
        verbose_name_plural = 'DeveloperKeys'