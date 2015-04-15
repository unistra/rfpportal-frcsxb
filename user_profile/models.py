from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect

# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    title = models.CharField(max_length=255,null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    organization = models.CharField(max_length=255,null=True)
    address = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=255,null=True)
    state = models.CharField(max_length=255,null=True)
    zip = models.PositiveIntegerField(null=True)
    country = models.CharField(max_length= 255,null=True)
    is_pi = models.BooleanField(default=False)
    is_reviewer = models.BooleanField(default=False)
    num_connection = models.IntegerField(default=0, editable=False)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance,num_connection=0)

def update_userprofile(sender, instance, created, **kwargs):
    if not created:
        UserProfile.objects.filter(user=instance.pk).update(first_name = instance.first_name, last_name = instance.last_name)
        print('UserProfile information updated?')

def udpate_num_of_connection(sender, request, user, **kwargs):
    u_num = UserProfile.objects.get(user = user.pk).num_connection
    u_num += 1
    UserProfile.objects.filter(user = user.pk).update(num_connection = u_num)
    print(u_num)

post_save.connect(create_user_profile, sender = User)
post_save.connect(update_userprofile, sender = User)
user_logged_in.connect(udpate_num_of_connection, sender = User)
