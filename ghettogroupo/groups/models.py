import uuid
from slugify import slugify

from django.urls import reverse_lazy
from django.db import models
from django.utils.translation import ugettext_lazy as _


GROUPS = [
    ("PUBLIC", "PUBLIC"),
    ("PRIVATE", "PRIVATE")
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

    def get_group_url(self):
        return reverse_lazy('group-page', kwargs={"code": self.code})
    
    def get_all_members(self):
        return Membership.objects.filter(group=self)

    def get_active_members(self):
        return self.get_all_members().filter(isActive=True)
    
    def get_managers(self):
        return self.get_active_members().filter(isManager=True)
    
    def get_assigners(self):
        return self.get_active_members().filter(isAssigner=True)
    
    


class Membership(models.Model):
    membership_id = models.UUIDField(_("Membership ID"), primary_key=True, default=uuid.uuid4, editable=False)
    group = models.ForeignKey("groups.Group", verbose_name=_("Group"), on_delete=models.CASCADE)
    member = models.ForeignKey("users.User", verbose_name=_("Member"), db_column='username', on_delete=models.CASCADE)
    isOwner = models.BooleanField(_("Is Owner"), default=False)
    isAssigner = models.BooleanField(_("Is Assigner"), default=False)
    isManager = models.BooleanField(_("Is Manager"), default=False)
    isActive = models.BooleanField(_("Is Active"), default=True)
    

    class Meta:
        verbose_name = _("Membership")
        verbose_name_plural = _("Memberships")
        unique_together = ('group', 'member')

    def __str__(self):
        return '{}'.format(self.member.username)
    
    def __unicode__(self):
        return self.member


class Request(models.Model):
    user = models.ForeignKey("users.User", verbose_name=_("User"), on_delete=models.CASCADE)
    group = models.ForeignKey(Group, verbose_name=_("Group"), on_delete=models.CASCADE)
    isInvite = models.BooleanField(_("Is Invite"), default=False)


    class Meta:
        verbose_name = _("Request")
        verbose_name_plural = _("Requests")

    def __str__(self):
        return '{}'.format(self.user)

    def __unicode__(self):
        return self.user
