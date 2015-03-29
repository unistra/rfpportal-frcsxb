from django.db import models
from user_profile.models import UserProfile

from django.contrib.auth.models import User

class RfpCampaign(models.Model):
    name=models.CharField(max_length=255)
    year=models.PositiveIntegerField()

class RequestForProposal(models.Model):
    name=models.CharField(max_length=255)

class Project(models.Model):
    name=models.CharField(max_length=255)
    user=models.ForeignKey(User)
    rfp=models.ForeignKey(RfpCampaign)

class Review(models.Model):
    name=models.CharField(max_length=255)
    project=models.ForeignKey(Project)
    user=models.ForeignKey(User)


