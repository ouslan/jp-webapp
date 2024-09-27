from django.shortcuts import render

def sign_in_page(request):
    return render(request, "signin.html")