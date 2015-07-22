from django.contrib import admin
from models import UserProfile
from rfp.admin import ProjectInLine
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django import forms
from django.contrib.auth.forms import UserCreationForm as CreationForm

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["first_name","last_name","organization"]
    list_filter = ["organization"]
    search_fields = ['last_name']

#class UserAdmin(admin.ModelAdmin):
    #inlines = [UserProfileInline,]

#admin.site.unregister(User)

#admin.site.register(User, UserAdmin)

admin.site.register(UserProfile,UserProfileAdmin)
