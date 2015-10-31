__author__ = 'Sylvestre'
from django import forms
from django.forms import ModelForm
from django.forms.models import modelformset_factory
from django.utils.translation import ugettext_lazy as _
from models import Project,RfpCampaign,Review,File_Test,ProposedReviewer,BudgetLine

category_choices = (
    ('OC', 'Operating Cost'),
    ('HR', 'Recruitment'),
    ('EQ', 'Equipment'),
)

ratings = (
    ('','----------'),
    ('Top 10', 'Top 10 % = High Priority'),
    ('Top 20', 'Top 20% = Somewhat High Priority'),
    ('Top 30', 'Top 30% = Average Priority'),
    ('Top 50', 'Top 50% = Low Priority'),
)

contract = (
    ('','----------'),
    ('PhD','PhD'),
    ('Post-Doc','Post-Doc'),
    ('Research Scientist', 'Research Scientist'),
    ('Technician', 'Technician'),
    ('Other', 'Other(master student,...)'),
)

class ReviewWaiverForm(forms.Form):
    CHOICES = (('True', 'Yes, I will review this project.',), ('False', 'No, I will not review this project.',))
    no_conflict = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)


from django.core.mail import send_mail,mail_admins
from portal_frc import settings

class ReviewWaiverContactForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)

    def save(self):
        mail_admins('Reviewer message', self.cleaned_data['message'])
        send_mail('A reviewer sent you a message', self.cleaned_data['message'], 'admin@icfrc.fr',
        ['admin@icfrc.fr'], fail_silently=False)


class ProjectFormModel(ModelForm):

    class Meta:
        model = Project
        exclude = {'status','confirmation_email_sent', 'awarded_amount','user'}
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'requested_amount' : forms.NumberInput(attrs={'class':'form-control'}),
            'starting_date' : forms.DateInput(attrs={'class':'form-control'}),
            'project_duration' : forms.NumberInput(attrs={'class':'form-control'}),
            'purpose' : forms.TextInput(attrs={'class':'form-control'}),
            'scope_of_work' : forms.Textarea(attrs={'class':'form-control'}),
            'anticipated_impact' : forms.Textarea(attrs={'class':'form-control'}),
            'document' : forms.FileInput(attrs={'class':'form-control'}),
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
            'additional_funding' : _('Additional co-funding, if any (please specify funding body and amount):')
        }


class ProjectForm(forms.Form):

        name=forms.CharField(required=True, label = 'Project title:', widget=forms.TextInput(attrs={'class':'form-control'}))
        starting_date=forms.DateField(required=True, label = 'Starting Date:', widget=forms.DateInput(attrs={'class':'form-control'}))
        project_duration=forms.IntegerField(label='Duration (months):',widget=forms.DateInput(attrs={'class':'form-control'}))
        requested_amount=forms.IntegerField(required=True, label = 'Requested amount (Eur.):',widget=forms.NumberInput(attrs={'class':'form-control'}))
        keywords = forms.CharField(required=True, label = 'Keywords (10 max.):',widget=forms.TextInput(attrs={'class':'form-control'}))
        abstract = forms.CharField(max_length=1000,required=True, label ='Abstract (1000 characters max.):', widget=forms.Textarea(attrs={'class' : 'form-control'}))
        document = forms.FileField(label='Upload your document:',required=False)

        def __init__(self, *args, **kwargs):
            questions = kwargs.pop('questions')
            super(ProjectForm,self).__init__(*args, **kwargs)

            for i, label in enumerate(questions):
                self.fields['custom_%s' % i] = forms.CharField(label=label,required=False,widget=forms.Textarea(attrs={'class':'form-control'}))

        def extra_answers(self):
            for name, value in self.cleaned_data.items():
                if name.startswith('custom_'):
                    yield (self.fields[name].label, value)

class UpdateForm(ModelForm):

    class Meta:
        model = Project
        exclude = ['rfp','user','status','confirmation_email_sent','awarded_amount']
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
            'additional_funding' : forms.Textarea(attrs={'class':'form-control'}),

        }
        labels = {
            'name' : _('Project Title:'),
            'requested_amount' : _('Requested amount from FRC:'),
            'starting_date' : _('Planned starting date:'),
            'project_duration' : _('Expected duration of project (months):'),
            'purpose' : _('Keywords relating to project (10 max.):'),
            'scope_of_work' : _('Abstract (300 words max.):'),
            'anticipated_impact' : _('Link with other existing projects:'),

            'rfp' : _('Category:'),
            'user' : _(' '),
            'additional_funding' : _('Additional co-funding, if any (please specify funding body and amount):'),
            'document' : _('Select a document to update the current file: ')
        }

class DashboardEditForm(ModelForm):

    class Meta:
        model = Project
        exclude = {'rfp','user',}
        widgets = {
            'custom_0' : forms.Textarea(attrs={'class':'form-control'}),
            'custom_1' : forms.Textarea(attrs={'class':'form-control'}),
            'custom_2' : forms.Textarea(attrs={'class':'form-control'}),
            'custom_3' : forms.Textarea(attrs={'class':'form-control'}),
            'custom_4' : forms.Textarea(attrs={'class':'form-control'}),
            'custom_5' : forms.Textarea(attrs={'class':'form-control'}),
            'custom_6' : forms.Textarea(attrs={'class':'form-control'}),
            'custom_7' : forms.Textarea(attrs={'class':'form-control'}),
            'custom_8' : forms.Textarea(attrs={'class':'form-control'}),
            'custom_9' : forms.Textarea(attrs={'class':'form-control'}),
            'abstract' : forms.Textarea(attrs={'class':'form-control'}),
        }

class RfpCampaignForm(ModelForm):
    class Meta:
        model = RfpCampaign
        fields = ['name','year']
        widgets = {
            'deadline' : forms.DateInput(attrs={'class':'form-control'}),
            'starting_date' : forms.DateInput(attrs={'class':'form-control'}),
        }

class ReviewForm(forms.Form):
    rating = forms.ChoiceField(required=True,choices = ratings,label='Overall scientific priority of the proposal based on the following scale (proposals rated in the upper 20% are more likely to be accepted for funding)', widget=forms.Select(attrs={'class':'form-control'}))

    def __init__(self, *args, **kwargs):
            questions = kwargs.pop('questions')
            super(ReviewForm,self).__init__(*args, **kwargs)

            for i, label in enumerate(questions):
                self.fields['custom_%s' % i] = forms.CharField(label=label,required=False,widget=forms.Textarea(attrs={'class':'form-control'}))

    def extra_answers(self):
        for name, value in self.cleaned_data.items():
            if name.startswith('custom_'):
                yield (self.fields[name].label, value)

class ProposedReviewerForm(ModelForm):
    first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = ProposedReviewer
        exclude = {'project','type','invited'}
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
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = ProposedReviewer
        exclude = {'project','type','address','state','postcode','invited'}
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
        'quote' : _('Quote')
        }

class BudgetLineHR(ModelForm):


    item = forms.CharField(required=True,label='Contract Type (PhD, Post-doc...)', widget=forms.Select(choices=contract,attrs={'class':'form-control'}))
    amount = forms.FloatField(required=True,label='Amount (Eur.)', widget=forms.NumberInput(attrs={'class':'form-control','readonly':''}))
    duration = forms.IntegerField(required=True,label='Duration (months)',widget=forms.NumberInput(attrs={'class':'form-control'}))
    monthly_salary = forms.IntegerField(required=True,label='Monthly Salary (Eur.)',widget=forms.NumberInput(attrs={'class':'form-control'}))

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
        'duration' : _('Duration (months)'),
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
        }


class ReviewRankForm(forms.Form):
    RATE=(
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    rank = forms.IntegerField(required=True,label='Rate this review: ',widget=forms.Select(choices=RATE))


class file_test (forms.Form):
    name=forms.CharField(label='File Name:',widget=forms.TextInput(attrs={'class':'form-control'}))
    document=forms.FileField(label='Upload your document: ',widget=forms.FileInput(attrs={'class':'form-control'}))
