__author__ = 'Sylvestre'
from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from models import Project,RfpCampaign,RequestForProposal,Review,File_Test

class  RequestForProposalForm(ModelForm):
    class Meta:
        model = RequestForProposal
        fields = ['name']

class ProjectForm(forms.Form):
    name = forms.CharField(label='Project Name:',widget=forms.TextInput(attrs={'class':'form-control'}))
    requested_amount=forms.IntegerField(label='Requested Amount ($):',widget=forms.NumberInput(attrs={'class':'form-control'}))
    starting_date=forms.DateField(label='Planned starting date:',widget=forms.DateInput(attrs={'class':'form-control'}))
    project_duration=forms.IntegerField(label='Project Duration (months):',widget=forms.NumberInput(attrs={'class':'form-control'}))
    ending_date=forms.DateField(label='Ending date:',widget=forms.DateInput(attrs={'class':'form-control'}))

    purpose=forms.CharField(label='In less than 25 words, please indicate the purpose of the project:',widget=forms.TextInput(attrs={'class':'form-control'}))
    scope_of_work=forms.CharField(label='Indicate the scope of work (400 words max.):',widget=forms.Textarea(attrs={'class':'form-control'}))
    anticipated_impact=forms.CharField(label='Indicate the anticipated impact (400 words max.):',widget=forms.Textarea(attrs={'class':'form-control'}))
    document=forms.FileField(label='Upload your document: ',widget=forms.FileInput(attrs={'class':'form-control'}))
    rfp_id = forms.IntegerField(label='',widget=forms.NumberInput(attrs={'class':'hide'}))

    class Meta:
        model=Project

class UpdateForm(ModelForm):

    class Meta:
        model = Project
        exclude = ['rfp','user']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'requested_amount' : forms.NumberInput(attrs={'class':'form-control'}),
            'starting_date' : forms.DateInput(attrs={'class':'form-control'}),
            'project_duration' : forms.NumberInput(attrs={'class':'form-control'}),
            'ending_date' : forms.DateInput(attrs={'class':'form-control'}),

            'purpose' : forms.TextInput(attrs={'class':'form-control'}),
            'scope_of_work' : forms.Textarea(attrs={'class':'form-control'}),
            'anticipated_impact' : forms.Textarea(attrs={'class':'form-control'}),
            'document' : forms.FileInput(attrs={'class':'form-control'})
        }
        labels = {
            'name' : _('Name of the Poject: '),
            'document' : _('Select a document to update the current file: '),
        }


class RfpCampaignForm(ModelForm):
    class Meta:
        model = RfpCampaign
        fields = ['name','year']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['name']

class file_test (forms.Form):
    name=forms.CharField(label='File Name:',widget=forms.TextInput(attrs={'class':'form-control'}))
    document=forms.FileField(label='Upload your document: ',widget=forms.FileInput(attrs={'class':'form-control'}))
