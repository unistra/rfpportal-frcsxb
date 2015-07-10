__author__ = 'Sylvestre'

from django import template
from rfp.models import Project,Review,RfpCampaign
from django.contrib.auth.models import User,Group,Permission
import datetime

register = template.Library()

@register.filter(name='reviews_breakdown')
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



@register.filter(name='count_review')
def count_review(self,s):
    """
    Give the number of review related to the project with the status s.
    :param s: str self: Object
    :return: int
    """
    n = Review.objects.filter(project = self.id, status = s).count()
    return n

@register.filter(name='number_invitation')
def number_invitation(self):
    """
    Return the number of created review for the considered user.
    :return: int
    """
    return Review.objects.filter(user=self.user.id).count()

@register.filter(name='number_completed')
def number_of_completed_review(self):
    """
    Return the number of completed review for the considered user.
    :return: int
    """
    return Review.objects.filter(user = self.user.id, status = 'completed').count()


@register.filter(name='is_pi')
def is_pi(self):
    return self.groups.filter(name = 'Principal_Investigator').exists()

@register.filter(name='is_rev')
def is_reviewer(self):
    return self.groups.filter(name = 'Reviewer').exists()


@register.filter(name='count_project')
def count_project(self,s):
    """
    Give the number of project with the status s in the corresponding rfp.
    :param s: str self: Object
    :return: int
    """
    n = Project.objects.filter(rfp = self.id, status = s).count()
    return n

@register.filter(name='count_review_rfp')
def count_review_rfp(self,s):
    """
    Give the number of review related to the project with the status s.
    :param s: str self: Object
    :return: int
    """
    n = Review.objects.filter(project__rfp = self, status = s).count()
    return n

@register.filter(name='total_requested')
def total_requested(self):
    """
    Total amount requested per Request for Proposal.
    :return: int
    """
    p = Project.objects.filter(rfp = self)
    n = 0
    for project in p :
        n += project.requested_amount

    return n

@register.filter(name='days_left')
def days_left(self):
    """
    Gives the number of days left before a Request for Proposal will close.
    :return: int
    """
    delta = self.deadline - datetime.date.today()
    n = delta.days

    return n