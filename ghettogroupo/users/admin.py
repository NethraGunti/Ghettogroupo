from django.contrib import admin
from django.contrib.admin.views.main import ChangeList

from users.models import User, UserProfile, Interest
from users.forms import InterestForm

admin.site.register(Interest)


class ProfileInline(admin.TabularInline):
    model = UserProfile


class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline, ]


class InterestUserAdmin(admin.ModelAdmin):
    model = UserProfile
    filter_horizontal = ['interest',]

admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, InterestUserAdmin)
