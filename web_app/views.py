import pandas as pd
from django.shortcuts import render
from .models import *
from web_app import graphics_function as gf

def home(request):
    return render(request, "home.html")


def macro(request):
    return render(request, "macro.html")

def datos_demograficos(request):
    return render(request, "demograficos.html")

def OfHome(request):
    return render(request, "OfficialHome.html")


def ciclos_economicos(request):
    x = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013,
           2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
    y =[14, 55, 44, 13, 29, 20, 45, 39, 29, 10, 50, 60, 39, 36, 49, 18, 49, 50, 69, 18, 13,
           11, 4, 2, 1]
    
    x_title = ''
    y_title = ''
    
    fig = gf.graph(x, y, x_title, y_title)
    
    ciclos_economicos = fig.to_html()
    
    context = {'ciclos_economicos': ciclos_economicos}
    return render(request, "ciclos_economicos.html", context)
    
def indicadores(request):
    x = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013,
           2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
    y =[14, 55, 44, 13, 29, 20, 45, 39, 29, 10, 50, 60, 39, 36, 49, 18, 49, 50, 69, 18, 13,
           11, 4, 2, 1]
    
    x_title = 'Años'
    y_title = 'Indices'
    
    fig = gf.graph(x, y, x_title, y_title)
    
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