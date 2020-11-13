from django.contrib import admin

from payments.models import Subscription, Plan

admin.site.register(Subscription)
admin.site.register(Plan)