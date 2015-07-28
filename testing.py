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

from django.contrib.auth.models import User,Group
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import Http404

from django.forms.models import model_to_dict
import datetime
import logging

from user_profile.models import UserProfile

from rfp.models import Project,Review,RfpCampaign,File_Test,ProposedReviewer,BudgetLine,send_mandrill_email
from rfp.views import is_reviewer
from django.core.urlresolvers import reverse

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


g = Group.objects.get(name='Principal_Investigator')
n = g.user_set.count()



