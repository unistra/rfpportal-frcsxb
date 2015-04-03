__author__ = 'Sylvestre'
from django import forms
from django.forms import ModelForm
from models import Project,RfpCampaign,RequestForProposal,Review

class  RequestForProposalForm(ModelForm):
    class Meta:
        model = RequestForProposal
        fields = ['name']

class ProjectForm(forms.Form):
    name = forms.CharField(label='Project Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    requested_amount=forms.IntegerField(label='Requested Amount ($)',widget=forms.NumberInput(attrs={'class':'form-control'}))
    starting_date=forms.DateField(label='Planned starting date',widget=forms.DateInput(attrs={'class':'form-control'}))
    project_duration=forms.IntegerField(label='Project Duration (months)',widget=forms.NumberInput(attrs={'class':'form-control'}))
    ending_date=forms.DateField(label='Ending date',widget=forms.DateInput(attrs={'class':'form-control'}))

    purpose=forms.CharField(label='In less than 25 words, please indicate the purpose of the project',widget=forms.TextInput(attrs={'class':'form-control'}))
    scope_of_work=forms.CharField(label='Indicate the scope of work (400 words max.)',widget=forms.Textarea(attrs={'class':'form-control'}))
    anticipated_impact=forms.CharField(label='Indicate the anticipated impact (400 words max.)',widget=forms.Textarea(attrs={'class':'form-control'}))
    rfp_id = forms.IntegerField()

    class Meta:
        model=Project

class RfpCampaignForm(ModelForm):
    class Meta:
        model = RfpCampaign
        fields = ['name','year']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['name']

