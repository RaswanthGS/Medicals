from dataclasses import field
from socket import fromshare
from django import forms
from django.forms import ModelForm
from .models import Medicals

class PostForm(ModelForm):
    class Meta:
        model = Medicals
        fields = '__all__'
        widgets = {
            'Name' : forms.TextInput(attrs = {'class':'form-group form-control', 'style':'',}),
            'Number' : forms.NumberInput(attrs = {'class':'form-group form-control', 'style':''}),
            'Email_id' : forms.EmailInput(attrs = {'class':'form-group form-control', 'style':''}),
            'Message' : forms.Textarea(attrs = {'class':'form-group form-control', 'rows':4, 'style':''}),
        }