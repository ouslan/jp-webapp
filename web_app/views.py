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
    if request.method == "POST":
        # Retrieve form data
        income_expenses_year_1 = request.POST.get('income_expenses_year_1')
        income_expenses_year_2 = request.POST.get('income_expenses_year_2')
        income_life_1 = request.POST.get('income_life_1')
        income_life_2 = request.POST.get('income_life_2')
        income_disability_1 = request.POST.get('income_disability_1')
        income_disability_2 = request.POST.get('income_disability_2')
        income_auto_1 = request.POST.get('income_auto_1')
        income_auto_2 = request.POST.get('income_auto_2')
        income_other_1 = request.POST.get('income_other_1')
        income_other_2 = request.POST.get('income_other_2')
        income_interest_1 = request.POST.get('income_interest_1')
        income_interest_2 = request.POST.get('income_interest_2')
        income_rent_1 = request.POST.get('income_rent_1')
        income_rent_2 = request.POST.get('income_rent_2')
        income_other_2_1 = request.POST.get('income_other_2_1')
        income_other_2_2 = request.POST.get('income_other_2_2')
        total_income_1 = request.POST.get('total_income_1')
        total_income_2 = request.POST.get('total_income_2')
        expenses_life_1 = request.POST.get('expenses_life_1')
        expenses_life_2 = request.POST.get('expenses_life_2')
        expenses_disability_1 = request.POST.get('expenses_disability_1')
        expenses_disability_2 = request.POST.get('expenses_disability_2')
        expenses_auto_1 = request.POST.get('expenses_auto_1')
        expenses_auto_2 = request.POST.get('expenses_auto_2')
        expenses_other_1 = request.POST.get('expenses_other_1')
        expenses_other_2 = request.POST.get('expenses_other_2')
        expenses_salaries_1 = request.POST.get('expenses_salaries_1')
        expenses_salaries_2 = request.POST.get('expenses_salaries_2')
        expenses_interes_1 = request.POST.get('expenses_interes_1')
        expenses_interes_2 = request.POST.get('expenses_interes_2')
        expenses_rent_1 = request.POST.get('expenses_rent_1')
        expenses_rent_2 = request.POST.get('expenses_rent_2')
        expenses_depreciation_1 = request.POST.get('expenses_depreciation_1')
        expenses_depreciation_2 = request.POST.get('expenses_depreciation_2')
        expenses_donations_1 = request.POST.get('expenses_donations_1')
        expenses_donations_2 = request.POST.get('expenses_donations_2')
        expenses_commissions_1 = request.POST.get('expenses_commissions_1')
        expenses_commissions_2 = request.POST.get('expenses_commissions_2')
        expenses_employees_1 = request.POST.get('expenses_employees_1')
        expenses_employees_2 = request.POST.get('expenses_employees_2')
        expenses_brokers_1 = request.POST.get('expenses_brokers_1')
        expenses_brokers_2 = request.POST.get('expenses_brokers_2')
        expenses_other_operational_1 = request.POST.get('expenses_other_operational_1')
        expenses_other_operational_2 = request.POST.get('expenses_other_operational_2')
        total_expenses_1 = request.POST.get('total_expenses_1')
        total_expenses_2 = request.POST.get('total_expenses_2')
        net_profit_1 = request.POST.get('net_profit_1')
        net_profit_2 = request.POST.get('net_profit_2')
        balance_year_1 = request.POST.get('balance_year_1')
        balance_year_2 = request.POST.get('balance_year_2')
        guaranteed_1 = request.POST.get('guaranteed_1')
        guaranteed_2 = request.POST.get('guaranteed_2')
        guaranteed_3 = request.POST.get('guaranteed_3')
        guaranteed_4 = request.POST.get('guaranteed_4')
        veterans_1 = request.POST.get('veterans_1')
        veterans_2 = request.POST.get('veterans_2')
        veterans_3 = request.POST.get('veterans_3')
        veterans_4 = request.POST.get('veterans_4')
        conventional_1 = request.POST.get('conventional_1')
        conventional_2 = request.POST.get('conventional_2')
        conventional_3 = request.POST.get('conventional_3')
        conventional_4 = request.POST.get('conventional_4')
        other_1 = request.POST.get('other_1')
        other_2 = request.POST.get('other_2')
        other_3 = request.POST.get('other_3')
        other_4 = request.POST.get('other_4')
        policy_loans_1 = request.POST.get('policy_loans_1')
        policy_loans_2 = request.POST.get('policy_loans_2')
        policy_loans_3 = request.POST.get('policy_loans_3')
        policy_loans_4 = request.POST.get('policy_loans_4')
        other_specify_1 = request.POST.get('other_specify_1')
        other_specify_2 = request.POST.get('other_specify_2')
        other_specify_3 = request.POST.get('other_specify_3')
        other_specify_4 = request.POST.get('other_specify_4')
        policy_reserves_1 = request.POST.get('policy_reserves_1')
        policy_reserves_2 = request.POST.get('policy_reserves_2')
        accrued_dividends_1 = request.POST.get('accrued_dividends_1')
        accrued_dividends_2 = request.POST.get('accrued_dividends_2')
        signature = request.POST.get('signature')
        date = request.POST.get('date')
        position_telephone = request.POST.get('position_telephone')
        
        csv_file_path = 'src/data/balanza_de_pago_data/JP-361.csv'
        file_exists = os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            if not file_exists:
                writer.writerow([
                                'income_expenses_year_1', 'income_expenses_year_2',
                                'income_life_1', 'income_life_2', 'income_disability_1',
                                'income_disability_2', 'income_auto_1', 'income_auto_2',
                                'income_other_1', 'income_other_2', 'income_interest_1', 
                                'income_interest_2', 'income_rent_1', 'income_rent_2',
                                'income_other_2_1', 'income_other_2_2', 'total_income_1', 
                                'total_income_2', 'expenses_life_1', 'expenses_life_2',
                                'expenses_disability_1', 'expenses_disability_2', 
                                'expenses_auto_1', 'expenses_auto_2', 'expenses_other_1',
                                'expenses_other_2', 'expenses_salaries_1', 'expenses_salaries_2',
                                'expenses_interes_1', 'expenses_interes_2', 'expenses_rent_1',  
                                'expenses_rent_2', 'expenses_depreciation_1', 'expenses_depreciation_2',
                                'expenses_donations_1', 'expenses_donations_2', 'expenses_commissions_1',
                                'expenses_commissions_2', 'expenses_employees_1', 'expenses_employees_2',
                                'expenses_brokers_1', 'expenses_brokers_2', 'expenses_other_operational_1',
                                'expenses_other_operational_2', 'total_expenses_1', 'total_expenses_2',
                                'net_profit_1', 'net_profit_2', 'balance_year_1', 'balance_year_2',
                                'guaranteed_1', 'guaranteed_2', 'guaranteed_3', 'guaranteed_4',
                                'veterans_1', 'veterans_2', 'veterans_3', 'veterans_4', 
                                'conventional_1', 'conventional_2', 'conventional_3', 'conventional_4',
                                'other_1', 'other_2', 'other_3', 'other_4', 'policy_loans_1',
                                'policy_loans_2', 'policy_loans_3', 'policy_loans_4', 'other_specify_1',
                                'other_specify_2', 'other_specify_3', 'other_specify_4', 'policy_reserves_1',
                                'policy_reserves_2', 'accrued_dividends_1', 'accrued_dividends_2',
                                'signature', 'date', 'position_telephone'
                                ])
            
            writer.writerow([
                            income_expenses_year_1, income_expenses_year_2,
                            income_life_1, income_life_2, income_disability_1, 
                            income_disability_2, income_auto_1, income_auto_2, 
                            income_other_1, income_other_2, income_interest_1, 
                            income_interest_2, income_rent_1, income_rent_2,
                            income_other_2_1, income_other_2_2, total_income_1,
                            total_income_2, expenses_life_1, expenses_life_2,
                            expenses_disability_1, expenses_disability_2,
                            expenses_auto_1, expenses_auto_2, expenses_other_1,
                            expenses_other_2, expenses_salaries_1, expenses_salaries_2,
                            expenses_interes_1, expenses_interes_2, expenses_rent_1,
                            expenses_rent_2, expenses_depreciation_1, expenses_depreciation_2,
                            expenses_donations_1, expenses_donations_2, expenses_commissions_1,
                            expenses_commissions_2, expenses_employees_1, expenses_employees_2,
                            expenses_brokers_1, expenses_brokers_2, expenses_other_operational_1,
                            expenses_other_operational_2, total_expenses_1, total_expenses_2,
                            net_profit_1, net_profit_2, balance_year_1, balance_year_2,
                            guaranteed_1, guaranteed_2, guaranteed_3, guaranteed_4,
                            veterans_1, veterans_2, veterans_3, veterans_4,
                            conventional_1, conventional_2, conventional_3, conventional_4,
                            other_1, other_2, other_3, other_4, policy_loans_1,
                            policy_loans_2, policy_loans_3, policy_loans_4, other_specify_1,
                            other_specify_2, other_specify_3, other_specify_4, policy_reserves_1,
                            policy_reserves_2, accrued_dividends_1, accrued_dividends_2,
                            signature, date, position_telephone
                            ])  

        return render(request, "cuestionarios/succesfull.html")
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
        
        #TABLE 1
        form_1 = request.POST.get('form_1')
        fiscal_year_1 = request.POST.get('fiscal_year_1')
        company_name_1 = request.POST.get('company_name_1')
        liaison_officer_1 = request.POST.get('liaison_officer_1')
        tel_1 = request.POST.get('tel_1')
        project_1 = request.POST.get('project_1')
        branches_1 = request.POST.get('branches_1')
        
        project_name_1_1 = request.POST.get('project_name_1_1')
        city_1_1 = request.POST.get('city_1_1')
        total_number_project_1_1 = request.POST.get('total_number_project_1_1')
        total_cost_1_1 = request.POST.get('total_cost_1_1')
        start_date_1_1 = request.POST.get('start_date_1_1')
        end_date_1_1 = request.POST.get('end_date_1_1')
        value_first_trimester_1_1 = request.POST.get('value_first_trimester_1_1')
        value_second_trimester_1_1 = request.POST.get('value_second_trimester_1_1')
        value_third_trimester_1_1 = request.POST.get('value_third_trimester_1_1')
        value_fourth_trimester_1_1 = request.POST.get('value_fourth_trimester_1_1')
        
        project_name_1_2 = request.POST.get('project_name_1_2')
        city_1_2 = request.POST.get('city_1_2')
        total_number_project_1_2 = request.POST.get('total_number_project_1_2')
        total_cost_1_2 = request.POST.get('total_cost_1_2')
        start_date_1_2 = request.POST.get('start_date_1_2')
        end_date_1_2 = request.POST.get('end_date_1_2')
        value_first_trimester_1_2 = request.POST.get('value_first_trimester_1_2')
        value_second_trimester_1_2 = request.POST.get('value_second_trimester_1_2')
        value_third_trimester_1_2 = request.POST.get('value_third_trimester_1_2')
        value_fourth_trimester_1_2 = request.POST.get('value_fourth_trimester_1_2')
        
        project_name_1_3 = request.POST.get('project_name_1_3')
        city_1_3 = request.POST.get('city_1_3')
        total_number_project_1_3 = request.POST.get('total_number_project_1_3')
        total_cost_1_3 = request.POST.get('total_cost_1_3')
        start_date_1_3 = request.POST.get('start_date_1_3')
        end_date_1_3 = request.POST.get('end_date_1_3')
        value_first_trimester_1_3 = request.POST.get('value_first_trimester_1_3')
        value_second_trimester_1_3 = request.POST.get('value_second_trimester_1_3')
        value_third_trimester_1_3 = request.POST.get('value_third_trimester_1_3')
        value_fourth_trimester_1_3 = request.POST.get('value_fourth_trimester_1_3')
        
        project_name_1_4 = request.POST.get('project_name_1_4')
        city_1_4 = request.POST.get('city_1_4')
        total_number_project_1_4 = request.POST.get('total_number_project_1_4')
        total_cost_1_4 = request.POST.get('total_cost_1_4')
        start_date_1_4 = request.POST.get('start_date_1_4')
        end_date_1_4 = request.POST.get('end_date_1_4')
        value_first_trimester_1_4 = request.POST.get('value_first_trimester_1_4')
        value_second_trimester_1_4 = request.POST.get('value_second_trimester_1_4')
        value_third_trimester_1_4 = request.POST.get('value_third_trimester_1_4')
        value_fourth_trimester_1_4 = request.POST.get('value_fourth_trimester_1_4')
        
        project_name_1_5 = request.POST.get('project_name_1_5')
        city_1_5 = request.POST.get('city_1_5')
        total_number_project_1_5 = request.POST.get('total_number_project_1_5')
        total_cost_1_5 = request.POST.get('total_cost_1_5')
        start_date_1_5 = request.POST.get('start_date_1_5')
        end_date_1_5 = request.POST.get('end_date_1_5')
        value_first_trimester_1_5 = request.POST.get('value_first_trimester_1_5')
        value_second_trimester_1_5 = request.POST.get('value_second_trimester_1_5')
        value_third_trimester_1_5 = request.POST.get('value_third_trimester_1_5')
        value_fourth_trimester_1_5 = request.POST.get('value_fourth_trimester_1_5')
        
        
        #TABLE 2
        form_2 = request.POST.get('form_2')
        fiscal_year_2 = request.POST.get('fiscal_year_2')
        company_name_2 = request.POST.get('company_name_2')
        liaison_officer_2 = request.POST.get('liaison_officer_2')
        tel_2 = request.POST.get('tel_2')
        project_2 = request.POST.get('project_2')
        branches_2 = request.POST.get('branches_2')
        
        project_name_2_1 = request.POST.get('project_name_2_1')
        city_2_1 = request.POST.get('city_2_1')
        total_number_project_2_1 = request.POST.get('total_number_project_2_1')
        total_cost_2_1 = request.POST.get('total_cost_2_1')
        start_date_2_1 = request.POST.get('start_date_2_1')
        end_date_2_1 = request.POST.get('end_date_2_1')
        value_first_trimester_2_1 = request.POST.get('value_first_trimester_2_1')
        value_second_trimester_2_1 = request.POST.get('value_second_trimester_2_1')
        value_third_trimester_2_1 = request.POST.get('value_third_trimester_2_1')
        value_fourth_trimester_2_1 = request.POST.get('value_fourth_trimester_2_1')
        
        project_name_2_2 = request.POST.get('project_name_2_2')
        city_2_2 = request.POST.get('city_2_2')
        total_number_project_2_2 = request.POST.get('total_number_project_2_2')
        total_cost_2_2 = request.POST.get('total_cost_2_2')
        start_date_2_2 = request.POST.get('start_date_2_2')
        end_date_2_2 = request.POST.get('end_date_2_2')
        value_first_trimester_2_2 = request.POST.get('value_first_trimester_2_2')
        value_second_trimester_2_2 = request.POST.get('value_second_trimester_2_2')
        value_third_trimester_2_2 = request.POST.get('value_third_trimester_2_2')
        value_fourth_trimester_2_2 = request.POST.get('value_fourth_trimester_2_2')
        
        project_name_2_3 = request.POST.get('project_name_2_3')
        city_2_3 = request.POST.get('city_2_3')
        total_number_project_2_3 = request.POST.get('total_number_project_2_3')
        total_cost_2_3 = request.POST.get('total_cost_2_3')
        start_date_2_3 = request.POST.get('start_date_2_3')
        end_date_2_3 = request.POST.get('end_date_2_3')
        value_first_trimester_2_3 = request.POST.get('value_first_trimester_2_3')
        value_second_trimester_2_3 = request.POST.get('value_second_trimester_2_3')
        value_third_trimester_2_3 = request.POST.get('value_third_trimester_2_3')
        value_fourth_trimester_2_3 = request.POST.get('value_fourth_trimester_2_3')
        
        project_name_2_4 = request.POST.get('project_name_2_4')
        city_2_4 = request.POST.get('city_2_4')
        total_number_project_2_4 = request.POST.get('total_number_project_2_4')
        total_cost_2_4 = request.POST.get('total_cost_2_4')
        start_date_2_4 = request.POST.get('start_date_2_4')
        end_date_2_4 = request.POST.get('end_date_2_4')
        value_first_trimester_2_4 = request.POST.get('value_first_trimester_2_4')
        value_second_trimester_2_4 = request.POST.get('value_second_trimester_2_4')
        value_third_trimester_2_4 = request.POST.get('value_third_trimester_2_4')
        value_fourth_trimester_2_4 = request.POST.get('value_fourth_trimester_2_4')
        
        project_name_2_5 = request.POST.get('project_name_2_5')
        city_2_5 = request.POST.get('city_2_5')
        total_number_project_2_5 = request.POST.get('total_number_project_2_5')
        total_cost_2_5 = request.POST.get('total_cost_2_5')
        start_date_2_5 = request.POST.get('start_date_2_5')
        end_date_2_5 = request.POST.get('end_date_2_5')
        value_first_trimester_2_5 = request.POST.get('value_first_trimester_2_5')
        value_second_trimester_2_5 = request.POST.get('value_second_trimester_2_5')
        value_third_trimester_2_5 = request.POST.get('value_third_trimester_2_5')
        value_fourth_trimester_2_5 = request.POST.get('value_fourth_trimester_2_5')
        
        
        #TABLE 3
        form_3 = request.POST.get('form_3')
        fiscal_year_3 = request.POST.get('fiscal_year_3')
        company_name_3 = request.POST.get('company_name_3')
        liaison_officer_3 = request.POST.get('liaison_officer_3')
        tel_3 = request.POST.get('tel_3')
        project_3 = request.POST.get('project_3')
        branches_3 = request.POST.get('branches_3')
        
        project_name_3_1 = request.POST.get('project_name_3_1')
        city_3_1 = request.POST.get('city_3_1')
        total_number_project_3_1 = request.POST.get('total_number_project_3_1')
        total_cost_3_1 = request.POST.get('total_cost_3_1')
        start_date_3_1 = request.POST.get('start_date_3_1')
        end_date_3_1 = request.POST.get('end_date_3_1')
        value_first_trimester_3_1 = request.POST.get('value_first_trimester_3_1')
        value_second_trimester_3_1 = request.POST.get('value_second_trimester_3_1')
        value_third_trimester_3_1 = request.POST.get('value_third_trimester_3_1')
        value_fourth_trimester_3_1 = request.POST.get('value_fourth_trimester_3_1')
        
        project_name_3_2 = request.POST.get('project_name_3_2')
        city_3_2 = request.POST.get('city_3_2')
        total_number_project_3_2 = request.POST.get('total_number_project_3_2')
        total_cost_3_2 = request.POST.get('total_cost_3_2')
        start_date_3_2 = request.POST.get('start_date_3_2')
        end_date_3_2 = request.POST.get('end_date_3_2')
        value_first_trimester_3_2 = request.POST.get('value_first_trimester_3_2')
        value_second_trimester_3_2 = request.POST.get('value_second_trimester_3_2')
        value_third_trimester_3_2 = request.POST.get('value_third_trimester_3_2')
        value_fourth_trimester_3_2 = request.POST.get('value_fourth_trimester_3_2')
        
        project_name_3_3 = request.POST.get('project_name_3_3')
        city_3_3 = request.POST.get('city_3_3')
        total_number_project_3_3 = request.POST.get('total_number_project_3_3')
        total_cost_3_3 = request.POST.get('total_cost_3_3')
        start_date_3_3 = request.POST.get('start_date_3_3')
        end_date_3_3 = request.POST.get('end_date_3_3')
        value_first_trimester_3_3 = request.POST.get('value_first_trimester_3_3')
        value_second_trimester_3_3 = request.POST.get('value_second_trimester_3_3')
        value_third_trimester_3_3 = request.POST.get('value_third_trimester_3_3')
        value_fourth_trimester_3_3 = request.POST.get('value_fourth_trimester_3_3')
        
        project_name_3_4 = request.POST.get('project_name_3_4')
        city_3_4 = request.POST.get('city_3_4')
        total_number_project_3_4 = request.POST.get('total_number_project_3_4')
        total_cost_3_4 = request.POST.get('total_cost_3_4')
        start_date_3_4 = request.POST.get('start_date_3_4')
        end_date_3_4 = request.POST.get('end_date_3_4')
        value_first_trimester_3_4 = request.POST.get('value_first_trimester_3_4')
        value_second_trimester_3_4 = request.POST.get('value_second_trimester_3_4')
        value_third_trimester_3_4 = request.POST.get('value_third_trimester_3_4')
        value_fourth_trimester_3_4 = request.POST.get('value_fourth_trimester_3_4')
        
        project_name_3_5 = request.POST.get('project_name_3_5')
        city_3_5 = request.POST.get('city_3_5')
        total_number_project_3_5 = request.POST.get('total_number_project_3_5')
        total_cost_3_5 = request.POST.get('total_cost_3_5')
        start_date_3_5 = request.POST.get('start_date_3_5')
        end_date_3_5 = request.POST.get('end_date_3_5')
        value_first_trimester_3_5 = request.POST.get('value_first_trimester_3_5')
        value_second_trimester_3_5 = request.POST.get('value_second_trimester_3_5')
        value_third_trimester_3_5 = request.POST.get('value_third_trimester_3_5')
        value_fourth_trimester_3_5 = request.POST.get('value_fourth_trimester_3_5')
        
        
        #TABLE 4
        form_4 = request.POST.get('form_4')
        fiscal_year_4 = request.POST.get('fiscal_year_4')
        company_name_4 = request.POST.get('company_name_4')
        liaison_officer_4 = request.POST.get('liaison_officer_4')
        tel_4 = request.POST.get('tel_4')
        project_4 = request.POST.get('project_4')
        branches_4 = request.POST.get('branches_4')
        
        project_name_4_1 = request.POST.get('project_name_4_1')
        city_4_1 = request.POST.get('city_4_1')
        total_number_project_4_1 = request.POST.get('total_number_project_4_1')
        total_cost_4_1 = request.POST.get('total_cost_4_1')
        start_date_4_1 = request.POST.get('start_date_4_1')
        end_date_4_1 = request.POST.get('end_date_4_1')
        value_first_trimester_4_1 = request.POST.get('value_first_trimester_4_1')
        value_second_trimester_4_1 = request.POST.get('value_second_trimester_4_1')
        value_third_trimester_4_1 = request.POST.get('value_third_trimester_4_1')
        value_fourth_trimester_4_1 = request.POST.get('value_fourth_trimester_4_1')
        
        project_name_4_2 = request.POST.get('project_name_4_2')
        city_4_2 = request.POST.get('city_4_2')
        total_number_project_4_2 = request.POST.get('total_number_project_4_2')
        total_cost_4_2 = request.POST.get('total_cost_4_2')
        start_date_4_2 = request.POST.get('start_date_4_2')
        end_date_4_2 = request.POST.get('end_date_4_2')
        value_first_trimester_4_2 = request.POST.get('value_first_trimester_4_2')
        value_second_trimester_4_2 = request.POST.get('value_second_trimester_4_2')
        value_third_trimester_4_2 = request.POST.get('value_third_trimester_4_2')
        value_fourth_trimester_4_2 = request.POST.get('value_fourth_trimester_4_2')
        
        project_name_4_3 = request.POST.get('project_name_4_3')
        city_4_3 = request.POST.get('city_4_3')
        total_number_project_4_3 = request.POST.get('total_number_project_4_3')
        total_cost_4_3 = request.POST.get('total_cost_4_3')
        start_date_4_3 = request.POST.get('start_date_4_3')
        end_date_4_3 = request.POST.get('end_date_4_3')
        value_first_trimester_4_3 = request.POST.get('value_first_trimester_4_3')
        value_second_trimester_4_3 = request.POST.get('value_second_trimester_4_3')
        value_third_trimester_4_3 = request.POST.get('value_third_trimester_4_3')
        value_fourth_trimester_4_3 = request.POST.get('value_fourth_trimester_4_3')
        
        project_name_4_4 = request.POST.get('project_name_4_4')
        city_4_4 = request.POST.get('city_4_4')
        total_number_project_4_4 = request.POST.get('total_number_project_4_4')
        total_cost_4_4 = request.POST.get('total_cost_4_4')
        start_date_4_4 = request.POST.get('start_date_4_4')
        end_date_4_4 = request.POST.get('end_date_4_4')
        value_first_trimester_4_4 = request.POST.get('value_first_trimester_4_4')
        value_second_trimester_4_4 = request.POST.get('value_second_trimester_4_4')
        value_third_trimester_4_4 = request.POST.get('value_third_trimester_4_4')
        value_fourth_trimester_4_4 = request.POST.get('value_fourth_trimester_4_4')
        
        project_name_4_5 = request.POST.get('project_name_4_5')
        city_4_5 = request.POST.get('city_4_5')
        total_number_project_4_5 = request.POST.get('total_number_project_4_5')
        total_cost_4_5 = request.POST.get('total_cost_4_5')
        start_date_4_5 = request.POST.get('start_date_4_5')
        end_date_4_5 = request.POST.get('end_date_4_5')
        value_first_trimester_4_5 = request.POST.get('value_first_trimester_4_5')
        value_second_trimester_4_5 = request.POST.get('value_second_trimester_4_5')
        value_third_trimester_4_5 = request.POST.get('value_third_trimester_4_5')
        value_fourth_trimester_4_5 = request.POST.get('value_fourth_trimester_4_5')
        
        
        csv_file_path = 'src/data/construcción/JP-541.csv'
        file_exists = os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0

        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            if not file_exists:
                writer.writerow([   
                                    'form_1', 'fiscal_year_1', 'company_name_1', 'liaison_officer_1', 'tel_1', 'project_1', 'branches_1',
                                    'project_name_1_1', 'city_1_1', 'total_number_project_1_1', 'total_cost_1_1', 'start_date_1_1', 'end_date_1_1', 'value_first_trimester_1_1', 'value_second_trimester_1_1', 'value_third_trimester_1_1', 'value_fourth_trimester_1_1',
                                    'project_name_1_2', 'city_1_2', 'total_number_project_1_2', 'total_cost_1_2', 'start_date_1_2', 'end_date_1_2', 'value_first_trimester_1_2', 'value_second_trimester_1_2', 'value_third_trimester_1_2', 'value_fourth_trimester_1_2',
                                    'project_name_1_3', 'city_1_3', 'total_number_project_1_3', 'total_cost_1_3', 'start_date_1_3', 'end_date_1_3', 'value_first_trimester_1_3', 'value_second_trimester_1_3', 'value_third_trimester_1_3', 'value_fourth_trimester_1_3',
                                    'project_name_1_4', 'city_1_4', 'total_number_project_1_4', 'total_cost_1_4', 'start_date_1_4', 'end_date_1_4', 'value_first_trimester_1_4', 'value_second_trimester_1_4', 'value_third_trimester_1_4', 'value_fourth_trimester_1_4',
                                    'project_name_1_5', 'city_1_5', 'total_number_project_1_5', 'total_cost_1_5', 'start_date_1_5', 'end_date_1_5', 'value_first_trimester_1_5', 'value_second_trimester_1_5', 'value_third_trimester_1_5', 'value_fourth_trimester_1_5',
                                    
                                    'form_2', 'fiscal_year_2', 'company_name_2', 'liaison_officer_2', 'tel_2', 'project_2', 'branches_2',
                                    'project_name_2_1', 'city_2_1', 'total_number_project_2_1', 'total_cost_2_1', 'start_date_2_1', 'end_date_2_1', 'value_first_trimester_2_1', 'value_second_trimester_2_1', 'value_third_trimester_2_1', 'value_fourth_trimester_2_1',
                                    'project_name_2_2', 'city_2_2', 'total_number_project_2_2', 'total_cost_2_2', 'start_date_2_2', 'end_date_2_2', 'value_first_trimester_2_2', 'value_second_trimester_2_2', 'value_third_trimester_2_2', 'value_fourth_trimester_2_2',
                                    'project_name_2_3', 'city_2_3', 'total_number_project_2_3', 'total_cost_2_3', 'start_date_2_3', 'end_date_2_3', 'value_first_trimester_2_3', 'value_second_trimester_2_3', 'value_third_trimester_2_3', 'value_fourth_trimester_2_3',
                                    'project_name_2_4', 'city_2_4', 'total_number_project_2_4', 'total_cost_2_4', 'start_date_2_4', 'end_date_2_4', 'value_first_trimester_2_4', 'value_second_trimester_2_4', 'value_third_trimester_2_4', 'value_fourth_trimester_2_4',
                                    'project_name_2_5', 'city_2_5', 'total_number_project_2_5', 'total_cost_2_5', 'start_date_2_5', 'end_date_2_5', 'value_first_trimester_2_5', 'value_second_trimester_2_5', 'value_third_trimester_2_5', 'value_fourth_trimester_2_5',
                                    
                                    'form_3', 'fiscal_year_3', 'company_name_3', 'liaison_officer_3', 'tel_3', 'project_3', 'branches_3',
                                    'project_name_3_1', 'city_3_1', 'total_number_project_3_1', 'total_cost_3_1', 'start_date_3_1', 'end_date_3_1', 'value_first_trimester_3_1', 'value_second_trimester_3_1', 'value_third_trimester_3_1', 'value_fourth_trimester_3_1',
                                    'project_name_3_2', 'city_3_2', 'total_number_project_3_2', 'total_cost_3_2', 'start_date_3_2', 'end_date_3_2', 'value_first_trimester_3_2', 'value_second_trimester_3_2', 'value_third_trimester_3_2', 'value_fourth_trimester_3_2',
                                    'project_name_3_3', 'city_3_3', 'total_number_project_3_3', 'total_cost_3_3', 'start_date_3_3', 'end_date_3_3', 'value_first_trimester_3_3', 'value_second_trimester_3_3', 'value_third_trimester_3_3', 'value_fourth_trimester_3_3',
                                    'project_name_3_4', 'city_3_4', 'total_number_project_3_4', 'total_cost_3_4', 'start_date_3_4', 'end_date_3_4', 'value_first_trimester_3_4', 'value_second_trimester_3_4', 'value_third_trimester_3_4', 'value_fourth_trimester_3_4',
                                    'project_name_3_5', 'city_3_5', 'total_number_project_3_5', 'total_cost_3_5', 'start_date_3_5', 'end_date_3_5', 'value_first_trimester_3_5', 'value_second_trimester_3_5', 'value_third_trimester_3_5', 'value_fourth_trimester_3_5',
                                    
                                    'form_4', 'fiscal_year_4', 'company_name_4', 'liaison_officer_4', 'tel_4', 'project_4', 'branches_4',
                                    'project_name_4_1', 'city_4_1', 'total_number_project_4_1', 'total_cost_4_1', 'start_date_4_1', 'end_date_4_1', 'value_first_trimester_4_1', 'value_second_trimester_4_1', 'value_third_trimester_4_1', 'value_fourth_trimester_4_1',
                                    'project_name_4_2', 'city_4_2', 'total_number_project_4_2', 'total_cost_4_2', 'start_date_4_2', 'end_date_4_2', 'value_first_trimester_4_2', 'value_second_trimester_4_2', 'value_third_trimester_4_2', 'value_fourth_trimester_4_2',
                                    'project_name_4_3', 'city_4_3', 'total_number_project_4_3', 'total_cost_4_3', 'start_date_4_3', 'end_date_4_3', 'value_first_trimester_4_3', 'value_second_trimester_4_3', 'value_third_trimester_4_3', 'value_fourth_trimester_4_3',
                                    'project_name_4_4', 'city_4_4', 'total_number_project_4_4', 'total_cost_4_4', 'start_date_4_4', 'end_date_4_4', 'value_first_trimester_4_4', 'value_second_trimester_4_4', 'value_third_trimester_4_4', 'value_fourth_trimester_4_4',
                                    'project_name_4_5', 'city_4_5', 'total_number_project_4_5', 'total_cost_4_5', 'start_date_4_5', 'end_date_4_5', 'value_first_trimester_4_5', 'value_second_trimester_4_5', 'value_third_trimester_4_5', 'value_fourth_trimester_4_5',
                                ])
            
            writer.writerow([   
                                form_1, fiscal_year_1, company_name_1, liaison_officer_1, tel_1, project_1, branches_1,
                                project_name_1_1, city_1_1, total_number_project_1_1, total_cost_1_1, start_date_1_1, end_date_1_1, value_first_trimester_1_1, value_second_trimester_1_1, value_third_trimester_1_1, value_fourth_trimester_1_1,
                                project_name_1_2, city_1_2, total_number_project_1_2, total_cost_1_2, start_date_1_2, end_date_1_2, value_first_trimester_1_2, value_second_trimester_1_2, value_third_trimester_1_2, value_fourth_trimester_1_2,
                                project_name_1_3, city_1_3, total_number_project_1_3, total_cost_1_3, start_date_1_3, end_date_1_3, value_first_trimester_1_3, value_second_trimester_1_3, value_third_trimester_1_3, value_fourth_trimester_1_3,
                                project_name_1_4, city_1_4, total_number_project_1_4, total_cost_1_4, start_date_1_4, end_date_1_4, value_first_trimester_1_4, value_second_trimester_1_4, value_third_trimester_1_4, value_fourth_trimester_1_4,
                                project_name_1_5, city_1_5, total_number_project_1_5, total_cost_1_5, start_date_1_5, end_date_1_5, value_first_trimester_1_5, value_second_trimester_1_5, value_third_trimester_1_5, value_fourth_trimester_1_5,
                                
                                form_2, fiscal_year_2, company_name_2, liaison_officer_2, tel_2, project_2, branches_2,
                                project_name_2_1, city_2_1, total_number_project_2_1, total_cost_2_1, start_date_2_1, end_date_2_1, value_first_trimester_2_1, value_second_trimester_2_1, value_third_trimester_2_1, value_fourth_trimester_2_1,
                                project_name_2_2, city_2_2, total_number_project_2_2, total_cost_2_2, start_date_2_2, end_date_2_2, value_first_trimester_2_2, value_second_trimester_2_2, value_third_trimester_2_2, value_fourth_trimester_2_2,
                                project_name_2_3, city_2_3, total_number_project_2_3, total_cost_2_3, start_date_2_3, end_date_2_3, value_first_trimester_2_3, value_second_trimester_2_3, value_third_trimester_2_3, value_fourth_trimester_2_3,
                                project_name_2_4, city_2_4, total_number_project_2_4, total_cost_2_4, start_date_2_4, end_date_2_4, value_first_trimester_2_4, value_second_trimester_2_4, value_third_trimester_2_4, value_fourth_trimester_2_4,
                                project_name_2_5, city_2_5, total_number_project_2_5, total_cost_2_5, start_date_2_5, end_date_2_5, value_first_trimester_2_5, value_second_trimester_2_5, value_third_trimester_2_5, value_fourth_trimester_2_5,
                                
                                form_3, fiscal_year_3, company_name_3, liaison_officer_3, tel_3, project_3, branches_3,
                                project_name_3_1, city_3_1, total_number_project_3_1, total_cost_3_1, start_date_3_1, end_date_3_1, value_first_trimester_3_1, value_second_trimester_3_1, value_third_trimester_3_1, value_fourth_trimester_3_1,
                                project_name_3_2, city_3_2, total_number_project_3_2, total_cost_3_2, start_date_3_2, end_date_3_2, value_first_trimester_3_2, value_second_trimester_3_2, value_third_trimester_3_2, value_fourth_trimester_3_2,
                                project_name_3_3, city_3_3, total_number_project_3_3, total_cost_3_3, start_date_3_3, end_date_3_3, value_first_trimester_3_3, value_second_trimester_3_3, value_third_trimester_3_3, value_fourth_trimester_3_3,
                                project_name_3_4, city_3_4, total_number_project_3_4, total_cost_3_4, start_date_3_4, end_date_3_4, value_first_trimester_3_4, value_second_trimester_3_4, value_third_trimester_3_4, value_fourth_trimester_3_4,
                                project_name_3_5, city_3_5, total_number_project_3_5, total_cost_3_5, start_date_3_5, end_date_3_5, value_first_trimester_3_5, value_second_trimester_3_5, value_third_trimester_3_5, value_fourth_trimester_3_5,
                                
                
                                form_4, fiscal_year_4, company_name_4, liaison_officer_4, tel_4, project_4, branches_4,
                                project_name_4_1, city_4_1, total_number_project_4_1, total_cost_4_1, start_date_4_1, end_date_4_1, value_first_trimester_4_1, value_second_trimester_4_1, value_third_trimester_4_1, value_fourth_trimester_4_1,
                                project_name_4_2, city_4_2, total_number_project_4_2, total_cost_4_2, start_date_4_2, end_date_4_2, value_first_trimester_4_2, value_second_trimester_4_2, value_third_trimester_4_2, value_fourth_trimester_4_2,
                                project_name_4_3, city_4_3, total_number_project_4_3, total_cost_4_3, start_date_4_3, end_date_4_3, value_first_trimester_4_3, value_second_trimester_4_3, value_third_trimester_4_3, value_fourth_trimester_4_3,
                                project_name_4_4, city_4_4, total_number_project_4_4, total_cost_4_4, start_date_4_4, end_date_4_4, value_first_trimester_4_4, value_second_trimester_4_4, value_third_trimester_4_4, value_fourth_trimester_4_4,
                                project_name_4_5, city_4_5, total_number_project_4_5, total_cost_4_5, start_date_4_5, end_date_4_5, value_first_trimester_4_5, value_second_trimester_4_5, value_third_trimester_4_5, value_fourth_trimester_4_5,
                             ])  

        return render(request, "cuestionarios/succesfull.html")
    
    return render(request, "cuestionarios/construcción/JP-541.html")


def succesfull_page(request):
    return render(request, "cuestionarios/succesfull.html")



