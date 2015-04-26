__author__ = 'Sylvestre'
from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^create_project/$',views.create_project,name='create_project'),
    url(r'^(?P<projectId>\d+)/$',views.project_detail,name='project_detail'),
    url(r'^edit_project/(?P<projectId>\d+)/$',views.edit_project,name='edit_project'),
    url(r'^propose_reviewer/(?P<projectId>\d+)/$',views.propose_reviewer,name='propose_reviewer'),
    url(r'^edit_reviewer/(?P<proposedreviewerId>\d+)/$',views.edit_reviewer,name='edit_reviewer'),
    url(r'^proposed_reviewer_list/(?P<projectId>\d+)/$',views.prop_reviewer_list,name='prop_reviewer_list'),
    url(r'^post_review/(?P<projectId>\d+)/$',views.post_review,name='post_review'),
    url(r'^rfp/(?P<rfpcampaignId>\d+)/$',views.rfp_campaign,name='rfpcampaign_detail'),
    #url(r'^rfp/create_project/(?P<rfp>\d+)/$',views.create_project,name='create_project'),
    url(r'^rfp/$',views.rfp_list,name='rfp_list'),
    url(r'^file_test/$',views.test_file,name='file_test'),

    #url(r'^profile/$',views.,name='user_profile'),
)

