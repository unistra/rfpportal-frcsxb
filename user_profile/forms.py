__author__ = 'Sylvestre'
from django import forms

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

    address = forms.CharField(required=False,max_length=255,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    zip = forms.IntegerField(required=False,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    city = forms.CharField(required=False,max_length=255,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    country = forms.CharField(required=False,max_length=255,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    is_pi = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'class' : 'form-control'}))
    is_reviewer = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'class' : 'form-control'}))

