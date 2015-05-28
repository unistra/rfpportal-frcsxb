__author__ = 'Sylvestre'
from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^create_project/$',views.create_project,name='create_project'),
    url(r'^(?P<projectId>\d+)/$',views.project_detail,name='project_detail'),
    url(r'^(?P<projectId>\d+)/budget/$',views.project_detail_budget,name='project_budget'),
    url(r'^(?P<projectId>\d+)/reviewer/$',views.project_detail_reviewers,name='project_reviewer'),

    url(r'^add_budget_eq/(?P<projectId>\d+)/$',views.add_budget_eq,name='add_budget_eq'),
    url(r'^add_budget_op/(?P<projectId>\d+)/$',views.add_budget_op,name='add_budget_op'),
    url(r'^add_budget_hr/(?P<projectId>\d+)/$',views.add_budget_hr,name='add_budget_hr'),

    url(r'^edit_budget_hr/(?P<budgetlineId>\d+)/$',views.edit_budget_hr,name='edit_budget_hr'),
    url(r'^edit_budget_eq/(?P<budgetlineId>\d+)/$',views.edit_budget_eq,name='edit_budget_eq'),
    url(r'^edit_budget_op/(?P<budgetlineId>\d+)/$',views.edit_budget_op,name='edit_budget_op'),


    url(r'^edit_project/(?P<projectId>\d+)/$',views.edit_project,name='edit_project'),
    url(r'^propose_reviewer/(?P<projectId>\d+)/$',views.propose_reviewer,name='propose_reviewer'),
    url(r'^edit_reviewer/(?P<proposedreviewerId>\d+)/$',views.edit_reviewer,name='edit_reviewer'),
    url(r'^edit_excluded_reviewer/(?P<proposedreviewerId>\d+)/$',views.edit_excluded_reviewer,name='edit_excluded_reviewer'),
    url(r'^add_unique_reviewer/(?P<projectId>\d+)/$',views.add_unique_reviewer,name='add_unique_reviewer'),
    url(r'^exclude_unique_reviewer/(?P<projectId>\d+)/$',views.exclude_unique_reviewer,name='exclude_unique_reviewer'),

    url(r'^proposed_reviewer_list/(?P<projectId>\d+)/$',views.prop_reviewer_list,name='prop_reviewer_list'),
    url(r'^post_review/(?P<projectId>\d+)/$',views.post_review,name='post_review'),
    url(r'^rfp/(?P<rfpcampaignId>\d+)/$',views.rfp_campaign,name='rfpcampaign_detail'),
    url(r'^rfp/$',views.list_of_call_for_proposal,name='rfp_list'),
    url(r'^file_test/$',views.test_file,name='file_test'),
)
