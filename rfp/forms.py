__author__ = 'Sylvestre'
from django import forms
from django.forms import ModelForm
from django.forms.models import modelformset_factory
from django.utils.translation import ugettext_lazy as _
from models import Project,RfpCampaign,Review,File_Test,ProposedReviewer,BudgetLine

class ProjectForm(ModelForm):

    class Meta:
        model = Project
        exclude = {'status','confirmation_email_sent'}
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
        exclude = ['rfp','user','status','confirmation_email_sent']
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
        exclude = {'user','project','name','date'}
        widgets = {
            'question_1' : forms.Textarea(attrs={'class':'form-control'}),
            'question_2' : forms.Textarea(attrs={'class':'form-control'}),
            'document' : forms.FileInput(attrs={'class':'form-control'})
        }
        labels = {
            'question_1' : _('Describe innovation'),
            'question_2' : _('Describe outputs and impact on subject'),
        }

class ProposedReviewerForm(ModelForm):
    first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = ProposedReviewer
        exclude = {'project','type'}
        widgets = {
            'institution' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
            'city' : forms.TextInput(attrs={'class':'form-control'}),
            'state' : forms.TextInput(attrs={'class':'form-control'}),
            'postcode' : forms.TextInput(attrs={'class':'form-control'}),
            'country' : forms.TextInput(attrs={'class':'form-control'}),
        }

class ExcludedReviewerForm(ModelForm):
    first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = ProposedReviewer
        exclude = {'project','type','email','address','state','postcode'}
        widgets = {
            'institution' : forms.TextInput(attrs={'class':'form-control'}),
            'city' : forms.TextInput(attrs={'class':'form-control'}),
            'country' : forms.TextInput(attrs={'class':'form-control'}),
        }


ProposedReviewerFormSet = modelformset_factory(
            ProposedReviewer,
            exclude = {'project'},
            widgets = {
            #'project' : forms.TextInput(attrs={'class':'hide', 'default' : '{{ project.id }}'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'institution' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
            'city' : forms.TextInput(attrs={'class':'form-control'}),
            'state' : forms.TextInput(attrs={'class':'form-control'}),
            'postcode' : forms.TextInput(attrs={'class':'form-control'}),
            'country' : forms.TextInput(attrs={'class':'form-control'}),
        },
            labels = {
                'project' : _('do_not_show')
            },
            extra = 3,
                                               )
category_choices = (
    ('OC', 'Operating Cost'),
    ('HR', 'Recruitment'),
    ('EQ', 'Equipment'),
)

class BudgetLineForm(ModelForm):
    item = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    amount = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={'class':'form-control'}))

    class Meta:
        model = BudgetLine
        exclude = {'project','category'}
        widgets = {
        }
        labels = {
        'item' : _('Item'),
        'amount' : _('Amount'),
        'category' : _('Category'),
        'project' : _(' ')
        }

class BudgetLineEQ(ModelForm):
    item = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    amount = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={'class':'form-control'}))

    class Meta:
        model = BudgetLine
        exclude = {'project','category','monthly_salary','duration'}
        widgets = {
        'item' : forms.TextInput(attrs={'class':'form-control'}),
        'amount' : forms.NumberInput(attrs={'class':'form-control'}),
        'quote' : forms.FileInput(attrs={'class':'form-control'}),
        }
        labels = {
        'item' : _('Item'),
        'amount' : _('Amount'),
        'category' : _('Category'),
        'quote' : _('Quote')
        }

class BudgetLineHR(ModelForm):
    item = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    amount = forms.FloatField(required=True,widget=forms.NumberInput(attrs={'class':'form-control'}))
    duration = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={'class':'form-control'}))
    monthly_salary = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={'class':'form-control'}))

    class Meta:
        model = BudgetLine
        exclude = {'project','category','quote'}
        widgets = {
        'item' : forms.TextInput(attrs={'class':'form-control'}),
        'duration' : forms.NumberInput(attrs={'class':'form-control'}),
        'monthly_salary' : forms.NumberInput(attrs={'class':'form-control'}),
        'amount' : forms.NumberInput(attrs={'class':'form-control'}),
        }
        labels = {
        'item' : _('Contract Type (PhD, Post-doc...)'),
        'amount' : _('Total'),
        'duration' : _('Duration'),
        'monthly_salary' : _("Monthly Salary")
        }

class BudgetLineOP(ModelForm):
    item = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    amount = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={'class':'form-control'}))

    class Meta:
        model = BudgetLine
        exclude = {'project','category','quote','duration','monthly_salary'}
        widgets = {
        'item' : forms.TextInput(attrs={'class':'form-control'}),
        'amount' : forms.NumberInput(attrs={'class':'form-control'}),
        }
        labels = {
        'item' : _('Item'),
        'amount' : _('Amount'),
        'category' : _('Category'),
        'project' : _(' ')
        }


OCBudgetLineFormSet = modelformset_factory(
    BudgetLine,

    exclude = {'project','category'},
    widgets = {
        'item' : forms.TextInput(attrs={'class':'form-control'}),
        'amount' : forms.NumberInput(attrs={'class':'form-control'}),
    },
    labels = {
        'item' : _('Item'),
        'amount' : _('Amount'),
    },
    extra = 3,
    max_num = 5,
    can_delete= True,
)

EQBudgetLineFormSet = modelformset_factory(
    BudgetLine,

    exclude = {'project','category'},
    widgets = {
        'item' : forms.TextInput(attrs={'class':'form-control'}),
        'amount' : forms.NumberInput(attrs={'class':'form-control'}),
    },
    labels = {
        'item' : _('Item'),
        'amount' : _('Amount'),
    },
    extra = 3,
    max_num = 5,
    can_delete= True,
)

HRBudgetLineFormSet = modelformset_factory(
    BudgetLine,
    exclude = {'project','category'},
    widgets = {
        'item' : forms.TextInput(attrs={'class':'form-control'}),
        'amount' : forms.NumberInput(attrs={'class':'form-control'}),
    },
    labels = {
        'item' : _('Item'),
        'amount' : _('Amount'),
    },
    extra = 3,
    max_num = 5,
    can_delete= True,
)

class file_test (forms.Form):
    name=forms.CharField(label='File Name:',widget=forms.TextInput(attrs={'class':'form-control'}))
    document=forms.FileField(label='Upload your document: ',widget=forms.FileInput(attrs={'class':'form-control'}))
