__author__ = 'Sylvestre'
from django import forms
from models import UserProfile
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class sign_up(forms.Form):

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
    zip = forms.IntegerField(required=False,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    city = forms.CharField(required=False,max_length=255,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    country = forms.CharField(required=False,max_length=255,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    is_pi = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'class' : 'form-control'}))
    is_reviewer = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'class' : 'form-control'}))

class UserUpdate(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ['user','is_pi','is_reviewer','title']

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

