from django.contrib import admin

from users.models import User, UserProfile, Interest

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Interest)