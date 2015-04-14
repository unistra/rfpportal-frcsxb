from django.db import models
from user_profile.models import UserProfile
from django.core.files.storage import FileSystemStorage

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
    project_duration=models.IntegerField(null=True)
    ending_date=models.DateField(null=True)
    purpose=models.CharField(max_length=255,null=True)
    scope_of_work=models.CharField(max_length=4000,null=True)
    anticipated_impact=models.CharField(max_length=4000,null=True)
    document=models.FileField(null=True)

class Review(models.Model):
    user=models.ForeignKey(User)
    project=models.ForeignKey(Project)
    name=models.CharField(max_length=255,blank=True)
    question_1 = models.CharField(max_length=4000,null=True,blank=True)
    question_2 = models.CharField(max_length=4000,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    document=models.FileField(null=True,upload_to=('reviews'),blank=True)

class File_Test(models.Model):
    name=models.CharField(max_length=255)
    document=models.FileField(null=True)
