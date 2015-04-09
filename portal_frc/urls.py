from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'real_estate.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^user_profile/', include('user_profile.urls')),
    url(r'^project/', include('rfp.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('^', include('django.contrib.auth.urls',)),
    url(r'^/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'registration/logout.html'}),
    url(r'^/login/?next=/$', 'django.contrib.auth.views.login',),
    url(r'^$',views.index,name='home_page'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

