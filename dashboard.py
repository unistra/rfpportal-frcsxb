"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'rfpportal.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name

class CustomIndexDashboard(Dashboard):
    """
    #Custom index dashboard for www.
    """

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

         # append an app list module for "Administration"
        self.children.append(modules.ModelList(
            title = _('User Administration'),
            column=1,
            collapsible=False,
            models=('django.contrib.*',),
        ))



        # append a group for "Administration" & "Applications"
        """
        self.children.append(modules.Group(
            title=_('Administration'),
            column=1,
            collapsible=True,
            children = [

                modules.AppList(
                    _('Administration'),
                    column=1,
                    collapsible=False,
                    models=('django.contrib.*',),
                ),


                modules.AppList(
                    _('Contacts'),
                    column=0,
                    css_classes=('collapse closed',),
                    exclude=('django.contrib.*',
                             'rfp.models.*'),
                )
            ]



        ))
        """

        # append an app list module for "Applications"
        self.children.append(modules.Group(
            title = _('Portal Management'),
            column=1,
            collapsible=True,
            children = [

                modules.ModelList(
                title = 'Proposals',
                css_classes=('collapse closed',),
                models = ('rfp.models.Project','rfp.models.Review'),
                exclude=('django.contrib.*',),),

                modules.ModelList(
                title = 'Call for Proposals',
                css_classes=('collapse closed',),
                models = ('rfp.models.RequestForProposal','rfp.models.RfpCampaign','rfp.models.ProposedReviewer'),
                exclude=('django.contrib.*',),),

                modules.ModelList(
                title = 'Contact Management',
                css_classes=('collapse closed',),
                models=('user_profile.models.UserProfile',),)

                ]
        ))



        
        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Media Management'),
            column=2,
            children=[
                {
                    'title': _('FileBrowser'),
                    'url': '/admin/filebrowser/browse/',
                    'external': False,
                },
            ]
        ))
        
        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Support'),
            column=2,
            children=[
                {
                    'title': _('Django Documentation'),
                    'url': 'http://docs.djangoproject.com/',
                    'external': True,
                },
                {
                    'title': _('Grappelli Documentation'),
                    'url': 'http://packages.python.org/django-grappelli/',
                    'external': True,
                },
                {
                    'title': _('Grappelli Google-Code'),
                    'url': 'http://code.google.com/p/django-grappelli/',
                    'external': True,
                },
                {
                    'title': _('Contact the webmaster'),
                    'url': 'mailto:sylvestre.gug@gmail.com',
                    'external': True,
                },
            ]
        ))

        """
        # append a feed module
        self.children.append(modules.Feed(
            _('Latest Django News'),
            column=2,
            feed_url='http://www.djangoproject.com/rss/weblog/',
            limit=5
        ))
        """
        
        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=3,
        ))


