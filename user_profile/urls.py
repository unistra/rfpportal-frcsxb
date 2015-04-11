__author__ = 'Sylvestre'

from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^sign_up/$',views.create_profile,name='create_profile'),
    url(r'^profile/$',views.index_profile,name='user_profile'),
    url(r'^edit_profile/$',views.edit_profile,name='edit_profile'),

)

