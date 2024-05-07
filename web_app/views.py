import pandas as pd
from django.shortcuts import redirect, render
import plotly.express as px
from .forms import SignInForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
import plotly.graph_objects as go


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
    fig = px.scatter( x = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 
                        2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024], 
                y = [14, 55, 44, 13, 29, 20, 45, 39, 29, 10, 50, 60, 39, 36, 49, 18, 49, 50, 69, 18, 13, 
                    11, 4, 2, 1], 
                labels={'x':'Time', 'y':'Values'},
                )

    fig.add_trace(go.Scatter(x=[2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 
                            2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024], 
                            y=[14, 55, 44, 13, 29, 20, 45, 39, 29, 10, 50, 60, 39, 36, 49, 18, 49, 50, 69, 18, 13, 
                                11, 4, 2, 1], 
                            mode='lines+markers',
                            name='test',
                            line=dict(color='firebrick', width=4),
                            marker=dict(size=15, color='LightSkyBlue')))

    fig.update_layout(
        autosize=True,
        width=900,
        height=500,
        margin=dict(
            l=50,
            r=50,
            b=50,
            t=50,
            pad=4
        ),
        paper_bgcolor="#CDDAFF",
    )
    indicadores = fig.to_html()

    context = {'indicadores': indicadores}
    return render(request, "indicadores.html", context)