__author__ = 'Sylvestre'
from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
#Create a new project
    url(r'^create_project/(?P<rfpId>\d+)/$',views.create_project,name='create_project'),
    url(r'^create_project_budget/(?P<projectId>\d+)/$',views.create_project_budget,name='create_project_budget'),
    url(r'^create_project_reviewers/(?P<projectId>\d+)/$',views.create_project_reviewer,name='create_project_reviewer'),
    url(r'^create_project_summary/(?P<projectId>\d+)/$',views.create_project_summary,name='create_project_summary'),
    url(r'^create_project_previous/(?P<projectId>\d+)/$',views.create_project_previous,name='create_project_previous'),
    url(r'^delete_project/(?P<projectId>\d+)/$',views.delete_project,name='delete_project'),
    #url(r'^final_project_submisson/(?P<projectId>\d+)/$',views.final_project_submisson,name='final_project_submisson'),

#Add new Budget Line to a Project
    url(r'^add_budget_eq/(?P<projectId>\d+)/$',views.add_budget_eq,name='add_budget_eq'),
    url(r'^add_budget_op/(?P<projectId>\d+)/$',views.add_budget_op,name='add_budget_op'),
    url(r'^add_budget_hr/(?P<projectId>\d+)/$',views.add_budget_hr,name='add_budget_hr'),

#Consult an existing Project
    url(r'^(?P<projectId>\d+)/$',views.project_detail,name='project_detail'),
    url(r'^(?P<projectId>\d+)/budget/$',views.project_detail_budget,name='project_budget'),
    url(r'^(?P<projectId>\d+)/reviewer/$',views.project_detail_reviewers,name='project_reviewer'),
    url(r'^(?P<projectId>\d+)/your_review/$',views.project_review,name='project_review'),
    url(r'^(?P<projectId>\d+)/recommendations/$',views.project_detail_recommendations,name='project_recommendations'),
    url(r'^(?P<reviewId>\d+)/view_review/$',views.view_review,name='view_review'),

#Edit existing Budget Line
    url(r'^edit_budget_hr/(?P<budgetlineId>\d+)/$',views.edit_budget_hr,name='edit_budget_hr'),
    url(r'^edit_budget_eq/(?P<budgetlineId>\d+)/$',views.edit_budget_eq,name='edit_budget_eq'),
    url(r'^edit_budget_op/(?P<budgetlineId>\d+)/$',views.edit_budget_op,name='edit_budget_op'),

#Edit an existing Project
    url(r'^edit_project/(?P<projectId>\d+)/$',views.edit_project,name='edit_project'),

#Propose Reviewer for an existing Project
    url(r'^edit_reviewer/(?P<proposedreviewerId>\d+)/$',views.edit_reviewer,name='edit_reviewer'),
    url(r'^add_unique_reviewer/(?P<projectId>\d+)/$',views.add_unique_reviewer,name='add_unique_reviewer'),

#Exclude Reviewer for an existing Project
    url(r'^edit_excluded_reviewer/(?P<proposedreviewerId>\d+)/$',views.edit_excluded_reviewer,name='edit_excluded_reviewer'),
    url(r'^exclude_unique_reviewer/(?P<projectId>\d+)/$',views.exclude_unique_reviewer,name='exclude_unique_reviewer'),

#Post a Review for an existing project
    url(r'^post_review/(?P<reviewId>\d+)/$',views.post_review,name='post_review'),
    url(r'^post_review_waiver/(?P<reviewId>\d+)/$',views.post_review_waiver,name='post_review_waiver'),
    url(r'^post_review_waiver_refuse/(?P<reviewId>\d+)/$',views.post_review_waiver_refuse,name='post_review_waiver_refuse'),

#List of open Call For Proposals
    url(r'^rfp/(?P<rfpcampaignId>\d+)/$',views.rfp_campaign,name='rfpcampaign_detail'),
    url(r'^rfp/$',views.list_of_call_for_proposal,name='rfp_list'),

#Redirect if lost
    url(r'^login_no_permission/$', views.no_permission, name='no_permission'),
    url(r'^no_permission/$', 'django.contrib.auth.views.login',{'template_name': 'registration/no_permission_login.html'},name='login_no_permission'),

#Testing
    url(r'^test/$',views.test,name='test'),
    url(r'^propose_reviewer/(?P<projectId>\d+)/$',views.propose_reviewer,name='propose_reviewer'),
    url(r'^proposed_reviewer_list/(?P<projectId>\d+)/$',views.prop_reviewer_list,name='prop_reviewer_list'),

)
