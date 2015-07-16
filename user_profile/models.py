from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.forms import PasswordResetForm


#Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    title = models.CharField(max_length=255,null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    organization = models.CharField(max_length=255,null=True, blank=True)
    insitute_research_unit = models.CharField(max_length=255,null=True, blank=True)
    address = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=255,null=True)
    state = models.CharField(max_length=255,null=True,blank=True)
    zip = models.CharField(max_length=255,null=True)
    country = models.CharField(max_length= 255,null=True)
    is_pi = models.BooleanField(default=False)
    is_reviewer = models.BooleanField(default=False)
    num_connection = models.IntegerField(default=0, editable=False)
    num_rated_review = models.IntegerField(default=0, editable=False)
    rated_review_avg = models.IntegerField(default=0, editable=False)
    reset_password = models.BooleanField(default=True)

    def __unicode__(self):
        return self.first_name + str(" ") + self.last_name

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def ResetPwd(self,request):
        reset_form = PasswordResetForm({'email': self.user.email})
        print(self.user.email)
        assert reset_form.is_valid()
        print(reset_form)
        reset_form.save(
                request=request,
                use_https=request.is_secure(),
                subject_template_name='registration/create_user_invitation_email_subject.txt',
                email_template_name='registration/create_user_invitation_email.html',
            )

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance,num_connection=0,first_name = instance.first_name,last_name=instance.last_name)

def update_userprofile(sender, instance, created, **kwargs):
    if not created:
        UserProfile.objects.filter(user=instance.pk).update(first_name = instance.first_name, last_name = instance.last_name)

def udpate_num_of_connection(sender, request, user, **kwargs):
    u_num = UserProfile.objects.get(user = user.pk).num_connection
    u_num += 1
    UserProfile.objects.filter(user = user.pk).update(num_connection = u_num)
    print(u_num)

post_save.connect(create_user_profile, sender = User)
post_save.connect(update_userprofile, sender = User)
user_logged_in.connect(udpate_num_of_connection, sender = User)
