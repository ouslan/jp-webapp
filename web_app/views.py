import pandas as pd
from django.shortcuts import render
from .models import *
from web_app import graphics_function as gf
import csv
from django.shortcuts import render, redirect
from django.http import HttpResponse
import os

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
    if request.method == "POST":
        # Retrieve form data
        start_month = request.POST.get('start_month')
        end_month = request.POST.get('end_month')
        year = request.POST.get('year')
        name = request.POST.get('name')
        direction = request.POST.get('direction')
        liaison_officer = request.POST.get('liaison_officer')
        title = request.POST.get('title')
        tel = request.POST.get('tel')
        nombre_agencia_federal = request.POST.get('nombre_agencia_federal')
        catalogo_federal = request.POST.get('catalogo_federal')
        sai_federal = request.POST.get('sai_federal')
        titulo_federal = request.POST.get('titulo_federal')
        aportacion_aprobada_federal = request.POST.get('aportacion_aprobada_federal')
        fecha_aprobacion_federal = request.POST.get('fecha_aprobacion_federal')
        aportacion_recibida_federal = request.POST.get('aportacion_recibida_federal')
        fecha_recibo_federal = request.POST.get('fecha_recibo_federal')
        aportacion_gastada_federal = request.POST.get('aportacion_gastada_federal')
        fecha_gasto_federal = request.POST.get('fecha_gasto_federal')
        agencia_local_table_box = request.POST.get('agencia_local_table_box')
        catalogo_local = request.POST.get('catalogo_local')
        programa_local = request.POST.get('programa_local')
        aportacion_federal_aprobada_local = request.POST.get('aportacion_federal_aprobada_local')
        fecha_aprobacion_local = request.POST.get('fecha_aprobacion_local')
        aportacion_federal_recibida_local = request.POST.get('aportacion_federal_recibida_local')
        fecha_recibo_local = request.POST.get('fecha_recibo_local')
        aportacion_federal_gastada_local = request.POST.get('aportacion_federal_gastada_local')
        fecha_gasto_local = request.POST.get('fecha_gasto_local')
        numero_cuenta_local = request.POST.get('numero_cuenta_local')
        
        csv_file_path = 'src/data/balanza_de_pago_data/JP-304.csv'
        file_exists = os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            if not file_exists:
                writer.writerow(['start_month', 'end_month', 'year', 'name',
                                'direction', 'liaison_officer', 'title', 'tel',
                                'nombre_agencia_federal', 'catalogo_federal', 'sai_federal',
                                'titulo_federal', 'aportacion_aprobada_federal', 'fecha_aprobacion_federal',
                                'aportacion_recibida_federal', 'fecha_recibo_federal', 'aportacion_gastada_federal',
                                'fecha_gasto_federal', 'agencia_local_table_box', 'catalogo_local', 'programa_local',
                                'aportacion_federal_aprobada_local', 'fecha_aprobacion_local', 'aportacion_federal_recibida_local',
                                'fecha_recibo_local', 'aportacion_federal_gastada_local', 'fecha_gasto_local', 'numero_cuenta_local'
                                ])
            
            writer.writerow([start_month, end_month, year, name,
                             direction, liaison_officer, title, tel,
                             nombre_agencia_federal, catalogo_federal, sai_federal,
                             titulo_federal, aportacion_aprobada_federal, fecha_aprobacion_federal,
                             aportacion_recibida_federal, fecha_recibo_federal, aportacion_gastada_federal,
                             fecha_gasto_federal, agencia_local_table_box, catalogo_local, programa_local,
                             aportacion_federal_aprobada_local, fecha_aprobacion_local, aportacion_federal_recibida_local,
                             fecha_recibo_local, aportacion_federal_gastada_local, fecha_gasto_local, numero_cuenta_local
                             ])  

        return render(request, "cuestionarios/succesfull.html")
    
    return render(request, "cuestionarios/balanza_de_pagos/JP-304.html")

def JP_361(request):
    return render(request, "cuestionarios/balanza_de_pagos/JP-361.html")


def IP_110(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get('company_name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        liaison_officer = request.POST.get('liaison_officer')
        ssn = request.POST.get('ssn')
        tel = request.POST.get('tel')
        fax = request.POST.get('fax')
        legal_form = request.POST.get('legal_form')
        cfc = request.POST.get('cfc')
        business_type = request.POST.get('business_type')
        business_function = request.POST.get('business_function')
        branches = request.POST.get('branches')
        closing_date = request.POST.get('closing_date')
        services_revenues_12 = request.POST.get('services_revenues_12')
        services_revenues_13 = request.POST.get('services_revenues_13')
        industries_businesses_12 = request.POST.get('industries_businesses_12')
        industries_businesses_13 = request.POST.get('industries_businesses_13')
        people_12 = request.POST.get('people_12')
        people_13 = request.POST.get('people_13')
        sales_12 = request.POST.get('sales_12')
        sales_13 = request.POST.get('sales_13')
        incomes_rents_12 = request.POST.get('incomes_rents_12')
        incomes_rents_13 = request.POST.get('incomes_rents_12')
        incomes_interests_12 = request.POST.get('incomes_interests_12')
        incomes_interests_13 = request.POST.get('incomes_interests_13')
        dividends_12 = request.POST.get('dividends_12')
        dividends_13 = request.POST.get('dividends_13')
        others_incomes_12 = request.POST.get('others_incomes_12')
        others_incomes_13 = request.POST.get('others_incomes_13')
        total_income_12 = request.POST.get('total_income_12')
        total_income_13 = request.POST.get('total_income_13')
        expenses_12 = request.POST.get('expenses_12')
        expenses_13 = request.POST.get('expenses_13')
        salaries_2012 = request.POST.get('salaries_2012') 
        salaries_2013 = request.POST.get('salaries_2013')
        expenses_interests_12 = request.POST.get('expenses_interests_12')
        expenses_interests_13 = request.POST.get('expenses_interests_13')
        expenses_rents_12 = request.POST.get('expenses_rents_12')
        expenses_rents_13 = request.POST.get('expenses_rents_13')
        depreciation_12 = request.POST.get('depreciation_12')
        depreciation_13 = request.POST.get('depreciation_13')
        bad_debts_12 = request.POST.get('bad_debts_12')
        bad_debts_13 = request.POST.get('bad_debts_13')
        donations_12 = request.POST.get('donations_12')
        donations_13 = request.POST.get('donations_13')
        sales_tax_12 = request.POST.get('sales_tax_12')
        sales_tax_13 = request.POST.get('sales_tax_13')
        machinery_12 = request.POST.get('machinery_12')
        machinery_13 = request.POST.get('machinery_13')
        other_purchases_12 = request.POST.get('other_purchases_12')
        other_purchases_13 = request.POST.get('other_purchases_13')
        licenses_12 = request.POST.get('licenses_12')
        licenses_13 = request.POST.get('licenses_13')
        other_expenses_12 = request.POST.get('other_expenses_12')
        other_expenses_13 = request.POST.get('other_expenses_13')
        total_expenses_12 = request.POST.get('total_expenses_12')
        total_expenses_13 = request.POST.get('total_expenses_13')
        net_profit_12 = request.POST.get('net_profit_12')
        net_profit_13 = request.POST.get('net_profit_13')
        income_tax_12 = request.POST.get('income_tax_12')
        income_tax_13 = request.POST.get('income_tax_13')
        profit_after_tax_12 = request.POST.get('profit_after_tax_12')
        profit_after_tax_13 = request.POST.get('profit_after_tax_13')
        withheld_tax_12 = request.POST.get('withheld_tax_12')
        withheld_tax_13 = request.POST.get('withheld_tax_13')
        signature = request.POST.get('signature')
        rank = request.POST.get('rank')
        
        
        csv_file_path = 'src/data/ingreso_neto_data/IP_110_data.csv'
        file_exists = os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            if not file_exists:
                writer.writerow(['company_name','address','email','liaison_officer','ssn','tel','fax',
                                 'legal_form','cfc','business_type','business_function','branches',
                                 'closing_date','services_revenues_12','services_revenues_13',
                                 'industries_businesses_12','industries_businesses_13','people_12',
                                 'people_13','sales_12','sales_13','incomes_rents_12','incomes_rents_13'
                                 ,'incomes_interests_12','incomes_interests_13','dividends_12','dividends_13',
                                 'others_incomes_12','others_incomes_13','total_income_12','total_income_13',
                                 'expenses_12','expenses_13','salaries_2012','salaries_2013','expenses_interests_12'
                                 ,'expenses_interests_13','expenses_rents_12','expenses_rents_13','depreciation_12',
                                 'depreciation_13','bad_debts_12','bad_debts_13','donations_12','donations_13','sales_tax_12'
                                 ,'sales_tax_13','machinery_12','machinery_13','other_purchases_12','other_purchases_13',
                                 'licenses_12','licenses_13','other_expenses_12','other_expenses_13','total_expenses_12',
                                 'total_expenses_13','net_profit_12','net_profit_13','income_tax_12','income_tax_13',
                                 'profit_after_tax_12','profit_after_tax_13','withheld_tax_12','withheld_tax_13',
                                 'signature','rank'
                                ])
            
            writer.writerow([company_name, address, email, liaison_officer, 
                             ssn, tel, fax, legal_form, cfc, business_type,
                             business_function, branches, closing_date,
                             services_revenues_12, services_revenues_13,
                             industries_businesses_12, industries_businesses_13,
                             people_12, people_13, sales_12, sales_13,
                             incomes_rents_12, incomes_rents_13,
                             incomes_interests_12, incomes_interests_13,
                             dividends_12, dividends_13,
                             others_incomes_12, others_incomes_13,
                             total_income_12, total_income_13,
                             expenses_12, expenses_13,
                             salaries_2012, salaries_2013,
                             expenses_interests_12, expenses_interests_13,
                             expenses_rents_12, expenses_rents_13,
                             depreciation_12, depreciation_13,
                             bad_debts_12, bad_debts_13,
                             donations_12, donations_13,
                             sales_tax_12, sales_tax_13,
                             machinery_12, machinery_13,
                             other_purchases_12, other_purchases_13,
                             licenses_12, licenses_13,
                             other_expenses_12, other_expenses_13,
                             total_expenses_12, total_expenses_13,
                             net_profit_12, net_profit_13,
                             income_tax_12, income_tax_13,
                             profit_after_tax_12, profit_after_tax_13,
                             withheld_tax_12, withheld_tax_13,
                             signature, rank
                            ])  

        return render(request, "cuestionarios/succesfull.html")

    return render(request, "cuestionarios/ingreso_neto/IP-110.html")


def JP_541(request):
    if request.method == "POST":
        # Retrieve form data
        
        csv_file_path = 'src/data/construcción/JP-541.csv'
        file_exists = os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            if not file_exists:
                writer.writerow([
                                ])
            
            writer.writerow([
                             ])  

        return render(request, "cuestionarios/succesfull.html")
    return render(request, "cuestionarios/construcción/JP-541.html")


def succesfull_page(request):
    return render(request, "cuestionarios/succesfull.html")



