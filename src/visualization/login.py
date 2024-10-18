from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def log_in_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('web_app:forms')
        else:
            return render(request, "registration/login.html")
    
    return render(request, "registration/login.html")
