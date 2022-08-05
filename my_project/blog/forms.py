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
            'Name' : forms.TextInput(attrs = {'class':'form-group form-control', 'style':'margin-left:2%; border:2px solid black',}),
            'Number' : forms.NumberInput(attrs = {'class':'form-group form-control', 'style':'margin-left:2%; border:2px solid black'}),
            'Email_id' : forms.EmailInput(attrs = {'class':'form-group form-control', 'style':'margin-left:2%; border:2px solid black'}),
            'Message' : forms.Textarea(attrs = {'class':'form-group form-control', 'rows':6, 'style':'margin-left:2%; border:2px solid black'}),
        }