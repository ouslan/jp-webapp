from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def change_email(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(username=request.user.username, password=password)
        if user is not None:
            user.email = email
            user.save()
            return redirect("web_app:log_in_page")

    return render(request, "registration/add_email.html")
