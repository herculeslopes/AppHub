from dataclasses import field
from django import forms

from .models import User


# class UserLoginForm(forms.Form):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'signup-form-input'}))
#     password = forms.CharField(widget=forms.TextInput(attrs={'class': 'signup-form-input'}))


class UserLoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'login-form-input'}))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'login-form-input',
        'type': 'password'
    }))

    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]

# class UserSignupForm(forms.Form):
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'signup-form-input'
#     }))
#     password = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'signup-form-input', 'type': 'password'
#     }))
#     password_confirmation = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'signup-form-input', 'type': 'password'
#     }))


class UserSignupForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'signup-form-input',
        'placeholder': 'Enter your username'
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'signup-form-input',
        'placeholder': 'Enter your username',
        'type': 'email'
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'signup-form-input',
        'type': 'password'
    }))
    password_confirmation = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'signup-form-input',
        'type': 'password'
    }))


    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]


    def clean_username(self):
        username = self.cleaned_data.get('username')

        # Checking if there is another user with the same username
        queryset = None
        try:
            queryset = User.objects.get(username__exact=username)
            print('username taken')
        
        except Exception:
            print(Exception)

        if queryset != None:
            raise forms.ValidationError('Username already taken')
        if len(username) < 5:
            raise forms.ValidationError('Your username must have more than 5 characters!')
        if username.startswith('1'):
            raise forms.ValidationError('You rusername cannot start with the number 1!')

        return username


    def clean_email(self):
        email = self.cleaned_data.get('email')

        # Checking if there is another user with the same email
        queryset = None
        try:
            queryset = User.objects.get(emaiL__exact=email)

        except Exception:
            print(Exception)

        if queryset != None:
            raise forms.ValidationError('Email already taken')

        return email    