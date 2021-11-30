from django import forms
from django.core import validators


class CreateContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(150)
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(200)
        ]
    )

    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'rows': '8',
                   'cols': '20'}),
    )
