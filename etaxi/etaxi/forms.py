from django.forms import ModelForm
from .models import *
from django import forms
from django.db import models
from phonenumber_field.formfields import *


class DriverAddForm(ModelForm):
   
    confirmation = forms.BooleanField(initial=True, widget=forms.CheckboxInput(attrs={'class': 'custom-checkbox', 'id': 'confirmation'}))
    class Meta:
        model = Driver
        fields = ['name', 'phone_number','city','confirmation']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'application-input', 'placeholder':"Ваше имя",}),
            'phone_number': RegionalPhoneNumberWidget(attrs={'class':"application-input", 'placeholder':"+7 999 999 99"}),
            'city': forms.Select(attrs={'class': 'main-select', }), 
        }
        
        error_messages = {'phone_number': {'invalid': 'Введите  корректный  номер  телефона, в следующем формате +79129786539'}}
           
    def __init__(self, *args, **kwargs):
         super(DriverAddForm, self).__init__(*args, **kwargs)
         self.fields['city'].empty_label = 'Выберите город'
         
class DriverAddFormOffer(ModelForm):
   
    confirmation = forms.BooleanField(initial=True, widget=forms.CheckboxInput(attrs={'class': 'custom-checkbox', 'id': 'verification'}))
    class Meta:
        model = Driver
        fields = ['name', 'phone_number', 'confirmation',]
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'offer-form__name', 'placeholder':"Ваше имя",}),
            'phone_number': RegionalPhoneNumberWidget(attrs={'class':"offer-form__number", 'placeholder':"+7 (999) 999-99-99"}),
        }
        
        error_messages = {'phone_number': {'invalid': 'Введите  корректный  номер  телефона, в следующем формате +79129786539'}}
        
class DriverAddFormQuest(ModelForm):
   
    confirmation = forms.BooleanField(initial=True, widget=forms.CheckboxInput(attrs={'class': 'custom-checkbox', 'id': 'question'}))
    class Meta:
        model = Driver
        fields = ['name', 'phone_number', 'confirmation', 'question',]
        
        widgets = {
            'name': forms.TextInput(attrs={'class':"form__input", 'placeholder':"Ваше имя",}),
            'phone_number': RegionalPhoneNumberWidget(attrs={'class':"form__input", 'placeholder':"+7 (999) 999-99-99"}),
            'question': forms.Textarea(attrs={'class':'form__input-big', 'placeholder':"Ваш вопрос"}),
        }
        
        error_messages = {'phone_number': {'invalid': 'Введите  корректный  номер  телефона, в следующем формате +79129786539'}}