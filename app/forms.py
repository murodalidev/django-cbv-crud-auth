from django import forms
from app.models import *


class CreatePublisherForm(forms.ModelForm):

    class Meta:
        model = Publisher
        fields = ['name', 'address', 'state_province', 'country', 'about', 'website']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'state_province': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
        }


class CreateAuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['salutation', 'name', 'email', 'headshot']

        widgets = {
            'salutation': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'headshot': forms.FileInput(attrs={'class': 'form-control', 'style': "padding: 3px"}),
        }


class BookCreateForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'authors', 'publisher', 'about', 'publication_date']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'authors': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'publisher': forms.Select(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control'}),
            'publication_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }