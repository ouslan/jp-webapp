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

def datos_demograficos(request):
    return render(request, "demograficos.html")


def ciclos_economicos(request):
    fig = px.scatter(
        x=[2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013,
           2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
        y=[14, 55, 44, 13, 29, 20, 45, 39, 29, 10, 50, 60, 39, 36, 49, 18, 49, 50, 69, 18, 13,
           11, 4, 2, 1],
    )

    fig.add_trace(go.Scatter(
        x=[2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013,
           2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
        y=[14, 55, 44, 13, 29, 20, 45, 39, 29, 10, 50, 60, 39, 36, 49, 18, 49, 50, 69, 18, 13,
           11, 4, 2, 1],
        mode='lines+markers',
        name='test',
        line=dict(color='#000000', width=3),
        marker=dict(size=10, color='#0080FF'),
        hoverinfo='text',
    ))

    fig.update_layout(
        margin=dict(l=0, r=1, t=25, b=0),
        plot_bgcolor='#F7F7F7',
        titlefont=dict(size=16, color='rgb(20, 24, 54)', family='Arial'),
        hovermode='x',
        
        xaxis = dict(
            color = 'white',
            showgrid=True,
            showticklabels=True,
            linecolor='black',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='black'
            ),
        ),
        yaxis = dict(
            color='white',
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor='black',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='black'
            ),
        ),
    )
    
    ciclos_economicos = fig.to_html()

    context = {'ciclos_economicos': ciclos_economicos}
    return render(request, "ciclos_economicos.html", context)
    
def indicadores(request):
    fig = px.scatter(
        x=[2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013,
           2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
        y=[14, 55, 44, 13, 29, 20, 45, 39, 29, 10, 50, 60, 39, 36, 49, 18, 49, 50, 69, 18, 13,
           11, 4, 2, 1],
        labels={'x': 'Time', 'y': 'Values'},
    )

    fig.add_trace(go.Scatter(
        x=[2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013,
           2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
        y=[14, 55, 44, 13, 29, 20, 45, 39, 29, 10, 50, 60, 39, 36, 49, 18, 49, 50, 69, 18, 13,
           11, 4, 2, 1],
        mode='lines+markers',
        name='test',
        line=dict(color='#FF2525', width=3),
        marker=dict(size=10, color='#00CDFF'),
        hoverinfo='text',
    ))

    fig.update_layout(
        plot_bgcolor='#F7F7F7',
        titlefont=dict(size=16, color='rgb(20, 24, 54)', family='Arial'),
        hovermode='x',
        
        xaxis = dict(
            title = 'Año',
            color = 'black',
            showgrid=True,
            showticklabels=True,
            linecolor='black',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='black'
            ),
        ),
        yaxis = dict(
            title='Índice',
            color='black',
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor='black',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='black'
            ),
        ),
        legend={
            'orientation': 'h',
            'xanchor': 'center', 'x': 0.5, 'y': -0.3},
                font = dict(
                family='Arial',
                size=12,
                color='black'
            )
    )
    
    indicadores_html = fig.to_html()
    indicadores_html2 = fig.to_html()
    indicadores_html3 = fig.to_html()
    indicadores_html4 = fig.to_html()
    indicadores_html5 = fig.to_html()
    indicadores_html6 = fig.to_html()
    indicadores_html7 = fig.to_html()
    indicadores_html8 = fig.to_html()
    indicadores_html9 = fig.to_html()
    indicadores_html10 = fig.to_html()
    indicadores_html11 = fig.to_html()
    indicadores_html12 = fig.to_html()
    indicadores_html13 = fig.to_html()
    indicadores_html14 = fig.to_html()
    indicadores_html15 = fig.to_html()
    indicadores_html16 = fig.to_html()
    indicadores_html17 = fig.to_html()
    indicadores_html18 = fig.to_html()

    context = {'indicadores': indicadores_html, 
               'indicadores2': indicadores_html2, 
               'indicadores3': indicadores_html3, 
               'indicadores4': indicadores_html4, 
               'indicadores5': indicadores_html5, 
               'indicadores6': indicadores_html6,
               'indicadores7': indicadores_html7,
               'indicadores8': indicadores_html8,
               'indicadores9': indicadores_html9,
               'indicadores10': indicadores_html10,
               'indicadores11': indicadores_html11,
               'indicadores12': indicadores_html12,
               'indicadores13': indicadores_html13,
               'indicadores14': indicadores_html14,
               'indicadores15': indicadores_html15,
               'indicadores16': indicadores_html16,
               'indicadores17': indicadores_html17,
               'indicadores18': indicadores_html18,
               }
    return render(request, "indicadores.html", context)