from django import forms
from .models import *
class RegistrationForm(forms.ModelForm):
    email = forms.CharField(label='Email', widget=forms.EmailInput)
    login = forms.CharField(label='Login', widget=forms.TextInput)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = Registration
        exclude = ['']


