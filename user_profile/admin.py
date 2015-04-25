from django.contrib import admin
from models import UserProfile
from rfp.admin import ProjectInLine
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
#

class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ["last_name"]
    list_display = ["last_name","first_name","city"]

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False
    inline_classes = ('collapse open',)


class UserAdmin (AuthUserAdmin):
    inlines = [
        UserProfileInline,
    ]

# unregister old user admin
admin.site.unregister(User)
# register new user admin
admin.site.register(User, UserAdmin)
