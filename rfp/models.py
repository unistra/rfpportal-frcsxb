from django.db import models
from user_profile.models import UserProfile

from django.contrib.auth.models import User


class RequestForProposal(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(max_length=4000,null=True)

    def __unicode__(self):
        return self.name

class RfpCampaign(models.Model):
    request_for_proposal=models.ForeignKey(RequestForProposal)
    name=models.CharField(max_length=255,null=True)
    year=models.PositiveIntegerField(null=True)
    instructions=models.TextField(max_length=4000,null=True)

    def __unicode__(self):
        return self.name


class Project(models.Model):
    name=models.CharField(max_length=255)
    user=models.ForeignKey(User)
    rfp=models.ForeignKey(RfpCampaign)
    requested_amount=models.IntegerField(null=True)
    starting_date=models.DateField(null=True)
    ending_date=models.DateField(null=True)
    scope_of_work=models.CharField(max_length=4000,null=True)
    purpose=models.CharField(max_length=255,null=True)
    anticipated_impact=models.CharField(max_length=4000,null=True)
    project_duration=models.IntegerField(null=True)

class Review(models.Model):
    name=models.CharField(max_length=255)
    project=models.ForeignKey(Project)
    user=models.ForeignKey(User)

