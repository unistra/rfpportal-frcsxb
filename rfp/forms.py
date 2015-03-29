__author__ = 'Sylvestre'
from django import forms
from django.forms import ModelForm
from models import Project,RfpCampaign,RequestForProposal,Review

class  RequestForProposalForm(ModelForm):
    class Meta:
        model = RequestForProposal
        fields = ['name']

class ProjectForm(forms.Form):
    name = forms.CharField(max_length=255)
    rfp_id = forms.IntegerField()

class RfpCampaignForm(ModelForm):
    class Meta:
        model = RfpCampaign
        fields = ['name','year']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['name']

