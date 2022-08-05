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
            'name' : forms.TextInput(attrs = {'class':'form-group form-control', 'style':'border: 2px solid black; width:120%',}),
            'number' : forms.NumberInput(attrs = {'class':'form-group form-control', 'style':'border: 2px solid black; width:120%'}),
            'email_id' : forms.EmailInput(attrs = {'class':'form-group form-control', 'style':'border: 2px solid black; width:120%'}),
            'message' : forms.Textarea(attrs = {'class':'form-group form-control', 'rows':3, 'style':'border: 2px solid black; width:120%'}),
        }