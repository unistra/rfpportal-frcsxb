__author__ = 'Sylvestre'
from django import forms

class sign_up(forms.Form):
    username=forms.CharField(max_length=255)
    password=forms.CharField(max_length=255,widget=forms.PasswordInput)
    email = forms.EmailField()

