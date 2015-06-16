from django.db import models
from user_profile.models import UserProfile
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import logging

from django.contrib.auth.models import User

class RfpCampaign(models.Model):
    CATEGORY_CHOICES = ( ('Synergy', 'Synergy'),
                         ('Innovation', 'Innovation'),
                         ('Labex_CSC', 'Labex CSC'),
                         )
    name=models.CharField(max_length=255,null=True)
    category=models.CharField(max_length=255,null=True,choices=CATEGORY_CHOICES)
    add_reviewer=models.BooleanField(default=True)
    year=models.PositiveIntegerField(null=True)
    instructions=models.TextField(max_length=4000,null=True)
    logo = models.ImageField(upload_to='image',null=True,blank=True)
    review_questions = models.CharField(max_length = 4000, null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_questions(self):
        list = self.review_questions.split('; ')
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
    purpose=models.CharField(max_length=4000,null=True,blank=True,verbose_name=U"Keywords")
    scope_of_work=models.CharField(max_length=4000,null=True,blank=True,verbose_name=u"Abstract")
    anticipated_impact=models.CharField(max_length=4000,null=True,blank=True,verbose_name=u"Link with other project")
    document=models.FileField(upload_to='project',null=True,blank=True)
    status=models.CharField(max_length=255,blank=True,null=True)
    confirmation_email_sent = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def list_of_reviewers_id(self):
        l = list()
        reviews = Review.objects.filter(project = self)
        for r in reviews:
            l.append(r.user.id)
        return l

    def send_project_confirmation_email(self):

         if not self.confirmation_email_sent:

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
    rating = models.CharField(max_length=255, null=True,blank=True)
    status = models.CharField(max_length=255,default='pending',blank=True)
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
    date = models.DateField(auto_now=True)
    document = models.FileField(upload_to=('reviews'),null=True,blank=True)

    def __unicode__(self):
        return (str(self.user.first_name) + " " + str(self.user.last_name) + " for: " + str(self.project.name))

    def send_confirmation_email_to_reviewer(self):
        if not self.status == 'completed':
            c = {'review' : self}

            msg_plain = render_to_string('rfp/email/review_confirmation.txt',c)
            msg_html = render_to_string('rfp/email/review_confirmation.html',c)

            conf_plain = render_to_string('rfp/email/review_admin_confirmation.txt',c)
            conf_html = render_to_string('rfp/email/review_admin_confirmation.html',c)

            send_mail('Thank you! Your review has been succesfully submitted.',
                      msg_plain, 'contact@icfrc.fr', [self.user.email],
                      html_message=msg_html, fail_silently=False)

            send_mail('Review Submitted',
                      conf_plain, 'contact@icfrc.fr', ['contact@icfrc.fr'],
                      html_message=conf_html, fail_silently=False)



def set_review_as_completed(sender, instance, created, **kwargs):
        if instance.rating:
            instance.send_confirmation_email_to_reviewer()
            print('Confirmation Sent!')
        return instance.status

def send_invitation_to_review_email(sender, instance, created, **kwargs):
    if created:
        from urlcrypt import lib as urlcrypt
        from django.core.urlresolvers import reverse
        token_accept = urlcrypt.generate_login_token(instance.user, reverse('post_review_waiver', args=[instance.id]))

        url_accept = reverse('urlcrypt_redirect', args=(token_accept,))
        url_refuse = reverse('urlcrypt_redirect', args=(token_accept,))

        c = {'url_accept' : url_accept, 'url_refuse' : url_refuse, 'review' : instance}
        msg_plain = render_to_string('rfp/email/review_invitation.html', c)
        msg_html = render_to_string('rfp/email/review_invitation.html', c)
        msg_subject = render_to_string('rfp/email/review_invitation_subject.txt', c)

        send_mail(msg_subject,msg_plain,'contact@icfrc.fr',[instance.user.email],html_message=msg_html,fail_silently=False)

        print('Invitation sent')

        instance.status = 'invited'
        instance.save()
        print('Review status changed')

class File_Test(models.Model):
    name=models.CharField(max_length=255)
    document=models.FileField(null=True)

#post_save.connect(send_project_confirmation_email,sender = Project)

post_save.connect(send_invitation_to_review_email,sender= Review)
#post_save.connect(set_review_as_completed, sender = Review)
