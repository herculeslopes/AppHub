from dataclasses import fields
from django import forms

from .models import Software

class PublishSoftwareForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input publish-form-input',
    }))

    # description = forms.CharField(widget=forms.Textarea(attrs={
    #     'class', 'publish-form-textarea',
    # }))

    # description = forms.CharField(widget=forms.TextInput(attrs={
    #     'class', 'publish-form-textarea',
    # }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-textarea publish-form-textarea',
    }))

    class Meta:
        model = Software
        fields = [
            'name',
            'description',
        ]