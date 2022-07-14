from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as lg, logout as lgout
from . import forms

# Create your views here.


def register(request):
    if request.method =="POST":
        form = forms.Register(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(username=data.get("username"),email=data.get("email"),password=data.get("password"))
            return redirect(to="post:homepage")
    else:
        form = forms.Register()

    context = {
        "form":form,
    }
    return render(request,template_name="account/register.html",context=context)



def login(request):
    if request.method == "POST":
        form = forms.Login(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,username=data.get("username"), password=data.get("password"))
            if user is not None:
                lg(request,user)
                return redirect(to="post:homepage")
    else:
        form = forms.Login()

    context = {
        "form":form,
    }
    return render(request,template_name="account/login.html",context=context)


def logout(request):
    lgout(request)
    return redirect(to="post:homepage")



