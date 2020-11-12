from django.db import models
from django.utils.translation import ugettext_lazy as _

PLANS = [
    ('REGULAR', 'REGULAR'),
    ('EDUCATIONAL TIER 1', 'EDUCATIONAL TIER 1'),
    ('EDUCATIONAL TIER 2', 'EDUCATIONAL TIER 2'),
    ('WORKSPACE TIER 1', 'WORKSPACE TIER 1'),
    ('WORKSPACE TIER 2', 'WORKSPACE TIER 2'),
]


class Plan(models.Model):
    plan = models.CharField(_("Plan"), max_length=50, choices=PLANS)
    group_cap = models.IntegerField(_("Total Groups"))
    member_cap = models.IntegerField(_("Member Cap per Group"))
    pricing = models.FloatField(_("Price"))
    

    class Meta:
        verbose_name = _( "Plan")
        verbose_name_plural = _( "Plans")

    def __str__(self):
        return self.name
