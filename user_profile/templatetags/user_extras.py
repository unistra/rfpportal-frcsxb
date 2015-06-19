__author__ = 'Sylvestre'

from django import template
from rfp.models import Project,Review,RfpCampaign

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
