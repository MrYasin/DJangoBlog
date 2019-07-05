from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm

from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.

def register(request):

    form = RegisterForm(request.POST or None)

    if form.is_valid():
        
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.success(request, "Registered successfully.")

        return redirect("index")

    context = {
        "form" : form
    }

    return render(request,"register.html", context=context)

def loginUser(request):

    form = LoginForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:

            messages.warning(request, "Wrong username or password..")
            return render(request,"login.html", context=context)
        
        messages.success(request, "Login successful.")
        login(request, user)
        return redirect("index")

    return render(request,"login.html", context=context)


def logoutUser(request):

    logout(request)
    messages.info(request, "Logout successful.")

    return redirect("index")



