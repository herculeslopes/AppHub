from dataclasses import fields
from django import forms

from .models import Platform, Software

class PublishSoftwareForm(forms.ModelForm):
    # PLATFORM_OPTIONS = (
    #     ('L', 'Linux'),
    #     ('W', 'Window'),
    #     ('A', 'Apple'),
    # )

    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input publish-form-input',
    }))

    version = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input publish-form-input',
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-textarea publish-form-textarea',
    }))

    project_url = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input publish-form-input',
    }))

    # platforms = forms.MultipleChoiceField(
    #     widget=forms.CheckboxSelectMultiple(attrs={
    #         'class': 'form-multiselect',
    #     }), choices=PLATFORM_OPTIONS
    # )

    platforms = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-multiselect',
        }), queryset=Platform.objects.all()
    )

    class Meta:
        model = Software
        fields = [
            'name',
            'version',
            'description',
            'project_url',
            'platforms',
        ]