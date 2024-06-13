import pandas as pd
from django.shortcuts import render
from .models import *
from web_app import graphics_function as gf

def home(request):
    return render(request, "home.html")


def macro(request):
    x = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013,
           2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
    y =[14, 55, 44, 13, 29, 20, 45, 39, 29, 10, 50, 60, 39, 36, 49, 18, 49, 50, 69, 18, 13,
           11, 4, 2, 1]
    
    x_title = ''
    
    y_title = ''
    
    fig = gf.graph(x, y, x_title, y_title)
    
    macro_html_1 = fig.to_html()
    macro_html_2 = fig.to_html()

    context = {'macro1': macro_html_1, 
               'macro2': macro_html_2
              }
    
    return render(request, "macro.html", context)

def datos_demograficos(request):
    return render(request, "demograficos.html")


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
    df = pd.read_csv('src/data/indicadores.csv')
    df_x = df.melt(var_name='Year')
    df_y = df.melt(value_name='Value')
    
    x = df_x['Year']
    y = df_y['Value']
    
    x_1 = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013]
    y_1 = [14, 55, 44, 13, 29, 20, 45, 39, 29, 10, 50, 60, 39, 12]
    
    x_title = 'Años'
    y_title = 'Indices'
    
    fig = gf.graph(x, y, x_title, y_title)
    fig_1 = gf.graph(x_1, y_1, x_title, y_title)
    
    indicadores_html = fig.to_html()
    indicadores_html2 = fig_1.to_html()
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


def JP_304(request):
    return render(request, "cuestionarios/balanza_de_pagos/JP-304.html")


def IP_110(request):
    return render(request, "cuestionarios/ingreso_neto/IP-110.html")

def JP_541(request):
    return render(request, "cuestionarios/construcción/JP-541.html")