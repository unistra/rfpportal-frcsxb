from django.db import models
from user_profile.models import UserProfile
from django.core.files.storage import FileSystemStorage

from django.contrib.auth.models import User

class RequestForProposal(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(max_length=4000,null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Fund"
        verbose_name_plural = "Funds"

class RfpCampaign(models.Model):
    request_for_proposal=models.ForeignKey(RequestForProposal)
    name=models.CharField(max_length=255,null=True)
    year=models.PositiveIntegerField(null=True)
    instructions=models.TextField(max_length=4000,null=True)
    logo = models.ImageField(upload_to='image',null=True,blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Call for proposal"
        verbose_name_plural = "Call for proposals"

class Project(models.Model):
    rfp=models.ForeignKey(RfpCampaign)
    name=models.CharField(max_length=255)
    user=models.ForeignKey(User,blank=True,null=True)
    starting_date=models.DateField(null=True)
    ending_date=models.DateField(null=True,blank=True)
    project_duration=models.IntegerField(null=True,blank=True)
    requested_amount=models.IntegerField(null=True)
    additional_funding = models.CharField(max_length = 4000, null = True, blank = True)
    purpose=models.CharField(max_length=4000,null=True,blank=True)
    scope_of_work=models.CharField(max_length=4000,null=True,blank=True)
    anticipated_impact=models.CharField(max_length=4000,null=True,blank=True)
    document=models.FileField(upload_to='project',null=True,blank=True)

    def __unicode__(self):
        return self.name

class ProposedReviewer(models.Model):
    project=models.ForeignKey(Project,null=True)
    first_name = models.CharField(max_length=255,blank=True,null=True)
    last_name = models.CharField(max_length=255,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    institution = models.CharField(max_length=255,blank=True,null=True)
    address = models.CharField(max_length=255,blank=True,null=True)
    city = models.CharField(max_length=255,blank=True,null=True)
    state = models.CharField(max_length=255,blank=True,null=True)
    postcode = models.CharField(max_length = 255,blank=True,null=True)
    country = models.CharField(max_length=255,blank=True,null=True)
    type = models.CharField(max_length=255,null=True,blank=True)


    def __unicode__(self):
        return (str(self.first_name) + " " + str(self.last_name) + " - " + str(self.institution))

class BudgetLine(models.Model):
    project = models.ForeignKey(Project,null = True,editable=False)
    item = models.CharField(max_length = 255, null=True, blank=True)
    category = models.CharField(max_length = 255, null=True, blank=True)
    duration = models.IntegerField(null=True,blank=True)
    monthly_salary = models.IntegerField(null=True,blank=True)
    quote=models.FileField(upload_to='quotes',null=True,blank=True)
    amount = models.FloatField(null=True, blank = True)

    def __unicode__(self):
        return  (str(self.category) + " " +str(self.item))


class Review(models.Model):
    user = models.ForeignKey(User,verbose_name=u"Reviewer")
    project = models.ForeignKey(Project, verbose_name=u"Project")
    name = models.CharField(max_length=255,blank=True)
    question_1 = models.CharField(max_length=4000,null=True,blank=True)
    question_2 = models.CharField(max_length=4000,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    document = models.FileField(upload_to=('reviews'),null=True,blank=True)

    def __unicode__(self):
        return (str(self.user.first_name) + " " + str(self.user.last_name) + " for: " + str(self.project.name))


class File_Test(models.Model):
    name=models.CharField(max_length=255)
    document=models.FileField(null=True)
