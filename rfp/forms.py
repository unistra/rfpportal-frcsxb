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
            'user' : forms.Select(attrs={'class':'hide'}),
            'ending_date' : forms.DateInput(attrs={'class':'form-control'}),
            'additional_funding' : forms.Textarea(attrs={'class':'form-control'}),
        }

        labels = {
            'name' : _('Project Title:'),
            'requested_amount' : _('Requested amount from FRC:'),
            'starting_date' : _('Planned starting date:'),
            'ending_date' : _('Ending date:'),
            'project_duration' : _('Expected duration of project (months):'),
            'purpose' : _('Keywords relating to project (10 max.):'),
            'scope_of_work' : _('Abstract (300 words max.):'),
            'anticipated_impact' : _('Link with other existing projects:'),
            'document' : _('Upload your document:'),
            'rfp' : _('Category:'),
            'user' : _(' '),
            'additional_funding' : _('Additional co-funding, if any (please specify funding body and amount):')
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
            'purpose' : forms.TextInput(attrs={'class':'form-control'}),
            'scope_of_work' : forms.Textarea(attrs={'class':'form-control'}),
            'anticipated_impact' : forms.Textarea(attrs={'class':'form-control'}),
            'document' : forms.FileInput(attrs={'class':'form-control'}),
            'rfp' : forms.Select(attrs={'class':'form-control'}),
            'user' : forms.Select(attrs={'class':'hide'}),
            'ending_date' : forms.DateInput(attrs={'class':'form-control'}),
            'additional_funding' : forms.Textarea(attrs={'class':'form-control'}),

        }
        labels = {
            'name' : _('Project Title:'),
            'requested_amount' : _('Requested amount from FRC:'),
            'starting_date' : _('Planned starting date:'),
            'ending_date' : _('Ending date:'),
            'project_duration' : _('Expected duration of project (months):'),
            'purpose' : _('Keywords relating to project (10 max.):'),
            'scope_of_work' : _('Abstract (300 words max.):'),
            'anticipated_impact' : _('Link with other existing projects:'),

            'rfp' : _('Category:'),
            'user' : _(' '),
            'additional_funding' : _('Additional co-funding, if any (please specify funding body and amount):'),
            'document' : _('Select a document to update the current file: ')
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
