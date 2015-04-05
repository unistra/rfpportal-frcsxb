__author__ = 'Sylvestre'
from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^create_project/$',views.create_project,name='create_project'),
    url(r'^(?P<projectId>\d+)/$',views.project_detail,name='project_detail'),
    url(r'^rfp/(?P<rfpcampaignId>\d+)/$',views.rfp_campaign,name='rfpcampaign_detail'),
    url(r'^rfp/$',views.rfp_list,name='rfp_list'),

    #url(r'^profile/$',views.,name='user_profile'),
)

