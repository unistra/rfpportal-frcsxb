__author__ = 'Sylvestre'

from models import UserProfile
from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from rfp.models import Project,RfpCampaign,Review,File_Test,ProposedReviewer,BudgetLine
from django.contrib.auth.models import User

class CreateUser(forms.Form):
    username = forms.CharField(max_length=30)
    first_name = forms.CharField()
    last_name = forms.CharField()
    password1=forms.CharField(max_length=30,widget=forms.PasswordInput()) #render_value=False
    password2=forms.CharField(max_length=30,widget=forms.PasswordInput())
    email=forms.EmailField(required=False)

    def clean_username(self): # check if username dos not exist before
        try:
            User.objects.get(username=self.cleaned_data['username']) #get user from user model
        except User.DoesNotExist :
            return self.cleaned_data['username']

        raise forms.ValidationError("this username exist already")


    def clean(self): # check if password 1 and password2 match each other
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:#check if both pass first validation
            if self.cleaned_data['password1'] != self.cleaned_data['password2']: # check if they match each other
                raise forms.ValidationError("Passwords do not match each other")

        return self.cleaned_data


    def save(self): # create new user
        new_user=User.objects.create_user(username=self.cleaned_data['username'],
                                        password=self.cleaned_data['password1'],
                                        email=self.cleaned_data['email'],
                                        )
        new_user.first_name = self.cleaned_data['first_name']
        new_user.last_name = self.cleaned_data['last_name']
        new_user.save()

        return new_user

class UserDetails(forms.Form):

    TITLE_CHOICES = (
        ('p', 'Pr.'),
        ('d', 'Dr.'),
        ('m', 'Mr.'),
        ('mm', 'Mrs.'),
    )

    username=forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password=forms.CharField(max_length=255,widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control'}))

    title = forms.ChoiceField(required=False,choices=TITLE_CHOICES)
    first_name=forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    organization = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class' : 'form-control'}))

    address = forms.CharField(required=False,max_length=255,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    zip = forms.CharField(max_length=255,required=False,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    city = forms.CharField(required=False,max_length=255,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    country = forms.CharField(required=False,max_length=255,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    is_pi = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'class' : 'form-control'}))
    is_reviewer = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'class' : 'form-control'}))

class UserUpdate(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ['user','is_pi','is_reviewer','title','reset_password']

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'organization' : forms.TextInput(attrs={'class':'form-control'}),
            'insitute_research_unit' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
            'zip' : forms.TextInput(attrs={'class':'form-control'}),
            'state' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'city' : forms.TextInput(attrs={'class':'form-control'}),
            'country' : forms.TextInput(attrs = {'class' : 'form-control'}),
        }

        labels = {
            'insitute_research_unit' : _('Reasearch Group/Unit:'),
            'state' : _('State/Region:'),
            'zip' : _('Postcode:')
        }

class RfpCreate(ModelForm):

    class Meta:
        model = RfpCampaign
        exclude = {}
        widget = {
           'review_questions': forms.Textarea(),
        }

class SearchForm(forms.Form):
    search = forms.CharField(max_length=255)

