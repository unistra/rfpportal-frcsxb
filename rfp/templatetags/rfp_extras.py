__author__ = 'Sylvestre'

from django import template
from rfp.models import Project,Review,RfpCampaign
from django.contrib.auth.models import User,Group,Permission

register = template.Library()

@register.filter(name='count_project')
def count_project(self,s):
    """
    Give the number of project with the status s in the corresponding rfp.
    :param s: str self: Object
    :return: int
    """
    n = Project.objects.filter(rfp = self.id, status = s).count()
    return n