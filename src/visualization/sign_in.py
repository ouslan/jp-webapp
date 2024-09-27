from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib import messages
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
            if not username or not password:
                messages.error(request, "Por favor ingrese un nombre de usuario y contraseña.")
            else:
                messages.error(request, "El usuario no existe o la contraseña es incorrecta.")
            return render(request, "signin.html")
    
    return render(request, "signin.html")
