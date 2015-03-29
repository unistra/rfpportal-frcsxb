from django.contrib import admin
from models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ["last_name"]
    list_display = ["last_name","first_name","city"]


# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)