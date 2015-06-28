__author__ = 'Sylvestre'

from django import template
from rfp.models import Project,Review,RfpCampaign
from django.contrib.auth.models import User,Group,Permission

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