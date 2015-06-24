from django.db import models
from django.contrib.sites.models import Site
from user_profile.models import UserProfile
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import logging

def send_mandrill_email(self,mandrill_template_name, context_dict):
        """
        Send a mandrill template email.
        :param mandrill_template_name: str
        """
        from django.core.mail import EmailMessage

        msg = EmailMessage(to=[self.user.email],)
        msg.template_name = mandrill_template_name
        msg.global_merge_vars = context_dict
        msg.send()

def username_exists(username):
        """
        Return True if self.email exists among Users emails list.
        """
        l = list()
        users = User.objects.all()
        for u in users:
            l.append(u.username)

        return username in l

def add_user_to_group(user,group):
    from django.contrib.auth.models import User,Group
    g = Group.objects.get(name=group)
    u = User.objects.get(id = user.id)
    u.groups.add(g)
    u.save()

from django.contrib.auth.models import User

class RfpCampaign(models.Model):
    CATEGORY_CHOICES = ( ('Synergy', 'Synergy'),
                         ('Innovation', 'Innovation'),
                         ('Labex_CSC', 'Labex CSC'),
                         )
    STATUS_CHOICES = ( ('open', 'Open, Call for proposal is open for submission.'),
                         ('under_review', 'Under review, reviews are being collected prior to board meeting.'),
                         ('closed', 'Closed, results have been communicated.'),
                         )

    name=models.CharField(max_length=255,null=True)
    category=models.CharField(max_length=255,null=True,choices=CATEGORY_CHOICES)
    add_reviewer=models.BooleanField(default=True)
    year=models.PositiveIntegerField(null=True)
    instructions=models.TextField(max_length=4000,null=True)

    logo = models.ImageField(upload_to='image',null=True,blank=True)
    review_questions = models.CharField(max_length = 4000, null=True, blank=True)
    deadline = models.DateField()
    status = models.CharField(max_length=255,null=True,choices=STATUS_CHOICES,default='open')
    email_template_project_confirmation = models.CharField(max_length=255,null=True,blank=True,default='project_submission_confirmation_email_default',verbose_name=u"Email template for project submission confirmation.")
    email_template_review_invitation = models.CharField(max_length=255,null=True,blank=True, verbose_name=u"Email template for invitation to review.")
    email_template_review_confirmation = models.CharField(max_length=255,null=True,blank=True,default='review_submission_confirmation_email_default', verbose_name=u"Email template for confirmation and thank you for your review.")
    email_template_review_follow_up = models.CharField(max_length=255,null=True,blank=True, verbose_name=u"Email template for follow up with reviewer.")
    email_template_rfp_closed = models.CharField(max_length=255,null=True,blank=True, verbose_name=u"Email template to anounce results.")

    def __unicode__(self):
        return (str(self.year) + " " + str(self.name))

    def get_questions(self):
        list = self.review_questions.split('; ')
        b = tuple(list)
        return b

    class Meta:
        verbose_name = "Call for proposal"
        verbose_name_plural = "Call for proposals"

class Project(models.Model):
    STATUS_CHOICES = (
        ('pending','Pending'),
        ('under_review','Under Review'),
        ('granted','Granted'),
        ('not_granted','Not Granted'),
    )
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
    status=models.CharField(max_length=255,default='pending',choices=STATUS_CHOICES)
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

                c = {'project_name' : str(self), 'full_name' : (str(self.user.first_name) + " " + str(self.user.last_name))}
                send_mandrill_email(self,self.rfp.email_template_project_confirmation,c)

                c = {'project':self}
                conf_plain = render_to_string('rfp/email/project_admin_confirmation.txt',c)
                conf_html = render_to_string('rfp/email/project_admin_confirmation.html',c)

                send_mail('Project Submitted',
                          conf_plain, 'admin@icfrc.fr', ['admin@icfrc.fr','sgug@outlook.com'],
                          html_message=conf_html, fail_silently=False)

                self.confirmation_email_sent = True
                self.save()

class ProposedReviewer(models.Model):
    TYPE_CHOICES = (
        ('ADMIN_PROPOSED','Proposed by admin'),
        ('USER_PROPOSED', 'Proposed by User'),
        ('USER_EXCLUDED', 'Excluded Reviewer'),
    )
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
    type = models.CharField(max_length=255,blank=True,null=True,choices=TYPE_CHOICES)

    def __unicode__(self):
        return (str(self.first_name) + " " + str(self.last_name) + " - " + str(self.institution))

    def is_user(self):
        """
        Return True if self.email exists among Users emails list.
        """
        l = list()
        users = User.objects.all()
        for u in users:
            l.append(u.email)

        return self.email in l

    def invite_reviewer(self):

        #If proposed reviewer is already a user
        if self.is_user():
            user = User.objects.get(email=self.email)
            print('User is: ')
            print(user)

        #If proposed reviewer is not a user yet
        if not self.is_user():
            import random
            username = str(str(self.first_name)[:1] + str(self.last_name))

            #Verify username is unused and set a new one if needed.
            while username_exists(username):
                    username = str(str(self.first_name)[:1] + str(self.last_name))
                    n = str(random.randint(1, 1000))
                    username = str(username + n)
                    print('tested username is: ')
                    print (username)

                    if not username_exists(username):
                        print ('THIS NEW user profile does not exists!')
                        break

            password = 'frc@2015'

            #Create new user.
            user = User.objects.create_user(username, self.email, password, first_name = self.first_name, last_name = self.last_name) #Create new user.
            user.save()

            #Add to the reviewer group
            group = 'Reviewer'
            add_user_to_group(user,group)

            #Update UserProfile with ProposedReviewer Information
            user_profile = UserProfile.objects.filter(user_id=user.id).update(first_name = self.first_name, last_name = self.last_name, organization = self.institution, address = self.address, city = self.city,
            state = self.state, country = self.country, zip = self.postcode)


        #Create the review for the user.
        review_tuple = Review.objects.get_or_create(user = user, project = self.project,  )

        print ('The review is: ')
        review = review_tuple[0]

        #Send invitation to review the corresponding project.
        review.send_invitation_email_to_reviewer()
        print('Email sent ?!')

        return review

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
    STATUS_CHOICES = (
        ('pending','pending'),
        ('refused', 'refused'),
        ('accepted', 'accepted'),
        ('completed', 'completed'),
    )

    user = models.ForeignKey(User,verbose_name=u"Reviewer")
    project = models.ForeignKey(Project, verbose_name=u"Project")
    rating = models.CharField(max_length=255, null=True,blank=True)
    status = models.CharField(max_length=255,default='pending',choices=STATUS_CHOICES)
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
            c = {'full_name' : (str(self.user.first_name) + " " + str(self.user.last_name)), 'project_name': str(self.project.name), 'category_name' : str(self.project.rfp.category), 'category_year' : str(self.project.rfp.year)}
            send_mandrill_email(self,self.project.rfp.email_template_review_confirmation,c)

            c = {'review' : self}
            conf_plain = render_to_string('rfp/email/review_admin_confirmation.txt',c)
            conf_html = render_to_string('rfp/email/review_admin_confirmation.html',c)

            send_mail('Review Submitted',
                      conf_plain, 'admin@icfrc.fr', ['admin@icfrc.fr','sgug@outlook.com'],
                      html_message=conf_html, fail_silently=False)

    def send_invitation_email_to_reviewer(self):
            """
            Send an email including a link. Clicking the link log the user in and redirect to the review survey page.
            """
            from urlcrypt import lib as urlcrypt
            from django.core.urlresolvers import reverse
            token_accept = urlcrypt.generate_login_token(self.user, reverse('post_review_waiver', args=[self.id]))
            url_accept = reverse('urlcrypt_redirect', args=(token_accept,))
            site = Site.objects.get(id=1)
            url_refuse = reverse('urlcrypt_redirect', args=(token_accept,))

            c = {'reviewer_full_name' : str(str(self.user.first_name) + " " + str(self.user.last_name)), 'project' : self.project.name,
                 'author' : str(str(self.project.user.first_name) + str(self.project.user.last_name)),
                 'abstract' : self.project.scope_of_work, 'keywords':self.project.purpose,
                 'url_accept' : str(str(site.domain)+str(url_accept)),'url_refuse' : str(str(site.domain)+str(url_accept))}

            send_mandrill_email(self,self.project.rfp.email_template_review_invitation,c)

class File_Test(models.Model):
    name=models.CharField(max_length=255)
    document=models.FileField(null=True)

#post_save.connect(send_project_confirmation_email,sender = Project)
#post_save.connect(set_review_as_completed, sender = Review)

