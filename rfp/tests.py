from django.test import TestCase
from models import Project,Review,RequestForProposal,RfpCampaign
import os
# Create your tests here.


def new_project(project):
            np = Project.get(id=project)
            return np

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal_frc.settings")
    new_project(1)
