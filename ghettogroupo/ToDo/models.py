from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey("users.User", verbose_name=_("User"), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title