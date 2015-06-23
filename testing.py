__author__ = 'Sylvestre'

print('file is running!')


from django.db import models
from django.contrib.sites.models import Site
from user_profile.models import UserProfile
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import logging

from django.contrib.auth.models import User
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import Http404

from django.forms.models import model_to_dict
import datetime
import logging

from user_profile.models import UserProfile

from rfp.models import Project,Review,RfpCampaign,File_Test,ProposedReviewer,BudgetLine,send_mandrill_email
from django.core.urlresolvers import reverse

self = Review.objects.get(id=23)
site = Site.objects.get(id=1)

def send_invitation_email_to_reviewer(self):
        """
        Send invitation to review to a User, including a link with login credentials.
        :return:
        """
        from django.contrib.sites.shortcuts import get_current_site
        from urlcrypt import lib as urlcrypt
        from django.core.urlresolvers import reverse
        token_accept = urlcrypt.generate_login_token(self.user, reverse('post_review_waiver', args=[self.id]))
        url_accept = reverse('urlcrypt_redirect', args=(token_accept,))

        url_refuse = reverse('urlcrypt_redirect', args=(token_accept,))

        c = {'reviewer_full_name' : str(str(self.user.first_name) + " " + str(self.user.last_name)), 'project' : self.project.name,
             'author' : str(str(self.project.user.first_name) + str(self.project.user.last_name)),
             'abstract' : self.project.scope_of_work, 'keywords':self.project.purpose,
             'url_accept' : str(str(site.domain)+str(url_accept)),'url_refuse' : str(str(site.domain)+str(url_accept))}

        send_mandrill_email(self,self.project.rfp.email_template_review_invitation,c)

send_invitation_email_to_reviewer(self)
