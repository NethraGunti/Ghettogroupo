from django.db import models
from django.utils.translation import ugettext_lazy as _

PLANS = [
    ('REGULAR', 'REGULAR'), #g=1, m=20, c=$1,
    ('EDUCATIONAL TIER 1', 'EDUCATIONAL TIER 1'), #g=1, m=100, c=$15,
    ('EDUCATIONAL TIER 2', 'EDUCATIONAL TIER 2'), #g=3, m=200, c=$40,
    ('WORKSPACE TIER 1', 'WORKSPACE TIER 1'), #g=2, m=500, c=$50,
    ('WORKSPACE TIER 2', 'WORKSPACE TIER 2'), #g=5, m=500, c=$100,
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
        return self.plan



class Subscription(models.Model):
    user = models.ForeignKey("users.User", verbose_name=_("user_subscription"), on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, verbose_name=_("user_plan"), on_delete=models.CASCADE)    
    isActive = models.BooleanField(_("subscription_active"), default=False)

    class Meta:
        verbose_name = _("Subscription")
        verbose_name_plural = _("Subscriptions")

    def __str__(self):
        return self.user.username
