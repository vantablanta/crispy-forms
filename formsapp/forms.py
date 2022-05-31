from email import message
from .models import RandomModel
from  django.forms import ModelForm
from django import forms 


class RandomForm(ModelForm):
        class Meta():
            model= RandomModel
            fields =  ['name', 'email', 'message']
            widgets = {
                'name' : forms.TextInput(attrs={'class':'form-control blue', 'placeholder':'Hello', }),
                'email' : forms.EmailInput(attrs={'class':'form-control'}),
                'message' : forms.Textarea(attrs={'class':'form-control'}),
            }


