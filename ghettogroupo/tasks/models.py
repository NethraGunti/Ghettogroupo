from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

from groups.models import Membership


class Task(models.Model):
    assigned_by = models.ForeignKey("users.User", verbose_name=_("Assigned By"), on_delete=models.CASCADE)
    assigned_group = models.ForeignKey("groups.Group", verbose_name=_("Assigned Group"), on_delete=models.CASCADE)
    task_title = models.CharField(_("Task Title"), max_length=100)
    task_desc = models.CharField(_("Task Description"), max_length=500)
    deadline = models.DateTimeField(_("Task Deadline"), null=True, blank=True)
    attachment = models.FileField(_("File"), upload_to='taskfiles/', null=True, blank=True)
    
    def __str__(self):
        return self.task_title

    def __unicode__(self):
        return self.task_title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
    
    def clean(self):
        membership = self.assigned_by
        if membership.isAssigner or membership.isOwner:
            return self
        else:
            raise ValidationError('User does not have enough permissions to assign task')
    
    def assigned_to(self):
        subgroup = Subgroup.objects.filter(task=self).values_list('assigned_to__pk')
        if subgroup:
            return Membership.objects.filter(pk__in=subgroup)
        return  Membership.objects.filter(group=self.assigned_group)


class Subgroup(models.Model):
    assigned_to = models.ForeignKey("groups.Membership", verbose_name=_("Assigned To"), on_delete=models.CASCADE)
    task = models.ForeignKey(Task, verbose_name=_("Task"), on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = _("Subgroup")
        verbose_name_plural = _("Subgroups")

    def __str__(self):
        return '{} {}'.format(self.assigned_to , self.task)
    
    def __unicode__(self):
        return self.assigned_to.member
