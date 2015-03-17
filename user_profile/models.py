from django.db import models

# Create your models here.

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255,null=True)
    address = models.CharField(max_length=255,null=True)
    zip = models.PositiveIntegerField(null=True)
    city = models.CharField(max_length=255,null=True)
    is_pi = models.BooleanField(default=False)
    is_reviewer = models.BooleanField(default=False)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

