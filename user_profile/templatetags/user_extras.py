__author__ = 'Sylvestre'

from django import template
from rfp.models import Project,Review,RfpCampaign,BudgetLine,ProposedReviewer,Tag
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

@register.filter(name='count_proposedreviewer')
def count_proposed_reviewer(self):
    """
    Give the number of review related to the project with the status s.
    :param s: str self: Object
    :return: int
    """
    n = ProposedReviewer.objects.filter(project = self.id,type = 'USER_PROPOSED').count()
    return n

@register.filter(name='number_invitation')
def number_invitation(self):
    """
    Return the number of created review for the considered user.
    :return: int
    """
    return Review.objects.filter(user=self.id).count()

@register.filter(name='number_completed')
def number_of_completed_review(self):
    """
    Return the number of completed review for the considered user.
    :return: int
    """
    return Review.objects.filter(user = self.id, status = 'completed').count()


@register.filter(name='is_pi')
def is_pi(self):
    return self.groups.filter(name = 'Principal_Investigator').exists()

@register.filter(name='is_rev')
def is_reviewer(self):
    return self.groups.filter(name = 'Reviewer').exists()

@register.filter(name='is_sb')
def is_cs(self):
    return self.groups.filter(name = 'Scientific_board').exists()


@register.filter(name='count_project')
def count_project(self,s):
    """
    Give the number of project with the status s in the corresponding rfp.
    :param s: str self: RfpCampaign
    :return: int
    """
    n = Project.objects.filter(rfp = self.id, status = s).count()
    return n

@register.filter(name='count_review_rfp')
def count_review_rfp(self,s):
    """
    Give the number of review related to the project with the status s.
    :param s: str self: Project
    :return: int
    """
    n = Review.objects.filter(project__rfp = self, status = s).count()
    return n

@register.filter(name='total_requested')
def total_requested(self):
    """
    Total amount requested per Request for Proposal.
    :param self: RfpCampaign
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

@register.filter(name='bl_total')
def bl_total(self,s):
    """
    Summ all budget lines amount of  category s for a project.
    :param s: str
    :return: int
    """
    total_budgeted = 0
    budget_list = BudgetLine.objects.filter(project = self, category = s)

    for line in budget_list :
        total_budgeted += line.amount

    return total_budgeted

@register.filter(name='awarded')
def awarded(self):
    """
    Sum all awarded amount for projects of the consid3red User.
    :param: User
    :return: int.
    """
    total_awarded = 0
    projects = Project.objects.filter(user = self)
    for p in projects:
        if p.awarded_amount is not None:
            total_awarded += p.awarded_amount

    return total_awarded

@register.filter(name='granted')
def granted(self):
    """
    Count the number of projects with status granted for the considered User.
    :param: User
    :return: int.
    """
    return Project.objects.filter(user=self,status='granted').count()

@register.filter(name='tag_list')
def get_project_tag(self):
    """
    Return the list of tag for the project.
    :return: QuerySet
    """
    return Tag.objects.filter(project=self)