from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def sign_in_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username=username, password=password)
        if user is not None:
            return render(request, "forms/forms.html")
        else:
            return render(request, "signin.html")
    
    return render(request, "signin.html")