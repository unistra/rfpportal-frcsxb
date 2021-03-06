__author__ = 'Sylvestre'

from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',

    url(r'^sign_up/$',views.create_profile,name='create_profile'),
    url(r'^profile/$',views.index_profile,name='user_profile'),
    url(r'^edit_profile/$',views.edit_profile,name='edit_profile'),
    url(r'^welcome/$',views.post_homepage_login_landing_page,name='post_homepage_login_landing_page'),

    #user_dashboard and Admin controls
    url(r'^dashboard/$',views.dashboard,name='dashboard'),
    url(r'^dashboard/dashboard_rfp_listing/$',views.dashboard_rfp_listing,name='dashboard_rfp_listing'),
    url(r'^dashboard/dashboard_rfp_details/(?P<rfpId>\d+)/$',views.dashboard_rfp_details,name='dashboard_rfp_details'),


    url(r'^dashboard/dashboard_project_details/(?P<projectId>\d+)/$',views.dashboard_project_details,name='dashboard_project_details'),
    url(r'^dashboard/dashboard_project_list/$',views.dashboard_project_list,name='dashboard_project_list'),
    url(r'^dashboard/dashboard_create_rfp/$',views.dashboard_create_rfp,name='dashboard_create_rfp'),
    url(r'^dashboard/dashboard_edit_rfp/(?P<rfpId>\d+)/$',views.dashboard_edit_rfp,name='dashboard_edit_rfp'),
    url(r'^dashboard/dashboard_reviewers_list/$',views.dashboard_reviewers_list,name='dashboard_reviewers_list'),
    url(r'^dashboard/dashboard_reviewer_detail/(?P<reviewerId>\d+)/$',views.dashboard_reviewer_detail,name='dashboard_reviewer_detail'),
    url(r'^dashboard/dashboard_review_list/$',views.dashboard_review_list,name='dashboard_review_list'),
    url(r'^dashboard/dashboard_add_admin_proposed_reviewer/(?P<projectId>\d+)/$',views.dashboard_add_admin_proposed_reviewer,name='dashboard_add_admin_proposed_reviewer'),
    url(r'^dashboard/dashboard_invite_reviewer/(?P<propRId>\d+)/$',views.dashboard_invite_reviewer,name='dashboard_invite_reviewer'),
    url(r'^dashboard/dashboard_follow_up_with_reviewer/(?P<reviewId>\d+)/$',views.dashboard_follow_up_with_reviewer,name='dashboard_follow_up_with_reviewer'),
    url(r'^dashboard/dashboard_send_results/(?P<projectId>\d+)/$',views.dashboard_send_results,name='dashboard_send_results'),
    url(r'^dashboard/dashboard_pi_list/$',views.dashboard_pi_list,name='dashboard_pi_list'),
    url(r'^dashboard/dashboard_pi_details/(?P<userId>\d+)/$',views.dashboard_pi_details,name='dashboard_pi_details'),

    url(r'^dashboard/dashboard_project_edit/(?P<projectId>\d+)/$',views.dashboard_project_edit,name='dashboard_project_edit'),
    url(r'^dashboard/dashboard_pi_create/$',views.dashboard_pi_create,name='dashboard_pi_create'),
    url(r'^dashboard/reset_pwd/(?P<UserId>\d+)/$',views.reset_pwd,name='reset_pwd'),
    url(r'^dashboard/dashboard_edit_profile/(?P<userId>\d+)/$',views.dashboard_edit_profile,name='dashboard_edit_profile'),

    #Scientific Board pages
    url(r'^scib/project_details/(?P<projectId>\d+)/$',views.scientific_board_project_details,name='scientific_board_project_details'),
    url(r'^scib/project_details/archives/$',views.scientific_board_project_archives,name='scientific_board_project_archives'),
    url(r'^scib/project_details/add_tag/(?P<projectId>\d+)/$',views.add_tag,name='add_tag'),
    url(r'^scib/project_details/remove_tag/(?P<projectId>\d+)/$',views.remove_tag,name='remove_tag')
)
