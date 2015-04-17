__author__ = 'Sylvestre'
from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from models import Project,RfpCampaign,RequestForProposal,Review,File_Test

class  RequestForProposalForm(ModelForm):
    class Meta:
        model = RequestForProposal
        fields = ['name']

class ProjectForm(ModelForm):

    class Meta:
        model = Project
        exclude = {}
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'requested_amount' : forms.NumberInput(attrs={'class':'form-control'}),
            'starting_date' : forms.DateInput(attrs={'class':'form-control'}),
            'project_duration' : forms.NumberInput(attrs={'class':'form-control'}),
            'purpose' : forms.TextInput(attrs={'class':'form-control'}),
            'scope_of_work' : forms.Textarea(attrs={'class':'form-control'}),
            'anticipated_impact' : forms.Textarea(attrs={'class':'form-control'}),
            'document' : forms.FileInput(attrs={'class':'form-control'}),
            'rfp' : forms.Select(attrs={'class':'form-control'}),
            'user' : forms.Select(attrs={'class':'hide'})
        }

        labels = {
            'name' : _('Project Name:'),
            'requested_amount' : _('Requested Amount:'),
            'starting_date' : _('Planned starting date:'),
            'project_duration' : _('Project Duration (months):'),
            'purpose' : _('In less than 25 words, please indicate the purpose of the project:'),
            'scope_of_work' : _('Abstract:'),
            'anticipated_impact' : _('Anticipated Impact:'),
            'document' : _('Upload your document:'),
            'rfp' : _('Category:'),
            'user' : _(' ')
        }


class UpdateForm(ModelForm):

    class Meta:
        model = Project
        exclude = ['rfp','user']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'requested_amount' : forms.NumberInput(attrs={'class':'form-control'}),
            'starting_date' : forms.DateInput(attrs={'class':'form-control'}),
            'project_duration' : forms.NumberInput(attrs={'class':'form-control'}),
            #'ending_date' : forms.DateInput(attrs={'class':'form-control'}),

            'purpose' : forms.TextInput(attrs={'class':'form-control'}),
            'scope_of_work' : forms.Textarea(attrs={'class':'form-control'}),
            'anticipated_impact' : forms.Textarea(attrs={'class':'form-control'}),
            'document' : forms.FileInput(attrs={'class':'form-control'})
        }
        labels = {
            'name' : _('Name of the Project: '),
            'document' : _('Select a document to update the current file: '),
        }


class RfpCampaignForm(ModelForm):
    class Meta:
        model = RfpCampaign
        fields = ['name','year']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        exclude = {'user','project'}
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'question_1' : forms.Textarea(attrs={'class':'form-control'}),
            'question_2' : forms.Textarea(attrs={'class':'form-control'}),
            'date' : forms.DateInput(attrs={'class':'form-control'}),
            'document' : forms.FileInput(attrs={'class':'form-control'})
        }

class file_test (forms.Form):
    name=forms.CharField(label='File Name:',widget=forms.TextInput(attrs={'class':'form-control'}))
    document=forms.FileField(label='Upload your document: ',widget=forms.FileInput(attrs={'class':'form-control'}))
