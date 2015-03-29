__author__ = 'Sylvestre'
from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^create_project/$',views.create_project,name='create_project'),
    #url(r'^profile/$',views.,name='user_profile'),
)

