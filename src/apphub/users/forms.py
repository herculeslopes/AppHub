from django import forms

from .models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'signup-form-input'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'signup-form-input'}))

class UserSignupForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'signup-form-input'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'signup-form-input'}))
    password_confirmation = forms.CharField(widget=forms.TextInput(attrs={'class': 'signup-form-input'}))