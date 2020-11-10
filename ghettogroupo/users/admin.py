from django.contrib import admin

from users.models import User, UserProfile, Interest

# admin.site.register(UserProfile)
# admin.site.register(Interest)

class InterestInline(admin.TabularInline):
    model = Interest

class ProfileInline(admin.TabularInline):
    model = UserProfile

class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline, InterestInline]
    # def get_inline_instances(self, request, obj=None):
        # if not obj:
            # return []
        # unfiltered = super(UserAdmin, self).get_inline_instances(request, obj)
        # if obj.relationships.all():
        #     return [x for x in unfiltered if isinstance(x,RelationshipInlineTo)]
        # else:
        #     return [x for x in unfiltered if isinstance(x,RelationshipInlineFrom)]
admin.site.register(User, UserAdmin)
