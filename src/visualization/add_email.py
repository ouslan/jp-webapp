from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def change_email(request):    
  return render(request, "registration/add_email.html")
