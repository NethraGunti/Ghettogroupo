from django.contrib import admin

from groups.models import Group, Membership, Request

admin.site.register(Group)
admin.site.register(Membership)
admin.site.register(Request)
