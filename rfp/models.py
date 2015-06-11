from django.db import models
from user_profile.models import UserProfile
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from django.contrib.auth.models import User

class RfpCampaign(models.Model):
    name=models.CharField(max_length=255,null=True)
    year=models.PositiveIntegerField(null=True)
    instructions=models.TextField(max_length=4000,null=True)
    logo = models.ImageField(upload_to='image',null=True,blank=True)
    review_questions = models.CharField(max_length = 4000, null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_questions(self):
        list = str(self.review_questions).split(',')
        b = tuple(list)
        return b

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
    status=models.CharField(max_length=255,blank=True,null=True)
    confirmation_email_sent = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def send_project_confirmation_email(self):
    #Send a Thank you for your project confirmation email.
         print(self.confirmation_email_sent)

         if not self.confirmation_email_sent:
            self.confirmation_email_sent = True
            c = {'project' : self}

            msg_plain = render_to_string('rfp/email/project_confirmation.txt',c)
            msg_html = render_to_string('rfp/email/project_confirmation.html',c)

            conf_plain = render_to_string('rfp/email/project_admin_confirmation.txt',c)
            conf_html = render_to_string('rfp/email/project_admin_confirmation.html',c)

            send_mail('Your project has been succesfully submitted',
                      msg_plain, 'contact@icfrc.fr', [self.user.email],
                      html_message=msg_html, fail_silently=False)
            send_mail('Project Submitted',
                      conf_plain, 'contact@icfrc.fr', ['contact@icfrc.fr'],
                      html_message=conf_html, fail_silently=False)

            self.confirmation_email_sent = True
            self.save()
            print('Email Sent ??)')

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
    custom_0 = models.CharField(max_length=4000,null=True,blank=True)
    custom_1 = models.CharField(max_length=4000,null=True,blank=True)
    custom_2 = models.CharField(max_length=4000,null=True,blank=True)
    custom_3 = models.CharField(max_length=4000,null=True,blank=True)
    custom_4 = models.CharField(max_length=4000,null=True,blank=True)
    custom_5 = models.CharField(max_length=4000,null=True,blank=True)
    custom_6 = models.CharField(max_length=4000,null=True,blank=True)
    custom_7 = models.CharField(max_length=4000,null=True,blank=True)
    custom_8 = models.CharField(max_length=4000,null=True,blank=True)
    custom_9 = models.CharField(max_length=4000,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    document = models.FileField(upload_to=('reviews'),null=True,blank=True)

    def __unicode__(self):
        return (str(self.user.first_name) + " " + str(self.user.last_name) + " for: " + str(self.project.name))

class File_Test(models.Model):
    name=models.CharField(max_length=255)
    document=models.FileField(null=True)

#post_save.connect(send_project_confirmation_email,sender = Project)
