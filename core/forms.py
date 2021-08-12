from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AddForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ('login','password')

        widgets = {
            'login': forms.TextInput(),
            'password': forms.TextInput(),
        }

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('brand','car_model','manufacturing_date','power_output')

        widgets = {
            'brand': forms.TextInput(),
            'car_model': forms.TextInput(),
            'manufacturing_date': forms.DateInput(format='%d/%m/%Y'),
            'power_output': forms.NumberInput(),
        }

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']