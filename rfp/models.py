from django.db import models
from django.contrib.sites.models import Site
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import logging
from django.forms.models import model_to_dict
from django.contrib.auth.models import User,Group

from user_profile.models import UserProfile

def send_mandrill_email(self,mandrill_template_name, context_dict):
        """
        Send a mandrill template email to the owner of self.
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

    starting_date = models.DateField()
    deadline = models.DateField()
    status = models.CharField(max_length=255,null=True,choices=STATUS_CHOICES,default='open')

    budget_hr = models.BooleanField(default=True)
    budget_eq = models.BooleanField(default=True)
    budget_op = models.BooleanField(default=True)

    instructions=models.TextField(max_length=4000,null=True)

    template = models.FileField(upload_to='rfp_templates',null=True,blank=True)
    logo = models.ImageField(upload_to='image',null=True,blank=True)

    project_questions = models.TextField(max_length = 4000, null=True, blank=True, verbose_name=u"Project questions (one question per line, maximum of 10 questions permitted.)")
    review_questions = models.TextField(max_length = 4000, null=True, blank=True, verbose_name=u"Review questions (one question per line, maximum of 10 questions permitted.)")

    email_template_project_confirmation = models.CharField(max_length=255,default='project_submission_confirmation_email_default',verbose_name=u"Email template for project submission confirmation.")
    email_template_review_invitation = models.CharField(max_length=255,default='review_invitation_email_default', verbose_name=u"Email template for invitation to review.")
    email_template_review_confirmation = models.CharField(max_length=255,default='review_submission_confirmation_email_default', verbose_name=u"Email template for confirmation and thank you for your review.")
    email_template_review_follow_up = models.CharField(max_length=255,default='review_follow_up_on_invitation_default', verbose_name=u"Email template for follow up with reviewer.")
    email_template_rfp_closed = models.CharField(max_length=255,default='project_results_anouncement_email_default', verbose_name=u"Email template to anounce results.")

    def __unicode__(self):
        return str(self.year) +  str(' ') + self.name

    def get_review_questions(self):
        list = self.review_questions.splitlines()
        b = tuple(list)
        return b

    def get_project_questions(self):
        list = self.project_questions.splitlines()
        b = tuple(list)
        return b

    def list_of_project(self):
        return Project.objects.filter(rfp=self)

    def project_count(self, s):
        n = Project.objects.filter(rfp = self, status = s).count()
        return n

    class Meta:
        verbose_name = "Call for proposal"
        verbose_name_plural = "Call for proposals"

class Project(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('submitted','Submitted'),
        ('granted','Granted'),
        ('not_granted','Not Granted'),
    )
    rfp=models.ForeignKey(RfpCampaign)
    name=models.CharField(max_length=255)
    user=models.ForeignKey(User,blank=True,null=True)
    starting_date=models.DateField(null=True)
    project_duration=models.IntegerField(null=True,blank=True)
    requested_amount=models.IntegerField(null=True)
    awarded_amount=models.IntegerField(blank=True,null=True)
    additional_funding = models.CharField(max_length = 4000, null = True, blank = True)
    keywords=models.CharField(max_length=4000,null=True,blank=True,verbose_name=U"Keywords")
    abstract=models.CharField(max_length=4000,null=True,blank=True,verbose_name=u"Abstract")
    document=models.FileField(upload_to='project',null=True,blank=True)
    status=models.CharField(max_length=255,default='draft',choices=STATUS_CHOICES)
    confirmation_email_sent = models.BooleanField(default=False)
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

    def __unicode__(self):
        return self.name

    def review_count(self):
        n = Review.objects.filter(project = self)
        return n

    def review_completed_count(self):
        n = Review.objects.filter(project = self, status = 'completed').count()
        return n

    def list_of_reviewers_id(self):
        l = list()
        reviews = Review.objects.filter(project = self)
        for r in reviews:
            l.append(r.user.id)
        return l

    def send_project_confirmation_email(self):
        """
        Send the confirmation email after the project has been successfully submitted. Set status to submitted.
        """
        if not self.confirmation_email_sent:
                c = {'project_name' : self.name, 'full_name' : self.user.first_name + str(" ") + self.user.last_name}
                send_mandrill_email(self,self.rfp.email_template_project_confirmation,c)

                c = {'project':self}
                conf_plain = render_to_string('rfp/email/project_admin_confirmation.txt',c)
                conf_html = render_to_string('rfp/email/project_admin_confirmation.html',c)

                send_mail('Project Submitted',
                          conf_plain, 'admin@icfrc.fr', ['admin@icfrc.fr','sgug@outlook.com'],
                          html_message=conf_html, fail_silently=False)

                self.status = 'submitted'
                self.confirmation_email_sent = True
                self.save()

    def send_results_email(self):
            """
            Send the project result email to PI including a link. Clicking the link log the user in and redirect to the project details page.
            """
            #Create the link with credentials
            from urlcrypt import lib as urlcrypt
            from django.core.urlresolvers import reverse
            project = Project.objects.get(id = self.id)
            token_accept = urlcrypt.generate_login_token(self.user, reverse('project_detail', args = [project.pk]))
            url_to_project = reverse('urlcrypt_redirect', args=(token_accept,))
            site = Site.objects.get(id=1)


            #Set the email template variables
            c = {'full_name' : self.user.first_name + str(" ") + self.user.last_name,
                 'project' : self.name, 'rfp_name' : self.rfp.name,
                 'url_to_project' : str(str(site.domain)+str(url_to_project))}

            #Send the Madrill email template
            send_mandrill_email(self,self.rfp.email_template_rfp_closed,c)

class ProposedReviewer(models.Model):
    TYPE_CHOICES = (
        ('ADMIN_PROPOSED','Proposed by Admin'),
        ('USER_PROPOSED', 'Proposed by User'),
        ('USER_EXCLUDED', 'Excluded Reviewer'),
        ('BOARD_SUGGESTED', 'Proposed by Board Member')
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
    invited = models.BooleanField(default=False)

    def __unicode__(self):
        return self.first_name + str(' ') + self.last_name + str(" - ") + self.institution

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

        #Check if the proposed reviewer is an existing user
        if self.is_user():
            user = User.objects.get(email=self.email)

        #If proposed reviewer is not a user yet
        if not self.is_user():
            import random
            username = self.first_name[:1] + self.last_name

            #Verify username is unused and set a new one if needed.
            while username_exists(username):
                    username = self.first_name[:1] + self.last_name
                    n = str(random.randint(1, 1000))
                    username = str(username + n)

                    if not username_exists(username):
                        break

            password = 'frc@2015'

            #Create new user.
            user = User.objects.create_user(username, self.email, password) #Create new user.
            user.save()
            user.first_name = self.first_name
            user.last_name = self.last_name
            user.save()

            #Add this user to Reviewer group
            g = Group.objects.get(name='Reviewer')
            g.user_set.add(user)

            #Update UserProfile with ProposedReviewer Information
            user_profile = UserProfile.objects.filter(user_id=user.id).update(first_name = self.first_name, last_name = self.last_name, organization = self.institution, address = self.address, city = self.city,
            state = self.state, country = self.country, zip = self.postcode)


        #Create the review for the user.
        review_tuple = Review.objects.get_or_create(user = user, project = self.project,  )
        review = review_tuple[0]

        #Send invitation to review the corresponding project.
        review.send_invitation_email_to_reviewer()

        return review

class BudgetLine(models.Model):
    project = models.ForeignKey(Project,null = True,editable=False)
    item = models.CharField(max_length = 255, null=True, blank=True)
    category = models.CharField(max_length = 255, null=True, blank=True)
    duration = models.IntegerField(null=True,blank=True)
    monthly_salary = models.IntegerField(null=True,blank=True)
    quote=models.FileField(upload_to='quotes',null=True,blank=True)
    amount = models.IntegerField(null=True, blank = True)

    def __unicode__(self):
        return  self.category + str(" ") + self.item

    def get_data(self):
        return model_to_dict(self)

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
    dropped = models.BooleanField(default=False)
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
    note = models.IntegerField(default=0)

    def __unicode__(self):
        return self.user.first_name + str(" ") + self.user.last_name + str(" for: ") + self.project.name

    def send_confirmation_email_to_reviewer(self):
        if not self.status == 'completed':
            c = {'full_name' : self.user.first_name + str(" ") + self.user.last_name, 'project_name': self.project.name, 'category_name' : self.project.rfp.category, 'category_year' : self.project.rfp.year}
            send_mandrill_email(self,self.project.rfp.email_template_review_confirmation,c)

            c = {'review' : self}
            conf_plain = render_to_string('rfp/email/review_admin_confirmation.txt',c)
            conf_html = render_to_string('rfp/email/review_admin_confirmation.html',c)

            send_mail('Review Submitted',
                      conf_plain, 'admin@icfrc.fr', ['admin@icfrc.fr','sgug@outlook.com'],
                      html_message=conf_html, fail_silently=False)

    def send_invitation_email_to_reviewer(self):
            """
            Send an invitation to review email including a link. Clicking the link log the user in and redirect to the review survey page.
            """

            #Create the link with credentials
            from urlcrypt import lib as urlcrypt
            from django.core.urlresolvers import reverse

            token_accept = urlcrypt.generate_login_token(self.user, reverse('post_review_waiver', args=[self.id]))
            token_refuse = urlcrypt.generate_login_token(self.user, reverse('post_review_waiver_refuse', args = [self.id]))
            url_accept = reverse('urlcrypt_redirect', args=(token_accept,))
            url_refuse = reverse('urlcrypt_redirect', args = (token_refuse,))
            site = Site.objects.get(id=1)


            #Set the email template variables
            c = {'username':self.user.username, 'reviewer_full_name' : self.user.get_full_name(), 'project' : self.project.name,
                 'author' : self.project.user.get_full_name(),
                 'abstract' : self.project.abstract, 'keywords':self.project.keywords,
                 'url_accept' : str(str(site.domain)+str(url_accept)),'url_refuse' : str(str(site.domain)+str(url_refuse))}

            #Send the Mandrill email template
            send_mandrill_email(self, self.project.rfp.email_template_review_invitation, c)

    def send_follow_up_invitation_email_to_reviewer(self):
            """
            Send the follow up email to reviewer including a link. Clicking the link log the user in and redirect to the project details page.
            """
            #Create the link with credentials

            from urlcrypt import lib as urlcrypt
            from django.core.urlresolvers import reverse
            project = Project.objects.get(id = self.project.id)
            token_accept = urlcrypt.generate_login_token(self.user, reverse('project_detail', args = [project.pk]))
            url_to_project = reverse('urlcrypt_redirect', args=(token_accept,))
            site = Site.objects.get(id=1)

            #Set the email template variables
            c = {'username':self.user.username,'reviewer_full_name' : self.user.first_name + str(" ") + self.user.last_name, 'project' : self.project.name,
                 'author' : self.project.user.first_name + str(' ') + self.project.user.last_name,
                 'abstract' : self.project.abstract, 'keywords':self.project.keywords,
                 'url_to_project' : str(str(site.domain)+str(url_to_project))}

            #Send the Madrill email template
            send_mandrill_email(self,self.project.rfp.email_template_review_follow_up,c)

class Tag(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)

class File_Test(models.Model):
    name=models.CharField(max_length=255)
    document=models.FileField(null=True)

#post_save.connect(send_project_confirmation_email,sender = Project)
#post_save.connect(set_review_as_completed, sender = Review)

