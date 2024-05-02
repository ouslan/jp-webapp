from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from .forms import SignInForm
from .models import Order


def signin(request):        
  if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password1')

          user = authenticate(request, username=username, password1=password)

          if user is not None:
              login(request, user)
              return redirect('home')
          else:
             # messages.error(request, 'Invalid username or password')
              return redirect('signin')
          
  context = {}
  
  return render(request, "signin.html", context)

def home(request):
    return render(request, "home.html")
