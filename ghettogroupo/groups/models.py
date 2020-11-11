import uuid
from slugify import slugify

from django.urls import reverse_lazy
from django.db import models
from django.utils.translation import ugettext_lazy as _

GROUPS = [
    ("Regular", "Regular"),
    ("Education", "Educational"),
    ("Organization", "Organization")
]
class Group(models.Model):
    code = models.UUIDField(_("Code"), unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    type =  models.CharField(_("Type"), max_length=50, choices=GROUPS)
    owner = models.ForeignKey("users.User", verbose_name=_("Owner"), on_delete=models.CASCADE)
    name = models.CharField(_("Group Name"), max_length=50)
    description = models.TextField(_("Description"))

    class Meta:
        verbose_name = _("Group")
        verbose_name_plural = _("Groups")

    def __str__(self):
        return self.name

    def get_group_url(self, user):
        return reverse_lazy('test', kwargs={"username": user.username, "code": self.code})
