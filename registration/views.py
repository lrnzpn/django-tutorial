from django.shortcuts import render, redirect
# import built in django forms
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

# Create your views here.
def register(response):
    if response.method == 'POST': # create new user
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        
        return redirect('/')
    else:
        form = RegisterForm()
        
    return render(response, "registration/register.html",{"form":form})