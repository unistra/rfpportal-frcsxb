__author__ = 'Sylvestre'

print('file is running!')

from django.contrib.auth.models import User
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import Http404

from django.forms.models import model_to_dict
import datetime
import logging

from user_profile.models import UserProfile

from rfp.models import Project,Review,RfpCampaign,File_Test,ProposedReviewer,BudgetLine
from django.core.urlresolvers import reverse

self = Project.objects.get(id=2)
reviews = Review.objects.filter(project = self.id)

def reviews_breakdown(self):
    """
    Calculate the number of reviews per status.
    :return: dict.
    """
    statuses = Review.STATUS_CHOICES
    d = dict()

    for status in statuses:
        s = status[0]
        n = Review.objects.filter(project = self.id, status = s).count()
        d.update({s:n})

    return d

r = reviews_breakdown(self)
print r

