from django.forms import ModelForm
from .models import *
from django import forms
from django.db import models
from phonenumber_field.formfields import *


class DriverAddForm(ModelForm):
   
    confirmation = forms.BooleanField(required=True, initial=True, widget=forms.CheckboxInput(attrs={'class': 'custom-checkbox', 'id':'confirmation'},))
   
    class Meta:
        model = Driver
        fields = '__all__'
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'application-input', 'placeholder':"Ваше имя",}),
            'phone_number': RegionalPhoneNumberWidget(attrs={'class':"application-input", 'placeholder':"+7 (999) 999-99-99"}),
            'city': forms.Select(attrs={'class': 'main-select', }),
        }
        
    def __init__(self, *args, **kwargs):
         super(DriverAddForm, self).__init__(*args, **kwargs)
         self.fields['city'].empty_label = "Выберите город"
        
   
        
        
