# modify forms 
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm): # inherit forms
    # add few attr
    email = forms.EmailField()
    
    # change parent properties
    class Meta:
        # save in user db
        model = User # change user model
        fields = ['username','email','password1','password2',] # order of appearance