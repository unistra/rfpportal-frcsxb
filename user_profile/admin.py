from django.contrib import admin
from models import UserProfile
from rfp.admin import ProjectInLine
from django.contrib.auth.models import User
#

class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ["last_name"]
    list_display = ["last_name","first_name","city"]


# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
