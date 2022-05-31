from email import message
from .models import RandomModel
from  django.forms import ModelForm
from django import forms 


class RandomForm(ModelForm):
        class Meta():
            model= RandomModel
            fields =  ['name', 'email', 'message']
            

