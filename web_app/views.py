from os import login_tty
import pandas as pd
from django.shortcuts import redirect, render
import plotly.express as px
from django.http import HttpResponse
from .forms import CreateUserForm, SignInForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def signin(request):        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            form = SignInForm(initial={'username': username})
            context = {'form': form}
            return render(request, "signin.html", context)
          
    form = SignInForm()
    context = {'form': form}
  
    return render(request, "signin.html", context)

def home(request):
    return render(request, "home.html")


def macro(request):
    return render(request, "macro.html")


def ciclos_economicos(request):
    return render(request, "ciclos_economicos.html")


def indicadores(request):
    return render(request, "indicadores.html")