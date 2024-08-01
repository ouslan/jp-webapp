import pandas as pd
from django.shortcuts import render
from .models import *
from web_app import graphics_function as gf
import csv
from django.shortcuts import render, redirect
from django.http import HttpResponse
from src.dao.data_db_dao import DAO
import os
from src.formularios.form_ip_110 import IP_110
from src.formularios.form_jp_304 import JP_304
from src.formularios.form_jp_361 import JP_361
from src.formularios.form_jp_362 import JP_362
from src.formularios.form_jp_364 import JP_364
from src.formularios.form_jp_529 import JP_529
from src.formularios.form_jp_541 import JP_541
from src.formularios.form_jp_363 import JP_363
from src.formularios.form_jp_560_63110 import JP_560_63110
from src.formularios.form_ip_210 import IP_210
from src.formularios.form_ip_220 import IP_220
from src.formularios.form_jp_560_63111 import JP_560_63111
from src.formularios.form_ip_230 import IP_230
from src.formularios.form_jp_560_63210 import JP_560_63210
from src.formularios.form_jp_560_2 import JP_560_2


def home(request):
    return render(request, "home.html")

def macro(request):
    x = [
        2000,
        2001,
        2002,
        2003,
        2004,
        2005,
        2006,
        2007,
        2008,
        2009,
        2010,
        2011,
        2012,
        2013,
        2014,
        2015,
        2016,
        2017,
        2018,
        2019,
        2020,
        2021,
        2022,
        2023,
        2024,
    ]
    y = [
        14,
        55,
        44,
        13,
        29,
        20,
        45,
        39,
        29,
        10,
        50,
        60,
        39,
        36,
        49,
        18,
        49,
        50,
        69,
        18,
        13,
        11,
        4,
        2,
        1,
    ]

    x_title = ""

    y_title = ""

    fig = gf.graph(x, y, x_title, y_title)

    macro_html_1 = fig.to_html()
    macro_html_2 = fig.to_html()

    context = {"macro1": macro_html_1, "macro2": macro_html_2}

    return render(request, "macro.html", context)

def datos_demograficos(request):
    return render(request, "demograficos.html")

def ciclos_economicos(request):
    x = [
        2000,
        2001,
        2002,
        2003,
        2004,
        2005,
        2006,
        2007,
        2008,
        2009,
        2010,
        2011,
        2012,
        2013,
        2014,
        2015,
        2016,
        2017,
        2018,
        2019,
        2020,
        2021,
        2022,
        2023,
        2024,
    ]
    y = [
        14,
        55,
        44,
        13,
        29,
        20,
        45,
        39,
        29,
        10,
        50,
        60,
        39,
        36,
        49,
        18,
        49,
        50,
        69,
        18,
        13,
        11,
        4,
        2,
        1,
    ]

    x_title = ""
    y_title = ""

    fig = gf.graph(x, y, x_title, y_title)

    ciclos_economicos = fig.to_html()

    context = {"ciclos_economicos": ciclos_economicos}
    return render(request, "ciclos_economicos.html", context)

def indicadores(request):
    df = pd.read_csv("src/data/indicadores.csv")
    df_x = df.melt(var_name="Year")
    df_y = df.melt(value_name="Value")

    x = df_x["Year"]
    y = df_y["Value"]

    x_1 = [
        2000,
        2001,
        2002,
        2003,
        2004,
        2005,
        2006,
        2007,
        2008,
        2009,
        2010,
        2011,
        2012,
        2013,
    ]
    y_1 = [14, 55, 44, 13, 29, 20, 45, 39, 29, 10, 50, 60, 39, 12]

    x_title = "Años"
    y_title = "Indices"

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

    context = {
        "indicadores": indicadores_html,
        "indicadores2": indicadores_html2,
        "indicadores3": indicadores_html3,
        "indicadores4": indicadores_html4,
        "indicadores5": indicadores_html5,
        "indicadores6": indicadores_html6,
        "indicadores7": indicadores_html7,
        "indicadores8": indicadores_html8,
        "indicadores9": indicadores_html9,
        "indicadores10": indicadores_html10,
        "indicadores11": indicadores_html11,
        "indicadores12": indicadores_html12,
        "indicadores13": indicadores_html13,
        "indicadores14": indicadores_html14,
        "indicadores15": indicadores_html15,
        "indicadores16": indicadores_html16,
        "indicadores17": indicadores_html17,
        "indicadores18": indicadores_html18,
    }
    return render(request, "indicadores.html", context)

def succesfull_page(request):
    return render(request, "forms/succesfull.html")

def Forms(request):
    return render(request, "forms/forms.html")





def JP_375(request):
    if request.method == "POST":
        # Retrieve form data
        year_1 = request.POST.get("year_1")
        year_2 = request.POST.get("year_2")
        year_3 = request.POST.get("year_3")

        FHA_1 = request.POST.get("FHA_1")
        FHA_2 = request.POST.get("FHA_2")
        FHA_3 = request.POST.get("FHA_3")

        veteran_1 = request.POST.get("veteran_1")
        veteran_2 = request.POST.get("veteran_2")
        veteran_3 = request.POST.get("veteran_3")

        bank_1 = request.POST.get("bank_1")
        bank_2 = request.POST.get("bank_2")
        bank_3 = request.POST.get("bank_3")

        conventional_1 = request.POST.get("conventional_1")
        conventional_2 = request.POST.get("conventional_2")
        conventional_3 = request.POST.get("conventional_3")

        other_1 = request.POST.get("other_1")
        other_2 = request.POST.get("other_2")
        other_3 = request.POST.get("other_3")

        FHA_2_1 = request.POST.get("FHA_2_1")
        FHA_2_2 = request.POST.get("FHA_2_2")
        FHA_2_3 = request.POST.get("FHA_2_3")

        veteran_2_1 = request.POST.get("veteran_2_1")
        veteran_2_2 = request.POST.get("veteran_2_2")
        veteran_2_3 = request.POST.get("veteran_2_3")

        conventional_2_1 = request.POST.get("conventional_2_1")
        conventional_2_2 = request.POST.get("conventional_2_2")
        conventional_2_3 = request.POST.get("conventional_2_3")

        others_2_1 = request.POST.get("others_2_1")
        others_2_2 = request.POST.get("others_2_2")
        others_2_3 = request.POST.get("others_2_3")

        FHA_3_1 = request.POST.get("FHA_3_1")
        FHA_3_2 = request.POST.get("FHA_3_2")
        FHA_3_3 = request.POST.get("FHA_3_3")

        veteran_3_1 = request.POST.get("veteran_3_1")
        veteran_3_2 = request.POST.get("veteran_3_2")
        veteran_3_3 = request.POST.get("veteran_3_3")

        bank_2_1 = request.POST.get("bank_2_1")
        bank_2_2 = request.POST.get("bank_2_2")
        bank_2_3 = request.POST.get("bank_2_3")

        conventional_3_1 = request.POST.get("conventional_3_1")
        conventional_3_2 = request.POST.get("conventional_3_2")
        conventional_3_3 = request.POST.get("conventional_3_3")

        others_3_1 = request.POST.get("others_3_1")
        others_3_2 = request.POST.get("others_3_2")
        others_3_3 = request.POST.get("others_3_3")

        FHA_4_1 = request.POST.get("FHA_4_1")
        FHA_4_2 = request.POST.get("FHA_4_2")
        FHA_4_3 = request.POST.get("FHA_4_3")

        veteran_4_1 = request.POST.get("veteran_4_1")
        veteran_4_2 = request.POST.get("veteran_4_2")
        veteran_4_3 = request.POST.get("veteran_4_3")

        conventional_4_1 = request.POST.get("conventional_4_1")
        conventional_4_2 = request.POST.get("conventional_4_2")
        conventional_4_3 = request.POST.get("conventional_4_3")

        others_4_1 = request.POST.get("others_4_1")
        others_4_2 = request.POST.get("others_4_2")
        others_4_3 = request.POST.get("others_4_3")

        commissions_1 = request.POST.get("commissions_1")
        commissions_2 = request.POST.get("commissions_2")
        commissions_3 = request.POST.get("commissions_3")

        phone = request.POST.get("phone")
        signature = request.POST.get("signature")
        position = request.POST.get("position")

        csv_file_path = "data/cuestionarios/balanza_de_pagos/JP-375.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "year_1",
                        "year_2",
                        "year_3",
                        "FHA_1",
                        "FHA_2",
                        "FHA_3",
                        "veteran_1",
                        "veteran_2",
                        "veteran_3",
                        "bank_1",
                        "bank_2",
                        "bank_3",
                        "conventional_1",
                        "conventional_2",
                        "conventional_3",
                        "other_1",
                        "other_2",
                        "other_3",
                        "FHA_2_1",
                        "FHA_2_2",
                        "FHA_2_3",
                        "veteran_2_1",
                        "veteran_2_2",
                        "veteran_2_3",
                        "conventional_2_1",
                        "conventional_2_2",
                        "conventional_2_3",
                        "others_2_1",
                        "others_2_2",
                        "others_2_3",
                        "FHA_3_1",
                        "FHA_3_2",
                        "FHA_3_3",
                        "veteran_3_1",
                        "veteran_3_2",
                        "veteran_3_3",
                        "bank_2_1",
                        "bank_2_2",
                        "bank_2_3",
                        "conventional_3_1",
                        "conventional_3_2",
                        "conventional_3_3",
                        "others_3_1",
                        "others_3_2",
                        "others_3_3",
                        "FHA_4_1",
                        "FHA_4_2",
                        "FHA_4_3",
                        "veteran_4_1",
                        "veteran_4_2",
                        "veteran_4_3",
                        "conventional_4_1",
                        "conventional_4_2",
                        "conventional_4_3",
                        "others_4_1",
                        "others_4_2",
                        "others_4_3",
                        "commissions_1",
                        "commissions_2",
                        "commissions_3",
                        "phone",
                        "signature",
                        "position",
                    ]
                )

            writer.writerow(
                [
                    year_1,
                    year_2,
                    year_3,
                    FHA_1,
                    FHA_2,
                    FHA_3,
                    veteran_1,
                    veteran_2,
                    veteran_3,
                    bank_1,
                    bank_2,
                    bank_3,
                    conventional_1,
                    conventional_2,
                    conventional_3,
                    other_1,
                    other_2,
                    other_3,
                    FHA_2_1,
                    FHA_2_2,
                    FHA_2_3,
                    veteran_2_1,
                    veteran_2_2,
                    veteran_2_3,
                    conventional_2_1,
                    conventional_2_2,
                    conventional_2_3,
                    others_2_1,
                    others_2_2,
                    others_2_3,
                    FHA_3_1,
                    FHA_3_2,
                    FHA_3_3,
                    veteran_3_1,
                    veteran_3_2,
                    veteran_3_3,
                    bank_2_1,
                    bank_2_2,
                    bank_2_3,
                    conventional_3_1,
                    conventional_3_2,
                    conventional_3_3,
                    others_3_1,
                    others_3_2,
                    others_3_3,
                    FHA_4_1,
                    FHA_4_2,
                    FHA_4_3,
                    veteran_4_1,
                    veteran_4_2,
                    veteran_4_3,
                    conventional_4_1,
                    conventional_4_2,
                    conventional_4_3,
                    others_4_1,
                    others_4_2,
                    others_4_3,
                    commissions_1,
                    commissions_2,
                    commissions_3,
                    phone,
                    signature,
                    position,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/balanza_de_pagos/JP-375.csv",
            dtypes={
                "year_1": int,
                "year_2": int,
                "year_3": int,
                "FHA_1": float,
                "FHA_2": float,
                "FHA_3": float,
                "veteran_1": float,
                "veteran_2": float,
                "veteran_3": float,
                "bank_1": float,
                "bank_2": float,
                "bank_3": float,
                "conventional_1": float,
                "conventional_2": float,
                "conventional_3": float,
                "other_1": float,
                "other_2": float,
                "other_3": float,
                "FHA_2_1": float,
                "FHA_2_2": float,
                "FHA_2_3": float,
                "veteran_2_1": float,
                "veteran_2_2": float,
                "veteran_2_3": float,
                "conventional_2_1": float,
                "conventional_2_2": float,
                "conventional_2_3": float,
                "others_2_1": float,
                "others_2_2": float,
                "others_2_3": float,
                "FHA_3_1": float,
                "FHA_3_2": float,
                "FHA_3_3": float,
                "veteran_3_1": float,
                "veteran_3_2": float,
                "veteran_3_3": float,
                "bank_2_1": float,
                "bank_2_2": float,
                "bank_2_3": float,
                "conventional_3_1": float,
                "conventional_3_2": float,
                "conventional_3_3": float,
                "others_3_1": float,
                "others_3_2": float,
                "others_3_3": float,
                "FHA_4_1": float,
                "FHA_4_2": float,
                "FHA_4_3": float,
                "veteran_4_1": float,
                "veteran_4_2": float,
                "veteran_4_3": float,
                "conventional_4_1": float,
                "conventional_4_2": float,
                "conventional_4_3": float,
                "others_4_1": float,
                "others_4_2": float,
                "others_4_3": float,
                "commissions_1": float,
                "commissions_2": float,
                "commissions_3": float,
                "phone": str,
                "signature": str,
                "position": str,
            },
            table_name="JP_375",
            table_id="25",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/balanza_de_pagos/JP-375.html")


def IP_480(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get("company_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")
        legal_form = request.POST.get("legal_form")
        cfc = request.POST.get("cfc")
        business_function = request.POST.get("business_function")
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        operation_incomes_1 = request.POST.get("operation_incomes_1")
        operation_incomes_2 = request.POST.get("operation_incomes_2")
        people_A_1 = request.POST.get("people_A_1")
        people_A_2 = request.POST.get("people_A_2")
        industries_businesses_A_1 = request.POST.get("industries_businesses_A_1")
        industries_businesses_A_2 = request.POST.get("industries_businesses_A_2")
        incomes_interests_1 = request.POST.get("incomes_interests_1")
        incomes_interests_2 = request.POST.get("incomes_interests_2")
        incomes_rents_1 = request.POST.get("incomes_rents_1")
        incomes_rents_2 = request.POST.get("incomes_rents_2")
        dividends_1 = request.POST.get("dividends_1")
        dividends_2 = request.POST.get("dividends_2")
        others_incomes_1 = request.POST.get("others_incomes_1")
        others_incomes_2 = request.POST.get("others_incomes_2")
        total_incomes_1 = request.POST.get("total_incomes_1")
        total_incomes_2 = request.POST.get("total_incomes_2")
        salaries_1 = request.POST.get("salaries_1")
        salaries_2 = request.POST.get("salaries_2")
        expenses_interests_1 = request.POST.get("expenses_interests_1")
        expenses_interests_2 = request.POST.get("expenses_interests_2")
        expenses_rents_1 = request.POST.get("expenses_rents_1")
        expenses_rents_2 = request.POST.get("expenses_rents_2")
        depreciation_1 = request.POST.get("depreciation_1")
        depreciation_2 = request.POST.get("depreciation_2")
        donations_1 = request.POST.get("donations_1")
        donations_2 = request.POST.get("donations_2")
        sales_tax_1 = request.POST.get("sales_tax_1")
        sales_tax_2 = request.POST.get("sales_tax_2")
        machinery_1 = request.POST.get("machinery_1")
        machinery_2 = request.POST.get("machinery_2")
        other_purchases_1 = request.POST.get("other_purchases_1")
        other_purchases_2 = request.POST.get("other_purchases_2")
        licenses_1 = request.POST.get("licenses_1")
        licenses_2 = request.POST.get("licenses_2")
        other_expenses_1 = request.POST.get("other_expenses_1")
        other_expenses_2 = request.POST.get("other_expenses_2")
        total_expenses_1 = request.POST.get("total_expenses_1")
        total_expenses_2 = request.POST.get("total_expenses_2")
        net_profit_1 = request.POST.get("net_profit_1")
        net_profit_2 = request.POST.get("net_profit_2")
        income_tax_1 = request.POST.get("income_tax_1")
        income_tax_2 = request.POST.get("income_tax_2")
        profit_after_tax_1 = request.POST.get("profit_after_tax_1")
        profit_after_tax_2 = request.POST.get("profit_after_tax_2")
        withheld_tax_1 = request.POST.get("withheld_tax_1")
        withheld_tax_2 = request.POST.get("withheld_tax_2")
        signature = request.POST.get("signature")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-480.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "company_name",
                        "address",
                        "email",
                        "liaison_officer",
                        "ssn",
                        "tel",
                        "fax",
                        "legal_form",
                        "cfc",
                        "business_function",
                        "closing_date",
                        "start_year",
                        "end_year",
                        "operation_incomes_1",
                        "operation_incomes_2",
                        "people_A_1",
                        "people_A_2",
                        "industries_businesses_A_1",
                        "industries_businesses_A_2",
                        "incomes_interests_1",
                        "incomes_interests_2",
                        "incomes_rents_1",
                        "incomes_rents_2",
                        "dividends_1",
                        "dividends_2",
                        "others_incomes_1",
                        "others_incomes_2",
                        "total_incomes_1",
                        "total_incomes_2",
                        "salaries_1",
                        "salaries_2",
                        "expenses_interests_1",
                        "expenses_interests_2",
                        "expenses_rents_1",
                        "expenses_rents_2",
                        "depreciation_1",
                        "depreciation_2",
                        "donations_1",
                        "donations_2",
                        "sales_tax_1",
                        "sales_tax_2",
                        "machinery_1",
                        "machinery_2",
                        "other_purchases_1",
                        "other_purchases_2",
                        "licenses_1",
                        "licenses_2",
                        "other_expenses_1",
                        "other_expenses_2",
                        "total_expenses_1",
                        "total_expenses_2",
                        "net_profit_1",
                        "net_profit_2",
                        "income_tax_1",
                        "income_tax_2",
                        "profit_after_tax_1",
                        "profit_after_tax_2",
                        "withheld_tax_1",
                        "withheld_tax_2",
                        "signature",
                        "rank",
                    ]
                )

            writer.writerow(
                [
                    company_name,
                    address,
                    email,
                    liaison_officer,
                    ssn,
                    tel,
                    fax,
                    legal_form,
                    cfc,
                    business_function,
                    closing_date,
                    start_year,
                    end_year,
                    operation_incomes_1,
                    operation_incomes_2,
                    people_A_1,
                    people_A_2,
                    industries_businesses_A_1,
                    industries_businesses_A_2,
                    incomes_interests_1,
                    incomes_interests_2,
                    incomes_rents_1,
                    incomes_rents_2,
                    dividends_1,
                    dividends_2,
                    others_incomes_1,
                    others_incomes_2,
                    total_incomes_1,
                    total_incomes_2,
                    salaries_1,
                    salaries_2,
                    expenses_interests_1,
                    expenses_interests_2,
                    expenses_rents_1,
                    expenses_rents_2,
                    depreciation_1,
                    depreciation_2,
                    donations_1,
                    donations_2,
                    sales_tax_1,
                    sales_tax_2,
                    machinery_1,
                    machinery_2,
                    other_purchases_1,
                    other_purchases_2,
                    licenses_1,
                    licenses_2,
                    other_expenses_1,
                    other_expenses_2,
                    total_expenses_1,
                    total_expenses_2,
                    net_profit_1,
                    net_profit_2,
                    income_tax_1,
                    income_tax_2,
                    profit_after_tax_1,
                    profit_after_tax_2,
                    withheld_tax_1,
                    withheld_tax_2,
                    signature,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-480.csv",
            dtypes={
                "company_name": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "ssn": str,
                "tel": str,
                "fax": str,
                "legal_form": str,
                "cfc": str,
                "business_function": str,
                "closing_date": str,
                "start_year": int,
                "end_year": int,
                "operation_incomes_1": float,
                "operation_incomes_2": float,
                "people_A_1": float,
                "people_A_2": float,
                "industries_businesses_A_1": float,
                "industries_businesses_A_2": float,
                "incomes_interests_1": float,
                "incomes_interests_2": float,
                "incomes_rents_1": float,
                "incomes_rents_2": float,
                "dividends_1": float,
                "dividends_2": float,
                "others_incomes_1": float,
                "others_incomes_2": float,
                "total_incomes_1": float,
                "total_incomes_2": float,
                "salaries_1": float,
                "salaries_2": float,
                "expenses_interests_1": float,
                "expenses_interests_2": float,
                "expenses_rents_1": float,
                "expenses_rents_2": float,
                "depreciation_1": float,
                "depreciation_2": float,
                "donations_1": float,
                "donations_2": float,
                "sales_tax_1": float,
                "sales_tax_2": float,
                "machinery_1": float,
                "machinery_2": float,
                "other_purchases_1": float,
                "other_purchases_2": float,
                "licenses_1": float,
                "licenses_2": float,
                "other_expenses_1": float,
                "other_expenses_2": float,
                "total_expenses_1": float,
                "total_expenses_2": float,
                "net_profit_1": float,
                "net_profit_2": float,
                "income_tax_1": float,
                "income_tax_2": float,
                "profit_after_tax_1": float,
                "profit_after_tax_2": float,
                "withheld_tax_1": float,
                "withheld_tax_2": float,
                "signature": str,
                "rank": str,
            },
            table_name="IP_480",
            table_id="27",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-480.html")


def IP_420(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get("company_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")

        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")

        legal_form = request.POST.get("legal_form")
        cfc = request.POST.get("cfc")
        main_line = request.POST.get("main_line")
        business_type = request.POST.get("business_type")
        other_business_type = request.POST.get("other_business_type")
        accounting_period = request.POST.get("accounting_period")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        incomes_sales_1 = request.POST.get("incomes_sales_1")
        incomes_sales_2 = request.POST.get("incomes_sales_2")
        incomes_from_people_1 = request.POST.get("incomes_from_people_1")
        incomes_from_people_2 = request.POST.get("incomes_from_people_2")
        incomes_industries_businesses_1 = request.POST.get(
            "incomes_industries_businesses_1"
        )
        incomes_industries_businesses_2 = request.POST.get(
            "incomes_industries_businesses_2"
        )
        incomes_less_cost_1 = request.POST.get("incomes_less_cost_1")
        incomes_less_cost_2 = request.POST.get("incomes_less_cost_2")
        incomes_inventory_beginning_1 = request.POST.get(
            "incomes_inventory_beginning_1"
        )
        incomes_inventory_beginning_2 = request.POST.get(
            "incomes_inventory_beginning_2"
        )
        incomes_purchases_1 = request.POST.get("incomes_purchases_1")
        incomes_purchases_2 = request.POST.get("incomes_purchases_2")
        incomes_inventory_end_1 = request.POST.get("incomes_inventory_end_1")
        incomes_inventory_end_2 = request.POST.get("incomes_inventory_end_2")
        incomes_gross_profit_1 = request.POST.get("incomes_gross_profit_1")
        incomes_gross_profit_2 = request.POST.get("incomes_gross_profit_2")
        other_operation_incomes_1 = request.POST.get("other_operation_incomes_1")
        other_operation_incomes_2 = request.POST.get("other_operation_incomes_2")
        incomes_interests_1 = request.POST.get("incomes_interests_1")
        incomes_interests_2 = request.POST.get("incomes_interests_2")
        incomes_rent_1 = request.POST.get("incomes_rent_1")
        incomes_rent_2 = request.POST.get("incomes_rent_2")
        incomes_gain_loss_1 = request.POST.get("incomes_gain_loss_1")
        incomes_gain_loss_2 = request.POST.get("incomes_gain_loss_2")
        incomes_dividends_1 = request.POST.get("incomes_dividends_1")
        incomes_dividends_2 = request.POST.get("incomes_dividends_2")
        other_incomes_1 = request.POST.get("other_incomes_1")
        other_incomes_2 = request.POST.get("other_incomes_2")
        incomes_total_gross_1 = request.POST.get("incomes_total_gross_1")
        incomes_total_gross_2 = request.POST.get("incomes_total_gross_2")
        expenses_1 = request.POST.get("expenses_1")
        expenses_2 = request.POST.get("expenses_2")
        expenses_salaries_wages_bonus_1 = request.POST.get(
            "expenses_salaries_wages_bonus_1"
        )
        expenses_salaries_wages_bonus_2 = request.POST.get(
            "expenses_salaries_wages_bonus_2"
        )
        expenses_interests_1 = request.POST.get("expenses_interests_1")
        expenses_interests_2 = request.POST.get("expenses_interests_2")
        expenses_depreciation_1 = request.POST.get("expenses_depreciation_1")
        expenses_depreciation_2 = request.POST.get("expenses_depreciation_2")
        expenses_rent_1 = request.POST.get("expenses_rent_1")
        expenses_rent_2 = request.POST.get("expenses_rent_2")
        expenses_bad_debts_1 = request.POST.get("expenses_bad_debts_1")
        expenses_bad_debts_2 = request.POST.get("expenses_bad_debts_2")
        expenses_donations_1 = request.POST.get("expenses_donations_1")
        expenses_donations_2 = request.POST.get("expenses_donations_2")
        expenses_sales_taxes_1 = request.POST.get("expenses_sales_taxes_1")
        expenses_sales_taxes_2 = request.POST.get("expenses_sales_taxes_2")
        expenses_machinary_1 = request.POST.get("expenses_machinary_1")
        expenses_machinary_2 = request.POST.get("expenses_machinary_2")
        expenses_other_purchases_1 = request.POST.get("expenses_other_purchases_1")
        expenses_other_purchases_2 = request.POST.get("expenses_other_purchases_2")
        expenses_licenses_1 = request.POST.get("expenses_licenses_1")
        expenses_licenses_2 = request.POST.get("expenses_licenses_2")
        expenses_other_operations_1 = request.POST.get("expenses_other_operations_1")
        expenses_other_operations_2 = request.POST.get("expenses_other_operations_2")
        expenses_total_operations_1 = request.POST.get("expenses_total_operations_1")
        expenses_total_operations_2 = request.POST.get("expenses_total_operations_2")
        gross_profit_1 = request.POST.get("gross_profit_1")
        gross_profit_2 = request.POST.get("gross_profit_2")
        profit_income_tax_1 = request.POST.get("profit_income_tax_1")
        profit_income_tax_2 = request.POST.get("profit_income_tax_2")
        profit_after_income_tax_1 = request.POST.get("profit_after_income_tax_1")
        profit_after_income_tax_2 = request.POST.get("profit_after_income_tax_2")
        sales_tax_1 = request.POST.get("sales_tax_1")
        sales_tax_2 = request.POST.get("sales_tax_2")
        name = request.POST.get("name")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-420.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "company_name",
                        "address",
                        "email",
                        "liaison_officer",
                        "ssn",
                        "tel",
                        "fax",
                        "legal_form",
                        "cfc",
                        "main_line",
                        "business_type",
                        "other_business_type",
                        "accounting_period",
                        "start_year",
                        "end_year",
                        "incomes_sales_1",
                        "incomes_sales_2",
                        "incomes_from_people_1",
                        "incomes_from_people_2",
                        "incomes_industries_businesses_1",
                        "incomes_industries_businesses_2",
                        "incomes_less_cost_1",
                        "incomes_less_cost_2",
                        "incomes_inventory_beginning_1",
                        "incomes_inventory_beginning_2",
                        "incomes_purchases_1",
                        "incomes_purchases_2",
                        "incomes_inventory_end_1",
                        "incomes_inventory_end_2",
                        "incomes_gross_profit_1",
                        "incomes_gross_profit_2",
                        "other_operation_incomes_1",
                        "other_operation_incomes_2",
                        "incomes_interests_1",
                        "incomes_interests_2",
                        "incomes_rent_1",
                        "incomes_rent_2",
                        "incomes_gain_loss_1",
                        "incomes_gain_loss_2",
                        "incomes_dividends_1",
                        "incomes_dividends_2",
                        "other_incomes_1",
                        "other_incomes_2",
                        "incomes_total_gross_1",
                        "incomes_total_gross_2",
                        "expenses_1",
                        "expenses_2",
                        "expenses_salaries_wages_bonus_1",
                        "expenses_salaries_wages_bonus_2",
                        "expenses_interests_1",
                        "expenses_interests_2",
                        "expenses_depreciation_1",
                        "expenses_depreciation_2",
                        "expenses_rent_1",
                        "expenses_rent_2",
                        "expenses_bad_debts_1",
                        "expenses_bad_debts_2",
                        "expenses_donations_1",
                        "expenses_donations_2",
                        "expenses_sales_taxes_1",
                        "expenses_sales_taxes_2",
                        "expenses_machinary_1",
                        "expenses_machinary_2",
                        "expenses_other_purchases_1",
                        "expenses_other_purchases_2",
                        "expenses_licenses_1",
                        "expenses_licenses_2",
                        "expenses_other_operations_1",
                        "expenses_other_operations_2",
                        "expenses_total_operations_1",
                        "expenses_total_operations_2",
                        "gross_profit_1",
                        "gross_profit_2",
                        "profit_income_tax_1",
                        "profit_income_tax_2",
                        "profit_after_income_tax_1",
                        "profit_after_income_tax_2",
                        "sales_tax_1",
                        "sales_tax_2",
                        "name",
                        "rank",
                    ]
                )

            writer.writerow(
                [
                    company_name,
                    address,
                    email,
                    liaison_officer,
                    ssn,
                    tel,
                    fax,
                    legal_form,
                    cfc,
                    main_line,
                    business_type,
                    other_business_type,
                    accounting_period,
                    start_year,
                    end_year,
                    incomes_sales_1,
                    incomes_sales_2,
                    incomes_from_people_1,
                    incomes_from_people_2,
                    incomes_industries_businesses_1,
                    incomes_industries_businesses_2,
                    incomes_less_cost_1,
                    incomes_less_cost_2,
                    incomes_inventory_beginning_1,
                    incomes_inventory_beginning_2,
                    incomes_purchases_1,
                    incomes_purchases_2,
                    incomes_inventory_end_1,
                    incomes_inventory_end_2,
                    incomes_gross_profit_1,
                    incomes_gross_profit_2,
                    other_operation_incomes_1,
                    other_operation_incomes_2,
                    incomes_interests_1,
                    incomes_interests_2,
                    incomes_rent_1,
                    incomes_rent_2,
                    incomes_gain_loss_1,
                    incomes_gain_loss_2,
                    incomes_dividends_1,
                    incomes_dividends_2,
                    other_incomes_1,
                    other_incomes_2,
                    incomes_total_gross_1,
                    incomes_total_gross_2,
                    expenses_1,
                    expenses_2,
                    expenses_salaries_wages_bonus_1,
                    expenses_salaries_wages_bonus_2,
                    expenses_interests_1,
                    expenses_interests_2,
                    expenses_depreciation_1,
                    expenses_depreciation_2,
                    expenses_rent_1,
                    expenses_rent_2,
                    expenses_bad_debts_1,
                    expenses_bad_debts_2,
                    expenses_donations_1,
                    expenses_donations_2,
                    expenses_sales_taxes_1,
                    expenses_sales_taxes_2,
                    expenses_machinary_1,
                    expenses_machinary_2,
                    expenses_other_purchases_1,
                    expenses_other_purchases_2,
                    expenses_licenses_1,
                    expenses_licenses_2,
                    expenses_other_operations_1,
                    expenses_other_operations_2,
                    expenses_total_operations_1,
                    expenses_total_operations_2,
                    gross_profit_1,
                    gross_profit_2,
                    profit_income_tax_1,
                    profit_income_tax_2,
                    profit_after_income_tax_1,
                    profit_after_income_tax_2,
                    sales_tax_1,
                    sales_tax_2,
                    name,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-420.csv",
            dtypes={
                "company_name": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "ssn": str,
                "tel": str,
                "fax": str,
                "legal_form": str,
                "cfc": str,
                "main_line": str,
                "business_type": str,
                "other_business_type": str,
                "accounting_period": str,
                "start_year": int,
                "end_year": int,
                "incomes_sales_1": float,
                "incomes_sales_2": float,
                "incomes_from_people_1": float,
                "incomes_from_people_2": float,
                "incomes_industries_businesses_1": float,
                "incomes_industries_businesses_2": float,
                "incomes_less_cost_1": float,
                "incomes_less_cost_2": float,
                "incomes_inventory_beginning_1": float,
                "incomes_inventory_beginning_2": float,
                "incomes_purchases_1": float,
                "incomes_purchases_2": float,
                "incomes_inventory_end_1": float,
                "incomes_inventory_end_2": float,
                "incomes_gross_profit_1": float,
                "incomes_gross_profit_2": float,
                "other_operation_incomes_1": float,
                "other_operation_incomes_2": float,
                "incomes_interests_1": float,
                "incomes_interests_2": float,
                "incomes_rent_1": float,
                "incomes_rent_2": float,
                "incomes_gain_loss_1": float,
                "incomes_gain_loss_2": float,
                "incomes_dividends_1": float,
                "incomes_dividends_2": float,
                "other_incomes_1": float,
                "other_incomes_2": float,
                "incomes_total_gross_1": float,
                "incomes_total_gross_2": float,
                "expenses_1": float,
                "expenses_2": float,
                "expenses_salaries_wages_bonus_1": float,
                "expenses_salaries_wages_bonus_2": float,
                "expenses_interests_1": float,
                "expenses_interests_2": float,
                "expenses_depreciation_1": float,
                "expenses_depreciation_2": float,
                "expenses_rent_1": float,
                "expenses_rent_2": float,
                "expenses_bad_debts_1": float,
                "expenses_bad_debts_2": float,
                "expenses_donations_1": float,
                "expenses_donations_2": float,
                "expenses_sales_taxes_1": float,
                "expenses_sales_taxes_2": float,
                "expenses_machinary_1": float,
                "expenses_machinary_2": float,
                "expenses_other_purchases_1": float,
                "expenses_other_purchases_2": float,
                "expenses_licenses_1": float,
                "expenses_licenses_2": float,
                "expenses_other_operations_1": float,
                "expenses_other_operations_2": float,
                "expenses_total_operations_1": float,
                "expenses_total_operations_2": float,
                "gross_profit_1": float,
                "gross_profit_2": float,
                "profit_income_tax_1": float,
                "profit_income_tax_2": float,
                "profit_after_income_tax_1": float,
                "profit_after_income_tax_2": float,
                "sales_tax_1": float,
                "sales_tax_2": float,
                "name": str,
                "rank": str,
            },
            table_name="IP_420",
            table_id="29",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-420.html")


def IP_310(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get("company_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")
        legal_form = request.POST.get("legal_form")
        cfc = request.POST.get("cfc")
        end_month = request.POST.get("end_month")
        main_product_1 = request.POST.get("main_product_1")
        other_product_1 = request.POST.get("other_product_1")
        raw_material_used = request.POST.get("raw_material_used")
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        total_sales_1 = request.POST.get("total_sales_1")
        total_sales_2 = request.POST.get("total_sales_2")
        from_persons_1 = request.POST.get("from_persons_1")
        from_persons_2 = request.POST.get("from_persons_2")
        industries_businesses_1 = request.POST.get("industries_businesses_1")
        industries_businesses_2 = request.POST.get("industries_businesses_2")
        goods_manufactured_1 = request.POST.get("goods_manufactured_1")
        goods_manufactured_2 = request.POST.get("goods_manufactured_2")
        exports_val_1 = request.POST.get("exports_val_1")
        exports_val_2 = request.POST.get("exports_val_2")
        goods_manufactured_1_1 = request.POST.get("goods_manufactured_1_1")
        goods_manufactured_2_2 = request.POST.get("goods_manufactured_2_2")
        exports_val_1_1 = request.POST.get("exports_val_1_1")
        exports_val_2_2 = request.POST.get("exports_val_2_2")
        manufacturing_cost_1 = request.POST.get("manufacturing_cost_1")
        manufacturing_cost_2 = request.POST.get("manufacturing_cost_2")
        inventories_begginning_1 = request.POST.get("inventories_begginning_1")
        inventories_begginning_2 = request.POST.get("inventories_begginning_2")
        purchases_1 = request.POST.get("purchases_1")
        purchases_2 = request.POST.get("purchases_2")
        total_raw_1 = request.POST.get("total_raw_1")
        total_raw_2 = request.POST.get("total_raw_2")
        imported_1 = request.POST.get("imported_1")
        imported_2 = request.POST.get("imported_2")
        others_1 = request.POST.get("others_1")
        others_2 = request.POST.get("others_2")
        direct_wages_1 = request.POST.get("direct_wages_1")
        direct_wages_2 = request.POST.get("direct_wages_2")
        depreciation_1 = request.POST.get("depreciation_1")
        depreciation_2 = request.POST.get("depreciation_2")
        rent_land_1 = request.POST.get("rent_land_1")
        rent_land_2 = request.POST.get("rent_land_2")
        other_direct_1 = request.POST.get("other_direct_1")
        other_direct_2 = request.POST.get("other_direct_2")
        indirect_cost_1 = request.POST.get("indirect_cost_1")
        indirect_cost_2 = request.POST.get("indirect_cost_2")
        inventories_end_1 = request.POST.get("inventories_end_1")
        inventories_end_2 = request.POST.get("inventories_end_2")
        gross_profit_1 = request.POST.get("gross_profit_1")
        gross_profit_2 = request.POST.get("gross_profit_2")
        other_operating_1 = request.POST.get("other_operating_1")
        other_operating_2 = request.POST.get("other_operating_2")
        interest_1 = request.POST.get("interest_1")
        interest_2 = request.POST.get("interest_2")
        rent_land_3 = request.POST.get("rent_land_3")
        rent_land_4 = request.POST.get("rent_land_4")
        capital_gain_1 = request.POST.get("capital_gain_1")
        capital_gain_2 = request.POST.get("capital_gain_2")
        other_1 = request.POST.get("other_1")
        other_2 = request.POST.get("other_2")
        total_gross_1 = request.POST.get("total_gross_1")
        total_gross_2 = request.POST.get("total_gross_2")
        expenses_not_1 = request.POST.get("expenses_not_1")
        expenses_not_2 = request.POST.get("expenses_not_2")
        salaries_1 = request.POST.get("salaries_1")
        salaries_2 = request.POST.get("salaries_2")
        interest_3 = request.POST.get("interest_3")
        interest_4 = request.POST.get("interest_4")
        depreciation_3 = request.POST.get("depreciation_3")
        depreciation_4 = request.POST.get("depreciation_4")
        donations_1 = request.POST.get("donations_1")
        donations_2 = request.POST.get("donations_2")
        rent_land_5 = request.POST.get("rent_land_5")
        rent_land_6 = request.POST.get("rent_land_6")
        other_operating_3 = request.POST.get("other_operating_3")
        other_operating_4 = request.POST.get("other_operating_4")
        sales_tax_1 = request.POST.get("sales_tax_1")
        sales_tax_2 = request.POST.get("sales_tax_2")
        machinery_1 = request.POST.get("machinery_1")
        machinery_2 = request.POST.get("machinery_2")
        on_other_1 = request.POST.get("on_other_1")
        on_other_2 = request.POST.get("on_other_2")
        licenses_1 = request.POST.get("licenses_1")
        licenses_2 = request.POST.get("licenses_2")
        net_loss_1 = request.POST.get("net_loss_1")
        net_loss_2 = request.POST.get("net_loss_2")
        income_tax_1 = request.POST.get("income_tax_1")
        income_tax_2 = request.POST.get("income_tax_2")
        profit_after_tax_1 = request.POST.get("profit_after_tax_1")
        profit_after_tax_2 = request.POST.get("profit_after_tax_2")
        sales_and_use_withheld_1 = request.POST.get("sales_and_use_withheld_1")
        sales_and_use_withheld_2 = request.POST.get("sales_and_use_withheld_2")
        branches = request.POST.get("branches")
        branches_if_yes = request.POST.get("branches_if_yes")
        signature = request.POST.get("signature")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-310.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "company_name",
                        "address",
                        "email",
                        "liaison_officer",
                        "ssn",
                        "tel",
                        "fax",
                        "legal_form",
                        "cfc",
                        "end_month",
                        "main_product_1",
                        "other_product_1",
                        "raw_material_used",
                        "closing_date",
                        "start_year",
                        "end_year",
                        "total_sales_1",
                        "total_sales_2",
                        "from_persons_1",
                        "from_persons_2",
                        "industries_businesses_1",
                        "industries_businesses_2",
                        "goods_manufactured_1",
                        "goods_manufactured_2",
                        "exports_val_1",
                        "exports_val_2",
                        "goods_manufactured_1_1",
                        "goods_manufactured_2_2",
                        "exports_val_1_1",
                        "exports_val_2_2",
                        "manufacturing_cost_1",
                        "manufacturing_cost_2",
                        "inventories_begginning_1",
                        "inventories_begginning_2",
                        "purchases_1",
                        "purchases_2",
                        "total_raw_1",
                        "total_raw_2",
                        "imported_1",
                        "imported_2",
                        "others_1",
                        "others_2",
                        "direct_wages_1",
                        "direct_wages_2",
                        "depreciation_1",
                        "depreciation_2",
                        "rent_land_1",
                        "rent_land_2",
                        "other_direct_1",
                        "other_direct_2",
                        "indirect_cost_1",
                        "indirect_cost_2",
                        "inventories_end_1",
                        "inventories_end_2",
                        "gross_profit_1",
                        "gross_profit_2",
                        "other_operating_1",
                        "other_operating_2",
                        "interest_1",
                        "interest_2",
                        "rent_land_3",
                        "rent_land_4",
                        "capital_gain_1",
                        "capital_gain_2",
                        "other_1",
                        "other_2",
                        "total_gross_1",
                        "total_gross_2",
                        "expenses_not_1",
                        "expenses_not_2",
                        "salaries_1",
                        "salaries_2",
                        "interest_3",
                        "interest_4",
                        "depreciation_3",
                        "depreciation_4",
                        "donations_1",
                        "donations_2",
                        "rent_land_5",
                        "rent_land_6",
                        "other_operating_3",
                        "other_operating_4",
                        "sales_tax_1",
                        "sales_tax_2",
                        "machinery_1",
                        "machinery_2",
                        "on_other_1",
                        "on_other_2",
                        "licenses_1",
                        "licenses_2",
                        "net_loss_1",
                        "net_loss_2",
                        "income_tax_1",
                        "income_tax_2",
                        "profit_after_tax_1",
                        "profit_after_tax_2",
                        "sales_and_use_withheld_1",
                        "sales_and_use_withheld_2",
                        "branches",
                        "branches_if_yes",
                        "signature",
                        "rank",
                    ]
                )

            writer.writerow(
                [
                    company_name,
                    address,
                    email,
                    liaison_officer,
                    ssn,
                    tel,
                    fax,
                    legal_form,
                    cfc,
                    end_month,
                    main_product_1,
                    other_product_1,
                    raw_material_used,
                    closing_date,
                    start_year,
                    end_year,
                    total_sales_1,
                    total_sales_2,
                    from_persons_1,
                    from_persons_2,
                    industries_businesses_1,
                    industries_businesses_2,
                    goods_manufactured_1,
                    goods_manufactured_2,
                    exports_val_1,
                    exports_val_2,
                    goods_manufactured_1_1,
                    goods_manufactured_2_2,
                    exports_val_1_1,
                    exports_val_2_2,
                    manufacturing_cost_1,
                    manufacturing_cost_2,
                    inventories_begginning_1,
                    inventories_begginning_2,
                    purchases_1,
                    purchases_2,
                    total_raw_1,
                    total_raw_2,
                    imported_1,
                    imported_2,
                    others_1,
                    others_2,
                    direct_wages_1,
                    direct_wages_2,
                    depreciation_1,
                    depreciation_2,
                    rent_land_1,
                    rent_land_2,
                    other_direct_1,
                    other_direct_2,
                    indirect_cost_1,
                    indirect_cost_2,
                    inventories_end_1,
                    inventories_end_2,
                    gross_profit_1,
                    gross_profit_2,
                    other_operating_1,
                    other_operating_2,
                    interest_1,
                    interest_2,
                    rent_land_3,
                    rent_land_4,
                    capital_gain_1,
                    capital_gain_2,
                    other_1,
                    other_2,
                    total_gross_1,
                    total_gross_2,
                    expenses_not_1,
                    expenses_not_2,
                    salaries_1,
                    salaries_2,
                    interest_3,
                    interest_4,
                    depreciation_3,
                    depreciation_4,
                    donations_1,
                    donations_2,
                    rent_land_5,
                    rent_land_6,
                    other_operating_3,
                    other_operating_4,
                    sales_tax_1,
                    sales_tax_2,
                    machinery_1,
                    machinery_2,
                    on_other_1,
                    on_other_2,
                    licenses_1,
                    licenses_2,
                    net_loss_1,
                    net_loss_2,
                    income_tax_1,
                    income_tax_2,
                    profit_after_tax_1,
                    profit_after_tax_2,
                    sales_and_use_withheld_1,
                    sales_and_use_withheld_2,
                    branches,
                    branches_if_yes,
                    signature,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-310.csv",
            dtypes={
                "company_name": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "ssn": str,
                "tel": str,
                "fax": str,
                "legal_form": str,
                "cfc": str,
                "end_month": str,
                "main_product_1": str,
                "other_product_1": str,
                "raw_material_used": str,
                "closing_date": str,
                "start_year": int,
                "end_year": int,
                "total_sales_1": float,
                "total_sales_2": float,
                "from_persons_1": float,
                "from_persons_2": float,
                "industries_businesses_1": float,
                "industries_businesses_2": float,
                "goods_manufactured_1": float,
                "goods_manufactured_2": float,
                "exports_val_1": float,
                "exports_val_2": float,
                "goods_manufactured_1_1": float,
                "goods_manufactured_2_2": float,
                "exports_val_1_1": float,
                "exports_val_2_2": float,
                "manufacturing_cost_1": float,
                "manufacturing_cost_2": float,
                "inventories_begginning_1": float,
                "inventories_begginning_2": float,
                "purchases_1": float,
                "purchases_2": float,
                "total_raw_1": float,
                "total_raw_2": float,
                "imported_1": float,
                "imported_2": float,
                "others_1": float,
                "others_2": float,
                "direct_wages_1": float,
                "direct_wages_2": float,
                "depreciation_1": float,
                "depreciation_2": float,
                "rent_land_1": float,
                "rent_land_2": float,
                "other_direct_1": float,
                "other_direct_2": float,
                "indirect_cost_1": float,
                "indirect_cost_2": float,
                "inventories_end_1": float,
                "inventories_end_2": float,
                "gross_profit_1": float,
                "gross_profit_2": float,
                "other_operating_1": float,
                "other_operating_2": float,
                "interest_1": float,
                "interest_2": float,
                "rent_land_3": float,
                "rent_land_4": float,
                "capital_gain_1": float,
                "capital_gain_2": float,
                "other_1": float,
                "other_2": float,
                "total_gross_1": float,
                "total_gross_2": float,
                "expenses_not_1": float,
                "expenses_not_2": float,
                "salaries_1": float,
                "salaries_2": float,
                "interest_3": float,
                "interest_4": float,
                "depreciation_3": float,
                "depreciation_4": float,
                "donations_1": float,
                "donations_2": float,
                "rent_land_5": float,
                "rent_land_6": float,
                "other_operating_3": float,
                "other_operating_4": float,
                "sales_tax_1": float,
                "sales_tax_2": float,
                "machinery_1": float,
                "machinery_2": float,
                "on_other_1": float,
                "on_other_2": float,
                "licenses_1": float,
                "licenses_2": float,
                "net_loss_1": float,
                "net_loss_2": float,
                "income_tax_1": float,
                "income_tax_2": float,
                "profit_after_tax_1": float,
                "profit_after_tax_2": float,
                "sales_and_use_withheld_1": float,
                "sales_and_use_withheld_2": float,
                "branches": str,
                "branches_if_yes": str,
                "signature": str,
                "rank": str,
            },
            table_name="IP_310",
            table_id="30",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-310.html")


def JP_383(request):
    if request.method == "POST":
        # Retrieve form data
        other_section = request.POST.get("other_section")
        año = request.POST.get("año")
        julio_1 = request.POST.get("julio_1")
        julio_2 = request.POST.get("julio_2")
        julio_3 = request.POST.get("julio_3")
        julio_4 = request.POST.get("julio_4")
        julio_5 = request.POST.get("julio_5")
        julio_6 = request.POST.get("julio_6")
        agosto_1 = request.POST.get("agosto_1")
        agosto_2 = request.POST.get("agosto_2")
        agosto_3 = request.POST.get("agosto_3")
        agosto_4 = request.POST.get("agosto_4")
        agosto_5 = request.POST.get("agosto_5")
        agosto_6 = request.POST.get("agosto_6")
        septiembre_1 = request.POST.get("septiembre_1")
        septiembre_2 = request.POST.get("septiembre_2")
        septiembre_3 = request.POST.get("septiembre_3")
        septiembre_4 = request.POST.get("septiembre_4")
        septiembre_5 = request.POST.get("septiembre_5")
        septiembre_6 = request.POST.get("septiembre_6")
        subtotal_1 = request.POST.get("subtotal_1")
        subtotal_2 = request.POST.get("subtotal_2")
        subtotal_3 = request.POST.get("subtotal_3")
        subtotal_4 = request.POST.get("subtotal_4")
        subtotal_5 = request.POST.get("subtotal_5")
        subtotal_6 = request.POST.get("subtotal_6")
        octubre_1 = request.POST.get("octubre_1")
        octubre_2 = request.POST.get("octubre_2")
        octubre_3 = request.POST.get("octubre_3")
        octubre_4 = request.POST.get("octubre_4")
        octubre_5 = request.POST.get("octubre_5")
        octubre_6 = request.POST.get("octubre_6")
        noviembre_1 = request.POST.get("noviembre_1")
        noviembre_2 = request.POST.get("noviembre_2")
        noviembre_3 = request.POST.get("noviembre_3")
        noviembre_4 = request.POST.get("noviembre_4")
        noviembre_5 = request.POST.get("noviembre_5")
        noviembre_6 = request.POST.get("noviembre_6")
        diciembre_1 = request.POST.get("diciembre_1")
        diciembre_2 = request.POST.get("diciembre_2")
        diciembre_3 = request.POST.get("diciembre_3")
        diciembre_4 = request.POST.get("diciembre_4")
        diciembre_5 = request.POST.get("diciembre_5")
        diciembre_6 = request.POST.get("diciembre_6")
        subtotal_11 = request.POST.get("subtotal_11")
        subtotal_12 = request.POST.get("subtotal_12")
        subtotal_13 = request.POST.get("subtotal_13")
        subtotal_14 = request.POST.get("subtotal_14")
        subtotal_15 = request.POST.get("subtotal_15")
        subtotal_16 = request.POST.get("subtotal_16")
        año_1 = request.POST.get("año_1")
        enero_1 = request.POST.get("enero_1")
        enero_2 = request.POST.get("enero_2")
        enero_3 = request.POST.get("enero_3")
        enero_4 = request.POST.get("enero_4")
        enero_5 = request.POST.get("enero_5")
        enero_6 = request.POST.get("enero_6")
        febrero_1 = request.POST.get("febrero_1")
        febrero_2 = request.POST.get("febrero_2")
        febrero_3 = request.POST.get("febrero_3")
        febrero_4 = request.POST.get("febrero_4")
        febrero_5 = request.POST.get("febrero_5")
        febrero_6 = request.POST.get("febrero_6")
        marzo_1 = request.POST.get("marzo_1")
        marzo_2 = request.POST.get("marzo_2")
        marzo_3 = request.POST.get("marzo_3")
        marzo_4 = request.POST.get("marzo_4")
        marzo_5 = request.POST.get("marzo_5")
        marzo_6 = request.POST.get("marzo_6")
        subtotal_21 = request.POST.get("subtotal_21")
        subtotal_22 = request.POST.get("subtotal_22")
        subtotal_23 = request.POST.get("subtotal_23")
        subtotal_24 = request.POST.get("subtotal_24")
        subtotal_25 = request.POST.get("subtotal_25")
        subtotal_26 = request.POST.get("subtotal_26")
        abril_1 = request.POST.get("abril_1")
        abril_2 = request.POST.get("abril_2")
        abril_3 = request.POST.get("abril_3")
        abril_4 = request.POST.get("abril_4")
        abril_5 = request.POST.get("abril_5")
        abril_6 = request.POST.get("abril_6")
        mayo_1 = request.POST.get("mayo_1")
        mayo_2 = request.POST.get("mayo_2")
        mayo_3 = request.POST.get("mayo_3")
        mayo_4 = request.POST.get("mayo_4")
        mayo_5 = request.POST.get("mayo_5")
        mayo_6 = request.POST.get("mayo_6")
        junio_1 = request.POST.get("junio_1")
        junio_2 = request.POST.get("junio_2")
        junio_3 = request.POST.get("junio_3")
        junio_4 = request.POST.get("junio_4")
        junio_5 = request.POST.get("junio_5")
        junio_6 = request.POST.get("junio_6")
        subtotal_31 = request.POST.get("subtotal_31")
        subtotal_32 = request.POST.get("subtotal_32")
        subtotal_33 = request.POST.get("subtotal_33")
        subtotal_34 = request.POST.get("subtotal_34")
        subtotal_35 = request.POST.get("subtotal_35")
        subtotal_36 = request.POST.get("subtotal_36")
        total_1 = request.POST.get("total_1")
        total_2 = request.POST.get("total_2")
        total_3 = request.POST.get("total_3")
        total_4 = request.POST.get("total_4")
        total_5 = request.POST.get("total_5")
        total_6 = request.POST.get("total_6")
        signature = request.POST.get("signature")
        name = request.POST.get("name")
        title = request.POST.get("title")
        phone = request.POST.get("phone")

        csv_file_path = "data/cuestionarios/balanza_de_pagos/JP-383.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "other_section",
                        "año",
                        "julio_1",
                        "julio_2",
                        "julio_3",
                        "julio_4",
                        "julio_5",
                        "julio_6",
                        "agosto_1",
                        "agosto_2",
                        "agosto_3",
                        "agosto_4",
                        "agosto_5",
                        "agosto_6",
                        "septiembre_1",
                        "septiembre_2",
                        "septiembre_3",
                        "septiembre_4",
                        "septiembre_5",
                        "septiembre_6",
                        "subtotal_1",
                        "subtotal_2",
                        "subtotal_3",
                        "subtotal_4",
                        "subtotal_5",
                        "subtotal_6",
                        "octubre_1",
                        "octubre_2",
                        "octubre_3",
                        "octubre_4",
                        "octubre_5",
                        "octubre_6",
                        "noviembre_1",
                        "noviembre_2",
                        "noviembre_3",
                        "noviembre_4",
                        "noviembre_5",
                        "noviembre_6",
                        "diciembre_1",
                        "diciembre_2",
                        "diciembre_3",
                        "diciembre_4",
                        "diciembre_5",
                        "diciembre_6",
                        "subtotal_11",
                        "subtotal_12",
                        "subtotal_13",
                        "subtotal_14",
                        "subtotal_15",
                        "subtotal_16",
                        "año_1",
                        "enero_1",
                        "enero_2",
                        "enero_3",
                        "enero_4",
                        "enero_5",
                        "enero_6",
                        "febrero_1",
                        "febrero_2",
                        "febrero_3",
                        "febrero_4",
                        "febrero_5",
                        "febrero_6",
                        "marzo_1",
                        "marzo_2",
                        "marzo_3",
                        "marzo_4",
                        "marzo_5",
                        "marzo_6",
                        "subtotal_21",
                        "subtotal_22",
                        "subtotal_23",
                        "subtotal_24",
                        "subtotal_25",
                        "subtotal_26",
                        "abril_1",
                        "abril_2",
                        "abril_3",
                        "abril_4",
                        "abril_5",
                        "abril_6",
                        "mayo_1",
                        "mayo_2",
                        "mayo_3",
                        "mayo_4",
                        "mayo_5",
                        "mayo_6",
                        "junio_1",
                        "junio_2",
                        "junio_3",
                        "junio_4",
                        "junio_5",
                        "junio_6",
                        "subtotal_31",
                        "subtotal_32",
                        "subtotal_33",
                        "subtotal_34",
                        "subtotal_35",
                        "subtotal_36",
                        "total_1",
                        "total_2",
                        "total_3",
                        "total_4",
                        "total_5",
                        "total_6",
                        "signature",
                        "name",
                        "title",
                        "phone",
                    ]
                )

            writer.writerow(
                [
                    other_section,
                    año,
                    julio_1,
                    julio_2,
                    julio_3,
                    julio_4,
                    julio_5,
                    julio_6,
                    agosto_1,
                    agosto_2,
                    agosto_3,
                    agosto_4,
                    agosto_5,
                    agosto_6,
                    septiembre_1,
                    septiembre_2,
                    septiembre_3,
                    septiembre_4,
                    septiembre_5,
                    septiembre_6,
                    subtotal_1,
                    subtotal_2,
                    subtotal_3,
                    subtotal_4,
                    subtotal_5,
                    subtotal_6,
                    octubre_1,
                    octubre_2,
                    octubre_3,
                    octubre_4,
                    octubre_5,
                    octubre_6,
                    noviembre_1,
                    noviembre_2,
                    noviembre_3,
                    noviembre_4,
                    noviembre_5,
                    noviembre_6,
                    diciembre_1,
                    diciembre_2,
                    diciembre_3,
                    diciembre_4,
                    diciembre_5,
                    diciembre_6,
                    subtotal_11,
                    subtotal_12,
                    subtotal_13,
                    subtotal_14,
                    subtotal_15,
                    subtotal_16,
                    año_1,
                    enero_1,
                    enero_2,
                    enero_3,
                    enero_4,
                    enero_5,
                    enero_6,
                    febrero_1,
                    febrero_2,
                    febrero_3,
                    febrero_4,
                    febrero_5,
                    febrero_6,
                    marzo_1,
                    marzo_2,
                    marzo_3,
                    marzo_4,
                    marzo_5,
                    marzo_6,
                    subtotal_21,
                    subtotal_22,
                    subtotal_23,
                    subtotal_24,
                    subtotal_25,
                    subtotal_26,
                    abril_1,
                    abril_2,
                    abril_3,
                    abril_4,
                    abril_5,
                    abril_6,
                    mayo_1,
                    mayo_2,
                    mayo_3,
                    mayo_4,
                    mayo_5,
                    mayo_6,
                    junio_1,
                    junio_2,
                    junio_3,
                    junio_4,
                    junio_5,
                    junio_6,
                    subtotal_31,
                    subtotal_32,
                    subtotal_33,
                    subtotal_34,
                    subtotal_35,
                    subtotal_36,
                    total_1,
                    total_2,
                    total_3,
                    total_4,
                    total_5,
                    total_6,
                    signature,
                    name,
                    title,
                    phone,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/balanza_de_pagos/JP-383.csv",
            dtypes={
                "other_section": str,
                "año": int,
                "julio_1": float,
                "julio_2": float,
                "julio_3": float,
                "julio_4": float,
                "julio_5": float,
                "julio_6": float,
                "agosto_1": float,
                "agosto_2": float,
                "agosto_3": float,
                "agosto_4": float,
                "agosto_5": float,
                "agosto_6": float,
                "septiembre_1": float,
                "septiembre_2": float,
                "septiembre_3": float,
                "septiembre_4": float,
                "septiembre_5": float,
                "septiembre_6": float,
                "subtotal_1": float,
                "subtotal_2": float,
                "subtotal_3": float,
                "subtotal_4": float,
                "subtotal_5": float,
                "subtotal_6": float,
                "octubre_1": float,
                "octubre_2": float,
                "octubre_3": float,
                "octubre_4": float,
                "octubre_5": float,
                "octubre_6": float,
                "noviembre_1": float,
                "noviembre_2": float,
                "noviembre_3": float,
                "noviembre_4": float,
                "noviembre_5": float,
                "noviembre_6": float,
                "diciembre_1": float,
                "diciembre_2": float,
                "diciembre_3": float,
                "diciembre_4": float,
                "diciembre_5": float,
                "diciembre_6": float,
                "subtotal_11": float,
                "subtotal_12": float,
                "subtotal_13": float,
                "subtotal_14": float,
                "subtotal_15": float,
                "subtotal_16": float,
                "año_1": int,
                "enero_1": float,
                "enero_2": float,
                "enero_3": float,
                "enero_4": float,
                "enero_5": float,
                "enero_6": float,
                "febrero_1": float,
                "febrero_2": float,
                "febrero_3": float,
                "febrero_4": float,
                "febrero_5": float,
                "febrero_6": float,
                "marzo_1": float,
                "marzo_2": float,
                "marzo_3": float,
                "marzo_4": float,
                "marzo_5": float,
                "marzo_6": float,
                "subtotal_21": float,
                "subtotal_22": float,
                "subtotal_23": float,
                "subtotal_24": float,
                "subtotal_25": float,
                "subtotal_26": float,
                "abril_1": float,
                "abril_2": float,
                "abril_3": float,
                "abril_4": float,
                "abril_5": float,
                "abril_6": float,
                "mayo_1": float,
                "mayo_2": float,
                "mayo_3": float,
                "mayo_4": float,
                "mayo_5": float,
                "mayo_6": float,
                "junio_1": float,
                "junio_2": float,
                "junio_3": float,
                "junio_4": float,
                "junio_5": float,
                "junio_6": float,
                "subtotal_31": float,
                "subtotal_32": float,
                "subtotal_33": float,
                "subtotal_34": float,
                "subtotal_35": float,
                "subtotal_36": float,
                "total_1": float,
                "total_2": float,
                "total_3": float,
                "total_4": float,
                "total_5": float,
                "total_6": float,
                "signature": str,
                "name": str,
                "title": str,
                "phone": str,
            },
            table_name="JP_383",
            table_id="45",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/balanza_de_pagos/JP-383.html")


def IP_440(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get("company_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")
        legal_form = request.POST.get("legal_form")
        cfc = request.POST.get("cfc")
        main_line = request.POST.get("main_line")
        business_type = request.POST.get("business_type")
        other_business_type = request.POST.get("other_business_type")
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        sales_A_1 = request.POST.get("sales_A_1")
        sales_A_2 = request.POST.get("sales_A_2")
        people_A_1 = request.POST.get("people_A_1")
        people_A_2 = request.POST.get("people_A_2")
        industries_businesses_A_1 = request.POST.get("industries_businesses_A_1")
        industries_businesses_A_2 = request.POST.get("industries_businesses_A_2")
        less_cost_A_1 = request.POST.get("less_cost_A_1")
        less_cost_A_2 = request.POST.get("less_cost_A_2")
        inventory_beginning_1 = request.POST.get("inventory_beginning_1")
        inventory_beginning_2 = request.POST.get("inventory_beginning_2")
        purchases_A_1 = request.POST.get("purchases_A_1")
        purchases_A_2 = request.POST.get("purchases_A_2")
        inventory_end_1 = request.POST.get("inventory_end_1")
        inventory_end_2 = request.POST.get("inventory_end_2")
        gross_profit_A_1 = request.POST.get("gross_profit_A_1")
        gross_profit_A_2 = request.POST.get("gross_profit_A_2")
        other_income_A_1 = request.POST.get("other_income_A_1")
        other_income_A_2 = request.POST.get("other_income_A_2")
        interests_A_1 = request.POST.get("interests_A_1")
        interests_A_2 = request.POST.get("interests_A_2")
        rent_A_1 = request.POST.get("rent_A_1")
        rent_A_2 = request.POST.get("rent_A_2")
        capital_gain_A_1 = request.POST.get("capital_gain_A_1")
        capital_gain_A_2 = request.POST.get("capital_gain_A_2")
        dividends_A_1 = request.POST.get("dividends_A_1")
        dividends_A_2 = request.POST.get("dividends_A_2")
        other_A_1 = request.POST.get("other_A_1")
        other_A_2 = request.POST.get("other_A_2")
        total_gross_A_1 = request.POST.get("total_gross_A_1")
        total_gross_A_2 = request.POST.get("total_gross_A_2")
        expenses_1 = request.POST.get("expenses_1")
        expenses_2 = request.POST.get("expenses_2")
        salaries_1 = request.POST.get("salaries_1")
        salaries_2 = request.POST.get("salaries_2")
        expenses_interests_1 = request.POST.get("expenses_interests_1")
        expenses_interests_2 = request.POST.get("expenses_interests_2")
        expenses_rents_1 = request.POST.get("expenses_rents_1")
        expenses_rents_2 = request.POST.get("expenses_rents_2")
        depreciation_1 = request.POST.get("depreciation_1")
        depreciation_2 = request.POST.get("depreciation_2")
        bad_debts_1 = request.POST.get("bad_debts_1")
        bad_debts_2 = request.POST.get("bad_debts_2")
        donations_1 = request.POST.get("donations_1")
        donations_2 = request.POST.get("donations_2")
        sales_tax_1 = request.POST.get("sales_tax_1")
        sales_tax_2 = request.POST.get("sales_tax_2")
        machinery_1 = request.POST.get("machinery_1")
        machinery_2 = request.POST.get("machinery_2")
        other_purchases_1 = request.POST.get("other_purchases_1")
        other_purchases_2 = request.POST.get("other_purchases_2")
        licenses_1 = request.POST.get("licenses_1")
        licenses_2 = request.POST.get("licenses_2")
        other_expenses_1 = request.POST.get("other_expenses_1")
        other_expenses_2 = request.POST.get("other_expenses_2")
        total_expenses_1 = request.POST.get("total_expenses_1")
        total_expenses_2 = request.POST.get("total_expenses_2")
        net_profit_1 = request.POST.get("net_profit_1")
        net_profit_2 = request.POST.get("net_profit_2")
        income_tax_1 = request.POST.get("income_tax_1")
        income_tax_2 = request.POST.get("income_tax_2")
        profit_after_tax_1 = request.POST.get("profit_after_tax_1")
        profit_after_tax_2 = request.POST.get("profit_after_tax_2")
        sales_D_1 = request.POST.get("sales_D_1")
        sales_D_2 = request.POST.get("sales_D_2")
        name = request.POST.get("name")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-440.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "company_name",
                        "address",
                        "email",
                        "liaison_officer",
                        "ssn",
                        "tel",
                        "fax",
                        "legal_form",
                        "cfc",
                        "main_line",
                        "business_type",
                        "other_business_type",
                        "closing_date",
                        "start_year",
                        "end_year",
                        "sales_A_1",
                        "sales_A_2",
                        "people_A_1",
                        "people_A_2",
                        "industries_businesses_A_1",
                        "industries_businesses_A_2",
                        "less_cost_A_1",
                        "less_cost_A_2",
                        "inventory_beginning_1",
                        "inventory_beginning_2",
                        "purchases_A_1",
                        "purchases_A_2",
                        "inventory_end_1",
                        "inventory_end_2",
                        "gross_profit_A_1",
                        "gross_profit_A_2",
                        "other_income_A_1",
                        "other_income_A_2",
                        "interests_A_1",
                        "interests_A_2",
                        "rent_A_1",
                        "rent_A_2",
                        "capital_gain_A_1",
                        "capital_gain_A_2",
                        "dividends_A_1",
                        "dividends_A_2",
                        "other_A_1",
                        "other_A_2",
                        "total_gross_A_1",
                        "total_gross_A_2",
                        "expenses_1",
                        "expenses_2",
                        "salaries_1",
                        "salaries_2",
                        "expenses_interests_1",
                        "expenses_interests_2",
                        "expenses_rents_1",
                        "expenses_rents_2",
                        "depreciation_1",
                        "depreciation_2",
                        "bad_debts_1",
                        "bad_debts_2",
                        "donations_1",
                        "donations_2",
                        "sales_tax_1",
                        "sales_tax_2",
                        "machinery_1",
                        "machinery_2",
                        "other_purchases_1",
                        "other_purchases_2",
                        "licenses_1",
                        "licenses_2",
                        "other_expenses_1",
                        "other_expenses_2",
                        "total_expenses_1",
                        "total_expenses_2",
                        "net_profit_1",
                        "net_profit_2",
                        "income_tax_1",
                        "income_tax_2",
                        "profit_after_tax_1",
                        "profit_after_tax_2",
                        "sales_D_1",
                        "sales_D_2",
                        "name",
                        "rank",
                    ]
                )

            writer.writerow(
                [
                    company_name,
                    address,
                    email,
                    liaison_officer,
                    ssn,
                    tel,
                    fax,
                    legal_form,
                    cfc,
                    main_line,
                    business_type,
                    other_business_type,
                    closing_date,
                    start_year,
                    end_year,
                    sales_A_1,
                    sales_A_2,
                    people_A_1,
                    people_A_2,
                    industries_businesses_A_1,
                    industries_businesses_A_2,
                    less_cost_A_1,
                    less_cost_A_2,
                    inventory_beginning_1,
                    inventory_beginning_2,
                    purchases_A_1,
                    purchases_A_2,
                    inventory_end_1,
                    inventory_end_2,
                    gross_profit_A_1,
                    gross_profit_A_2,
                    other_income_A_1,
                    other_income_A_2,
                    interests_A_1,
                    interests_A_2,
                    rent_A_1,
                    rent_A_2,
                    capital_gain_A_1,
                    capital_gain_A_2,
                    dividends_A_1,
                    dividends_A_2,
                    other_A_1,
                    other_A_2,
                    total_gross_A_1,
                    total_gross_A_2,
                    expenses_1,
                    expenses_2,
                    salaries_1,
                    salaries_2,
                    expenses_interests_1,
                    expenses_interests_2,
                    expenses_rents_1,
                    expenses_rents_2,
                    depreciation_1,
                    depreciation_2,
                    bad_debts_1,
                    bad_debts_2,
                    donations_1,
                    donations_2,
                    sales_tax_1,
                    sales_tax_2,
                    machinery_1,
                    machinery_2,
                    other_purchases_1,
                    other_purchases_2,
                    licenses_1,
                    licenses_2,
                    other_expenses_1,
                    other_expenses_2,
                    total_expenses_1,
                    total_expenses_2,
                    net_profit_1,
                    net_profit_2,
                    income_tax_1,
                    income_tax_2,
                    profit_after_tax_1,
                    profit_after_tax_2,
                    sales_D_1,
                    sales_D_2,
                    name,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-440.csv",
            dtypes={
                "company_name": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "ssn": str,
                "tel": str,
                "fax": str,
                "legal_form": str,
                "cfc": str,
                "main_line": str,
                "business_type": str,
                "other_business_type": str,
                "closing_date": str,
                "start_year": int,
                "end_year": int,
                "sales_A_1": float,
                "sales_A_2": float,
                "people_A_1": float,
                "people_A_2": float,
                "industries_businesses_A_1": float,
                "industries_businesses_A_2": float,
                "less_cost_A_1": float,
                "less_cost_A_2": float,
                "inventory_beginning_1": float,
                "inventory_beginning_2": float,
                "purchases_A_1": float,
                "purchases_A_2": float,
                "inventory_end_1": float,
                "inventory_end_2": float,
                "gross_profit_A_1": float,
                "gross_profit_A_2": float,
                "other_income_A_1": float,
                "other_income_A_2": float,
                "interests_A_1": float,
                "interests_A_2": float,
                "rent_A_1": float,
                "rent_A_2": float,
                "capital_gain_A_1": float,
                "capital_gain_A_2": float,
                "dividends_A_1": float,
                "dividends_A_2": float,
                "other_A_1": float,
                "other_A_2": float,
                "total_gross_A_1": float,
                "total_gross_A_2": float,
                "expenses_1": float,
                "expenses_2": float,
                "salaries_1": float,
                "salaries_2": float,
                "expenses_interests_1": float,
                "expenses_interests_2": float,
                "expenses_rents_1": float,
                "expenses_rents_2": float,
                "depreciation_1": float,
                "depreciation_2": float,
                "bad_debts_1": float,
                "bad_debts_2": float,
                "donations_1": float,
                "donations_2": float,
                "sales_tax_1": float,
                "sales_tax_2": float,
                "machinery_1": float,
                "machinery_2": float,
                "other_purchases_1": float,
                "other_purchases_2": float,
                "licenses_1": float,
                "licenses_2": float,
                "other_expenses_1": float,
                "other_expenses_2": float,
                "total_expenses_1": float,
                "total_expenses_2": float,
                "net_profit_1": float,
                "net_profit_2": float,
                "income_tax_1": float,
                "income_tax_2": float,
                "profit_after_tax_1": float,
                "profit_after_tax_2": float,
                "sales_D_1": float,
                "sales_D_2": float,
                "name": str,
                "rank": str,
            },
            table_name="IP_440",
            table_id="31",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-440.html")


def IP_440g(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get("company_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")
        legal_form = request.POST.get("legal_form")
        cfc = request.POST.get("cfc")
        end_month = request.POST.get("end_month")

        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")

        sales_A_1 = request.POST.get("sales_A_1")
        sales_A_2 = request.POST.get("sales_A_2")

        fuel_A_1 = request.POST.get("fuel_A_1")
        fuel_A_2 = request.POST.get("fuel_A_2")

        other_products_A_1 = request.POST.get("other_products_A_1")
        other_products_A_2 = request.POST.get("other_products_A_2")

        less_cost_A_1 = request.POST.get("less_cost_A_1")
        less_cost_A_2 = request.POST.get("less_cost_A_2")

        inventory_beginning_1 = request.POST.get("inventory_beginning_1")
        inventory_beginning_2 = request.POST.get("inventory_beginning_2")

        purchases_A_1 = request.POST.get("purchases_A_1")
        purchases_A_2 = request.POST.get("purchases_A_2")

        inventory_end_1 = request.POST.get("inventory_end_1")
        inventory_end_2 = request.POST.get("inventory_end_2")

        gross_profit_A_1 = request.POST.get("gross_profit_A_1")
        gross_profit_A_2 = request.POST.get("gross_profit_A_2")

        other_income_A_1 = request.POST.get("other_income_A_1")
        other_income_A_2 = request.POST.get("other_income_A_2")

        interests_A_1 = request.POST.get("interests_A_1")
        interests_A_2 = request.POST.get("interests_A_2")

        rent_A_1 = request.POST.get("rent_A_1")
        rent_A_2 = request.POST.get("rent_A_2")

        capital_gain_A_1 = request.POST.get("capital_gain_A_1")
        capital_gain_A_2 = request.POST.get("capital_gain_A_2")

        dividends_A_1 = request.POST.get("dividends_A_1")
        dividends_A_2 = request.POST.get("dividends_A_2")

        others_A_1 = request.POST.get("others_A_1")
        others_A_2 = request.POST.get("others_A_2")

        total_gross_A_1 = request.POST.get("total_gross_A_1")
        total_gross_A_2 = request.POST.get("total_gross_A_2")

        cost_B_1 = request.POST.get("cost_B_1")
        cost_B_2 = request.POST.get("cost_B_2")

        salaries_B_1 = request.POST.get("salaries_B_1")
        salaries_B_2 = request.POST.get("salaries_B_2")

        interests_B_1 = request.POST.get("interests_B_1")
        interests_B_2 = request.POST.get("interests_B_2")

        depreciation_B_1 = request.POST.get("depreciation_B_1")
        depreciation_B_2 = request.POST.get("depreciation_B_2")

        rent_B_1 = request.POST.get("rent_B_1")
        rent_B_2 = request.POST.get("rent_B_2")

        bad_debts_B_1 = request.POST.get("bad_debts_B_1")
        bad_debts_B_2 = request.POST.get("bad_debts_B_2")

        donations_B_1 = request.POST.get("donations_B_1")
        donations_B_2 = request.POST.get("donations_B_2")

        sales_B_1 = request.POST.get("sales_B_1")
        sales_B_2 = request.POST.get("sales_B_2")

        purchases_B_1 = request.POST.get("purchases_B_1")
        purchases_B_2 = request.POST.get("purchases_B_2")

        other_purchases_B_1 = request.POST.get("other_purchases_B_1")
        other_purchases_B_2 = request.POST.get("other_purchases_B_2")

        licenses_B_1 = request.POST.get("licenses_B_1")
        licenses_B_2 = request.POST.get("licenses_B_2")

        other_operations_B_1 = request.POST.get("other_operations_B_1")
        other_operations_B_2 = request.POST.get("other_operations_B_2")

        total_operations_B_1 = request.POST.get("total_operations_B_1")
        total_operations_B_2 = request.POST.get("total_operations_B_2")

        net_profit_C_1 = request.POST.get("net_profit_C_1")
        net_profit_C_2 = request.POST.get("net_profit_C_2")

        income_C_1 = request.POST.get("income_C_1")
        income_C_2 = request.POST.get("income_C_2")

        profit_C_after_1 = request.POST.get("profit_C_after_1")
        profit_C_after_2 = request.POST.get("profit_C_after_2")

        sales_D_1 = request.POST.get("sales_D_1")
        sales_D_2 = request.POST.get("sales_D_2")

        name = request.POST.get("name")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-440g.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "company_name",
                        "address",
                        "email",
                        "liaison_officer",
                        "ssn",
                        "tel",
                        "fax",
                        "legal_form",
                        "cfc",
                        "end_month",
                        "start_year",
                        "end_year",
                        "sales_A_1",
                        "sales_A_2",
                        "fuel_A_1",
                        "fuel_A_2",
                        "other_products_A_1",
                        "other_products_A_2",
                        "less_cost_A_1",
                        "less_cost_A_2",
                        "inventory_beginning_1",
                        "inventory_beginning_2",
                        "purchases_A_1",
                        "purchases_A_2",
                        "inventory_end_1",
                        "inventory_end_2",
                        "gross_profit_A_1",
                        "gross_profit_A_2",
                        "other_income_A_1",
                        "other_income_A_2",
                        "interests_A_1",
                        "interests_A_2",
                        "rent_A_1",
                        "rent_A_2",
                        "capital_gain_A_1",
                        "capital_gain_A_2",
                        "dividends_A_1",
                        "dividends_A_2",
                        "others_A_1",
                        "others_A_2",
                        "total_gross_A_1",
                        "total_gross_A_2",
                        "cost_B_1",
                        "cost_B_2",
                        "salaries_B_1",
                        "salaries_B_2",
                        "interests_B_1",
                        "interests_B_2",
                        "depreciation_B_1",
                        "depreciation_B_2",
                        "rent_B_1",
                        "rent_B_2",
                        "bad_debts_B_1",
                        "bad_debts_B_2",
                        "donations_B_1",
                        "donations_B_2",
                        "sales_B_1",
                        "sales_B_2",
                        "purchases_B_1",
                        "purchases_B_2",
                        "other_purchases_B_1",
                        "other_purchases_B_2",
                        "licenses_B_1",
                        "licenses_B_2",
                        "other_operations_B_1",
                        "other_operations_B_2",
                        "total_operations_B_1",
                        "total_operations_B_2",
                        "net_profit_C_1",
                        "net_profit_C_2",
                        "income_C_1",
                        "income_C_2",
                        "profit_C_after_1",
                        "profit_C_after_2",
                        "sales_D_1",
                        "sales_D_2",
                        "name",
                        "rank",
                    ]
                )

            writer.writerow(
                [
                    company_name,
                    address,
                    email,
                    liaison_officer,
                    ssn,
                    tel,
                    fax,
                    legal_form,
                    cfc,
                    end_month,
                    start_year,
                    end_year,
                    sales_A_1,
                    sales_A_2,
                    fuel_A_1,
                    fuel_A_2,
                    other_products_A_1,
                    other_products_A_2,
                    less_cost_A_1,
                    less_cost_A_2,
                    inventory_beginning_1,
                    inventory_beginning_2,
                    purchases_A_1,
                    purchases_A_2,
                    inventory_end_1,
                    inventory_end_2,
                    gross_profit_A_1,
                    gross_profit_A_2,
                    other_income_A_1,
                    other_income_A_2,
                    interests_A_1,
                    interests_A_2,
                    rent_A_1,
                    rent_A_2,
                    capital_gain_A_1,
                    capital_gain_A_2,
                    dividends_A_1,
                    dividends_A_2,
                    others_A_1,
                    others_A_2,
                    total_gross_A_1,
                    total_gross_A_2,
                    cost_B_1,
                    cost_B_2,
                    salaries_B_1,
                    salaries_B_2,
                    interests_B_1,
                    interests_B_2,
                    depreciation_B_1,
                    depreciation_B_2,
                    rent_B_1,
                    rent_B_2,
                    bad_debts_B_1,
                    bad_debts_B_2,
                    donations_B_1,
                    donations_B_2,
                    sales_B_1,
                    sales_B_2,
                    purchases_B_1,
                    purchases_B_2,
                    other_purchases_B_1,
                    other_purchases_B_2,
                    licenses_B_1,
                    licenses_B_2,
                    other_operations_B_1,
                    other_operations_B_2,
                    total_operations_B_1,
                    total_operations_B_2,
                    net_profit_C_1,
                    net_profit_C_2,
                    income_C_1,
                    income_C_2,
                    profit_C_after_1,
                    profit_C_after_2,
                    sales_D_1,
                    sales_D_2,
                    name,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-440g.csv",
            dtypes={
                "company_name": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "ssn": str,
                "tel": str,
                "fax": str,
                "legal_form": str,
                "cfc": str,
                "end_month": str,
                "start_year": int,
                "end_year": int,
                "sales_A_1": float,
                "sales_A_2": float,
                "fuel_A_1": float,
                "fuel_A_2": float,
                "other_products_A_1": float,
                "other_products_A_2": float,
                "less_cost_A_1": float,
                "less_cost_A_2": float,
                "inventory_beginning_1": float,
                "inventory_beginning_2": float,
                "purchases_A_1": float,
                "purchases_A_2": float,
                "inventory_end_1": float,
                "inventory_end_2": float,
                "gross_profit_A_1": float,
                "gross_profit_A_2": float,
                "other_income_A_1": float,
                "other_income_A_2": float,
                "interests_A_1": float,
                "interests_A_2": float,
                "rent_A_1": float,
                "rent_A_2": float,
                "capital_gain_A_1": float,
                "capital_gain_A_2": float,
                "dividends_A_1": float,
                "dividends_A_2": float,
                "others_A_1": float,
                "others_A_2": float,
                "total_gross_A_1": float,
                "total_gross_A_2": float,
                "cost_B_1": float,
                "cost_B_2": float,
                "salaries_B_1": float,
                "salaries_B_2": float,
                "interests_B_1": float,
                "interests_B_2": float,
                "depreciation_B_1": float,
                "depreciation_B_2": float,
                "rent_B_1": float,
                "rent_B_2": float,
                "bad_debts_B_1": float,
                "bad_debts_B_2": float,
                "donations_B_1": float,
                "donations_B_2": float,
                "sales_B_1": float,
                "sales_B_2": float,
                "purchases_B_1": float,
                "purchases_B_2": float,
                "other_purchases_B_1": float,
                "other_purchases_B_2": float,
                "licenses_B_1": float,
                "licenses_B_2": float,
                "other_operations_B_1": float,
                "other_operations_B_2": float,
                "total_operations_B_1": float,
                "total_operations_B_2": float,
                "net_profit_C_1": float,
                "net_profit_C_2": float,
                "income_C_1": float,
                "income_C_2": float,
                "profit_C_after_1": float,
                "profit_C_after_2": float,
                "sales_D_1": float,
                "sales_D_2": float,
                "name": str,
                "rank": str,
            },
            table_name="IP_440g",
            table_id="33",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-440g.html")


def IP_310b(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get("company_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")
        legal_form = request.POST.get("legal_form")
        cfc = request.POST.get("cfc")
        end_month = request.POST.get("end_month")
        main_product_1 = request.POST.get("main_product_1")
        main_product_2 = request.POST.get("main_product_2")
        raw_material_used = request.POST.get("raw_material_used")
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        total_sales_1 = request.POST.get("total_sales_1")
        total_sales_2 = request.POST.get("total_sales_2")
        products_manufactured_1 = request.POST.get("products_manufactured_1")
        products_manufactured_2 = request.POST.get("products_manufactured_2")
        rum_1 = request.POST.get("rum_1")
        rum_2 = request.POST.get("rum_2")
        beer_1 = request.POST.get("beer_1")
        beer_2 = request.POST.get("beer_2")
        malt_1 = request.POST.get("malt_1")
        malt_2 = request.POST.get("malt_2")
        soft_drinks_1 = request.POST.get("soft_drinks_1")
        soft_drinks_2 = request.POST.get("soft_drinks_2")
        others_1 = request.POST.get("others_1")
        others_2 = request.POST.get("others_2")
        goods_acquired_1 = request.POST.get("goods_acquired_1")
        goods_acquired_2 = request.POST.get("goods_acquired_2")
        wines_1 = request.POST.get("wines_1")
        wines_2 = request.POST.get("wines_2")
        soft_drinks_3 = request.POST.get("soft_drinks_3")
        soft_drinks_4 = request.POST.get("soft_drinks_4")
        whiskey_1 = request.POST.get("whiskey_1")
        whiskey_2 = request.POST.get("whiskey_2")
        brandy_1 = request.POST.get("brandy_1")
        brandy_2 = request.POST.get("brandy_2")
        other_3 = request.POST.get("other_3")
        other_4 = request.POST.get("other_4")
        manufacturing_cost_1 = request.POST.get("manufacturing_cost_1")
        manufacturing_cost_2 = request.POST.get("manufacturing_cost_2")
        inventories_begginning_1 = request.POST.get("inventories_begginning_1")
        inventories_begginning_2 = request.POST.get("inventories_begginning_2")
        purchases_1 = request.POST.get("purchases_1")
        purchases_2 = request.POST.get("purchases_2")
        total_raw_1 = request.POST.get("total_raw_1")
        total_raw_2 = request.POST.get("total_raw_2")
        imported_1 = request.POST.get("imported_1")
        imported_2 = request.POST.get("imported_2")
        others_5 = request.POST.get("others_5")
        others_6 = request.POST.get("others_6")
        direct_wages_1 = request.POST.get("direct_wages_1")
        direct_wages_2 = request.POST.get("direct_wages_2")
        depreciation_1 = request.POST.get("depreciation_1")
        depreciation_2 = request.POST.get("depreciation_2")
        rent_land_1 = request.POST.get("rent_land_1")
        rent_land_2 = request.POST.get("rent_land_2")
        other_direct_1 = request.POST.get("other_direct_1")
        other_direct_2 = request.POST.get("other_direct_2")
        indirect_cost_1 = request.POST.get("indirect_cost_1")
        indirect_cost_2 = request.POST.get("indirect_cost_2")
        inventories_end_1 = request.POST.get("inventories_end_1")
        inventories_end_2 = request.POST.get("inventories_end_2")
        gross_profit_1 = request.POST.get("gross_profit_1")
        gross_profit_2 = request.POST.get("gross_profit_2")
        other_operating_1 = request.POST.get("other_operating_1")
        other_operating_2 = request.POST.get("other_operating_2")
        interest_1 = request.POST.get("interest_1")
        interest_2 = request.POST.get("interest_2")
        rent_land_3 = request.POST.get("rent_land_3")
        rent_land_4 = request.POST.get("rent_land_4")
        capital_gain_1 = request.POST.get("capital_gain_1")
        capital_gain_2 = request.POST.get("capital_gain_2")
        other_1 = request.POST.get("other_1")
        other_2 = request.POST.get("other_2")
        total_gross_1 = request.POST.get("total_gross_1")
        total_gross_2 = request.POST.get("total_gross_2")
        expenses_not_1 = request.POST.get("expenses_not_1")
        expenses_not_2 = request.POST.get("expenses_not_2")
        salaries_1 = request.POST.get("salaries_1")
        salaries_2 = request.POST.get("salaries_2")
        interest_3 = request.POST.get("interest_3")
        interest_4 = request.POST.get("interest_4")
        depreciation_3 = request.POST.get("depreciation_3")
        depreciation_4 = request.POST.get("depreciation_4")
        donations_1 = request.POST.get("donations_1")
        donations_2 = request.POST.get("donations_2")
        rent_land_5 = request.POST.get("rent_land_5")
        rent_land_6 = request.POST.get("rent_land_6")
        excise_taxes_1 = request.POST.get("excise_taxes_1")
        excise_taxes_2 = request.POST.get("excise_taxes_2")
        other_operating_3 = request.POST.get("other_operating_3")
        other_operating_4 = request.POST.get("other_operating_4")
        sales_tax_1 = request.POST.get("sales_tax_1")
        sales_tax_2 = request.POST.get("sales_tax_2")
        machinery_1 = request.POST.get("machinery_1")
        machinery_2 = request.POST.get("machinery_2")
        on_other_1 = request.POST.get("on_other_1")
        on_other_2 = request.POST.get("on_other_2")
        licenses_1 = request.POST.get("licenses_1")
        licenses_2 = request.POST.get("licenses_2")
        net_loss_1 = request.POST.get("net_loss_1")
        net_loss_2 = request.POST.get("net_loss_2")
        income_tax_1 = request.POST.get("income_tax_1")
        income_tax_2 = request.POST.get("income_tax_2")
        profit_after_tax_1 = request.POST.get("profit_after_tax_1")
        profit_after_tax_2 = request.POST.get("profit_after_tax_2")
        sales_and_use_withheld_1 = request.POST.get("sales_and_use_withheld_1")
        sales_and_use_withheld_2 = request.POST.get("sales_and_use_withheld_2")
        branches = request.POST.get("branches")
        branches_if_yes = request.POST.get("branches_if_yes")
        signature = request.POST.get("signature")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-310b.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "company_name",
                        "address",
                        "email",
                        "liaison_officer",
                        "ssn",
                        "tel",
                        "fax",
                        "legal_form",
                        "cfc",
                        "end_month",
                        "main_product_1",
                        "main_product_2",
                        "raw_material_used",
                        "closing_date",
                        "start_year",
                        "end_year",
                        "total_sales_1",
                        "total_sales_2",
                        "products_manufactured_1",
                        "products_manufactured_2",
                        "rum_1",
                        "rum_2",
                        "beer_1",
                        "beer_2",
                        "malt_1",
                        "malt_2",
                        "soft_drinks_1",
                        "soft_drinks_2",
                        "others_1",
                        "others_2",
                        "goods_acquired_1",
                        "goods_acquired_2",
                        "wines_1",
                        "wines_2",
                        "soft_drinks_3",
                        "soft_drinks_4",
                        "whiskey_1",
                        "whiskey_2",
                        "brandy_1",
                        "brandy_2",
                        "other_3",
                        "other_4",
                        "manufacturing_cost_1",
                        "manufacturing_cost_2",
                        "inventories_begginning_1",
                        "inventories_begginning_2",
                        "purchases_1",
                        "purchases_2",
                        "total_raw_1",
                        "total_raw_2",
                        "imported_1",
                        "imported_2",
                        "others_5",
                        "others_6",
                        "direct_wages_1",
                        "direct_wages_2",
                        "depreciation_1",
                        "depreciation_2",
                        "rent_land_1",
                        "rent_land_2",
                        "other_direct_1",
                        "other_direct_2",
                        "indirect_cost_1",
                        "indirect_cost_2",
                        "inventories_end_1",
                        "inventories_end_2",
                        "gross_profit_1",
                        "gross_profit_2",
                        "other_operating_1",
                        "other_operating_2",
                        "interest_1",
                        "interest_2",
                        "rent_land_3",
                        "rent_land_4",
                        "capital_gain_1",
                        "capital_gain_2",
                        "other_1",
                        "other_2",
                        "total_gross_1",
                        "total_gross_2",
                        "expenses_not_1",
                        "expenses_not_2",
                        "salaries_1",
                        "salaries_2",
                        "interest_3",
                        "interest_4",
                        "depreciation_3",
                        "depreciation_4",
                        "donations_1",
                        "donations_2",
                        "rent_land_5",
                        "rent_land_6",
                        "excise_taxes_1",
                        "excise_taxes_2",
                        "other_operating_3",
                        "other_operating_4",
                        "sales_tax_1",
                        "sales_tax_2",
                        "machinery_1",
                        "machinery_2",
                        "on_other_1",
                        "on_other_2",
                        "licenses_1",
                        "licenses_2",
                        "net_loss_1",
                        "net_loss_2",
                        "income_tax_1",
                        "income_tax_2",
                        "profit_after_tax_1",
                        "profit_after_tax_2",
                        "sales_and_use_withheld_1",
                        "sales_and_use_withheld_2",
                        "branches",
                        "branches_if_yes",
                        "signature",
                        "rank",
                    ]
                )

            writer.writerow(
                [
                    company_name,
                    address,
                    email,
                    liaison_officer,
                    ssn,
                    tel,
                    fax,
                    legal_form,
                    cfc,
                    end_month,
                    main_product_1,
                    main_product_2,
                    raw_material_used,
                    closing_date,
                    start_year,
                    end_year,
                    total_sales_1,
                    total_sales_2,
                    products_manufactured_1,
                    products_manufactured_2,
                    rum_1,
                    rum_2,
                    beer_1,
                    beer_2,
                    malt_1,
                    malt_2,
                    soft_drinks_1,
                    soft_drinks_2,
                    others_1,
                    others_2,
                    goods_acquired_1,
                    goods_acquired_2,
                    wines_1,
                    wines_2,
                    soft_drinks_3,
                    soft_drinks_4,
                    whiskey_1,
                    whiskey_2,
                    brandy_1,
                    brandy_2,
                    other_3,
                    other_4,
                    manufacturing_cost_1,
                    manufacturing_cost_2,
                    inventories_begginning_1,
                    inventories_begginning_2,
                    purchases_1,
                    purchases_2,
                    total_raw_1,
                    total_raw_2,
                    imported_1,
                    imported_2,
                    others_5,
                    others_6,
                    direct_wages_1,
                    direct_wages_2,
                    depreciation_1,
                    depreciation_2,
                    rent_land_1,
                    rent_land_2,
                    other_direct_1,
                    other_direct_2,
                    indirect_cost_1,
                    indirect_cost_2,
                    inventories_end_1,
                    inventories_end_2,
                    gross_profit_1,
                    gross_profit_2,
                    other_operating_1,
                    other_operating_2,
                    interest_1,
                    interest_2,
                    rent_land_3,
                    rent_land_4,
                    capital_gain_1,
                    capital_gain_2,
                    other_1,
                    other_2,
                    total_gross_1,
                    total_gross_2,
                    expenses_not_1,
                    expenses_not_2,
                    salaries_1,
                    salaries_2,
                    interest_3,
                    interest_4,
                    depreciation_3,
                    depreciation_4,
                    donations_1,
                    donations_2,
                    rent_land_5,
                    rent_land_6,
                    excise_taxes_1,
                    excise_taxes_2,
                    other_operating_3,
                    other_operating_4,
                    sales_tax_1,
                    sales_tax_2,
                    machinery_1,
                    machinery_2,
                    on_other_1,
                    on_other_2,
                    licenses_1,
                    licenses_2,
                    net_loss_1,
                    net_loss_2,
                    income_tax_1,
                    income_tax_2,
                    profit_after_tax_1,
                    profit_after_tax_2,
                    sales_and_use_withheld_1,
                    sales_and_use_withheld_2,
                    branches,
                    branches_if_yes,
                    signature,
                    rank,
                ]
            )
        
        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-310b.csv",
            dtypes={
                "company_name": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "ssn": str,
                "tel": str,
                "fax": str,
                "legal_form": str,
                "cfc": str,
                "end_month": str,
                "main_product_1": str,
                "main_product_2": str,
                "raw_material_used": str,
                "closing_date": str,
                "start_year": int,
                "end_year": int,
                "total_sales_1": float,
                "total_sales_2": float,
                "products_manufactured_1": float,
                "products_manufactured_2": float,
                "rum_1": float,
                "rum_2": float,
                "beer_1": float,
                "beer_2": float,
                "malt_1": float,
                "malt_2": float,
                "soft_drinks_1": float,
                "soft_drinks_2": float,
                "others_1": float,
                "others_2": float,
                "goods_acquired_1": float,
                "goods_acquired_2": float,
                "wines_1": float,
                "wines_2": float,
                "soft_drinks_3": float,
                "soft_drinks_4": float,
                "whiskey_1": float,
                "whiskey_2": float,
                "brandy_1": float,
                "brandy_2": float,
                "other_3": float,
                "other_4": float,
                "manufacturing_cost_1": float,
                "manufacturing_cost_2": float,
                "inventories_begginning_1": float,
                "inventories_begginning_2": float,
                "purchases_1": float,
                "purchases_2": float,
                "total_raw_1": float,
                "total_raw_2": float,
                "imported_1": float,
                "imported_2": float,
                "others_5": float,
                "others_6": float,
                "direct_wages_1": float,
                "direct_wages_2": float,
                "depreciation_1": float,
                "depreciation_2": float,
                "rent_land_1": float,
                "rent_land_2": float,
                "other_direct_1": float,
                "other_direct_2": float,
                "indirect_cost_1": float,
                "indirect_cost_2": float,
                "inventories_end_1": float,
                "inventories_end_2": float,
                "gross_profit_1": float,
                "gross_profit_2": float,
                "other_operating_1": float,
                "other_operating_2": float,
                "interest_1": float,
                "interest_2": float,
                "rent_land_3": float,
                "rent_land_4": float,
                "capital_gain_1": float,
                "capital_gain_2": float,
                "other_1": float,
                "other_2": float,
                "total_gross_1": float,
                "total_gross_2": float,
                "expenses_not_1": float,
                "expenses_not_2": float,
                "salaries_1": float,
                "salaries_2": float,
                "interest_3": float,
                "interest_4": float,
                "depreciation_3": float,
                "depreciation_4": float,
                "donations_1": float,
                "donations_2": float,
                "rent_land_5": float,
                "rent_land_6": float,
                "excise_taxes_1": float,
                "excise_taxes_2": float,
                "other_operating_3": float,
                "other_operating_4": float,
                "sales_tax_1": float,
                "sales_tax_2": float,
                "machinery_1": float,
                "machinery_2": float,
                "on_other_1": float,
                "on_other_2": float,
                "licenses_1": float,
                "licenses_2": float,
                "net_loss_1": float,
                "net_loss_2": float,
                "income_tax_1": float,
                "income_tax_2": float,
                "profit_after_tax_1": float,
                "profit_after_tax_2": float,
                "sales_and_use_withheld_1": float,
                "sales_and_use_withheld_2": float,
                "branches": str,
                "branches_if_yes": str,
                "signature": str,
                "rank": str,
            },
            table_name="IP_310b",
            table_id=32,
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-310b.html")


def IP_480a(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get("company_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")
        business_function = request.POST.get("business_function")
        legal_form = request.POST.get("legal_form")
        cfc = request.POST.get("cfc")
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        people_A_1 = request.POST.get("people_A_1")
        people_A_2 = request.POST.get("people_A_2")
        industries_businesses_A_1 = request.POST.get("industries_businesses_A_1")
        industries_businesses_A_2 = request.POST.get("industries_businesses_A_2")
        passenger_fares_1 = request.POST.get("passenger_fares_1")
        passenger_fares_2 = request.POST.get("passenger_fares_2")
        freight_1 = request.POST.get("freight_1")
        freight_2 = request.POST.get("freight_2")
        ship_USA_1 = request.POST.get("ship_USA_1")
        ship_USA_2 = request.POST.get("ship_USA_2")
        ship_VIRGISLND_1 = request.POST.get("ship_VIRGISLND_1")
        ship_VIRGISLND_2 = request.POST.get("ship_VIRGISLND_2")
        SHIP_fORECNTY_1 = request.POST.get("SHIP_fORECNTY_1")
        SHIP_fORECNTY_2 = request.POST.get("SHIP_fORECNTY_2")
        income_interest_1 = request.POST.get("income_interest_1")
        income_interest_2 = request.POST.get("income_interest_2")
        income_rent_1 = request.POST.get("income_rent_1")
        income_rent_2 = request.POST.get("income_rent_2")
        commissions_1 = request.POST.get("commissions_1")
        commissions_2 = request.POST.get("commissions_2")
        capital_gain_loss_1 = request.POST.get("capital_gain_loss_1")
        capital_gain_loss_2 = request.POST.get("capital_gain_loss_2")
        other_incomes_1 = request.POST.get("other_incomes_1")
        other_incomes_2 = request.POST.get("other_incomes_2")
        total_incomes_1 = request.POST.get("total_incomes_1")
        total_incomes_2 = request.POST.get("total_incomes_2")
        salaries_1 = request.POST.get("salaries_1")
        salaries_2 = request.POST.get("salaries_2")
        commissions_employees_1 = request.POST.get("commissions_employees_1")
        commissions_employees_2 = request.POST.get("commissions_employees_2")
        commissions_independent_1 = request.POST.get("commissions_independent_1")
        commissions_independent_2 = request.POST.get("commissions_independent_2")
        expenses_interests_1 = request.POST.get("expenses_interests_1")
        expenses_interests_2 = request.POST.get("expenses_interests_2")
        expenses_rents_1 = request.POST.get("expenses_rents_1")
        expenses_rents_2 = request.POST.get("expenses_rents_2")
        depreciation_1 = request.POST.get("depreciation_1")
        depreciation_2 = request.POST.get("depreciation_2")
        bad_debts_1 = request.POST.get("bad_debts_1")
        bad_debts_2 = request.POST.get("bad_debts_2")
        donations_1 = request.POST.get("donations_1")
        donations_2 = request.POST.get("donations_2")
        sales_tax_1 = request.POST.get("sales_tax_1")
        sales_tax_2 = request.POST.get("sales_tax_2")
        machinery_1 = request.POST.get("machinery_1")
        machinery_2 = request.POST.get("machinery_2")
        other_purchases_1 = request.POST.get("other_purchases_1")
        other_purchases_2 = request.POST.get("other_purchases_2")
        licenses_1 = request.POST.get("licenses_1")
        licenses_2 = request.POST.get("licenses_2")
        other_expenses_1 = request.POST.get("other_expenses_1")
        other_expenses_2 = request.POST.get("other_expenses_2")
        total_expenses_1 = request.POST.get("total_expenses_1")
        total_expenses_2 = request.POST.get("total_expenses_2")
        net_profit_1 = request.POST.get("net_profit_1")
        net_profit_2 = request.POST.get("net_profit_2")
        income_tax_1 = request.POST.get("income_tax_1")
        income_tax_2 = request.POST.get("income_tax_2")
        profit_after_tax_1 = request.POST.get("profit_after_tax_1")
        profit_after_tax_2 = request.POST.get("profit_after_tax_2")
        withheld_tax_1 = request.POST.get("withheld_tax_1")
        withheld_tax_2 = request.POST.get("withheld_tax_2")
        signature = request.POST.get("signature")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/JP-480a.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "company_name",
                        "address",
                        "email",
                        "liaison_officer",
                        "ssn",
                        "tel",
                        "fax",
                        "business_function",
                        "legal_form",
                        "cfc",
                        "closing_date",
                        "start_year",
                        "end_year",
                        "people_A_1",
                        "people_A_2",
                        "industries_businesses_A_1",
                        "industries_businesses_A_2",
                        "passenger_fares_1",
                        "passenger_fares_2",
                        "freight_1",
                        "freight_2",
                        "ship_USA_1",
                        "ship_USA_2",
                        "ship_VIRGISLND_1",
                        "ship_VIRGISLND_2",
                        "SHIP_fORECNTY_1",
                        "SHIP_fORECNTY_2",
                        "income_interest_1",
                        "income_interest_2",
                        "income_rent_1",
                        "income_rent_2",
                        "commissions_1",
                        "commissions_2",
                        "capital_gain_loss_1",
                        "capital_gain_loss_2",
                        "other_incomes_1",
                        "other_incomes_2",
                        "total_incomes_1",
                        "total_incomes_2",
                        "salaries_1",
                        "salaries_2",
                        "commissions_employees_1",
                        "commissions_employees_2",
                        "commissions_independent_1",
                        "commissions_independent_2",
                        "expenses_interests_1",
                        "expenses_interests_2",
                        "expenses_rents_1",
                        "expenses_rents_2",
                        "depreciation_1",
                        "depreciation_2",
                        "bad_debts_1",
                        "bad_debts_2",
                        "donations_1",
                        "donations_2",
                        "sales_tax_1",
                        "sales_tax_2",
                        "machinery_1",
                        "machinery_2",
                        "other_purchases_1",
                        "other_purchases_2",
                        "licenses_1",
                        "licenses_2",
                        "other_expenses_1",
                        "other_expenses_2",
                        "total_expenses_1",
                        "total_expenses_2",
                        "net_profit_1",
                        "net_profit_2",
                        "income_tax_1",
                        "income_tax_2",
                        "profit_after_tax_1",
                        "profit_after_tax_2",
                        "withheld_tax_1",
                        "withheld_tax_2",
                        "signature",
                        "rank",
                    ]
                )

            writer.writerow(
                [
                    company_name,
                    address,
                    email,
                    liaison_officer,
                    ssn,
                    tel,
                    fax,
                    business_function,
                    legal_form,
                    cfc,
                    closing_date,
                    start_year,
                    end_year,
                    people_A_1,
                    people_A_2,
                    industries_businesses_A_1,
                    industries_businesses_A_2,
                    passenger_fares_1,
                    passenger_fares_2,
                    freight_1,
                    freight_2,
                    ship_USA_1,
                    ship_USA_2,
                    ship_VIRGISLND_1,
                    ship_VIRGISLND_2,
                    SHIP_fORECNTY_1,
                    SHIP_fORECNTY_2,
                    income_interest_1,
                    income_interest_2,
                    income_rent_1,
                    income_rent_2,
                    commissions_1,
                    commissions_2,
                    capital_gain_loss_1,
                    capital_gain_loss_2,
                    other_incomes_1,
                    other_incomes_2,
                    total_incomes_1,
                    total_incomes_2,
                    salaries_1,
                    salaries_2,
                    commissions_employees_1,
                    commissions_employees_2,
                    commissions_independent_1,
                    commissions_independent_2,
                    expenses_interests_1,
                    expenses_interests_2,
                    expenses_rents_1,
                    expenses_rents_2,
                    depreciation_1,
                    depreciation_2,
                    bad_debts_1,
                    bad_debts_2,
                    donations_1,
                    donations_2,
                    sales_tax_1,
                    sales_tax_2,
                    machinery_1,
                    machinery_2,
                    other_purchases_1,
                    other_purchases_2,
                    licenses_1,
                    licenses_2,
                    other_expenses_1,
                    other_expenses_2,
                    total_expenses_1,
                    total_expenses_2,
                    net_profit_1,
                    net_profit_2,
                    income_tax_1,
                    income_tax_2,
                    profit_after_tax_1,
                    profit_after_tax_2,
                    withheld_tax_1,
                    withheld_tax_2,
                    signature,
                    rank,
                ]
            )
        
        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/JP-480a.csv",
            dtypes={
                "company_name": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "ssn": str,
                "tel": str,
                "fax": str,
                "business_function": str,
                "legal_form": str,
                "cfc": str,
                "closing_date": str,
                "start_year": int,
                "end_year": int,
                "people_A_1": float,
                "people_A_2": float,
                "industries_businesses_A_1": float,
                "industries_businesses_A_2": float,
                "passenger_fares_1": float,
                "passenger_fares_2": float,
                "freight_1": float,
                "freight_2": float,
                "ship_USA_1": float,
                "ship_USA_2": float,
                "ship_VIRGISLND_1": float,
                "ship_VIRGISLND_2": float,
                "SHIP_fORECNTY_1": float,
                "SHIP_fORECNTY_2": float,
                "income_interest_1": float,
                "income_interest_2": float,
                "income_rent_1": float,
                "income_rent_2": float,
                "commissions_1": float,
                "commissions_2": float,
                "capital_gain_loss_1": float,
                "capital_gain_loss_2": float,
                "other_incomes_1": float,
                "other_incomes_2": float,
                "total_incomes_1": float,
                "total_incomes_2": float,
                "salaries_1": float,
                "salaries_2": float,
                "commissions_employees_1": float,
                "commissions_employees_2": float,
                "commissions_independent_1": float,
                "commissions_independent_2": float,
                "expenses_interests_1": float,
                "expenses_interests_2": float,
                "expenses_rents_1": float,
                "expenses_rents_2": float,
                "depreciation_1": float,
                "depreciation_2": float,
                "bad_debts_1": float,
                "bad_debts_2": float,
                "donations_1": float,
                "donations_2": float,
                "sales_tax_1": float,
                "sales_tax_2": float,
                "machinery_1": float,
                "machinery_2": float,
                "other_purchases_1": float,
                "other_purchases_2": float,
                "licenses_1": float,
                "licenses_2": float,
                "other_expenses_1": float,
                "other_expenses_2": float,
                "total_expenses_1": float,
                "total_expenses_2": float,
                "net_profit_1": float,
                "net_profit_2": float,
                "income_tax_1": float,
                "income_tax_2": float,
                "profit_after_tax_1": float,
                "profit_after_tax_2": float,
                "withheld_tax_1": float,
                "withheld_tax_2": float,
                "signature": str,
                "rank": str,
            },
            table_name="IP_480a",
            table_id=34,
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-480a.html")


def IP_490(request):

    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get("company_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")
        legal_form = request.POST.get("legal_form")
        cfc = request.POST.get("cfc")
        business_type = request.POST.get("business_type")
        business_function = request.POST.get("business_function")
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        income_operations_1 = request.POST.get("income_operations_1")
        income_operations_2 = request.POST.get("income_operations_2")
        people_A_1 = request.POST.get("people_A_1")
        people_A_2 = request.POST.get("people_A_2")
        industries_businesses_A_1 = request.POST.get("industries_businesses_A_1")
        industries_businesses_A_2 = request.POST.get("industries_businesses_A_2")
        interest_A_1 = request.POST.get("interest_A_1")
        interest_A_2 = request.POST.get("interest_A_2")
        rent_land_1 = request.POST.get("rent_land_1")
        rent_land_2 = request.POST.get("rent_land_2")
        capital_gain_1 = request.POST.get("capital_gain_1")
        capital_gain_2 = request.POST.get("capital_gain_2")
        other_income_A_1 = request.POST.get("other_income_A_1")
        other_income_A_2 = request.POST.get("other_income_A_2")
        total_income_A_1 = request.POST.get("total_income_A_1")
        total_income_A_2 = request.POST.get("total_income_A_2")
        salaries_wages_bonus_B_1 = request.POST.get("salaries_wages_bonus_B_1")
        salaries_wages_bonus_B_2 = request.POST.get("salaries_wages_bonus_B_2")
        interests_B_1 = request.POST.get("interests_B_1")
        interests_B_2 = request.POST.get("interests_B_2")
        rent_B_1 = request.POST.get("rent_B_1")
        rent_B_2 = request.POST.get("rent_B_2")
        depreciation_B_1 = request.POST.get("depreciation_B_1")
        depreciation_B_2 = request.POST.get("depreciation_B_2")
        donation_B_1 = request.POST.get("donation_B_1")
        donation_B_2 = request.POST.get("donation_B_2")
        sales_taxes_B_1 = request.POST.get("sales_taxes_B_1")
        sales_taxes_B_2 = request.POST.get("sales_taxes_B_2")
        purchases_B_1 = request.POST.get("purchases_B_1")
        purchases_B_2 = request.POST.get("purchases_B_2")
        other_purchases_B_1 = request.POST.get("other_purchases_B_1")
        other_purchases_B_2 = request.POST.get("other_purchases_B_2")
        other_operations_B_1 = request.POST.get("other_operations_B_1")
        other_operations_B_2 = request.POST.get("other_operations_B_2")
        total_expenses_B_1 = request.POST.get("total_expenses_B_1")
        total_expenses_B_2 = request.POST.get("total_expenses_B_2")
        net_profit_1 = request.POST.get("net_profit_1")
        net_profit_2 = request.POST.get("net_profit_2")
        income_C_1 = request.POST.get("income_C_1")
        income_C_2 = request.POST.get("income_C_2")
        profit_C_after_1 = request.POST.get("profit_C_after_1")
        profit_C_after_2 = request.POST.get("profit_C_after_2")
        sales_D_1 = request.POST.get("sales_D_1")
        sales_D_2 = request.POST.get("sales_D_2")
        name = request.POST.get("name")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-490.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "company_name",
                        "address",
                        "email",
                        "liaison_officer",
                        "ssn",
                        "tel",
                        "fax",
                        "legal_form",
                        "cfc",
                        "business_type",
                        "business_function",
                        "closing_date",
                        "start_year",
                        "end_year",
                        "income_operations_1",
                        "income_operations_2",
                        "people_A_1",
                        "people_A_2",
                        "industries_businesses_A_1",
                        "industries_businesses_A_2",
                        "interest_A_1",
                        "interest_A_2",
                        "rent_land_1",
                        "rent_land_2",
                        "capital_gain_1",
                        "capital_gain_2",
                        "other_income_A_1",
                        "other_income_A_2",
                        "total_income_A_1",
                        "total_income_A_2",
                        "salaries_wages_bonus_B_1",
                        "salaries_wages_bonus_B_2",
                        "interests_B_1",
                        "interests_B_2",
                        "rent_B_1",
                        "rent_B_2",
                        "depreciation_B_1",
                        "depreciation_B_2",
                        "donation_B_1",
                        "donation_B_2",
                        "sales_taxes_B_1",
                        "sales_taxes_B_2",
                        "purchases_B_1",
                        "purchases_B_2",
                        "other_purchases_B_1",
                        "other_purchases_B_2",
                        "other_operations_B_1",
                        "other_operations_B_2",
                        "total_expenses_B_1",
                        "total_expenses_B_2",
                        "net_profit_1",
                        "net_profit_2",
                        "income_C_1",
                        "income_C_2",
                        "profit_C_after_1",
                        "profit_C_after_2",
                        "sales_D_1",
                        "sales_D_2",
                        "name",
                        "rank",
                    ]
                )

            writer.writerow(
                [
                    company_name,
                    address,
                    email,
                    liaison_officer,
                    ssn,
                    tel,
                    fax,
                    legal_form,
                    cfc,
                    business_type,
                    business_function,
                    closing_date,
                    start_year,
                    end_year,
                    income_operations_1,
                    income_operations_2,
                    people_A_1,
                    people_A_2,
                    industries_businesses_A_1,
                    industries_businesses_A_2,
                    interest_A_1,
                    interest_A_2,
                    rent_land_1,
                    rent_land_2,
                    capital_gain_1,
                    capital_gain_2,
                    other_income_A_1,
                    other_income_A_2,
                    total_income_A_1,
                    total_income_A_2,
                    salaries_wages_bonus_B_1,
                    salaries_wages_bonus_B_2,
                    interests_B_1,
                    interests_B_2,
                    rent_B_1,
                    rent_B_2,
                    depreciation_B_1,
                    depreciation_B_2,
                    donation_B_1,
                    donation_B_2,
                    sales_taxes_B_1,
                    sales_taxes_B_2,
                    purchases_B_1,
                    purchases_B_2,
                    other_purchases_B_1,
                    other_purchases_B_2,
                    other_operations_B_1,
                    other_operations_B_2,
                    total_expenses_B_1,
                    total_expenses_B_2,
                    net_profit_1,
                    net_profit_2,
                    income_C_1,
                    income_C_2,
                    profit_C_after_1,
                    profit_C_after_2,
                    sales_D_1,
                    sales_D_2,
                    name,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-490.csv",
            dtypes={
                "company_name": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "ssn": str,
                "tel": str,
                "fax": str,
                "legal_form": str,
                "cfc": str,
                "business_type": str,
                "business_function": str,
                "closing_date": str,
                "start_year": int,
                "end_year": int,
                "income_operations_1": float,
                "income_operations_2": float,
                "people_A_1": float,
                "people_A_2": float,
                "industries_businesses_A_1": float,
                "industries_businesses_A_2": float,
                "interest_A_1": float,
                "interest_A_2": float,
                "rent_land_1": float,
                "rent_land_2": float,
                "capital_gain_1": float,
                "capital_gain_2": float,
                "other_income_A_1": float,
                "other_income_A_2": float,
                "total_income_A_1": float,
                "total_income_A_2": float,
                "salaries_wages_bonus_B_1": float,
                "salaries_wages_bonus_B_2": float,
                "interests_B_1": float,
                "interests_B_2": float,
                "rent_B_1": float,
                "rent_B_2": float,
                "depreciation_B_1": float,
                "depreciation_B_2": float,
                "donation_B_1": float,
                "donation_B_2": float,
                "sales_taxes_B_1": float,
                "sales_taxes_B_2": float,
                "purchases_B_1": float,
                "purchases_B_2": float,
                "other_purchases_B_1": float,
                "other_purchases_B_2": float,
                "other_operations_B_1": float,
                "other_operations_B_2": float,
                "total_expenses_B_1": float,
                "total_expenses_B_2": float,
                "net_profit_1": float,
                "net_profit_2": float,
                "income_C_1": float,
                "income_C_2": float,
                "profit_C_after_1": float,
                "profit_C_after_2": float,
                "sales_D_1": float,
                "sales_D_2": float,
                "name": str,
                "rank": str,
            },
            table_name="IP_490",
            table_id="35",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-490.html")


def IP_520(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get("company_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")

        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")

        legal_form = request.POST.get("legal_form")
        cfc = request.POST.get("cfc")
        business_type = request.POST.get("business_type")
        closing_date = request.POST.get("closing_date")
        branches = request.POST.get("branches")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")

        incomes_interests_1 = request.POST.get("incomes_interests_1")
        incomes_interests_2 = request.POST.get("incomes_interests_2")
        incomes_personal_loans_1 = request.POST.get("incomes_personal_loans_1")
        incomes_personal_loans_2 = request.POST.get("incomes_personal_loans_2")
        incomes_mortage_loans_1 = request.POST.get("incomes_mortage_loans_1")
        incomes_mortage_loans_2 = request.POST.get("incomes_mortage_loans_2")
        incomes_other_1 = request.POST.get("incomes_other_1")
        incomes_other_2 = request.POST.get("incomes_other_2")
        incomes_rent_1 = request.POST.get("incomes_rent_1")
        incomes_rent_2 = request.POST.get("incomes_rent_2")
        incomes_dividends_1 = request.POST.get("incomes_dividends_1")
        incomes_dividends_2 = request.POST.get("incomes_dividends_2")
        incomes_financing_charges_1 = request.POST.get("incomes_financing_charges_1")
        incomes_financing_charges_2 = request.POST.get("incomes_financing_charges_2")
        incomes_service_charges_1 = request.POST.get("incomes_service_charges_1")
        incomes_service_charges_2 = request.POST.get("incomes_service_charges_2")
        incomes_commissions_1 = request.POST.get("incomes_commissions_1")
        incomes_commissions_2 = request.POST.get("incomes_commissions_2")
        incomes_finance_leasing_1 = request.POST.get("incomes_finance_leasing_1")
        incomes_finance_leasing_2 = request.POST.get("incomes_finance_leasing_2")
        incomes_capital_gain_loss_1 = request.POST.get("incomes_capital_gain_loss_1")
        incomes_capital_gain_loss_2 = request.POST.get("incomes_capital_gain_loss_2")
        incomes_other_operations_1 = request.POST.get("incomes_other_operations_1")
        incomes_other_operations_2 = request.POST.get("incomes_other_operations_2")
        incomes_total_1 = request.POST.get("incomes_total_1")
        incomes_total_2 = request.POST.get("incomes_total_2")
        expenses_salaries_wages_bonus_1 = request.POST.get(
            "expenses_salaries_wages_bonus_1"
        )
        expenses_salaries_wages_bonus_2 = request.POST.get(
            "expenses_salaries_wages_bonus_2"
        )
        expenses_interests_1 = request.POST.get("expenses_interests_1")
        expenses_interests_2 = request.POST.get("expenses_interests_2")
        interests_to_individuals_1 = request.POST.get("interests_to_individuals_1")
        interests_to_individuals_2 = request.POST.get("interests_to_individuals_2")
        interests_to_corporations_1 = request.POST.get("interests_to_corporations_1")
        interests_to_corporations_2 = request.POST.get("interests_to_corporations_2")
        corporation_936_1 = request.POST.get("corporation_936_1")
        corporation_936_2 = request.POST.get("corporation_936_2")
        other_corporation_1 = request.POST.get("other_corporation_1")
        other_corporation_2 = request.POST.get("other_corporation_2")
        interests_other_1 = request.POST.get("interests_other_1")
        interests_other_2 = request.POST.get("interests_other_2")
        expenses_rent_1 = request.POST.get("expenses_rent_1")
        expenses_rent_2 = request.POST.get("expenses_rent_2")
        expenses_depreciation_1 = request.POST.get("expenses_depreciation_1")
        expenses_depreciation_2 = request.POST.get("expenses_depreciation_2")
        expenses_bad_debts_1 = request.POST.get("expenses_bad_debts_1")
        expenses_bad_debts_2 = request.POST.get("expenses_bad_debts_2")
        expenses_donations_1 = request.POST.get("expenses_donations_1")
        expenses_donations_2 = request.POST.get("expenses_donations_2")
        expenses_sales_taxes_1 = request.POST.get("expenses_sales_taxes_1")
        expenses_sales_taxes_2 = request.POST.get("expenses_sales_taxes_2")
        expenses_machinary_1 = request.POST.get("expenses_machinary_1")
        expenses_machinary_2 = request.POST.get("expenses_machinary_2")
        expenses_other_purchases_1 = request.POST.get("expenses_other_purchases_1")
        expenses_other_purchases_2 = request.POST.get("expenses_other_purchases_2")
        expenses_licenses_1 = request.POST.get("expenses_licenses_1")
        expenses_licenses_2 = request.POST.get("expenses_licenses_2")
        expenses_other_operations_1 = request.POST.get("expenses_other_operations_1")
        expenses_other_operations_2 = request.POST.get("expenses_other_operations_2")
        expenses_total_1 = request.POST.get("expenses_total_1")
        expenses_total_2 = request.POST.get("expenses_total_2")
        gross_profit_1 = request.POST.get("gross_profit_1")
        gross_profit_2 = request.POST.get("gross_profit_2")
        profit_income_tax_1 = request.POST.get("profit_income_tax_1")
        profit_income_tax_2 = request.POST.get("profit_income_tax_2")
        profit_after_income_tax_1 = request.POST.get("profit_after_income_tax_1")
        profit_after_income_tax_2 = request.POST.get("profit_after_income_tax_2")
        dividends_paid_1 = request.POST.get("dividends_paid_1")
        dividends_paid_2 = request.POST.get("dividends_paid_2")
        sales_tax_1 = request.POST.get("sales_tax_1")
        sales_tax_2 = request.POST.get("sales_tax_2")

        name = request.POST.get("name")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-520.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "company_name",
                        "address",
                        "email",
                        "liaison_officer",
                        "ssn",
                        "tel",
                        "fax",
                        "legal_form",
                        "cfc",
                        "business_type",
                        "closing_date",
                        "branches",
                        "start_year",
                        "end_year",
                        "incomes_interests_1",
                        "incomes_interests_2",
                        "incomes_personal_loans_1",
                        "incomes_personal_loans_2",
                        "incomes_mortage_loans_1",
                        "incomes_mortage_loans_2",
                        "incomes_other_1",
                        "incomes_other_2",
                        "incomes_rent_1",
                        "incomes_rent_2",
                        "incomes_dividends_1",
                        "incomes_dividends_2",
                        "incomes_financing_charges_1",
                        "incomes_financing_charges_2",
                        "incomes_service_charges_1",
                        "incomes_service_charges_2",
                        "incomes_commissions_1",
                        "incomes_commissions_2",
                        "incomes_finance_leasing_1",
                        "incomes_finance_leasing_2",
                        "incomes_capital_gain_loss_1",
                        "incomes_capital_gain_loss_2",
                        "incomes_other_operations_1",
                        "incomes_other_operations_2",
                        "incomes_total_1",
                        "incomes_total_2",
                        "expenses_salaries_wages_bonus_1",
                        "expenses_salaries_wages_bonus_2",
                        "expenses_interests_1",
                        "expenses_interests_2",
                        "interests_to_individuals_1",
                        "interests_to_individuals_2",
                        "interests_to_corporations_1",
                        "interests_to_corporations_2",
                        "corporation_936_1",
                        "corporation_936_2",
                        "other_corporation_1",
                        "other_corporation_2",
                        "interests_other_1",
                        "interests_other_2",
                        "expenses_rent_1",
                        "expenses_rent_2",
                        "expenses_depreciation_1",
                        "expenses_depreciation_2",
                        "expenses_bad_debts_1",
                        "expenses_bad_debts_2",
                        "expenses_donations_1",
                        "expenses_donations_2",
                        "expenses_sales_taxes_1",
                        "expenses_sales_taxes_2",
                        "expenses_machinary_1",
                        "expenses_machinary_2",
                        "expenses_other_purchases_1",
                        "expenses_other_purchases_2",
                        "expenses_licenses_1",
                        "expenses_licenses_2",
                        "expenses_other_operations_1",
                        "expenses_other_operations_2",
                        "expenses_total_1",
                        "expenses_total_2",
                        "gross_profit_1",
                        "gross_profit_2",
                        "profit_income_tax_1",
                        "profit_income_tax_2",
                        "profit_after_income_tax_1",
                        "profit_after_income_tax_2",
                        "dividends_paid_1",
                        "dividends_paid_2",
                        "sales_tax_1",
                        "sales_tax_2",
                        "name",
                        "rank",
                    ]
                )

            writer.writerow(
                [
                    company_name,
                    address,
                    email,
                    liaison_officer,
                    ssn,
                    tel,
                    fax,
                    legal_form,
                    cfc,
                    business_type,
                    closing_date,
                    branches,
                    start_year,
                    end_year,
                    incomes_interests_1,
                    incomes_interests_2,
                    incomes_personal_loans_1,
                    incomes_personal_loans_2,
                    incomes_mortage_loans_1,
                    incomes_mortage_loans_2,
                    incomes_other_1,
                    incomes_other_2,
                    incomes_rent_1,
                    incomes_rent_2,
                    incomes_dividends_1,
                    incomes_dividends_2,
                    incomes_financing_charges_1,
                    incomes_financing_charges_2,
                    incomes_service_charges_1,
                    incomes_service_charges_2,
                    incomes_commissions_1,
                    incomes_commissions_2,
                    incomes_finance_leasing_1,
                    incomes_finance_leasing_2,
                    incomes_capital_gain_loss_1,
                    incomes_capital_gain_loss_2,
                    incomes_other_operations_1,
                    incomes_other_operations_2,
                    incomes_total_1,
                    incomes_total_2,
                    expenses_salaries_wages_bonus_1,
                    expenses_salaries_wages_bonus_2,
                    expenses_interests_1,
                    expenses_interests_2,
                    interests_to_individuals_1,
                    interests_to_individuals_2,
                    interests_to_corporations_1,
                    interests_to_corporations_2,
                    corporation_936_1,
                    corporation_936_2,
                    other_corporation_1,
                    other_corporation_2,
                    interests_other_1,
                    interests_other_2,
                    expenses_rent_1,
                    expenses_rent_2,
                    expenses_depreciation_1,
                    expenses_depreciation_2,
                    expenses_bad_debts_1,
                    expenses_bad_debts_2,
                    expenses_donations_1,
                    expenses_donations_2,
                    expenses_sales_taxes_1,
                    expenses_sales_taxes_2,
                    expenses_machinary_1,
                    expenses_machinary_2,
                    expenses_other_purchases_1,
                    expenses_other_purchases_2,
                    expenses_licenses_1,
                    expenses_licenses_2,
                    expenses_other_operations_1,
                    expenses_other_operations_2,
                    expenses_total_1,
                    expenses_total_2,
                    gross_profit_1,
                    gross_profit_2,
                    profit_income_tax_1,
                    profit_income_tax_2,
                    profit_after_income_tax_1,
                    profit_after_income_tax_2,
                    dividends_paid_1,
                    dividends_paid_2,
                    sales_tax_1,
                    sales_tax_2,
                    name,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-520.csv",
            dtypes={
                "company_name": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "ssn": str,
                "tel": str,
                "fax": str,
                "legal_form": str,
                "cfc": str,
                "business_type": str,
                "closing_date": str,
                "branches": str,
                "start_year": int,
                "end_year": int,
                "incomes_interests_1": float,
                "incomes_interests_2": float,
                "incomes_personal_loans_1": float,
                "incomes_personal_loans_2": float,
                "incomes_mortage_loans_1": float,
                "incomes_mortage_loans_2": float,
                "incomes_other_1": float,
                "incomes_other_2": float,
                "incomes_rent_1": float,
                "incomes_rent_2": float,
                "incomes_dividends_1": float,
                "incomes_dividends_2": float,
                "incomes_financing_charges_1": float,
                "incomes_financing_charges_2": float,
                "incomes_service_charges_1": float,
                "incomes_service_charges_2": float,
                "incomes_commissions_1": float,
                "incomes_commissions_2": float,
                "incomes_finance_leasing_1": float,
                "incomes_finance_leasing_2": float,
                "incomes_capital_gain_loss_1": float,
                "incomes_capital_gain_loss_2": float,
                "incomes_other_operations_1": float,
                "incomes_other_operations_2": float,
                "incomes_total_1": float,
                "incomes_total_2": float,
                "expenses_salaries_wages_bonus_1": float,
                "expenses_salaries_wages_bonus_2": float,
                "expenses_interests_1": float,
                "expenses_interests_2": float,
                "interests_to_individuals_1": float,
                "interests_to_individuals_2": float,
                "interests_to_corporations_1": float,
                "interests_to_corporations_2": float,
                "corporation_936_1": float,
                "corporation_936_2": float,
                "other_corporation_1": float,
                "other_corporation_2": float,
                "interests_other_1": float,
                "interests_other_2": float,
                "expenses_rent_1": float,
                "expenses_rent_2": float,
                "expenses_depreciation_1": float,
                "expenses_depreciation_2": float,
                "expenses_bad_debts_1": float,
                "expenses_bad_debts_2": float,
                "expenses_donations_1": float,
                "expenses_donations_2": float,
                "expenses_sales_taxes_1": float,
                "expenses_sales_taxes_2": float,
                "expenses_machinary_1": float,
                "expenses_machinary_2": float,
                "expenses_other_purchases_1": float,
                "expenses_other_purchases_2": float,
                "expenses_licenses_1": float,
                "expenses_licenses_2": float,
                "expenses_other_operations_1": float,
                "expenses_other_operations_2": float,
                "expenses_total_1": float,
                "expenses_total_2": float,
                "gross_profit_1": float,
                "gross_profit_2": float,
                "profit_income_tax_1": float,
                "profit_income_tax_2": float,
                "profit_after_income_tax_1": float,
                "profit_after_income_tax_2": float,
                "dividends_paid_1": float,
                "dividends_paid_2": float,
                "sales_tax_1": float,
                "sales_tax_2": float,
                "name": str,
                "rank": str,
            },
            table_name="IP_520",
            table_id="37",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-520.html")


def JP_536_2(request):
    if request.method == "POST":
        # Retrieve form data
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        inventario1 = request.POST.get("inventario1")
        inventario2 = request.POST.get("inventario2")
        compras1 = request.POST.get("compras1")
        compras2 = request.POST.get("compras2")
        depre1 = request.POST.get("depre1")
        depre2 = request.POST.get("depre2")
        maquinaria1 = request.POST.get("maquinaria1")
        maquinaria2 = request.POST.get("maquinaria2")
        equipo1 = request.POST.get("equipo1")
        equipo2 = request.POST.get("equipo2")
        computadora1 = request.POST.get("computadora1")
        computadora2 = request.POST.get("computadora2")
        alquiler1 = request.POST.get("alquiler1")
        alquiler2 = request.POST.get("alquiler2")
        licencia1 = request.POST.get("licencia1")
        licencia2 = request.POST.get("licencia2")
        company_name = request.POST.get("company_name")
        phone = request.POST.get("phone")
        name_title = request.POST.get("name_title")
        date = request.POST.get("date")

        csv_file_path = "data/cuestionarios/balanza_de_pagos/JP-536-2.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "start_year",
                        "end_year",
                        "inventario1",
                        "inventario2",
                        "compras1",
                        "compras2",
                        "depre1",
                        "depre2",
                        "maquinaria1",
                        "maquinaria2",
                        "equipo1",
                        "equipo2",
                        "computadora1",
                        "computadora2",
                        "alquiler1",
                        "alquiler2",
                        "licencia1",
                        "licencia2",
                        "company_name",
                        "phone",
                        "name_title",
                        "date",
                    ]
                )

            writer.writerow(
                [
                    start_year,
                    end_year,
                    inventario1,
                    inventario2,
                    compras1,
                    compras2,
                    depre1,
                    depre2,
                    maquinaria1,
                    maquinaria2,
                    equipo1,
                    equipo2,
                    computadora1,
                    computadora2,
                    alquiler1,
                    alquiler2,
                    licencia1,
                    licencia2,
                    company_name,
                    phone,
                    name_title,
                    date,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/balanza_de_pagos/JP-536-2.csv",
            dtypes={
                "start_year": int,
                "end_year": int,
                "inventario1": float,
                "inventario2": float,
                "compras1": float,
                "compras2": float,
                "depre1": float,
                "depre2": float,
                "maquinaria1": float,
                "maquinaria2": float,
                "equipo1": float,
                "equipo2": float,
                "computadora1": float,
                "computadora2": float,
                "alquiler1": float,
                "alquiler2": float,
                "licencia1": float,
                "licencia2": float,
                "company_name": str,
                "phone": str,
                "name_title": str,
                "date": str,
            },
            table_name="JP_536_2",
            table_id="18",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/balanza_de_pagos/JP-536-2.html")


def IP_510(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get("company_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")
        legal_form = request.POST.get("legal_form")
        cfc = request.POST.get("cfc")
        accounting_period = request.POST.get("accounting_period")
        main_product_1 = request.POST.get("main_product_1")
        main_product_2 = request.POST.get("main_product_2")
        raw_material_used = request.POST.get("raw_material_used")
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        sales_from_persons_1 = request.POST.get("sales_from_persons_1")
        sales_from_persons_2 = request.POST.get("sales_from_persons_2")
        sales_industries_businesses_1 = request.POST.get(
            "sales_industries_businesses_1"
        )
        sales_industries_businesses_2 = request.POST.get(
            "sales_industries_businesses_2"
        )
        sales_goods_1 = request.POST.get("sales_goods_1")
        sales_goods_2 = request.POST.get("sales_goods_2")
        sales_exports_goods_1 = request.POST.get("sales_exports_goods_1")
        sales_exports_goods_2 = request.POST.get("sales_exports_goods_2")
        sales_goods_from_others_firms_1 = request.POST.get(
            "sales_goods_from_others_firms_1"
        )
        sales_goods_from_others_firms_2 = request.POST.get(
            "sales_goods_from_others_firms_2"
        )
        sales_exports_goods_other_firms_1 = request.POST.get(
            "sales_exports_goods_other_firms_1"
        )
        sales_exports_goods_other_firms_2 = request.POST.get(
            "sales_exports_goods_other_firms_2"
        )
        total_cost_1 = request.POST.get("total_cost_1")
        total_cost_2 = request.POST.get("total_cost_2")
        total_cost_inventories_begginning_1 = request.POST.get(
            "total_cost_inventories_begginning_1"
        )
        total_cost_inventories_begginning_2 = request.POST.get(
            "total_cost_inventories_begginning_2"
        )
        total_cost_purchases_1 = request.POST.get("total_cost_purchases_1")
        total_cost_purchases_2 = request.POST.get("total_cost_purchases_2")
        total_cost_total_raw_1 = request.POST.get("total_cost_total_raw_1")
        total_cost_total_raw_2 = request.POST.get("total_cost_total_raw_2")
        total_cost_imported_1 = request.POST.get("total_cost_imported_1")
        total_cost_imported_2 = request.POST.get("total_cost_imported_2")
        total_cost_others_1 = request.POST.get("total_cost_others_1")
        total_cost_others_2 = request.POST.get("total_cost_others_2")
        total_cost_direct_wages_1 = request.POST.get("total_cost_direct_wages_1")
        total_cost_direct_wages_2 = request.POST.get("total_cost_direct_wages_2")
        total_cost_depreciation_1 = request.POST.get("total_cost_depreciation_1")
        total_cost_depreciation_2 = request.POST.get("total_cost_depreciation_2")
        total_cost_rent_land_1 = request.POST.get("total_cost_rent_land_1")
        total_cost_rent_land_2 = request.POST.get("total_cost_rent_land_2")
        total_cost_other_direct_1 = request.POST.get("total_cost_other_direct_1")
        total_cost_other_direct_2 = request.POST.get("total_cost_other_direct_2")
        total_cost_indirect_cost_1 = request.POST.get("total_cost_indirect_cost_1")
        total_cost_indirect_cost_2 = request.POST.get("total_cost_indirect_cost_2")
        total_cost_inventories_end_1 = request.POST.get("total_cost_inventories_end_1")
        total_cost_inventories_end_2 = request.POST.get("total_cost_inventories_end_2")
        gross_profit_1 = request.POST.get("gross_profit_1")
        gross_profit_2 = request.POST.get("gross_profit_2")
        other_operating_1 = request.POST.get("other_operating_1")
        other_operating_2 = request.POST.get("other_operating_2")
        other_operating_interest_1 = request.POST.get("other_operating_interest_1")
        other_operating_interest_2 = request.POST.get("other_operating_interest_2")
        other_operating_rent_land_1 = request.POST.get("other_operating_rent_land_1")
        other_operating_rent_land_2 = request.POST.get("other_operating_rent_land_2")
        other_operating_capital_gain_1 = request.POST.get(
            "other_operating_capital_gain_1"
        )
        other_operating_capital_gain_2 = request.POST.get(
            "other_operating_capital_gain_2"
        )
        other_operating_other_1 = request.POST.get("other_operating_other_1")
        other_operating_other_2 = request.POST.get("other_operating_other_2")
        total_gross_1 = request.POST.get("total_gross_1")
        total_gross_2 = request.POST.get("total_gross_2")
        expenses_not_included_1 = request.POST.get("expenses_not_included_1")
        expenses_not_included_2 = request.POST.get("expenses_not_included_2")
        expenses_not_included_salaries_1 = request.POST.get(
            "expenses_not_included_salaries_1"
        )
        expenses_not_included_salaries_2 = request.POST.get(
            "expenses_not_included_salaries_2"
        )
        expenses_not_included_interest_1 = request.POST.get(
            "expenses_not_included_interest_1"
        )
        expenses_not_included_interest_2 = request.POST.get(
            "expenses_not_included_interest_2"
        )
        expenses_not_included_depreciation_1 = request.POST.get(
            "expenses_not_included_depreciation_1"
        )
        expenses_not_included_depreciation_2 = request.POST.get(
            "expenses_not_included_depreciation_2"
        )
        expenses_not_included_donations_1 = request.POST.get(
            "expenses_not_included_donations_1"
        )
        expenses_not_included_donations_2 = request.POST.get(
            "expenses_not_included_donations_2"
        )
        expenses_not_included_rent_land_1 = request.POST.get(
            "expenses_not_included_rent_land_1"
        )
        expenses_not_included_rent_land_2 = request.POST.get(
            "expenses_not_included_rent_land_2"
        )
        expenses_not_included_other_operating_1 = request.POST.get(
            "expenses_not_included_other_operating_1"
        )
        expenses_not_included_other_operating_2 = request.POST.get(
            "expenses_not_included_other_operating_2"
        )
        expenses_not_included_sales_tax_1 = request.POST.get(
            "expenses_not_included_sales_tax_1"
        )
        expenses_not_included_sales_tax_2 = request.POST.get(
            "expenses_not_included_sales_tax_2"
        )
        expenses_not_included_machinery_1 = request.POST.get(
            "expenses_not_included_machinery_1"
        )
        expenses_not_included_machinery_2 = request.POST.get(
            "expenses_not_included_machinery_2"
        )
        expenses_not_included_on_other_1 = request.POST.get(
            "expenses_not_included_on_other_1"
        )
        expenses_not_included_on_other_2 = request.POST.get(
            "expenses_not_included_on_other_2"
        )
        expenses_not_included_licenses_1 = request.POST.get(
            "expenses_not_included_licenses_1"
        )
        expenses_not_included_licenses_2 = request.POST.get(
            "expenses_not_included_licenses_2"
        )
        net_profit_loss_1 = request.POST.get("net_profit_loss_1")
        net_profit_loss_2 = request.POST.get("net_profit_loss_2")
        net_profit_loss_income_tax_1 = request.POST.get("net_profit_loss_income_tax_1")
        net_profit_loss_income_tax_2 = request.POST.get("net_profit_loss_income_tax_2")
        profit_after_tax_1 = request.POST.get("profit_after_tax_1")
        profit_after_tax_2 = request.POST.get("profit_after_tax_2")
        sales_and_use_withheld_1 = request.POST.get("sales_and_use_withheld_1")
        sales_and_use_withheld_2 = request.POST.get("sales_and_use_withheld_2")
        branches = request.POST.get("branches")
        branches_if_yes = request.POST.get("branches_if_yes")
        name = request.POST.get("name")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-510.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "company_name",
                        "address",
                        "email",
                        "liaison_officer",
                        "ssn",
                        "tel",
                        "fax",
                        "legal_form",
                        "cfc",
                        "accounting_period",
                        "main_product_1",
                        "main_product_2",
                        "raw_material_used",
                        "closing_date",
                        "start_year",
                        "end_year",
                        "sales_from_persons_1",
                        "sales_from_persons_2",
                        "sales_industries_businesses_1",
                        "sales_industries_businesses_2",
                        "sales_goods_1",
                        "sales_goods_2",
                        "sales_exports_goods_1",
                        "sales_exports_goods_2",
                        "sales_goods_from_others_firms_1",
                        "sales_goods_from_others_firms_2",
                        "sales_exports_goods_other_firms_1",
                        "sales_exports_goods_other_firms_2",
                        "total_cost_1",
                        "total_cost_2",
                        "total_cost_inventories_begginning_1",
                        "total_cost_inventories_begginning_2",
                        "total_cost_purchases_1",
                        "total_cost_purchases_2",
                        "total_cost_total_raw_1",
                        "total_cost_total_raw_2",
                        "total_cost_imported_1",
                        "total_cost_imported_2",
                        "total_cost_others_1",
                        "total_cost_others_2",
                        "total_cost_direct_wages_1",
                        "total_cost_direct_wages_2",
                        "total_cost_depreciation_1",
                        "total_cost_depreciation_2",
                        "total_cost_rent_land_1",
                        "total_cost_rent_land_2",
                        "total_cost_other_direct_1",
                        "total_cost_other_direct_2",
                        "total_cost_indirect_cost_1",
                        "total_cost_indirect_cost_2",
                        "total_cost_inventories_end_1",
                        "total_cost_inventories_end_2",
                        "gross_profit_1",
                        "gross_profit_2",
                        "other_operating_1",
                        "other_operating_2",
                        "other_operating_interest_1",
                        "other_operating_interest_2",
                        "other_operating_rent_land_1",
                        "other_operating_rent_land_2",
                        "other_operating_capital_gain_1",
                        "other_operating_capital_gain_2",
                        "other_operating_other_1",
                        "other_operating_other_2",
                        "total_gross_1",
                        "total_gross_2",
                        "expenses_not_included_1",
                        "expenses_not_included_2",
                        "expenses_not_included_salaries_1",
                        "expenses_not_included_salaries_2",
                        "expenses_not_included_interest_1",
                        "expenses_not_included_interest_2",
                        "expenses_not_included_depreciation_1",
                        "expenses_not_included_depreciation_2",
                        "expenses_not_included_donations_1",
                        "expenses_not_included_donations_2",
                        "expenses_not_included_rent_land_1",
                        "expenses_not_included_rent_land_2",
                        "expenses_not_included_other_operating_1",
                        "expenses_not_included_other_operating_2",
                        "expenses_not_included_sales_tax_1",
                        "expenses_not_included_sales_tax_2",
                        "expenses_not_included_machinery_1",
                        "expenses_not_included_machinery_2",
                        "expenses_not_included_on_other_1",
                        "expenses_not_included_on_other_2",
                        "expenses_not_included_licenses_1",
                        "expenses_not_included_licenses_2",
                        "net_profit_loss_1",
                        "net_profit_loss_2",
                        "net_profit_loss_income_tax_1",
                        "net_profit_loss_income_tax_2",
                        "profit_after_tax_1",
                        "profit_after_tax_2",
                        "sales_and_use_withheld_1",
                        "sales_and_use_withheld_2",
                        "branches",
                        "branches_if_yes",
                        "name",
                        "rank",
                    ]
                )

            writer.writerow(
                [
                    company_name,
                    address,
                    email,
                    liaison_officer,
                    ssn,
                    tel,
                    fax,
                    legal_form,
                    cfc,
                    accounting_period,
                    main_product_1,
                    main_product_2,
                    raw_material_used,
                    closing_date,
                    start_year,
                    end_year,
                    sales_from_persons_1,
                    sales_from_persons_2,
                    sales_industries_businesses_1,
                    sales_industries_businesses_2,
                    sales_goods_1,
                    sales_goods_2,
                    sales_exports_goods_1,
                    sales_exports_goods_2,
                    sales_goods_from_others_firms_1,
                    sales_goods_from_others_firms_2,
                    sales_exports_goods_other_firms_1,
                    sales_exports_goods_other_firms_2,
                    total_cost_1,
                    total_cost_2,
                    total_cost_inventories_begginning_1,
                    total_cost_inventories_begginning_2,
                    total_cost_purchases_1,
                    total_cost_purchases_2,
                    total_cost_total_raw_1,
                    total_cost_total_raw_2,
                    total_cost_imported_1,
                    total_cost_imported_2,
                    total_cost_others_1,
                    total_cost_others_2,
                    total_cost_direct_wages_1,
                    total_cost_direct_wages_2,
                    total_cost_depreciation_1,
                    total_cost_depreciation_2,
                    total_cost_rent_land_1,
                    total_cost_rent_land_2,
                    total_cost_other_direct_1,
                    total_cost_other_direct_2,
                    total_cost_indirect_cost_1,
                    total_cost_indirect_cost_2,
                    total_cost_inventories_end_1,
                    total_cost_inventories_end_2,
                    gross_profit_1,
                    gross_profit_2,
                    other_operating_1,
                    other_operating_2,
                    other_operating_interest_1,
                    other_operating_interest_2,
                    other_operating_rent_land_1,
                    other_operating_rent_land_2,
                    other_operating_capital_gain_1,
                    other_operating_capital_gain_2,
                    other_operating_other_1,
                    other_operating_other_2,
                    total_gross_1,
                    total_gross_2,
                    expenses_not_included_1,
                    expenses_not_included_2,
                    expenses_not_included_salaries_1,
                    expenses_not_included_salaries_2,
                    expenses_not_included_interest_1,
                    expenses_not_included_interest_2,
                    expenses_not_included_depreciation_1,
                    expenses_not_included_depreciation_2,
                    expenses_not_included_donations_1,
                    expenses_not_included_donations_2,
                    expenses_not_included_rent_land_1,
                    expenses_not_included_rent_land_2,
                    expenses_not_included_other_operating_1,
                    expenses_not_included_other_operating_2,
                    expenses_not_included_sales_tax_1,
                    expenses_not_included_sales_tax_2,
                    expenses_not_included_machinery_1,
                    expenses_not_included_machinery_2,
                    expenses_not_included_on_other_1,
                    expenses_not_included_on_other_2,
                    expenses_not_included_licenses_1,
                    expenses_not_included_licenses_2,
                    net_profit_loss_1,
                    net_profit_loss_2,
                    net_profit_loss_income_tax_1,
                    net_profit_loss_income_tax_2,
                    profit_after_tax_1,
                    profit_after_tax_2,
                    sales_and_use_withheld_1,
                    sales_and_use_withheld_2,
                    branches,
                    branches_if_yes,
                    name,
                    rank,
                ]
            )
        
        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-510.csv",
            dtypes={
                "company_name": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "ssn": str,
                "tel": str,
                "fax": str,
                "legal_form": str,
                "cfc": str,
                "accounting_period": str,
                "main_product_1": str,
                "main_product_2": str,
                "raw_material_used": str,
                "closing_date": str,
                "start_year": int,
                "end_year": int,
                "sales_from_persons_1": float,
                "sales_from_persons_2": float,
                "sales_industries_businesses_1": float,
                "sales_industries_businesses_2": float,
                "sales_goods_1": float,
                "sales_goods_2": float,
                "sales_exports_goods_1": float,
                "sales_exports_goods_2": float,
                "sales_goods_from_others_firms_1": float,
                "sales_goods_from_others_firms_2": float,
                "sales_exports_goods_other_firms_1": float,
                "sales_exports_goods_other_firms_2": float,
                "total_cost_1": float,
                "total_cost_2": float,
                "total_cost_inventories_begginning_1": float,
                "total_cost_inventories_begginning_2": float,
                "total_cost_purchases_1": float,
                "total_cost_purchases_2": float,
                "total_cost_total_raw_1": float,
                "total_cost_total_raw_2": float,
                "total_cost_imported_1": float,
                "total_cost_imported_2": float,
                "total_cost_others_1": float,
                "total_cost_others_2": float,
                "total_cost_direct_wages_1": float,
                "total_cost_direct_wages_2": float,
                "total_cost_depreciation_1": float,
                "total_cost_depreciation_2": float,
                "total_cost_rent_land_1": float,
                "total_cost_rent_land_2": float,
                "total_cost_other_direct_1": float,
                "total_cost_other_direct_2": float,
                "total_cost_indirect_cost_1": float,
                "total_cost_indirect_cost_2": float,
                "total_cost_inventories_end_1": float,
                "total_cost_inventories_end_2": float,
                "gross_profit_1": float,
                "gross_profit_2": float,
                "other_operating_1": float,
                "other_operating_2": float,
                "other_operating_interest_1": float,
                "other_operating_interest_2": float,
                "other_operating_rent_land_1": float,
                "other_operating_rent_land_2": float,
                "other_operating_capital_gain_1": float,
                "other_operating_capital_gain_2": float,
                "other_operating_other_1": float,
                "other_operating_other_2": float,
                "total_gross_1": float,
                "total_gross_2": float,
                "expenses_not_included_1": float,
                "expenses_not_included_2": float,
                "expenses_not_included_salaries_1": float,
                "expenses_not_included_salaries_2": float,
                "expenses_not_included_interest_1": float,
                "expenses_not_included_interest_2": float,
                "expenses_not_included_depreciation_1": float,
                "expenses_not_included_depreciation_2": float,
                "expenses_not_included_donations_1": float,
                "expenses_not_included_donations_2": float,
                "expenses_not_included_rent_land_1": float,
                "expenses_not_included_rent_land_2": float,
                "expenses_not_included_other_operating_1": float,
                "expenses_not_included_other_operating_2": float,
                "expenses_not_included_sales_tax_1": float,
                "expenses_not_included_sales_tax_2": float,
                "expenses_not_included_machinery_1": float,
                "expenses_not_included_machinery_2": float,
                "expenses_not_included_on_other_1": float,
                "expenses_not_included_on_other_2": float,
                "expenses_not_included_licenses_1": float,
                "expenses_not_included_licenses_2": float,
                "net_profit_loss_1": float,
                "net_profit_loss_2": float,
                "net_profit_loss_income_tax_1": float,
                "net_profit_loss_income_tax_2": float,
                "profit_after_tax_1": float,
                "profit_after_tax_2": float,
                "sales_and_use_withheld_1": float,
                "sales_and_use_withheld_2": float,
                "branches": str,
                "branches_if_yes": str,
                "name": str,
                "rank": str,
            },
            table_name="IP_510",
            table_id="36",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-510.html")


def JP_544(request):
    if request.method == "POST":
        # Retrieve form data
        institucion1 = request.POST.get("institucion1")
        proposito1 = request.POST.get("proposito1")
        dolares1 = request.POST.get("dolares1")

        institucion2 = request.POST.get("institucion2")
        proposito2 = request.POST.get("proposito2")
        dolares2 = request.POST.get("dolares2")

        institucion3 = request.POST.get("institucion3")
        proposito3 = request.POST.get("proposito3")
        dolares3 = request.POST.get("dolares3")

        institucion4 = request.POST.get("institucion4")
        proposito4 = request.POST.get("proposito4")
        dolares4 = request.POST.get("dolares4")

        institucion5 = request.POST.get("institucion5")
        proposito5 = request.POST.get("proposito5")
        dolares5 = request.POST.get("dolares5")

        institucion6 = request.POST.get("institucion6")
        proposito6 = request.POST.get("proposito6")
        dolares6 = request.POST.get("dolares6")

        institucion7 = request.POST.get("institucion7")
        proposito7 = request.POST.get("proposito7")
        dolares7 = request.POST.get("dolares7")

        institucion8 = request.POST.get("institucion8")
        proposito8 = request.POST.get("proposito8")
        dolares8 = request.POST.get("dolares8")

        institucion9 = request.POST.get("institucion9")
        proposito9 = request.POST.get("proposito9")
        dolares9 = request.POST.get("dolares9")

        institucion10 = request.POST.get("institucion10")
        proposito10 = request.POST.get("proposito10")
        dolares10 = request.POST.get("dolares10")

        institucion11 = request.POST.get("institucion11")
        proposito11 = request.POST.get("proposito11")
        dolares11 = request.POST.get("dolares11")

        institucion12 = request.POST.get("institucion12")
        proposito12 = request.POST.get("proposito12")
        dolares12 = request.POST.get("dolares12")

        institucion13 = request.POST.get("institucion13")
        proposito13 = request.POST.get("proposito13")
        dolares13 = request.POST.get("dolares13")

        institucion14 = request.POST.get("institucion14")
        proposito14 = request.POST.get("proposito14")
        dolares14 = request.POST.get("dolares14")

        operation_expenses = request.POST.get("operation_expenses")
        salary = request.POST.get("salary")
        SS_SD_SR_beneficios_marginales = request.POST.get(
            "SS_SD_SR_beneficios_marginales"
        )
        servicios_profecionales_c = request.POST.get("servicios_profecionales_c")
        intereses = request.POST.get("intereses")
        other_gastos = request.POST.get("other_gastos")
        to_people = request.POST.get("to_people")
        servicios_profecionales_a = request.POST.get("servicios_profecionales_a")
        pension = request.POST.get("pension")
        name_other_1 = request.POST.get("name_other_1")
        quantity_other_1 = request.POST.get("quantity_other_1")
        name_other_2 = request.POST.get("name_other_2")
        quantity_other_2 = request.POST.get("quantity_other_2")
        name_other_3 = request.POST.get("name_other_3")
        quantity_other_3 = request.POST.get("quantity_other_3")
        name_other_4 = request.POST.get("name_other_4")
        quantity_other_4 = request.POST.get("quantity_other_4")
        agencia = request.POST.get("agencia")
        prep = request.POST.get("prep")
        titulo = request.POST.get("titulo")
        telefono = request.POST.get("telefono")
        fecha = request.POST.get("fecha")

        csv_file_path = "data/cuestionarios/balanza_de_pagos/JP-544.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "institucion1",
                        "proposito1",
                        "dolares1",
                        "institucion2",
                        "proposito2",
                        "dolares2",
                        "institucion3",
                        "proposito3",
                        "dolares3",
                        "institucion4",
                        "proposito4",
                        "dolares4",
                        "institucion5",
                        "proposito5",
                        "dolares5",
                        "institucion6",
                        "proposito6",
                        "dolares6",
                        "institucion7",
                        "proposito7",
                        "dolares7",
                        "institucion8",
                        "proposito8",
                        "dolares8",
                        "institucion9",
                        "proposito9",
                        "dolares9",
                        "institucion10",
                        "proposito10",
                        "dolares10",
                        "institucion11",
                        "proposito11",
                        "dolares11",
                        "institucion12",
                        "proposito12",
                        "dolares12",
                        "institucion13",
                        "proposito13",
                        "dolares13",
                        "institucion14",
                        "proposito14",
                        "dolares14",
                        "operation_expenses",
                        "salary",
                        "SS_SD_SR_beneficios_marginales",
                        "servicios_profecionales_c",
                        "intereses",
                        "other_gastos",
                        "to_people",
                        "servicios_profecionales_a",
                        "pension",
                        "name_other_1",
                        "quantity_other_1",
                        "name_other_2",
                        "quantity_other_2",
                        "name_other_3",
                        "quantity_other_3",
                        "name_other_4",
                        "quantity_other_4",
                        "agencia",
                        "prep",
                        "titulo",
                        "telefono",
                        "fecha",
                    ]
                )

            writer.writerow(
                [
                    institucion1,
                    proposito1,
                    dolares1,
                    institucion2,
                    proposito2,
                    dolares2,
                    institucion3,
                    proposito3,
                    dolares3,
                    institucion4,
                    proposito4,
                    dolares4,
                    institucion5,
                    proposito5,
                    dolares5,
                    institucion6,
                    proposito6,
                    dolares6,
                    institucion7,
                    proposito7,
                    dolares7,
                    institucion8,
                    proposito8,
                    dolares8,
                    institucion9,
                    proposito9,
                    dolares9,
                    institucion10,
                    proposito10,
                    dolares10,
                    institucion11,
                    proposito11,
                    dolares11,
                    institucion12,
                    proposito12,
                    dolares12,
                    institucion13,
                    proposito13,
                    dolares13,
                    institucion14,
                    proposito14,
                    dolares14,
                    operation_expenses,
                    salary,
                    SS_SD_SR_beneficios_marginales,
                    servicios_profecionales_c,
                    intereses,
                    other_gastos,
                    to_people,
                    servicios_profecionales_a,
                    pension,
                    name_other_1,
                    quantity_other_1,
                    name_other_2,
                    quantity_other_2,
                    name_other_3,
                    quantity_other_3,
                    name_other_4,
                    quantity_other_4,
                    agencia,
                    prep,
                    titulo,
                    telefono,
                    fecha,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/balanza_de_pagos/JP-544.csv",
            dtypes={
                "institucion1": str,
                "proposito1": str,
                "dolares1": float,
                "institucion2": str,
                "proposito2": str,
                "dolares2": float,
                "institucion3": str,
                "proposito3": str,
                "dolares3": float,
                "institucion4": str,
                "proposito4": str,
                "dolares4": float,
                "institucion5": str,
                "proposito5": str,
                "dolares5": float,
                "institucion6": str,
                "proposito6": str,
                "dolares6": float,
                "institucion7": str,
                "proposito7": str,
                "dolares7": float,
                "institucion8": str,
                "proposito8": str,
                "dolares8": float,
                "institucion9": str,
                "proposito9": str,
                "dolares9": float,
                "institucion10": str,
                "proposito10": str,
                "dolares10": float,
                "institucion11": str,
                "proposito11": str,
                "dolares11": float,
                "institucion12": str,
                "proposito12": str,
                "dolares12": float,
                "institucion13": str,
                "proposito13": str,
                "dolares13": float,
                "institucion14": str,
                "proposito14": str,
                "dolares14": float,
                "operation_expenses": float,
                "salary": float,
                "SS_SD_SR_beneficios_marginales": float,
                "servicios_profecionales_c": float,
                "intereses": float,
                "other_gastos": float,
                "to_people": float,
                "servicios_profecionales_a": float,
                "pension": float,
                "name_other_1": str,
                "quantity_other_1": float,
                "name_other_2": str,
                "quantity_other_2": float,
                "name_other_3": str,
                "quantity_other_3": float,
                "name_other_4": str,
                "quantity_other_4": float,
                "agencia": str,
                "prep": str,
                "titulo": str,
                "telefono": str,
                "fecha": str,
            },
            table_name="JP_544",
            table_id="46",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/balanza_de_pagos/JP-544.html")


def JP_544_1(request):
    return render(request, "forms/yearly/balanza_de_pagos/JP-544-1.html")


def IP_520a(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get("company_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")
        legal_form = request.POST.get("legal_form")
        cfc = request.POST.get("cfc")
        start_month = request.POST.get("start_month")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        incomes_services_fee_1 = request.POST.get("incomes_services_fee_1")
        incomes_services_fee_2 = request.POST.get("incomes_services_fee_2")
        incomes_comissions_1 = request.POST.get("incomes_comissions_1")
        incomes_comissions_2 = request.POST.get("incomes_comissions_2")
        incomes_rent_1 = request.POST.get("incomes_rent_1")
        incomes_rent_2 = request.POST.get("incomes_rent_2")
        incomes_interest_1 = request.POST.get("incomes_interest_1")
        incomes_interest_2 = request.POST.get("incomes_interest_2")
        incomes_capital_gain_loss_1 = request.POST.get("incomes_capital_gain_loss_1")
        incomes_capital_gain_loss_2 = request.POST.get("incomes_capital_gain_loss_2")
        incomes_other_operating_1 = request.POST.get("incomes_other_operating_1")
        incomes_other_operating_2 = request.POST.get("incomes_other_operating_2")
        incomes_total_1 = request.POST.get("incomes_total_1")
        incomes_total_2 = request.POST.get("incomes_total_2")
        expenses_1 = request.POST.get("expenses_1")
        expenses_2 = request.POST.get("expenses_2")
        expenses_salaries_wages_bonus_1 = request.POST.get(
            "expenses_salaries_wages_bonus_1"
        )
        expenses_salaries_wages_bonus_2 = request.POST.get(
            "expenses_salaries_wages_bonus_2"
        )
        expenses_commissions_1 = request.POST.get("expenses_commissions_1")
        expenses_commissions_2 = request.POST.get("expenses_commissions_2")
        expenses_interests_1 = request.POST.get("expenses_interests_1")
        expenses_interests_2 = request.POST.get("expenses_interests_2")
        expenses_rent_1 = request.POST.get("expenses_rent_1")
        expenses_rent_2 = request.POST.get("expenses_rent_2")
        expenses_depreciation_1 = request.POST.get("expenses_depreciation_1")
        expenses_depreciation_2 = request.POST.get("expenses_depreciation_2")
        expenses_donation_1 = request.POST.get("expenses_donation_1")
        expenses_donation_2 = request.POST.get("expenses_donation_2")
        expenses_sales_tax_1 = request.POST.get("expenses_sales_tax_1")
        expenses_sales_tax_2 = request.POST.get("expenses_sales_tax_2")
        expenses_machinary_1 = request.POST.get("expenses_machinary_1")
        expenses_machinary_2 = request.POST.get("expenses_machinary_2")
        expenses_other_purchases_1 = request.POST.get("expenses_other_purchases_1")
        expenses_other_purchases_2 = request.POST.get("expenses_other_purchases_2")
        expenses_licenses_1 = request.POST.get("expenses_licenses_1")
        expenses_licenses_2 = request.POST.get("expenses_licenses_2")
        expenses_other_operation_1 = request.POST.get("expenses_other_operation_1")
        expenses_other_operation_2 = request.POST.get("expenses_other_operation_2")
        expenses_total_1 = request.POST.get("expenses_total_1")
        expenses_total_2 = request.POST.get("expenses_total_2")
        net_profit_loss_1 = request.POST.get("net_profit_loss_1")
        net_profit_loss_2 = request.POST.get("net_profit_loss_2")
        sales_tax_withheld_1 = request.POST.get("sales_tax_withheld_1")
        sales_tax_withheld_2 = request.POST.get("sales_tax_withheld_2")
        percent_local_enterprises = request.POST.get("percent_local_enterprises")
        percent_foreign_enterprises = request.POST.get("percent_foreign_enterprises")
        name = request.POST.get("name")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-520a.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "company_name",
                        "address",
                        "email",
                        "liaison_officer",
                        "ssn",
                        "tel",
                        "fax",
                        "legal_form",
                        "cfc",
                        "start_month",
                        "start_year",
                        "end_year",
                        "incomes_services_fee_1",
                        "incomes_services_fee_2",
                        "incomes_comissions_1",
                        "incomes_comissions_2",
                        "incomes_rent_1",
                        "incomes_rent_2",
                        "incomes_interest_1",
                        "incomes_interest_2",
                        "incomes_capital_gain_loss_1",
                        "incomes_capital_gain_loss_2",
                        "incomes_other_operating_1",
                        "incomes_other_operating_2",
                        "incomes_total_1",
                        "incomes_total_2",
                        "expenses_1",
                        "expenses_2",
                        "expenses_salaries_wages_bonus_1",
                        "expenses_salaries_wages_bonus_2",
                        "expenses_commissions_1",
                        "expenses_commissions_2",
                        "expenses_interests_1",
                        "expenses_interests_2",
                        "expenses_rent_1",
                        "expenses_rent_2",
                        "expenses_depreciation_1",
                        "expenses_depreciation_2",
                        "expenses_donation_1",
                        "expenses_donation_2",
                        "expenses_sales_tax_1",
                        "expenses_sales_tax_2",
                        "expenses_machinary_1",
                        "expenses_machinary_2",
                        "expenses_other_purchases_1",
                        "expenses_other_purchases_2",
                        "expenses_licenses_1",
                        "expenses_licenses_2",
                        "expenses_other_operation_1",
                        "expenses_other_operation_2",
                        "expenses_total_1",
                        "expenses_total_2",
                        "net_profit_loss_1",
                        "net_profit_loss_2",
                        "sales_tax_withheld_1",
                        "sales_tax_withheld_2",
                        "percent_local_enterprises",
                        "percent_foreign_enterprises",
                        "name",
                        "rank",
                    ]
                )

            writer.writerow(
                [
                    company_name,
                    address,
                    email,
                    liaison_officer,
                    ssn,
                    tel,
                    fax,
                    legal_form,
                    cfc,
                    start_month,
                    start_year,
                    end_year,
                    incomes_services_fee_1,
                    incomes_services_fee_2,
                    incomes_comissions_1,
                    incomes_comissions_2,
                    incomes_rent_1,
                    incomes_rent_2,
                    incomes_interest_1,
                    incomes_interest_2,
                    incomes_capital_gain_loss_1,
                    incomes_capital_gain_loss_2,
                    incomes_other_operating_1,
                    incomes_other_operating_2,
                    incomes_total_1,
                    incomes_total_2,
                    expenses_1,
                    expenses_2,
                    expenses_salaries_wages_bonus_1,
                    expenses_salaries_wages_bonus_2,
                    expenses_commissions_1,
                    expenses_commissions_2,
                    expenses_interests_1,
                    expenses_interests_2,
                    expenses_rent_1,
                    expenses_rent_2,
                    expenses_depreciation_1,
                    expenses_depreciation_2,
                    expenses_donation_1,
                    expenses_donation_2,
                    expenses_sales_tax_1,
                    expenses_sales_tax_2,
                    expenses_machinary_1,
                    expenses_machinary_2,
                    expenses_other_purchases_1,
                    expenses_other_purchases_2,
                    expenses_licenses_1,
                    expenses_licenses_2,
                    expenses_other_operation_1,
                    expenses_other_operation_2,
                    expenses_total_1,
                    expenses_total_2,
                    net_profit_loss_1,
                    net_profit_loss_2,
                    sales_tax_withheld_1,
                    sales_tax_withheld_2,
                    percent_local_enterprises,
                    percent_foreign_enterprises,
                    name,
                    rank,
                ]
            )
            
        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-520a.csv",
            dtypes={
                "company_name": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "ssn": str,
                "tel": str,
                "fax": str,
                "legal_form": str,
                "cfc": str,
                "start_month": str,
                "start_year": int,
                "end_year": int,
                "incomes_services_fee_1": float,
                "incomes_services_fee_2": float,
                "incomes_comissions_1": float,
                "incomes_comissions_2": float,
                "incomes_rent_1": float,
                "incomes_rent_2": float,
                "incomes_interest_1": float,
                "incomes_interest_2": float,
                "incomes_capital_gain_loss_1": float,
                "incomes_capital_gain_loss_2": float,
                "incomes_other_operating_1": float,
                "incomes_other_operating_2": float,
                "incomes_total_1": float,
                "incomes_total_2": float,
                "expenses_1": float,
                "expenses_2": float,
                "expenses_salaries_wages_bonus_1": float,
                "expenses_salaries_wages_bonus_2": float,
                "expenses_commissions_1": float,
                "expenses_commissions_2": float,
                "expenses_interests_1": float,
                "expenses_interests_2": float,
                "expenses_rent_1": float,
                "expenses_rent_2": float,
                "expenses_depreciation_1": float,
                "expenses_depreciation_2": float,
                "expenses_donation_1": float,
                "expenses_donation_2": float,
                "expenses_sales_tax_1": float,
                "expenses_sales_tax_2": float,
                "expenses_machinary_1": float,
                "expenses_machinary_2": float,
                "expenses_other_purchases_1": float,
                "expenses_other_purchases_2": float,
                "expenses_licenses_1": float,
                "expenses_licenses_2": float,
                "expenses_other_operation_1": float,
                "expenses_other_operation_2": float,
                "expenses_total_1": float,
                "expenses_total_2": float,
                "net_profit_loss_1": float,
                "net_profit_loss_2": float,
                "sales_tax_withheld_1": float,
                "sales_tax_withheld_2": float,
                "percent_local_enterprises": float,
                "percent_foreign_enterprises": float,
                "name": str,
                "rank": str,
            },
            table_name="IP_520a",
            table_id=38,
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-520a.html")


def IP_520s(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get("company_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")
        legal_form = request.POST.get("legal_form")
        cfc = request.POST.get("cfc")
        business_type = request.POST.get("business_type")
        other_business_type = request.POST.get("other_business_type")
        risk_type = request.POST.get("risk_type")
        branches = request.POST.get("branches")
        branches_if_yes = request.POST.get("branches_if_yes")
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        incomes_premium_earned_1 = request.POST.get("incomes_premium_earned_1")
        incomes_premium_earned_2 = request.POST.get("incomes_premium_earned_2")
        incomes_disability_1 = request.POST.get("incomes_disability_1")
        incomes_disability_2 = request.POST.get("incomes_disability_2")
        incomes_life_1 = request.POST.get("incomes_life_1")
        incomes_life_2 = request.POST.get("incomes_life_2")
        incomes_auto_1 = request.POST.get("incomes_auto_1")
        incomes_auto_2 = request.POST.get("incomes_auto_2")
        incomes_other_1 = request.POST.get("incomes_other_1")
        incomes_other_2 = request.POST.get("incomes_other_2")
        incomes_dividend_1 = request.POST.get("incomes_dividend_1")
        incomes_dividend_2 = request.POST.get("incomes_dividend_2")
        incomes_rent_1 = request.POST.get("incomes_rent_1")
        incomes_rent_2 = request.POST.get("incomes_rent_2")
        incomes_commissions_1 = request.POST.get("incomes_commissions_1")
        incomes_commissions_2 = request.POST.get("incomes_commissions_2")
        incomes_interests_1 = request.POST.get("incomes_interests_1")
        incomes_interests_2 = request.POST.get("incomes_interests_2")
        incomes_capital_gain_loss_1 = request.POST.get("incomes_capital_gain_loss_1")
        incomes_capital_gain_loss_2 = request.POST.get("incomes_capital_gain_loss_2")
        incomes_other_operation_1 = request.POST.get("incomes_other_operation_1")
        incomes_other_operation_2 = request.POST.get("incomes_other_operation_2")
        incomes_total_1 = request.POST.get("incomes_total_1")
        incomes_total_2 = request.POST.get("incomes_total_2")
        expenses_1 = request.POST.get("expenses_1")
        expenses_2 = request.POST.get("expenses_2")
        expenses_premium_earned_1 = request.POST.get("expenses_premium_earned_1")
        expenses_premium_earned_2 = request.POST.get("expenses_premium_earned_2")
        expenses_disability_1 = request.POST.get("expenses_disability_1")
        expenses_disability_2 = request.POST.get("expenses_disability_2")
        expenses_life_1 = request.POST.get("expenses_life_1")
        expenses_life_2 = request.POST.get("expenses_life_2")
        expenses_auto_1 = request.POST.get("expenses_auto_1")
        expenses_auto_2 = request.POST.get("expenses_auto_2")
        expenses_other_1 = request.POST.get("expenses_other_1")
        expenses_other_2 = request.POST.get("expenses_other_2")
        expenses_increase_reserves_1 = request.POST.get("expenses_increase_reserves_1")
        expenses_increase_reserves_2 = request.POST.get("expenses_increase_reserves_2")
        expenses_salaries_wages_bonus_1 = request.POST.get(
            "expenses_salaries_wages_bonus_1"
        )
        expenses_salaries_wages_bonus_2 = request.POST.get(
            "expenses_salaries_wages_bonus_2"
        )
        expenses_commissions_1 = request.POST.get("expenses_commissions_1")
        expenses_commissions_2 = request.POST.get("expenses_commissions_2")
        expenses_to_employees_1 = request.POST.get("expenses_to_employees_1")
        expenses_to_employees_2 = request.POST.get("expenses_to_employees_2")
        expenses_independent_agents_1 = request.POST.get(
            "expenses_independent_agents_1"
        )
        expenses_independent_agents_2 = request.POST.get(
            "expenses_independent_agents_2"
        )
        expenses_interest_1 = request.POST.get("expenses_interest_1")
        expenses_interest_2 = request.POST.get("expenses_interest_2")
        expenses_rent_1 = request.POST.get("expenses_rent_1")
        expenses_rent_2 = request.POST.get("expenses_rent_2")
        expenses_depreciation_1 = request.POST.get("expenses_depreciation_1")
        expenses_depreciation_2 = request.POST.get("expenses_depreciation_2")
        expenses_dividend_policy_holder_1 = request.POST.get(
            "expenses_dividend_policy_holder_1"
        )
        expenses_dividend_policy_holder_2 = request.POST.get(
            "expenses_dividend_policy_holder_2"
        )
        expenses_donation_1 = request.POST.get("expenses_donation_1")
        expenses_donation_2 = request.POST.get("expenses_donation_2")
        expenses_sales_tax_1 = request.POST.get("expenses_sales_tax_1")
        expenses_sales_tax_2 = request.POST.get("expenses_sales_tax_2")
        expenses_machinary_1 = request.POST.get("expenses_machinary_1")
        expenses_machinary_2 = request.POST.get("expenses_machinary_2")
        expenses_other_purchases_1 = request.POST.get("expenses_other_purchases_1")
        expenses_other_purchases_2 = request.POST.get("expenses_other_purchases_2")
        expenses_licenses_1 = request.POST.get("expenses_licenses_1")
        expenses_licenses_2 = request.POST.get("expenses_licenses_2")
        expenses_other_operating_1 = request.POST.get("expenses_other_operating_1")
        expenses_other_operating_2 = request.POST.get("expenses_other_operating_2")
        expenses_total_1 = request.POST.get("expenses_total_1")
        expenses_total_2 = request.POST.get("expenses_total_2")
        gross_profit_1 = request.POST.get("gross_profit_1")
        gross_profit_2 = request.POST.get("gross_profit_2")
        sales_tax_withheld_1 = request.POST.get("sales_tax_withheld_1")
        sales_tax_withheld_2 = request.POST.get("sales_tax_withheld_2")
        name = request.POST.get("name")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-520s.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "company_name",
                        "address",
                        "email",
                        "liaison_officer",
                        "ssn",
                        "tel",
                        "fax",
                        "legal_form",
                        "cfc",
                        "business_type",
                        "other_business_type",
                        "risk_type",
                        "branches",
                        "branches_if_yes",
                        "closing_date",
                        "start_year",
                        "end_year",
                        "incomes_premium_earned_1",
                        "incomes_premium_earned_2",
                        "incomes_disability_1",
                        "incomes_disability_2",
                        "incomes_life_1",
                        "incomes_life_2",
                        "incomes_auto_1",
                        "incomes_auto_2",
                        "incomes_other_1",
                        "incomes_other_2",
                        "incomes_dividend_1",
                        "incomes_dividend_2",
                        "incomes_rent_1",
                        "incomes_rent_2",
                        "incomes_commissions_1",
                        "incomes_commissions_2",
                        "incomes_interests_1",
                        "incomes_interests_2",
                        "incomes_capital_gain_loss_1",
                        "incomes_capital_gain_loss_2",
                        "incomes_other_operation_1",
                        "incomes_other_operation_2",
                        "incomes_total_1",
                        "incomes_total_2",
                        "expenses_1",
                        "expenses_2",
                        "expenses_premium_earned_1",
                        "expenses_premium_earned_2",
                        "expenses_disability_1",
                        "expenses_disability_2",
                        "expenses_life_1",
                        "expenses_life_2",
                        "expenses_auto_1",
                        "expenses_auto_2",
                        "expenses_other_1",
                        "expenses_other_2",
                        "expenses_increase_reserves_1",
                        "expenses_increase_reserves_2",
                        "expenses_salaries_wages_bonus_1",
                        "expenses_salaries_wages_bonus_2",
                        "expenses_commissions_1",
                        "expenses_commissions_2",
                        "expenses_to_employees_1",
                        "expenses_to_employees_2",
                        "expenses_independent_agents_1",
                        "expenses_independent_agents_2",
                        "expenses_interest_1",
                        "expenses_interest_2",
                        "expenses_rent_1",
                        "expenses_rent_2",
                        "expenses_depreciation_1",
                        "expenses_depreciation_2",
                        "expenses_dividend_policy_holder_1",
                        "expenses_dividend_policy_holder_2",
                        "expenses_donation_1",
                        "expenses_donation_2",
                        "expenses_sales_tax_1",
                        "expenses_sales_tax_2",
                        "expenses_machinary_1",
                        "expenses_machinary_2",
                        "expenses_other_purchases_1",
                        "expenses_other_purchases_2",
                        "expenses_licenses_1",
                        "expenses_licenses_2",
                        "expenses_other_operating_1",
                        "expenses_other_operating_2",
                        "expenses_total_1",
                        "expenses_total_2",
                        "gross_profit_1",
                        "gross_profit_2",
                        "sales_tax_withheld_1",
                        "sales_tax_withheld_2",
                        "name",
                        "rank",
                    ]
                )

            writer.writerow(
                [
                    company_name,
                    address,
                    email,
                    liaison_officer,
                    ssn,
                    tel,
                    fax,
                    legal_form,
                    cfc,
                    business_type,
                    other_business_type,
                    risk_type,
                    branches,
                    branches_if_yes,
                    closing_date,
                    start_year,
                    end_year,
                    incomes_premium_earned_1,
                    incomes_premium_earned_2,
                    incomes_disability_1,
                    incomes_disability_2,
                    incomes_life_1,
                    incomes_life_2,
                    incomes_auto_1,
                    incomes_auto_2,
                    incomes_other_1,
                    incomes_other_2,
                    incomes_dividend_1,
                    incomes_dividend_2,
                    incomes_rent_1,
                    incomes_rent_2,
                    incomes_commissions_1,
                    incomes_commissions_2,
                    incomes_interests_1,
                    incomes_interests_2,
                    incomes_capital_gain_loss_1,
                    incomes_capital_gain_loss_2,
                    incomes_other_operation_1,
                    incomes_other_operation_2,
                    incomes_total_1,
                    incomes_total_2,
                    expenses_1,
                    expenses_2,
                    expenses_premium_earned_1,
                    expenses_premium_earned_2,
                    expenses_disability_1,
                    expenses_disability_2,
                    expenses_life_1,
                    expenses_life_2,
                    expenses_auto_1,
                    expenses_auto_2,
                    expenses_other_1,
                    expenses_other_2,
                    expenses_increase_reserves_1,
                    expenses_increase_reserves_2,
                    expenses_salaries_wages_bonus_1,
                    expenses_salaries_wages_bonus_2,
                    expenses_commissions_1,
                    expenses_commissions_2,
                    expenses_to_employees_1,
                    expenses_to_employees_2,
                    expenses_independent_agents_1,
                    expenses_independent_agents_2,
                    expenses_interest_1,
                    expenses_interest_2,
                    expenses_rent_1,
                    expenses_rent_2,
                    expenses_depreciation_1,
                    expenses_depreciation_2,
                    expenses_dividend_policy_holder_1,
                    expenses_dividend_policy_holder_2,
                    expenses_donation_1,
                    expenses_donation_2,
                    expenses_sales_tax_1,
                    expenses_sales_tax_2,
                    expenses_machinary_1,
                    expenses_machinary_2,
                    expenses_other_purchases_1,
                    expenses_other_purchases_2,
                    expenses_licenses_1,
                    expenses_licenses_2,
                    expenses_other_operating_1,
                    expenses_other_operating_2,
                    expenses_total_1,
                    expenses_total_2,
                    gross_profit_1,
                    gross_profit_2,
                    sales_tax_withheld_1,
                    sales_tax_withheld_2,
                    name,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-520s.csv",
            dtypes={
                "company_name": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "ssn": str,
                "tel": str,
                "fax": str,
                "legal_form": str,
                "cfc": str,
                "business_type": str,
                "other_business_type": str,
                "risk_type": str,
                "branches": str,
                "branches_if_yes": str,
                "closing_date": str,
                "start_year": int,
                "end_year": int,
                "incomes_premium_earned_1": float,
                "incomes_premium_earned_2": float,
                "incomes_disability_1": float,
                "incomes_disability_2": float,
                "incomes_life_1": float,
                "incomes_life_2": float,
                "incomes_auto_1": float,
                "incomes_auto_2": float,
                "incomes_other_1": float,
                "incomes_other_2": float,
                "incomes_dividend_1": float,
                "incomes_dividend_2": float,
                "incomes_rent_1": float,
                "incomes_rent_2": float,
                "incomes_commissions_1": float,
                "incomes_commissions_2": float,
                "incomes_interests_1": float,
                "incomes_interests_2": float,
                "incomes_capital_gain_loss_1": float,
                "incomes_capital_gain_loss_2": float,
                "incomes_other_operation_1": float,
                "incomes_other_operation_2": float,
                "incomes_total_1": float,
                "incomes_total_2": float,
                "expenses_1": float,
                "expenses_2": float,
                "expenses_premium_earned_1": float,
                "expenses_premium_earned_2": float,
                "expenses_disability_1": float,
                "expenses_disability_2": float,
                "expenses_life_1": float,
                "expenses_life_2": float,
                "expenses_auto_1": float,
                "expenses_auto_2": float,
                "expenses_other_1": float,
                "expenses_other_2": float,
                "expenses_increase_reserves_1": float,
                "expenses_increase_reserves_2": float,
                "expenses_salaries_wages_bonus_1": float,
                "expenses_salaries_wages_bonus_2": float,
                "expenses_commissions_1": float,
                "expenses_commissions_2": float,
                "expenses_to_employees_1": float,
                "expenses_to_employees_2": float,
                "expenses_independent_agents_1": float,
                "expenses_independent_agents_2": float,
                "expenses_interest_1": float,
                "expenses_interest_2": float,
                "expenses_rent_1": float,
                "expenses_rent_2": float,
                "expenses_depreciation_1": float,
                "expenses_depreciation_2": float,
                "expenses_dividend_policy_holder_1": float,
                "expenses_dividend_policy_holder_2": float,
                "expenses_donation_1": float,
                "expenses_donation_2": float,
                "expenses_sales_tax_1": float,
                "expenses_sales_tax_2": float,
                "expenses_machinary_1": float,
                "expenses_machinary_2": float,
                "expenses_other_purchases_1": float,
                "expenses_other_purchases_2": float,
                "expenses_licenses_1": float,
                "expenses_licenses_2": float,
                "expenses_other_operating_1": float,
                "expenses_other_operating_2": float,
                "expenses_total_1": float,
                "expenses_total_2": float,
                "gross_profit_1": float,
                "gross_profit_2": float,
                "sales_tax_withheld_1": float,
                "sales_tax_withheld_2": float,
                "name": str,
                "rank": str,
            },
            table_name="IP_520s",
            table_id="39",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-520s.html")


def IP_530(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get("company_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")

        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")

        legal_form = request.POST.get("legal_form")
        cfc = request.POST.get("cfc")
        business_type = request.POST.get("business_type")
        other_business_type = request.POST.get("other_business_type")
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")

        incomes_from_persons_1 = request.POST.get("incomes_from_persons_1")
        incomes_from_persons_2 = request.POST.get("incomes_from_persons_2")
        incomes_industries_businesses_1 = request.POST.get(
            "incomes_industries_businesses_1"
        )
        incomes_industries_businesses_2 = request.POST.get(
            "incomes_industries_businesses_2"
        )
        incomes_rent_1 = request.POST.get("incomes_rent_1")
        incomes_rent_2 = request.POST.get("incomes_rent_2")
        incomes_interests_1 = request.POST.get("incomes_interests_1")
        incomes_interests_2 = request.POST.get("incomes_interests_2")
        incomes_comissions_1 = request.POST.get("incomes_comissions_1")
        incomes_comissions_2 = request.POST.get("incomes_comissions_2")
        incomes_gain_loss_1 = request.POST.get("incomes_gain_loss_1")
        incomes_gain_loss_2 = request.POST.get("incomes_gain_loss_2")
        incomes_operating_1 = request.POST.get("incomes_operating_1")
        incomes_operating_2 = request.POST.get("incomes_operating_2")
        expenses_salaries_wages_bonus_1 = request.POST.get(
            "expenses_salaries_wages_bonus_1"
        )
        expenses_salaries_wages_bonus_2 = request.POST.get(
            "expenses_salaries_wages_bonus_2"
        )
        expenses_interests_1 = request.POST.get("expenses_interests_1")
        expenses_interests_2 = request.POST.get("expenses_interests_2")
        expenses_rent_1 = request.POST.get("expenses_rent_1")
        expenses_rent_2 = request.POST.get("expenses_rent_2")
        expenses_depreciation_1 = request.POST.get("expenses_depreciation_1")
        expenses_depreciation_2 = request.POST.get("expenses_depreciation_2")
        expenses_donations_1 = request.POST.get("expenses_donations_1")
        expenses_donations_2 = request.POST.get("expenses_donations_2")
        expenses_sales_tax_1 = request.POST.get("expenses_sales_tax_1")
        expenses_sales_tax_2 = request.POST.get("expenses_sales_tax_2")
        expenses_machinary_equipment_1 = request.POST.get(
            "expenses_machinary_equipment_1"
        )
        expenses_machinary_equipment_2 = request.POST.get(
            "expenses_machinary_equipment_2"
        )
        expenses_other_purchases_1 = request.POST.get("expenses_other_purchases_1")
        expenses_other_purchases_2 = request.POST.get("expenses_other_purchases_2")
        expenses_licenses_1 = request.POST.get("expenses_licenses_1")
        expenses_licenses_2 = request.POST.get("expenses_licenses_2")
        expenses_other_operations_1 = request.POST.get("expenses_other_operations_1")
        expenses_other_operations_2 = request.POST.get("expenses_other_operations_2")
        expenses_total_1 = request.POST.get("expenses_total_1")
        expenses_total_2 = request.POST.get("expenses_total_2")
        gross_profit_1 = request.POST.get("gross_profit_1")
        gross_profit_2 = request.POST.get("gross_profit_2")
        profit_income_tax_1 = request.POST.get("profit_income_tax_1")
        profit_income_tax_2 = request.POST.get("profit_income_tax_2")
        profit_after_income_tax_1 = request.POST.get("profit_after_income_tax_1")
        profit_after_income_tax_2 = request.POST.get("profit_after_income_tax_2")
        sales_tax_withheld_1 = request.POST.get("sales_tax_withheld_1")
        sales_tax_withheld_2 = request.POST.get("sales_tax_withheld_2")

        name = request.POST.get("name")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-530.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "company_name",
                        "address",
                        "email",
                        "liaison_officer",
                        "ssn",
                        "tel",
                        "fax",
                        "legal_form",
                        "cfc",
                        "business_type",
                        "other_business_type",
                        "closing_date",
                        "start_year",
                        "end_year",
                        "incomes_from_persons_1",
                        "incomes_from_persons_2",
                        "incomes_industries_businesses_1",
                        "incomes_industries_businesses_2",
                        "incomes_rent_1",
                        "incomes_rent_2",
                        "incomes_interests_1",
                        "incomes_interests_2",
                        "incomes_comissions_1",
                        "incomes_comissions_2",
                        "incomes_gain_loss_1",
                        "incomes_gain_loss_2",
                        "incomes_operating_1",
                        "incomes_operating_2",
                        "expenses_salaries_wages_bonus_1",
                        "expenses_salaries_wages_bonus_2",
                        "expenses_interests_1",
                        "expenses_interests_2",
                        "expenses_rent_1",
                        "expenses_rent_2",
                        "expenses_depreciation_1",
                        "expenses_depreciation_2",
                        "expenses_donations_1",
                        "expenses_donations_2",
                        "expenses_sales_tax_1",
                        "expenses_sales_tax_2",
                        "expenses_machinary_equipment_1",
                        "expenses_machinary_equipment_2",
                        "expenses_other_purchases_1",
                        "expenses_other_purchases_2",
                        "expenses_licenses_1",
                        "expenses_licenses_2",
                        "expenses_other_operations_1",
                        "expenses_other_operations_2",
                        "expenses_total_1",
                        "expenses_total_2",
                        "gross_profit_1",
                        "gross_profit_2",
                        "profit_income_tax_1",
                        "profit_income_tax_2",
                        "profit_after_income_tax_1",
                        "profit_after_income_tax_2",
                        "sales_tax_withheld_1",
                        "sales_tax_withheld_2",
                        "name",
                        "rank",
                    ]
                )

            writer.writerow(
                [
                    company_name,
                    address,
                    email,
                    liaison_officer,
                    ssn,
                    tel,
                    fax,
                    legal_form,
                    cfc,
                    business_type,
                    other_business_type,
                    closing_date,
                    start_year,
                    end_year,
                    incomes_from_persons_1,
                    incomes_from_persons_2,
                    incomes_industries_businesses_1,
                    incomes_industries_businesses_2,
                    incomes_rent_1,
                    incomes_rent_2,
                    incomes_interests_1,
                    incomes_interests_2,
                    incomes_comissions_1,
                    incomes_comissions_2,
                    incomes_gain_loss_1,
                    incomes_gain_loss_2,
                    incomes_operating_1,
                    incomes_operating_2,
                    expenses_salaries_wages_bonus_1,
                    expenses_salaries_wages_bonus_2,
                    expenses_interests_1,
                    expenses_interests_2,
                    expenses_rent_1,
                    expenses_rent_2,
                    expenses_depreciation_1,
                    expenses_depreciation_2,
                    expenses_donations_1,
                    expenses_donations_2,
                    expenses_sales_tax_1,
                    expenses_sales_tax_2,
                    expenses_machinary_equipment_1,
                    expenses_machinary_equipment_2,
                    expenses_other_purchases_1,
                    expenses_other_purchases_2,
                    expenses_licenses_1,
                    expenses_licenses_2,
                    expenses_other_operations_1,
                    expenses_other_operations_2,
                    expenses_total_1,
                    expenses_total_2,
                    gross_profit_1,
                    gross_profit_2,
                    profit_income_tax_1,
                    profit_income_tax_2,
                    profit_after_income_tax_1,
                    profit_after_income_tax_2,
                    sales_tax_withheld_1,
                    sales_tax_withheld_2,
                    name,
                    rank,
                ]
            )
        
        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-530.csv",
            dtypes={
                "company_name": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "ssn": str,
                "tel": str,
                "fax": str,
                "legal_form": str,
                "cfc": str,
                "business_type": str,
                "other_business_type": str,
                "closing_date": str,
                "start_year": int,
                "end_year": int,
                "incomes_from_persons_1": float,
                "incomes_from_persons_2": float,
                "incomes_industries_businesses_1": float,
                "incomes_industries_businesses_2": float,
                "incomes_rent_1": float,
                "incomes_rent_2": float,
                "incomes_interests_1": float,
                "incomes_interests_2": float,
                "incomes_comissions_1": float,
                "incomes_comissions_2": float,
                "incomes_gain_loss_1": float,
                "incomes_gain_loss_2": float,
                "incomes_operating_1": float,
                "incomes_operating_2": float,
                "expenses_salaries_wages_bonus_1": float,
                "expenses_salaries_wages_bonus_2": float,
                "expenses_interests_1": float,
                "expenses_interests_2": float,
                "expenses_rent_1": float,
                "expenses_rent_2": float,
                "expenses_depreciation_1": float,
                "expenses_depreciation_2": float,
                "expenses_donations_1": float,
                "expenses_donations_2": float,
                "expenses_sales_tax_1": float,
                "expenses_sales_tax_2": float,
                "expenses_machinary_equipment_1": float,
                "expenses_machinary_equipment_2": float,
                "expenses_other_purchases_1": float,
                "expenses_other_purchases_2": float,
                "expenses_licenses_1": float,
                "expenses_licenses_2": float,
                "expenses_other_operations_1": float,
                "expenses_other_operations_2": float,
                "expenses_total_1": float,
                "expenses_total_2": float,
                "gross_profit_1": float,
                "gross_profit_2": float,
                "profit_income_tax_1": float,
                "profit_income_tax_2": float,
                "profit_after_income_tax_1": float,
                "profit_after_income_tax_2": float,
                "sales_tax_withheld_1": float,
                "sales_tax_withheld_2": float,
                "name": str,
                "rank": str,
            },
            table_name="IP_530",
            table_id=40,
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-530.html")


def IP_540(request):

    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get("company_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")
        legal_form = request.POST.get("legal_form")
        cfc = request.POST.get("cfc")
        business_type = request.POST.get("business_type")
        business_function = request.POST.get("business_function")
        branches = request.POST.get("branches")
        branches_yes = request.POST.get("branches_yes")
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        incomes_services_rendered_1 = request.POST.get("incomes_services_rendered_1")
        incomes_services_rendered_2 = request.POST.get("incomes_services_rendered_2")
        incomes_from_persons_1 = request.POST.get("incomes_from_persons_1")
        incomes_from_persons_2 = request.POST.get("incomes_from_persons_2")
        incomes_from_industries_and_businesses_1 = request.POST.get(
            "incomes_from_industries_and_businesses_1"
        )
        incomes_from_industries_and_businesses_2 = request.POST.get(
            "incomes_from_industries_and_businesses_2"
        )
        incomes_sale_merchandise_1 = request.POST.get("incomes_sale_merchandise_1")
        incomes_sale_merchandise_2 = request.POST.get("incomes_sale_merchandise_2")
        incomes_rent_machinery_and_equipment_1 = request.POST.get(
            "incomes_rent_machinery_and_equipment_1"
        )
        incomes_rent_machinery_and_equipment_2 = request.POST.get(
            "incomes_rent_machinery_and_equipment_2"
        )
        incomes_rent_land_and_building_1 = request.POST.get(
            "incomes_rent_land_and_building_1"
        )
        incomes_rent_land_and_building_2 = request.POST.get(
            "incomes_rent_land_and_building_2"
        )
        incomes_interests_1 = request.POST.get("incomes_interests_1")
        incomes_interests_2 = request.POST.get("incomes_interests_2")
        incomes_capital_gain_or_loss_1 = request.POST.get(
            "incomes_capital_gain_or_loss_1"
        )
        incomes_capital_gain_or_loss_2 = request.POST.get(
            "incomes_capital_gain_or_loss_2"
        )
        incomes_other_operating_income_1 = request.POST.get(
            "incomes_other_operating_income_1"
        )
        incomes_other_operating_income_2 = request.POST.get(
            "incomes_other_operating_income_2"
        )
        expenses_salaries_wages_bonus_1 = request.POST.get(
            "expenses_salaries_wages_bonus_1"
        )
        expenses_salaries_wages_bonus_2 = request.POST.get(
            "expenses_salaries_wages_bonus_2"
        )
        expenses_interests_1 = request.POST.get("expenses_interests_1")
        expenses_interests_2 = request.POST.get("expenses_interests_2")
        expenses_rent_1 = request.POST.get("expenses_rent_1")
        expenses_rent_2 = request.POST.get("expenses_rent_2")
        expenses_depreciation_1 = request.POST.get("expenses_depreciation_1")
        expenses_depreciation_2 = request.POST.get("expenses_depreciation_2")
        expenses_bad_debts_1 = request.POST.get("expenses_bad_debts_1")
        expenses_bad_debts_2 = request.POST.get("expenses_bad_debts_2")
        expenses_donations_1 = request.POST.get("expenses_donations_1")
        expenses_donations_2 = request.POST.get("expenses_donations_2")
        expenses_other_donations_1 = request.POST.get("expenses_other_donations_1")
        expenses_other_donations_2 = request.POST.get("expenses_other_donations_2")
        expenses_sales_taxes_1 = request.POST.get("expenses_sales_taxes_1")
        expenses_sales_taxes_2 = request.POST.get("expenses_sales_taxes_2")
        expenses_purchases_machinery_1 = request.POST.get(
            "expenses_purchases_machinery_1"
        )
        expenses_purchases_machinery_2 = request.POST.get(
            "expenses_purchases_machinery_2"
        )
        expenses_other_purchases_1 = request.POST.get("expenses_other_purchases_1")
        expenses_other_purchases_2 = request.POST.get("expenses_other_purchases_2")
        expenses_licenses_1 = request.POST.get("expenses_licenses_1")
        expenses_licenses_2 = request.POST.get("expenses_licenses_2")
        net_profit_1 = request.POST.get("net_profit_1")
        net_profit_2 = request.POST.get("net_profit_2")
        profit_income_tax_1 = request.POST.get("profit_income_tax_1")
        profit_income_tax_2 = request.POST.get("profit_income_tax_2")
        profit_after_income_tax_1 = request.POST.get("profit_after_income_tax_1")
        profit_after_income_tax_2 = request.POST.get("profit_after_income_tax_2")
        sales_tax_withheld_1 = request.POST.get("sales_tax_withheld_1")
        sales_tax_withheld_2 = request.POST.get("sales_tax_withheld_2")
        name = request.POST.get("name")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-540.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "company_name",
                        "address",
                        "email",
                        "liaison_officer",
                        "ssn",
                        "tel",
                        "fax",
                        "legal_form",
                        "cfc",
                        "business_type",
                        "business_function",
                        "branches",
                        "branches_yes",
                        "closing_date",
                        "start_year",
                        "end_year",
                        "incomes_services_rendered_1",
                        "incomes_services_rendered_2",
                        "incomes_from_persons_1",
                        "incomes_from_persons_2",
                        "incomes_from_industries_and_businesses_1",
                        "incomes_from_industries_and_businesses_2",
                        "incomes_sale_merchandise_1",
                        "incomes_sale_merchandise_2",
                        "incomes_rent_machinery_and_equipment_1",
                        "incomes_rent_machinery_and_equipment_2",
                        "incomes_rent_land_and_building_1",
                        "incomes_rent_land_and_building_2",
                        "incomes_interests_1",
                        "incomes_interests_2",
                        "incomes_capital_gain_or_loss_1",
                        "incomes_capital_gain_or_loss_2",
                        "incomes_other_operating_income_1",
                        "incomes_other_operating_income_2",
                        "expenses_salaries_wages_bonus_1",
                        "expenses_salaries_wages_bonus_2",
                        "expenses_interests_1",
                        "expenses_interests_2",
                        "expenses_rent_1",
                        "expenses_rent_2",
                        "expenses_depreciation_1",
                        "expenses_depreciation_2",
                        "expenses_bad_debts_1",
                        "expenses_bad_debts_2",
                        "expenses_donations_1",
                        "expenses_donations_2",
                        "expenses_other_donations_1",
                        "expenses_other_donations_2",
                        "expenses_sales_taxes_1",
                        "expenses_sales_taxes_2",
                        "expenses_purchases_machinery_1",
                        "expenses_purchases_machinery_2",
                        "expenses_other_purchases_1",
                        "expenses_other_purchases_2",
                        "expenses_licenses_1",
                        "expenses_licenses_2",
                        "net_profit_1",
                        "net_profit_2",
                        "profit_income_tax_1",
                        "profit_income_tax_2",
                        "profit_after_income_tax_1",
                        "profit_after_income_tax_2",
                        "sales_tax_withheld_1",
                        "sales_tax_withheld_2",
                        "name",
                        "rank",
                    ]
                )

            writer.writerow(
                [
                    company_name,
                    address,
                    email,
                    liaison_officer,
                    ssn,
                    tel,
                    fax,
                    legal_form,
                    cfc,
                    business_type,
                    business_function,
                    branches,
                    branches_yes,
                    closing_date,
                    start_year,
                    end_year,
                    incomes_services_rendered_1,
                    incomes_services_rendered_2,
                    incomes_from_persons_1,
                    incomes_from_persons_2,
                    incomes_from_industries_and_businesses_1,
                    incomes_from_industries_and_businesses_2,
                    incomes_sale_merchandise_1,
                    incomes_sale_merchandise_2,
                    incomes_rent_machinery_and_equipment_1,
                    incomes_rent_machinery_and_equipment_2,
                    incomes_rent_land_and_building_1,
                    incomes_rent_land_and_building_2,
                    incomes_interests_1,
                    incomes_interests_2,
                    incomes_capital_gain_or_loss_1,
                    incomes_capital_gain_or_loss_2,
                    incomes_other_operating_income_1,
                    incomes_other_operating_income_2,
                    expenses_salaries_wages_bonus_1,
                    expenses_salaries_wages_bonus_2,
                    expenses_interests_1,
                    expenses_interests_2,
                    expenses_rent_1,
                    expenses_rent_2,
                    expenses_depreciation_1,
                    expenses_depreciation_2,
                    expenses_bad_debts_1,
                    expenses_bad_debts_2,
                    expenses_donations_1,
                    expenses_donations_2,
                    expenses_other_donations_1,
                    expenses_other_donations_2,
                    expenses_sales_taxes_1,
                    expenses_sales_taxes_2,
                    expenses_purchases_machinery_1,
                    expenses_purchases_machinery_2,
                    expenses_other_purchases_1,
                    expenses_other_purchases_2,
                    expenses_licenses_1,
                    expenses_licenses_2,
                    net_profit_1,
                    net_profit_2,
                    profit_income_tax_1,
                    profit_income_tax_2,
                    profit_after_income_tax_1,
                    profit_after_income_tax_2,
                    sales_tax_withheld_1,
                    sales_tax_withheld_2,
                    name,
                    rank,
                ]
            )
        
        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-540.csv",
            dtypes={
                "company_name": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "ssn": str,
                "tel": str,
                "fax": str,
                "legal_form": str,
                "cfc": str,
                "business_type": str,
                "business_function": str,
                "branches": str,
                "branches_yes": str,
                "closing_date": str,
                "start_year": int,
                "end_year": int,
                "incomes_services_rendered_1": float,
                "incomes_services_rendered_2": float,
                "incomes_from_persons_1": float,
                "incomes_from_persons_2": float,
                "incomes_from_industries_and_businesses_1": float,
                "incomes_from_industries_and_businesses_2": float,
                "incomes_sale_merchandise_1": float,
                "incomes_sale_merchandise_2": float,
                "incomes_rent_machinery_and_equipment_1": float,
                "incomes_rent_machinery_and_equipment_2": float,
                "incomes_rent_land_and_building_1": float,
                "incomes_rent_land_and_building_2": float,
                "incomes_interests_1": float,
                "incomes_interests_2": float,
                "incomes_capital_gain_or_loss_1": float,
                "incomes_capital_gain_or_loss_2": float,
                "incomes_other_operating_income_1": float,
                "incomes_other_operating_income_2": float,
                "expenses_salaries_wages_bonus_1": float,
                "expenses_salaries_wages_bonus_2": float,
                "expenses_interests_1": float,
                "expenses_interests_2": float,
                "expenses_rent_1": float,
                "expenses_rent_2": float,
                "expenses_depreciation_1": float,
                "expenses_depreciation_2": float,
                "expenses_bad_debts_1": float,
                "expenses_bad_debts_2": float,
                "expenses_donations_1": float,
                "expenses_donations_2": float,
                "expenses_other_donations_1": float,
                "expenses_other_donations_2": float,
                "expenses_sales_taxes_1": float,
                "expenses_sales_taxes_2": float,
                "expenses_purchases_machinery_1": float,
                "expenses_purchases_machinery_2": float,
                "expenses_other_purchases_1": float,
                "expenses_other_purchases_2": float,
                "expenses_licenses_1": float,
                "expenses_licenses_2": float,
                "net_profit_1": float,
                "net_profit_2": float,
                "profit_income_tax_1": float,
                "profit_income_tax_2": float,
                "profit_after_income_tax_1": float,
                "profit_after_income_tax_2": float,
                "sales_tax_withheld_1": float,
                "sales_tax_withheld_2": float,
                "name": str,
                "rank": str,
            },
            table_name="IP_540",
            table_id=41,
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-540.html")


def IP_540J(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get("company_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")

        legal_form = request.POST.get("legal_form")
        cfc = request.POST.get("cfc")
        business_type = request.POST.get("business_type")
        business_function = request.POST.get("business_function")
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")

        incomes_from_persons_1 = request.POST.get("incomes_from_persons_1")
        incomes_from_persons_2 = request.POST.get("incomes_from_persons_2")
        incomes_industries_business_1 = request.POST.get(
            "incomes_industries_business_1"
        )
        incomes_industries_business_2 = request.POST.get(
            "incomes_industries_business_2"
        )
        expenses_newspapers_1 = request.POST.get("expenses_newspapers_1")
        expenses_newspapers_2 = request.POST.get("expenses_newspapers_2")
        expenses_radio_television_1 = request.POST.get("expenses_radio_television_1")
        expenses_radio_television_2 = request.POST.get("expenses_radio_television_2")
        expenses_other_1 = request.POST.get("expenses_other_1")
        expenses_other_2 = request.POST.get("expenses_other_2")
        gross_profit_1 = request.POST.get("gross_profit_1")
        gross_profit_2 = request.POST.get("gross_profit_2")
        dividends_paid_1 = request.POST.get("dividends_paid_1")
        dividends_paid_2 = request.POST.get("dividends_paid_2")
        expenses_interests_1 = request.POST.get("expenses_interests_1")
        expenses_interests_2 = request.POST.get("expenses_interests_2")
        expenses_rent_1 = request.POST.get("expenses_rent_1")
        expenses_rent_2 = request.POST.get("expenses_rent_2")
        expenses_gain_loss_1 = request.POST.get("expenses_gain_loss_1")
        expenses_gain_loss_2 = request.POST.get("expenses_gain_loss_2")
        dividends_paid_other_1 = request.POST.get("dividends_paid_other_1")
        dividends_paid_other_2 = request.POST.get("dividends_paid_other_2")
        incomes_total_1 = request.POST.get("incomes_total_1")
        incomes_total_2 = request.POST.get("incomes_total_2")
        expenses_total_1 = request.POST.get("expenses_total_1")
        expenses_total_2 = request.POST.get("expenses_total_2")
        salaries_wages_bonus_1 = request.POST.get("salaries_wages_bonus_1")
        salaries_wages_bonus_2 = request.POST.get("salaries_wages_bonus_2")
        interests_1 = request.POST.get("interests_1")
        interests_2 = request.POST.get("interests_2")
        rents_1 = request.POST.get("rents_1")
        rents_2 = request.POST.get("rents_2")
        depreciation_1 = request.POST.get("depreciation_1")
        depreciation_2 = request.POST.get("depreciation_2")
        other_taxes_1 = request.POST.get("other_taxes_1")
        other_taxes_2 = request.POST.get("other_taxes_2")
        donations_1 = request.POST.get("donations_1")
        donations_2 = request.POST.get("donations_2")
        sales_tax_1 = request.POST.get("sales_tax_1")
        sales_tax_2 = request.POST.get("sales_tax_2")
        machinery_1 = request.POST.get("machinery_1")
        machinery_2 = request.POST.get("machinery_2")
        other_purchases_1 = request.POST.get("other_purchases_1")
        other_purchases_2 = request.POST.get("other_purchases_2")
        licenses_1 = request.POST.get("licenses_1")
        licenses_2 = request.POST.get("licenses_2")
        other_operating_expenses_1 = request.POST.get("other_operating_expenses_1")
        other_operating_expenses_2 = request.POST.get("other_operating_expenses_2")
        profit_incomes_tax_1 = request.POST.get("profit_incomes_tax_1")
        profit_incomes_tax_2 = request.POST.get("profit_incomes_tax_2")
        profit_incomes_mortage_loans_1 = request.POST.get(
            "profit_incomes_mortage_loans_1"
        )
        profit_incomes_mortage_loans_2 = request.POST.get(
            "profit_incomes_mortage_loans_2"
        )
        sales_tax_withheld_1 = request.POST.get("sales_tax_withheld_1")
        sales_tax_withheld_2 = request.POST.get("sales_tax_withheld_2")

        name = request.POST.get("name")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-540J.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "company_name",
                        "address",
                        "email",
                        "liaison_officer",
                        "ssn",
                        "tel",
                        "fax",
                        "legal_form",
                        "cfc",
                        "business_type",
                        "business_function",
                        "closing_date",
                        "start_year",
                        "end_year",
                        "incomes_from_persons_1",
                        "incomes_from_persons_2",
                        "incomes_industries_business_1",
                        "incomes_industries_business_2",
                        "expenses_newspapers_1",
                        "expenses_newspapers_2",
                        "expenses_radio_television_1",
                        "expenses_radio_television_2",
                        "expenses_other_1",
                        "expenses_other_2",
                        "gross_profit_1",
                        "gross_profit_2",
                        "dividends_paid_1",
                        "dividends_paid_2",
                        "expenses_interests_1",
                        "expenses_interests_2",
                        "expenses_rent_1",
                        "expenses_rent_2",
                        "expenses_gain_loss_1",
                        "expenses_gain_loss_2",
                        "dividends_paid_other_1",
                        "dividends_paid_other_2",
                        "incomes_total_1",
                        "incomes_total_2",
                        "expenses_total_1",
                        "expenses_total_2",
                        "salaries_wages_bonus_1",
                        "salaries_wages_bonus_2",
                        "interests_1",
                        "interests_2",
                        "rents_1",
                        "rents_2",
                        "depreciation_1",
                        "depreciation_2",
                        "other_taxes_1",
                        "other_taxes_2",
                        "donations_1",
                        "donations_2",
                        "sales_tax_1",
                        "sales_tax_2",
                        "machinery_1",
                        "machinery_2",
                        "other_purchases_1",
                        "other_purchases_2",
                        "licenses_1",
                        "licenses_2",
                        "other_operating_expenses_1",
                        "other_operating_expenses_2",
                        "profit_incomes_tax_1",
                        "profit_incomes_tax_2",
                        "profit_incomes_mortage_loans_1",
                        "profit_incomes_mortage_loans_2",
                        "sales_tax_withheld_1",
                        "sales_tax_withheld_2",
                        "name",
                        "rank",
                    ]
                )

            writer.writerow(
                [
                    company_name,
                    address,
                    email,
                    liaison_officer,
                    ssn,
                    tel,
                    fax,
                    legal_form,
                    cfc,
                    business_type,
                    business_function,
                    closing_date,
                    start_year,
                    end_year,
                    incomes_from_persons_1,
                    incomes_from_persons_2,
                    incomes_industries_business_1,
                    incomes_industries_business_2,
                    expenses_newspapers_1,
                    expenses_newspapers_2,
                    expenses_radio_television_1,
                    expenses_radio_television_2,
                    expenses_other_1,
                    expenses_other_2,
                    gross_profit_1,
                    gross_profit_2,
                    dividends_paid_1,
                    dividends_paid_2,
                    expenses_interests_1,
                    expenses_interests_2,
                    expenses_rent_1,
                    expenses_rent_2,
                    expenses_gain_loss_1,
                    expenses_gain_loss_2,
                    dividends_paid_other_1,
                    dividends_paid_other_2,
                    incomes_total_1,
                    incomes_total_2,
                    expenses_total_1,
                    expenses_total_2,
                    salaries_wages_bonus_1,
                    salaries_wages_bonus_2,
                    interests_1,
                    interests_2,
                    rents_1,
                    rents_2,
                    depreciation_1,
                    depreciation_2,
                    other_taxes_1,
                    other_taxes_2,
                    donations_1,
                    donations_2,
                    sales_tax_1,
                    sales_tax_2,
                    machinery_1,
                    machinery_2,
                    other_purchases_1,
                    other_purchases_2,
                    licenses_1,
                    licenses_2,
                    other_operating_expenses_1,
                    other_operating_expenses_2,
                    profit_incomes_tax_1,
                    profit_incomes_tax_2,
                    profit_incomes_mortage_loans_1,
                    profit_incomes_mortage_loans_2,
                    sales_tax_withheld_1,
                    sales_tax_withheld_2,
                    name,
                    rank,
                ]
            )
        
        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-540J.csv",
            dtypes={
                "company_name": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "ssn": str,
                "tel": str,
                "fax": str,
                "legal_form": str,
                "cfc": str,
                "business_type": str,
                "business_function": str,
                "closing_date": str,
                "start_year": int,
                "end_year": int,
                "incomes_from_persons_1": float,
                "incomes_from_persons_2": float,
                "incomes_industries_business_1": float,
                "incomes_industries_business_2": float,
                "expenses_newspapers_1": float,
                "expenses_newspapers_2": float,
                "expenses_radio_television_1": float,
                "expenses_radio_television_2": float,
                "expenses_other_1": float,
                "expenses_other_2": float,
                "gross_profit_1": float,
                "gross_profit_2": float,
                "dividends_paid_1": float,
                "dividends_paid_2": float,
                "expenses_interests_1": float,
                "expenses_interests_2": float,
                "expenses_rent_1": float,
                "expenses_rent_2": float,
                "expenses_gain_loss_1": float,
                "expenses_gain_loss_2": float,
                "dividends_paid_other_1": float,
                "dividends_paid_other_2": float,
                "incomes_total_1": float,
                "incomes_total_2": float,
                "expenses_total_1": float,
                "expenses_total_2": float,
                "salaries_wages_bonus_1": float,
                "salaries_wages_bonus_2": float,
                "interests_1": float,
                "interests_2": float,
                "rents_1": float,
                "rents_2": float,
                "depreciation_1": float,
                "depreciation_2": float,
                "other_taxes_1": float,
                "other_taxes_2": float,
                "donations_1": float,
                "donations_2": float,
                "sales_tax_1": float,
                "sales_tax_2": float,
                "machinery_1": float,
                "machinery_2": float,
                "other_purchases_1": float,
                "other_purchases_2": float,
                "licenses_1": float,
                "licenses_2": float,
                "other_operating_expenses_1": float,
                "other_operating_expenses_2": float,
                "profit_incomes_tax_1": float,
                "profit_incomes_tax_2": float,
                "profit_incomes_mortage_loans_1": float,
                "profit_incomes_mortage_loans_2": float,
                "sales_tax_withheld_1": float,
                "sales_tax_withheld_2": float,
                "name": str,
                "rank": str,
            },
            table_name="IP_540J",
            table_id=42,
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-540J.html")


def JP_544_2(request):
    if request.method == "POST":
        # Retrieve form data
        university_name = request.POST.get("university_name")
        phone = request.POST.get("phone")
        contact_person = request.POST.get("contact_person")
        direction = request.POST.get("direction")
        email = request.POST.get("email")

        federal_agency_name_1 = request.POST.get("federal_agency_name_1")
        federal_program_1 = request.POST.get("federal_program_1")
        federal_recieved_amount_1 = request.POST.get("federal_recieved_amount_1")
        federal_date_receipt_1 = request.POST.get("federal_date_receipt_1")

        federal_agency_name_2 = request.POST.get("federal_agency_name_2")
        federal_program_2 = request.POST.get("federal_program_2")
        federal_recieved_amount_2 = request.POST.get("federal_recieved_amount_2")
        federal_date_receipt_2 = request.POST.get("federal_date_receipt_2")

        federal_agency_name_3 = request.POST.get("federal_agency_name_3")
        federal_program_3 = request.POST.get("federal_program_3")
        federal_recieved_amount_3 = request.POST.get("federal_recieved_amount_3")
        federal_date_receipt_3 = request.POST.get("federal_date_receipt_3")

        federal_agency_name_4 = request.POST.get("federal_agency_name_4")
        federal_program_4 = request.POST.get("federal_program_4")
        federal_recieved_amount_4 = request.POST.get("federal_recieved_amount_4")
        federal_date_receipt_4 = request.POST.get("federal_date_receipt_4")

        federal_agency_name_5 = request.POST.get("federal_agency_name_5")
        federal_program_5 = request.POST.get("federal_program_5")
        federal_recieved_amount_5 = request.POST.get("federal_recieved_amount_5")
        federal_date_receipt_5 = request.POST.get("federal_date_receipt_5")

        federal_agency_name_6 = request.POST.get("federal_agency_name_6")
        federal_program_6 = request.POST.get("federal_program_6")
        federal_recieved_amount_6 = request.POST.get("federal_recieved_amount_6")
        federal_date_receipt_6 = request.POST.get("federal_date_receipt_6")

        federal_agency_name_7 = request.POST.get("federal_agency_name_7")
        federal_program_7 = request.POST.get("federal_program_7")
        federal_recieved_amount_7 = request.POST.get("federal_recieved_amount_7")
        federal_date_receipt_7 = request.POST.get("federal_date_receipt_7")

        federal_agency_name_8 = request.POST.get("federal_agency_name_8")
        federal_program_8 = request.POST.get("federal_program_8")
        federal_recieved_amount_8 = request.POST.get("federal_recieved_amount_8")
        federal_date_receipt_8 = request.POST.get("federal_date_receipt_8")

        local_agency_name_1 = request.POST.get("local_agency_name_1")
        agency_program_1 = request.POST.get("agency_program_1")
        agency_recieved_amount_1 = request.POST.get("agency_recieved_amount_1")
        agency_date_receipt_1 = request.POST.get("agency_date_receipt_1")

        local_agency_name_2 = request.POST.get("local_agency_name_2")
        agency_program_2 = request.POST.get("agency_program_2")
        agency_recieved_amount_2 = request.POST.get("agency_recieved_amount_2")
        agency_date_receipt_2 = request.POST.get("agency_date_receipt_2")

        local_agency_name_3 = request.POST.get("local_agency_name_3")
        agency_program_3 = request.POST.get("agency_program_3")
        agency_recieved_amount_3 = request.POST.get("agency_recieved_amount_3")
        agency_date_receipt_3 = request.POST.get("agency_date_receipt_3")

        local_agency_name_4 = request.POST.get("local_agency_name_4")
        agency_program_4 = request.POST.get("agency_program_4")
        agency_recieved_amount_4 = request.POST.get("agency_recieved_amount_4")
        agency_date_receipt_4 = request.POST.get("agency_date_receipt_4")

        local_agency_name_5 = request.POST.get("local_agency_name_5")
        agency_program_5 = request.POST.get("agency_program_5")
        agency_recieved_amount_5 = request.POST.get("agency_recieved_amount_5")
        agency_date_receipt_5 = request.POST.get("agency_date_receipt_5")

        total_students_enrolled = request.POST.get("total_students_enrolled")
        students_recived_amount = request.POST.get("students_recived_amount")

        total_pell_grant_students = request.POST.get("total_pell_grant_students")
        pell_grant_students_amount = request.POST.get("pell_grant_students_amount")

        total_no_resident_student = request.POST.get("total_no_resident_student")
        no_resident_student_amount = request.POST.get("no_resident_student_amount")

        no_resident_students_bills = request.POST.get("no_resident_students_bills")

        loans_granted = request.POST.get("loans_granted")
        loans_granted_amount = request.POST.get("loans_granted_amount")

        donations_institution_name_1 = request.POST.get("donations_institution_name_1")
        donations_amount_1 = request.POST.get("donations_amount_1")
        donations_date_1 = request.POST.get("donations_date_1")

        donations_institution_name_2 = request.POST.get("donations_institution_name_2")
        donations_amount_2 = request.POST.get("donations_amount_2")
        donations_date_2 = request.POST.get("donations_date_2")

        donations_institution_name_3 = request.POST.get("donations_institution_name_3")
        donations_amount_3 = request.POST.get("donations_amount_3")
        donations_date_3 = request.POST.get("donations_date_3")

        donations_institution_name_4 = request.POST.get("donations_institution_name_4")
        donations_amount_4 = request.POST.get("donations_amount_4")
        donations_date_4 = request.POST.get("donations_date_4")

        donations_institution_name_5 = request.POST.get("donations_institution_name_5")
        donations_amount_5 = request.POST.get("donations_amount_5")
        donations_date_5 = request.POST.get("donations_date_5")

        profesional_services_amount = request.POST.get("profesional_services_amount")
        profesional_services_payment = request.POST.get("profesional_services_payment")

        other_payment_relations_1 = request.POST.get("other_payment_relations_1")
        other_payment_relations_amount_1 = request.POST.get(
            "other_payment_relations_amount_1"
        )
        other_payment_relations_payment_1 = request.POST.get(
            "other_payment_relations_payment_1"
        )

        other_payment_relations_2 = request.POST.get("other_payment_relations_2")
        other_payment_relations_amount_2 = request.POST.get(
            "other_payment_relations_amount_2"
        )
        other_payment_relations_payment_2 = request.POST.get(
            "other_payment_relations_payment_2"
        )

        other_payment_relations_3 = request.POST.get("other_payment_relations_3")
        other_payment_relations_amount_3 = request.POST.get(
            "other_payment_relations_amount_3"
        )
        other_payment_relations_payment_3 = request.POST.get(
            "other_payment_relations_payment_3"
        )

        other_payment_relations_4 = request.POST.get("other_payment_relations_4")
        other_payment_relations_amount_4 = request.POST.get(
            "other_payment_relations_amount_4"
        )
        other_payment_relations_payment_4 = request.POST.get(
            "other_payment_relations_payment_4"
        )

        acquired_value = request.POST.get("acquired_value")
        investment_amount = request.POST.get("investment_amount")
        recived_interest = request.POST.get("recived_interest")

        csv_file_path = "data/cuestionarios/balanza_de_pagos/JP-544-2.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "university_name",
                        "phone",
                        "contact_person",
                        "direction",
                        "email",
                        "federal_agency_name_1",
                        "federal_program_1",
                        "federal_recieved_amount_1",
                        "federal_date_receipt_1",
                        "federal_agency_name_2",
                        "federal_program_2",
                        "federal_recieved_amount_2",
                        "federal_date_receipt_2",
                        "federal_agency_name_3",
                        "federal_program_3",
                        "federal_recieved_amount_3",
                        "federal_date_receipt_3",
                        "federal_agency_name_4",
                        "federal_program_4",
                        "federal_recieved_amount_4",
                        "federal_date_receipt_4",
                        "federal_agency_name_5",
                        "federal_program_5",
                        "federal_recieved_amount_5",
                        "federal_date_receipt_5",
                        "federal_agency_name_6",
                        "federal_program_6",
                        "federal_recieved_amount_6",
                        "federal_date_receipt_6",
                        "federal_agency_name_7",
                        "federal_program_7",
                        "federal_recieved_amount_7",
                        "federal_date_receipt_7",
                        "federal_agency_name_8",
                        "federal_program_8",
                        "federal_recieved_amount_8",
                        "federal_date_receipt_8",
                        "local_agency_name_1",
                        "agency_program_1",
                        "agency_recieved_amount_1",
                        "agency_date_receipt_1",
                        "local_agency_name_2",
                        "agency_program_2",
                        "agency_recieved_amount_2",
                        "agency_date_receipt_2",
                        "local_agency_name_3",
                        "agency_program_3",
                        "agency_recieved_amount_3",
                        "agency_date_receipt_3",
                        "local_agency_name_4",
                        "agency_program_4",
                        "agency_recieved_amount_4",
                        "agency_date_receipt_4",
                        "local_agency_name_5",
                        "agency_program_5",
                        "agency_recieved_amount_5",
                        "agency_date_receipt_5",
                        "total_students_enrolled",
                        "students_recived_amount",
                        "total_pell_grant_students",
                        "pell_grant_students_amount",
                        "total_no_resident_student",
                        "no_resident_student_amount",
                        "no_resident_students_bills",
                        "loans_granted",
                        "loans_granted_amount",
                        "donations_institution_name_1",
                        "donations_amount_1",
                        "donations_date_1",
                        "donations_institution_name_2",
                        "donations_amount_2",
                        "donations_date_2",
                        "donations_institution_name_3",
                        "donations_amount_3",
                        "donations_date_3",
                        "donations_institution_name_4",
                        "donations_amount_4",
                        "donations_date_4",
                        "donations_institution_name_5",
                        "donations_amount_5",
                        "donations_date_5",
                        "profesional_services_amount",
                        "profesional_services_payment",
                        "other_payment_relations_1",
                        "other_payment_relations_amount_1",
                        "other_payment_relations_payment_1",
                        "other_payment_relations_2",
                        "other_payment_relations_amount_2",
                        "other_payment_relations_payment_2",
                        "other_payment_relations_3",
                        "other_payment_relations_amount_3",
                        "other_payment_relations_payment_3",
                        "other_payment_relations_4",
                        "other_payment_relations_amount_4",
                        "other_payment_relations_payment_4",
                        "acquired_value",
                        "investment_amount",
                        "recived_interest",
                    ]
                )

            writer.writerow(
                [
                    university_name,
                    phone,
                    contact_person,
                    direction,
                    email,
                    federal_agency_name_1,
                    federal_program_1,
                    federal_recieved_amount_1,
                    federal_date_receipt_1,
                    federal_agency_name_2,
                    federal_program_2,
                    federal_recieved_amount_2,
                    federal_date_receipt_2,
                    federal_agency_name_3,
                    federal_program_3,
                    federal_recieved_amount_3,
                    federal_date_receipt_3,
                    federal_agency_name_4,
                    federal_program_4,
                    federal_recieved_amount_4,
                    federal_date_receipt_4,
                    federal_agency_name_5,
                    federal_program_5,
                    federal_recieved_amount_5,
                    federal_date_receipt_5,
                    federal_agency_name_6,
                    federal_program_6,
                    federal_recieved_amount_6,
                    federal_date_receipt_6,
                    federal_agency_name_7,
                    federal_program_7,
                    federal_recieved_amount_7,
                    federal_date_receipt_7,
                    federal_agency_name_8,
                    federal_program_8,
                    federal_recieved_amount_8,
                    federal_date_receipt_8,
                    local_agency_name_1,
                    agency_program_1,
                    agency_recieved_amount_1,
                    agency_date_receipt_1,
                    local_agency_name_2,
                    agency_program_2,
                    agency_recieved_amount_2,
                    agency_date_receipt_2,
                    local_agency_name_3,
                    agency_program_3,
                    agency_recieved_amount_3,
                    agency_date_receipt_3,
                    local_agency_name_4,
                    agency_program_4,
                    agency_recieved_amount_4,
                    agency_date_receipt_4,
                    local_agency_name_5,
                    agency_program_5,
                    agency_recieved_amount_5,
                    agency_date_receipt_5,
                    total_students_enrolled,
                    students_recived_amount,
                    total_pell_grant_students,
                    pell_grant_students_amount,
                    total_no_resident_student,
                    no_resident_student_amount,
                    no_resident_students_bills,
                    loans_granted,
                    loans_granted_amount,
                    donations_institution_name_1,
                    donations_amount_1,
                    donations_date_1,
                    donations_institution_name_2,
                    donations_amount_2,
                    donations_date_2,
                    donations_institution_name_3,
                    donations_amount_3,
                    donations_date_3,
                    donations_institution_name_4,
                    donations_amount_4,
                    donations_date_4,
                    donations_institution_name_5,
                    donations_amount_5,
                    donations_date_5,
                    profesional_services_amount,
                    profesional_services_payment,
                    other_payment_relations_1,
                    other_payment_relations_amount_1,
                    other_payment_relations_payment_1,
                    other_payment_relations_2,
                    other_payment_relations_amount_2,
                    other_payment_relations_payment_2,
                    other_payment_relations_3,
                    other_payment_relations_amount_3,
                    other_payment_relations_payment_3,
                    other_payment_relations_4,
                    other_payment_relations_amount_4,
                    other_payment_relations_payment_4,
                    acquired_value,
                    investment_amount,
                    recived_interest,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/balanza_de_pagos/JP-544-2.csv",
            dtypes={
                "university_name": str,
                "phone": str,
                "contact_person": str,
                "direction": str,
                "email": str,
                "federal_agency_name_1": str,
                "federal_program_1": str,
                "federal_recieved_amount_1": int,
                "federal_date_receipt_1": str,
                "federal_agency_name_2": str,
                "federal_program_2": str,
                "federal_recieved_amount_2": int,
                "federal_date_receipt_2": str,
                "federal_agency_name_3": str,
                "federal_program_3": str,
                "federal_recieved_amount_3": int,
                "federal_date_receipt_3": str,
                "federal_agency_name_4": str,
                "federal_program_4": str,
                "federal_recieved_amount_4": int,
                "federal_date_receipt_4": str,
                "federal_agency_name_5": str,
                "federal_program_5": str,
                "federal_recieved_amount_5": int,
                "federal_date_receipt_5": str,
                "federal_agency_name_6": str,
                "federal_program_6": str,
                "federal_recieved_amount_6": int,
                "federal_date_receipt_6": str,
                "federal_agency_name_7": str,
                "federal_program_7": str,
                "federal_recieved_amount_7": int,
                "federal_date_receipt_7": str,
                "federal_agency_name_8": str,
                "federal_program_8": str,
                "federal_recieved_amount_8": int,
                "federal_date_receipt_8": str,
                "local_agency_name_1": str,
                "agency_program_1": str,
                "agency_recieved_amount_1": int,
                "agency_date_receipt_1": str,
                "local_agency_name_2": str,
                "agency_program_2": str,
                "agency_recieved_amount_2": int,
                "agency_date_receipt_2": str,
                "local_agency_name_3": str,
                "agency_program_3": str,
                "agency_recieved_amount_3": int,
                "agency_date_receipt_3": str,
                "local_agency_name_4": str,
                "agency_program_4": str,
                "agency_recieved_amount_4": int,
                "agency_date_receipt_4": str,
                "local_agency_name_5": str,
                "agency_program_5": str,
                "agency_recieved_amount_5": int,
                "agency_date_receipt_5": str,
                "total_students_enrolled": int,
                "students_recived_amount": float,
                "total_pell_grant_students": int,
                "pell_grant_students_amount": float,
                "total_no_resident_student": int,
                "no_resident_student_amount": float,
                "no_resident_students_bills": float,
                "loans_granted": int,
                "loans_granted_amount": float,
                "donations_institution_name_1": str,
                "donations_amount_1": float,
                "donations_date_1": str,
                "donations_institution_name_2": str,
                "donations_amount_2": float,
                "donations_date_2": str,
                "donations_institution_name_3": str,
                "donations_amount_3": float,
                "donations_date_3": str,
                "donations_institution_name_4": str,
                "donations_amount_4": float,
                "donations_date_4": str,
                "donations_institution_name_5": str,
                "donations_amount_5": float,
                "donations_date_5": str,
                "profesional_services_amount": int,
                "profesional_services_payment": float,
                "other_payment_relations_1": str,
                "other_payment_relations_amount_1": int,
                "other_payment_relations_payment_1": float,
                "other_payment_relations_2": str,
                "other_payment_relations_amount_2": int,
                "other_payment_relations_payment_2": float,
                "other_payment_relations_3": str,
                "other_payment_relations_amount_3": int,
                "other_payment_relations_payment_3": float,
                "other_payment_relations_4": str,
                "other_payment_relations_amount_4": int,
                "other_payment_relations_payment_4": float,
                "acquired_value": float,
                "investment_amount": float,
                "recived_interest": float,
            },
            table_name="JP_544_1",
            table_id=28,
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/balanza_de_pagos/JP-544-2.html")


def IP_610(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get("company_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")
        legal_form = request.POST.get("legal_form")
        cfc = request.POST.get("cfc")
        business_type = request.POST.get("business_type")
        business_function = request.POST.get("business_function")
        branches = request.POST.get("branches")
        branches_yes = request.POST.get("branches_yes")
        closing_date = request.POST.get("closing_date")

        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")

        incomes_services_rendered_1 = request.POST.get("incomes_services_rendered_1")
        incomes_services_rendered_2 = request.POST.get("incomes_services_rendered_2")
        incomes_unrestricted_A_1 = request.POST.get("incomes_unrestricted_A_1")
        incomes_unrestricted_A_2 = request.POST.get("incomes_unrestricted_A_2")
        incomes_restricted_A_1 = request.POST.get("incomes_restricted_A_1")
        incomes_restricted_A_2 = request.POST.get("incomes_restricted_A_2")
        incomes_sales_1 = request.POST.get("incomes_sales_1")
        incomes_sales_2 = request.POST.get("incomes_sales_2")
        incomes_rents_1 = request.POST.get("incomes_rents_1")
        incomes_rents_2 = request.POST.get("incomes_rents_2")
        incomes_interests_1 = request.POST.get("incomes_interests_1")
        incomes_interests_2 = request.POST.get("incomes_interests_2")
        incomes_capital_1 = request.POST.get("incomes_capital_1")
        incomes_capital_2 = request.POST.get("incomes_capital_2")
        incomes_total_1 = request.POST.get("incomes_total_1")
        incomes_total_2 = request.POST.get("incomes_total_2")

        expenses_1 = request.POST.get("expenses_1")
        expenses_2 = request.POST.get("expenses_2")
        expenses_salaries_1 = request.POST.get("expenses_salaries_1")
        expenses_salaries_2 = request.POST.get("expenses_salaries_2")
        expenses_interests_1 = request.POST.get("expenses_interests_1")
        expenses_interests_2 = request.POST.get("expenses_interests_2")
        expenses_rents_1 = request.POST.get("expenses_rents_1")
        expenses_rents_2 = request.POST.get("expenses_rents_2")
        expenses_depreciation_1 = request.POST.get("expenses_depreciation_1")
        expenses_depreciation_2 = request.POST.get("expenses_depreciation_2")
        expenses_debts_1 = request.POST.get("expenses_debts_1")
        expenses_debts_2 = request.POST.get("expenses_debts_2")
        expenses_donations_1 = request.POST.get("expenses_donations_1")
        expenses_donations_2 = request.POST.get("expenses_donations_2")
        expenses_tax_1 = request.POST.get("expenses_tax_1")
        expenses_tax_2 = request.POST.get("expenses_tax_2")
        expenses_machinery_1 = request.POST.get("expenses_machinery_1")
        expenses_machinery_2 = request.POST.get("expenses_machinery_2")
        other_purchases_1 = request.POST.get("other_purchases_1")
        other_purchases_2 = request.POST.get("other_purchases_2")
        expenses_licenses_1 = request.POST.get("expenses_licenses_1")
        expenses_licenses_2 = request.POST.get("expenses_licenses_2")
        expenses_other_1 = request.POST.get("expenses_other_1")
        expenses_other_2 = request.POST.get("expenses_other_2")
        net_profit_1 = request.POST.get("net_profit_1")
        net_profit_2 = request.POST.get("net_profit_2")
        income_tax_1 = request.POST.get("income_tax_1")
        income_tax_2 = request.POST.get("income_tax_2")
        profit_after_tax_1 = request.POST.get("profit_after_tax_1")
        profit_after_tax_2 = request.POST.get("profit_after_tax_2")
        withheld_tax_1 = request.POST.get("withheld_tax_1")
        withheld_tax_2 = request.POST.get("withheld_tax_2")

        signature = request.POST.get("signature")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-610.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "company_name",
                        "address",
                        "email",
                        "liaison_officer",
                        "ssn",
                        "tel",
                        "fax",
                        "legal_form",
                        "cfc",
                        "business_type",
                        "business_function",
                        "branches",
                        "branches_yes",
                        "closing_date",
                        "start_year",
                        "end_year",
                        "incomes_services_rendered_1",
                        "incomes_services_rendered_2",
                        "incomes_unrestricted_A_1",
                        "incomes_unrestricted_A_2",
                        "incomes_restricted_A_1",
                        "incomes_restricted_A_2",
                        "incomes_sales_1",
                        "incomes_sales_2",
                        "incomes_rents_1",
                        "incomes_rents_2",
                        "incomes_interests_1",
                        "incomes_interests_2",
                        "incomes_capital_1",
                        "incomes_capital_2",
                        "incomes_total_1",
                        "incomes_total_2",
                        "expenses_1",
                        "expenses_2",
                        "expenses_salaries_1",
                        "expenses_salaries_2",
                        "expenses_interests_1",
                        "expenses_interests_2",
                        "expenses_rents_1",
                        "expenses_rents_2",
                        "expenses_depreciation_1",
                        "expenses_depreciation_2",
                        "expenses_debts_1",
                        "expenses_debts_2",
                        "expenses_donations_1",
                        "expenses_donations_2",
                        "expenses_tax_1",
                        "expenses_tax_2",
                        "expenses_machinery_1",
                        "expenses_machinery_2",
                        "other_purchases_1",
                        "other_purchases_2",
                        "expenses_licenses_1",
                        "expenses_licenses_2",
                        "expenses_other_1",
                        "expenses_other_2",
                        "net_profit_1",
                        "net_profit_2",
                        "income_tax_1",
                        "income_tax_2",
                        "profit_after_tax_1",
                        "profit_after_tax_2",
                        "withheld_tax_1",
                        "withheld_tax_2",
                        "signature",
                        "rank",
                    ]
                )

            writer.writerow(
                [
                    company_name,
                    address,
                    email,
                    liaison_officer,
                    ssn,
                    tel,
                    fax,
                    legal_form,
                    cfc,
                    business_type,
                    business_function,
                    branches,
                    branches_yes,
                    closing_date,
                    start_year,
                    end_year,
                    incomes_services_rendered_1,
                    incomes_services_rendered_2,
                    incomes_unrestricted_A_1,
                    incomes_unrestricted_A_2,
                    incomes_restricted_A_1,
                    incomes_restricted_A_2,
                    incomes_sales_1,
                    incomes_sales_2,
                    incomes_rents_1,
                    incomes_rents_2,
                    incomes_interests_1,
                    incomes_interests_2,
                    incomes_capital_1,
                    incomes_capital_2,
                    incomes_total_1,
                    incomes_total_2,
                    expenses_1,
                    expenses_2,
                    expenses_salaries_1,
                    expenses_salaries_2,
                    expenses_interests_1,
                    expenses_interests_2,
                    expenses_rents_1,
                    expenses_rents_2,
                    expenses_depreciation_1,
                    expenses_depreciation_2,
                    expenses_debts_1,
                    expenses_debts_2,
                    expenses_donations_1,
                    expenses_donations_2,
                    expenses_tax_1,
                    expenses_tax_2,
                    expenses_machinery_1,
                    expenses_machinery_2,
                    other_purchases_1,
                    other_purchases_2,
                    expenses_licenses_1,
                    expenses_licenses_2,
                    expenses_other_1,
                    expenses_other_2,
                    net_profit_1,
                    net_profit_2,
                    income_tax_1,
                    income_tax_2,
                    profit_after_tax_1,
                    profit_after_tax_2,
                    withheld_tax_1,
                    withheld_tax_2,
                    signature,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-610.csv",
            dtypes={
                "company_name": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "ssn": str,
                "tel": str,
                "fax": str,
                "legal_form": str,
                "cfc": str,
                "business_type": str,
                "business_function": str,
                "branches": str,
                "branches_yes": str,
                "closing_date": str,
                "start_year": int,
                "end_year": int,
                "incomes_services_rendered_1": float,
                "incomes_services_rendered_2": float,
                "incomes_unrestricted_A_1": float,
                "incomes_unrestricted_A_2": float,
                "incomes_restricted_A_1": float,
                "incomes_restricted_A_2": float,
                "incomes_sales_1": float,
                "incomes_sales_2": float,
                "incomes_rents_1": float,
                "incomes_rents_2": float,
                "incomes_interests_1": float,
                "incomes_interests_2": float,
                "incomes_capital_1": float,
                "incomes_capital_2": float,
                "incomes_total_1": float,
                "incomes_total_2": float,
                "expenses_1": float,
                "expenses_2": float,
                "expenses_salaries_1": float,
                "expenses_salaries_2": float,
                "expenses_interests_1": float,
                "expenses_interests_2": float,
                "expenses_rents_1": float,
                "expenses_rents_2": float,
                "expenses_depreciation_1": float,
                "expenses_depreciation_2": float,
                "expenses_debts_1": float,
                "expenses_debts_2": float,
                "expenses_donations_1": float,
                "expenses_donations_2": float,
                "expenses_tax_1": float,
                "expenses_tax_2": float,
                "expenses_machinery_1": float,
                "expenses_machinery_2": float,
                "other_purchases_1": float,
                "other_purchases_2": float,
                "expenses_licenses_1": float,
                "expenses_licenses_2": float,
                "expenses_other_1": float,
                "expenses_other_2": float,
                "net_profit_1": float,
                "net_profit_2": float,
                "income_tax_1": float,
                "income_tax_2": float,
                "profit_after_tax_1": float,
                "profit_after_tax_2": float,
                "withheld_tax_1": float,
                "withheld_tax_2": float,
                "signature": str,
                "rank": str,
            },
            table_name="IP_610",
            table_id=26,
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-610.html")


def IP_710(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get("company_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")
        legal_form = request.POST.get("legal_form")
        cfc = request.POST.get("cfc")
        business_type = request.POST.get("business_type")
        business_function = request.POST.get("business_function")
        branches = request.POST.get("branches")
        branches_yes = request.POST.get("branches_yes")
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        total_income_1 = request.POST.get("total_income_1")
        total_income_2 = request.POST.get("total_income_2")
        incomes_service_1 = request.POST.get("incomes_service_1")
        incomes_service_2 = request.POST.get("incomes_service_2")
        incomes_from_persons_1 = request.POST.get("incomes_from_persons_1")
        incomes_from_persons_2 = request.POST.get("incomes_from_persons_2")
        incomes_from_industries_1 = request.POST.get("incomes_from_industries_1")
        incomes_from_industries_2 = request.POST.get("incomes_from_industries_2")
        incomes_from_sales_1 = request.POST.get("incomes_from_sales_1")
        incomes_from_sales_2 = request.POST.get("incomes_from_sales_2")
        income_rent_machinery_1 = request.POST.get("income_rent_machinery_1")
        income_rent_machinery_2 = request.POST.get("income_rent_machinery_2")
        income_rent_land_1 = request.POST.get("income_rent_land_1")
        income_rent_land_2 = request.POST.get("income_rent_land_2")
        income_interests_1 = request.POST.get("income_interests_1")
        income_interests_2 = request.POST.get("income_interests_2")
        income_capital_gain_or_loss_1 = request.POST.get(
            "income_capital_gain_or_loss_1"
        )
        income_capital_gain_or_loss_2 = request.POST.get(
            "income_capital_gain_or_loss_2"
        )
        income_other_operating_1 = request.POST.get("income_other_operating_1")
        income_other_operating_2 = request.POST.get("income_other_operating_2")
        total_expenses_1 = request.POST.get("total_expenses_1")
        total_expenses_2 = request.POST.get("total_expenses_2")
        expenses_salaries_1 = request.POST.get("expenses_salaries_1")
        expenses_salaries_2 = request.POST.get("expenses_salaries_2")
        expenses_interests_1 = request.POST.get("expenses_interests_1")
        expenses_interests_2 = request.POST.get("expenses_interests_2")
        expenses_rent_land_1 = request.POST.get("expenses_rent_land_1")
        expenses_rent_land_2 = request.POST.get("expenses_rent_land_2")
        expenses_depreciation_1 = request.POST.get("expenses_depreciation_1")
        expenses_depreciation_2 = request.POST.get("expenses_depreciation_2")
        expenses_bad_debts_1 = request.POST.get("expenses_bad_debts_1")
        expenses_bad_debts_2 = request.POST.get("expenses_bad_debts_2")
        expenses_donations_1 = request.POST.get("expenses_donations_1")
        expenses_donations_2 = request.POST.get("expenses_donations_2")
        expenses_other_operating_1 = request.POST.get("expenses_other_operating_1")
        expenses_other_operating_2 = request.POST.get("expenses_other_operating_2")
        expenses_sales_and_use_1 = request.POST.get("expenses_sales_and_use_1")
        expenses_sales_and_use_2 = request.POST.get("expenses_sales_and_use_2")
        expenses_purchases_machinery_1 = request.POST.get(
            "expenses_purchases_machinery_1"
        )
        expenses_purchases_machinery_2 = request.POST.get(
            "expenses_purchases_machinery_2"
        )
        expenses_other_purchases_1 = request.POST.get("expenses_other_purchases_1")
        expenses_other_purchases_2 = request.POST.get("expenses_other_purchases_2")
        expenses_licenses_1 = request.POST.get("expenses_licenses_1")
        expenses_licenses_2 = request.POST.get("expenses_licenses_2")
        profit_incomes_tax_1 = request.POST.get("profit_incomes_tax_1")
        profit_incomes_tax_2 = request.POST.get("profit_incomes_tax_2")
        profit_after_income_tax_1 = request.POST.get("profit_after_income_tax_1")
        profit_after_income_tax_2 = request.POST.get("profit_after_income_tax_2")
        sales_tax_withheld_1 = request.POST.get("sales_tax_withheld_1")
        sales_tax_withheld_2 = request.POST.get("sales_tax_withheld_2")
        name = request.POST.get("name")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-710.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "company_name",
                        "address",
                        "email",
                        "liaison_officer",
                        "ssn",
                        "tel",
                        "fax",
                        "legal_form",
                        "cfc",
                        "business_type",
                        "business_function",
                        "branches",
                        "branches_yes",
                        "closing_date",
                        "start_year",
                        "end_year",
                        "total_income_1",
                        "total_income_2",
                        "incomes_service_1",
                        "incomes_service_2",
                        "incomes_from_persons_1",
                        "incomes_from_persons_2",
                        "incomes_from_industries_1",
                        "incomes_from_industries_2",
                        "incomes_from_sales_1",
                        "incomes_from_sales_2",
                        "income_rent_machinery_1",
                        "income_rent_machinery_2",
                        "income_rent_land_1",
                        "income_rent_land_2",
                        "income_interests_1",
                        "income_interests_2",
                        "income_capital_gain_or_loss_1",
                        "income_capital_gain_or_loss_2",
                        "income_other_operating_1",
                        "income_other_operating_2",
                        "total_expenses_1",
                        "total_expenses_2",
                        "expenses_salaries_1",
                        "expenses_salaries_2",
                        "expenses_interests_1",
                        "expenses_interests_2",
                        "expenses_rent_land_1",
                        "expenses_rent_land_2",
                        "expenses_depreciation_1",
                        "expenses_depreciation_2",
                        "expenses_bad_debts_1",
                        "expenses_bad_debts_2",
                        "expenses_donations_1",
                        "expenses_donations_2",
                        "expenses_other_operating_1",
                        "expenses_other_operating_2",
                        "expenses_sales_and_use_1",
                        "expenses_sales_and_use_2",
                        "expenses_purchases_machinery_1",
                        "expenses_purchases_machinery_2",
                        "expenses_other_purchases_1",
                        "expenses_other_purchases_2",
                        "expenses_licenses_1",
                        "expenses_licenses_2",
                        "profit_incomes_tax_1",
                        "profit_incomes_tax_2",
                        "profit_after_income_tax_1",
                        "profit_after_income_tax_2",
                        "sales_tax_withheld_1",
                        "sales_tax_withheld_2",
                        "name",
                        "rank",
                    ]
                )

            writer.writerow(
                [
                    company_name,
                    address,
                    email,
                    liaison_officer,
                    ssn,
                    tel,
                    fax,
                    legal_form,
                    cfc,
                    business_type,
                    business_function,
                    branches,
                    branches_yes,
                    closing_date,
                    start_year,
                    end_year,
                    total_income_1,
                    total_income_2,
                    incomes_service_1,
                    incomes_service_2,
                    incomes_from_persons_1,
                    incomes_from_persons_2,
                    incomes_from_industries_1,
                    incomes_from_industries_2,
                    incomes_from_sales_1,
                    incomes_from_sales_2,
                    income_rent_machinery_1,
                    income_rent_machinery_2,
                    income_rent_land_1,
                    income_rent_land_2,
                    income_interests_1,
                    income_interests_2,
                    income_capital_gain_or_loss_1,
                    income_capital_gain_or_loss_2,
                    income_other_operating_1,
                    income_other_operating_2,
                    total_expenses_1,
                    total_expenses_2,
                    expenses_salaries_1,
                    expenses_salaries_2,
                    expenses_interests_1,
                    expenses_interests_2,
                    expenses_rent_land_1,
                    expenses_rent_land_2,
                    expenses_depreciation_1,
                    expenses_depreciation_2,
                    expenses_bad_debts_1,
                    expenses_bad_debts_2,
                    expenses_donations_1,
                    expenses_donations_2,
                    expenses_other_operating_1,
                    expenses_other_operating_2,
                    expenses_sales_and_use_1,
                    expenses_sales_and_use_2,
                    expenses_purchases_machinery_1,
                    expenses_purchases_machinery_2,
                    expenses_other_purchases_1,
                    expenses_other_purchases_2,
                    expenses_licenses_1,
                    expenses_licenses_2,
                    profit_incomes_tax_1,
                    profit_incomes_tax_2,
                    profit_after_income_tax_1,
                    profit_after_income_tax_2,
                    sales_tax_withheld_1,
                    sales_tax_withheld_2,
                    name,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-710.csv",
            dtypes={
                "company_name": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "ssn": str,
                "tel": str,
                "fax": str,
                "legal_form": str,
                "cfc": str,
                "business_type": str,
                "business_function": str,
                "branches": str,
                "branches_yes": str,
                "closing_date": str,
                "start_year": int,
                "end_year": int,
                "total_income_1": float,
                "total_income_2": float,
                "incomes_service_1": float,
                "incomes_service_2": float,
                "incomes_from_persons_1": float,
                "incomes_from_persons_2": float,
                "incomes_from_industries_1": float,
                "incomes_from_industries_2": float,
                "incomes_from_sales_1": float,
                "incomes_from_sales_2": float,
                "income_rent_machinery_1": float,
                "income_rent_machinery_2": float,
                "income_rent_land_1": float,
                "income_rent_land_2": float,
                "income_interests_1": float,
                "income_interests_2": float,
                "income_capital_gain_or_loss_1": float,
                "income_capital_gain_or_loss_2": float,
                "income_other_operating_1": float,
                "income_other_operating_2": float,
                "total_expenses_1": float,
                "total_expenses_2": float,
                "expenses_salaries_1": float,
                "expenses_salaries_2": float,
                "expenses_interests_1": float,
                "expenses_interests_2": float,
                "expenses_rent_land_1": float,
                "expenses_rent_land_2": float,
                "expenses_depreciation_1": float,
                "expenses_depreciation_2": float,
                "expenses_bad_debts_1": float,
                "expenses_bad_debts_2": float,
                "expenses_donations_1": float,
                "expenses_donations_2": float,
                "expenses_other_operating_1": float,
                "expenses_other_operating_2": float,
                "expenses_sales_and_use_1": float,
                "expenses_sales_and_use_2": float,
                "expenses_purchases_machinery_1": float,
                "expenses_purchases_machinery_2": float,
                "expenses_other_purchases_1": float,
                "expenses_other_purchases_2": float,
                "expenses_licenses_1": float,
                "expenses_licenses_2": float,
                "profit_incomes_tax_1": float,
                "profit_incomes_tax_2": float,
                "profit_after_income_tax_1": float,
                "profit_after_income_tax_2": float,
                "sales_tax_withheld_1": float,
                "sales_tax_withheld_2": float,
                "name": str,
                "rank": str,
            },
            table_name="IP_710",
            table_id=24,
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-710.html")


def IP_620(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get("company_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")
        legal_form = request.POST.get("legal_form")
        cfc = request.POST.get("cfc")
        business_type = request.POST.get("business_type")
        business_function = request.POST.get("business_function")
        branches = request.POST.get("branches")
        branches_yes = request.POST.get("branches_yes")
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")

        patients_service_revenue_from_persons_1 = request.POST.get(
            "patients_service_revenue_from_persons_1"
        )
        patients_service_revenue_from_persons_2 = request.POST.get(
            "patients_service_revenue_from_persons_2"
        )
        patients_service_revenue_from_industries_business_1 = request.POST.get(
            "patients_service_revenue_from_industries_business_1"
        )
        patients_service_revenue_from_industries_business_2 = request.POST.get(
            "patients_service_revenue_from_industries_business_2"
        )
        contractual_adjustments_1 = request.POST.get("contractual_adjustments_1")
        contractual_adjustments_2 = request.POST.get("contractual_adjustments_2")
        net_patient_service_revenue_1 = request.POST.get(
            "net_patient_service_revenue_1"
        )
        net_patient_service_revenue_2 = request.POST.get(
            "net_patient_service_revenue_2"
        )
        other_incomes_1 = request.POST.get("other_incomes_1")
        other_incomes_2 = request.POST.get("other_incomes_2")
        other_incomes_rent_1 = request.POST.get("other_incomes_rent_1")
        other_incomes_rent_2 = request.POST.get("other_incomes_rent_2")
        other_incomes_interest_1 = request.POST.get("other_incomes_interest_1")
        other_incomes_interest_2 = request.POST.get("other_incomes_interest_2")
        other_incomes_capital_gain_loss_1 = request.POST.get(
            "other_incomes_capital_gain_loss_1"
        )
        other_incomes_capital_gain_loss_2 = request.POST.get(
            "other_incomes_capital_gain_loss_2"
        )
        other_incomes_operating_1 = request.POST.get("other_incomes_operating_1")
        other_incomes_operating_2 = request.POST.get("other_incomes_operating_2")
        total_incomes_1 = request.POST.get("total_incomes_1")
        total_incomes_2 = request.POST.get("total_incomes_2")
        total_expenses_1 = request.POST.get("total_expenses_1")
        total_expenses_2 = request.POST.get("total_expenses_2")
        expenses_salaries_wages_bonus_1 = request.POST.get(
            "expenses_salaries_wages_bonus_1"
        )
        expenses_salaries_wages_bonus_2 = request.POST.get(
            "expenses_salaries_wages_bonus_2"
        )
        expenses_interest_1 = request.POST.get("expenses_interest_1")
        expenses_interest_2 = request.POST.get("expenses_interest_2")
        expenses_rent_1 = request.POST.get("expenses_rent_1")
        expenses_rent_2 = request.POST.get("expenses_rent_2")
        expenses_food_patients_1 = request.POST.get("expenses_food_patients_1")
        expenses_food_patients_2 = request.POST.get("expenses_food_patients_2")
        expenses_free_food_to_employees_1 = request.POST.get(
            "expenses_free_food_to_employees_1"
        )
        expenses_free_food_to_employees_2 = request.POST.get(
            "expenses_free_food_to_employees_2"
        )
        expenses_uniforms_1 = request.POST.get("expenses_uniforms_1")
        expenses_uniforms_2 = request.POST.get("expenses_uniforms_2")
        expenses_depreciation_1 = request.POST.get("expenses_depreciation_1")
        expenses_depreciation_2 = request.POST.get("expenses_depreciation_2")
        expenses_bad_debts_1 = request.POST.get("expenses_bad_debts_1")
        expenses_bad_debts_2 = request.POST.get("expenses_bad_debts_2")
        expenses_donations_1 = request.POST.get("expenses_donations_1")
        expenses_donations_2 = request.POST.get("expenses_donations_2")
        expenses_sales_tax_1 = request.POST.get("expenses_sales_tax_1")
        expenses_sales_tax_2 = request.POST.get("expenses_sales_tax_2")
        expenses_machinery_1 = request.POST.get("expenses_machinery_1")
        expenses_machinery_2 = request.POST.get("expenses_machinery_2")
        expenses_on_other_purchases_1 = request.POST.get(
            "expenses_on_other_purchases_1"
        )
        expenses_on_other_purchases_2 = request.POST.get(
            "expenses_on_other_purchases_2"
        )
        expenses_licenses_1 = request.POST.get("expenses_licenses_1")
        expenses_licenses_2 = request.POST.get("expenses_licenses_2")
        expenses_other_operating_1 = request.POST.get("expenses_other_operating_1")
        expenses_other_operating_2 = request.POST.get("expenses_other_operating_2")
        net_profit_loss_1 = request.POST.get("net_profit_loss_1")
        net_profit_loss_2 = request.POST.get("net_profit_loss_2")
        net_profit_loss_income_tax_1 = request.POST.get("net_profit_loss_income_tax_1")
        net_profit_loss_income_tax_2 = request.POST.get("net_profit_loss_income_tax_2")
        net_profit_after_tax_1 = request.POST.get("net_profit_after_tax_1")
        net_profit_after_tax_2 = request.POST.get("net_profit_after_tax_2")
        sales_and_use_withheld_1 = request.POST.get("sales_and_use_withheld_1")
        sales_and_use_withheld_2 = request.POST.get("sales_and_use_withheld_2")
        name = request.POST.get("name")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-620.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "company_name",
                        "address",
                        "email",
                        "liaison_officer",
                        "ssn",
                        "tel",
                        "fax",
                        "legal_form",
                        "cfc",
                        "business_type",
                        "business_function",
                        "branches",
                        "branches_yes",
                        "closing_date",
                        "start_year",
                        "end_year",
                        "patients_service_revenue_from_persons_1",
                        "patients_service_revenue_from_persons_2",
                        "patients_service_revenue_from_industries_business_1",
                        "patients_service_revenue_from_industries_business_2",
                        "contractual_adjustments_1",
                        "contractual_adjustments_2",
                        "net_patient_service_revenue_1",
                        "net_patient_service_revenue_2",
                        "other_incomes_1",
                        "other_incomes_2",
                        "other_incomes_rent_1",
                        "other_incomes_rent_2",
                        "other_incomes_interest_1",
                        "other_incomes_interest_2",
                        "other_incomes_capital_gain_loss_1",
                        "other_incomes_capital_gain_loss_2",
                        "other_incomes_operating_1",
                        "other_incomes_operating_2",
                        "total_incomes_1",
                        "total_incomes_2",
                        "total_expenses_1",
                        "total_expenses_2",
                        "expenses_salaries_wages_bonus_1",
                        "expenses_salaries_wages_bonus_2",
                        "expenses_interest_1",
                        "expenses_interest_2",
                        "expenses_rent_1",
                        "expenses_rent_2",
                        "expenses_food_patients_1",
                        "expenses_food_patients_2",
                        "expenses_free_food_to_employees_1",
                        "expenses_free_food_to_employees_2",
                        "expenses_uniforms_1",
                        "expenses_uniforms_2",
                        "expenses_depreciation_1",
                        "expenses_depreciation_2",
                        "expenses_bad_debts_1",
                        "expenses_bad_debts_2",
                        "expenses_donations_1",
                        "expenses_donations_2",
                        "expenses_sales_tax_1",
                        "expenses_sales_tax_2",
                        "expenses_machinery_1",
                        "expenses_machinery_2",
                        "expenses_on_other_purchases_1",
                        "expenses_on_other_purchases_2",
                        "expenses_licenses_1",
                        "expenses_licenses_2",
                        "expenses_other_operating_1",
                        "expenses_other_operating_2",
                        "net_profit_loss_1",
                        "net_profit_loss_2",
                        "net_profit_loss_income_tax_1",
                        "net_profit_loss_income_tax_2",
                        "net_profit_after_tax_1",
                        "net_profit_after_tax_2",
                        "sales_and_use_withheld_1",
                        "sales_and_use_withheld_2",
                        "name",
                        "rank",
                    ]
                )

            writer.writerow(
                [
                    company_name,
                    address,
                    email,
                    liaison_officer,
                    ssn,
                    tel,
                    fax,
                    legal_form,
                    cfc,
                    business_type,
                    business_function,
                    branches,
                    branches_yes,
                    closing_date,
                    start_year,
                    end_year,
                    patients_service_revenue_from_persons_1,
                    patients_service_revenue_from_persons_2,
                    patients_service_revenue_from_industries_business_1,
                    patients_service_revenue_from_industries_business_2,
                    contractual_adjustments_1,
                    contractual_adjustments_2,
                    net_patient_service_revenue_1,
                    net_patient_service_revenue_2,
                    other_incomes_1,
                    other_incomes_2,
                    other_incomes_rent_1,
                    other_incomes_rent_2,
                    other_incomes_interest_1,
                    other_incomes_interest_2,
                    other_incomes_capital_gain_loss_1,
                    other_incomes_capital_gain_loss_2,
                    other_incomes_operating_1,
                    other_incomes_operating_2,
                    total_incomes_1,
                    total_incomes_2,
                    total_expenses_1,
                    total_expenses_2,
                    expenses_salaries_wages_bonus_1,
                    expenses_salaries_wages_bonus_2,
                    expenses_interest_1,
                    expenses_interest_2,
                    expenses_rent_1,
                    expenses_rent_2,
                    expenses_food_patients_1,
                    expenses_food_patients_2,
                    expenses_free_food_to_employees_1,
                    expenses_free_food_to_employees_2,
                    expenses_uniforms_1,
                    expenses_uniforms_2,
                    expenses_depreciation_1,
                    expenses_depreciation_2,
                    expenses_bad_debts_1,
                    expenses_bad_debts_2,
                    expenses_donations_1,
                    expenses_donations_2,
                    expenses_sales_tax_1,
                    expenses_sales_tax_2,
                    expenses_machinery_1,
                    expenses_machinery_2,
                    expenses_on_other_purchases_1,
                    expenses_on_other_purchases_2,
                    expenses_licenses_1,
                    expenses_licenses_2,
                    expenses_other_operating_1,
                    expenses_other_operating_2,
                    net_profit_loss_1,
                    net_profit_loss_2,
                    net_profit_loss_income_tax_1,
                    net_profit_loss_income_tax_2,
                    net_profit_after_tax_1,
                    net_profit_after_tax_2,
                    sales_and_use_withheld_1,
                    sales_and_use_withheld_2,
                    name,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-620.csv",
            dtypes={
                "company_name": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "ssn": str,
                "tel": str,
                "fax": str,
                "legal_form": str,
                "cfc": str,
                "business_type": str,
                "business_function": str,
                "branches": str,
                "branches_yes": str,
                "closing_date": str,
                "start_year": int,
                "end_year": int,
                "patients_service_revenue_from_persons_1": float,
                "patients_service_revenue_from_persons_2": float,
                "patients_service_revenue_from_industries_business_1": float,
                "patients_service_revenue_from_industries_business_2": float,
                "contractual_adjustments_1": float,
                "contractual_adjustments_2": float,
                "net_patient_service_revenue_1": float,
                "net_patient_service_revenue_2": float,
                "other_incomes_1": float,
                "other_incomes_2": float,
                "other_incomes_rent_1": float,
                "other_incomes_rent_2": float,
                "other_incomes_interest_1": float,
                "other_incomes_interest_2": float,
                "other_incomes_capital_gain_loss_1": float,
                "other_incomes_capital_gain_loss_2": float,
                "other_incomes_operating_1": float,
                "other_incomes_operating_2": float,
                "total_incomes_1": float,
                "total_incomes_2": float,
                "total_expenses_1": float,
                "total_expenses_2": float,
                "expenses_salaries_wages_bonus_1": float,
                "expenses_salaries_wages_bonus_2": float,
                "expenses_interest_1": float,
                "expenses_interest_2": float,
                "expenses_rent_1": float,
                "expenses_rent_2": float,
                "expenses_food_patients_1": float,
                "expenses_food_patients_2": float,
                "expenses_free_food_to_employees_1": float,
                "expenses_free_food_to_employees_2": float,
                "expenses_uniforms_1": float,
                "expenses_uniforms_2": float,
                "expenses_depreciation_1": float,
                "expenses_depreciation_2": float,
                "expenses_bad_debts_1": float,
                "expenses_bad_debts_2": float,
                "expenses_donations_1": float,
                "expenses_donations_2": float,
                "expenses_sales_tax_1": float,
                "expenses_sales_tax_2": float,
                "expenses_machinery_1": float,
                "expenses_machinery_2": float,
                "expenses_on_other_purchases_1": float,
                "expenses_on_other_purchases_2": float,
                "expenses_licenses_1": float,
                "expenses_licenses_2": float,
                "expenses_other_operating_1": float,
                "expenses_other_operating_2": float,
                "net_profit_loss_1": float,
                "net_profit_loss_2": float,
                "net_profit_loss_income_tax_1": float,
                "net_profit_loss_income_tax_2": float,
                "net_profit_after_tax_1": float,
                "net_profit_after_tax_2": float,
                "sales_and_use_withheld_1": float,
                "sales_and_use_withheld_2": float,
                "name": str,
                "rank": str,
            },
            table_name="IP_620",
            table_id=22,
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-620.html")


def IP_540P(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get("company_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")

        legal_form = request.POST.get("legal_form")
        cfc = request.POST.get("cfc")
        business_type = request.POST.get("business_type")
        business_function = request.POST.get("business_function")
        branches = request.POST.get("branches")
        branches_yes = request.POST.get("branches_yes")
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")

        incomes_from_persons_1 = request.POST.get("incomes_from_persons_1")
        incomes_from_persons_2 = request.POST.get("incomes_from_persons_2")
        incomes_from_industries_and_businesses_1 = request.POST.get(
            "incomes_from_industries_and_businesses_1"
        )
        incomes_from_industries_and_businesses_2 = request.POST.get(
            "incomes_from_industries_and_businesses_2"
        )
        incomes_commissions_received_1 = request.POST.get(
            "incomes_commissions_received_1"
        )
        incomes_commissions_received_2 = request.POST.get(
            "incomes_commissions_received_2"
        )
        incomes_from_air_fare_1 = request.POST.get("incomes_from_air_fare_1")
        incomes_from_air_fare_2 = request.POST.get("incomes_from_air_fare_2")
        incomes_from_maritime_1 = request.POST.get("incomes_from_maritime_1")
        incomes_from_maritime_2 = request.POST.get("incomes_from_maritime_2")
        incomes_rent_1 = request.POST.get("incomes_rent_1")
        incomes_rent_2 = request.POST.get("incomes_rent_2")
        incomes_interests_1 = request.POST.get("incomes_interests_1")
        incomes_interests_2 = request.POST.get("incomes_interests_2")
        incomes_capital_gain_loss_1 = request.POST.get("incomes_capital_gain_loss_1")
        incomes_capital_gain_loss_2 = request.POST.get("incomes_capital_gain_loss_2")
        incomes_other_operating_1 = request.POST.get("incomes_other_operating_1")
        incomes_other_operating_2 = request.POST.get("incomes_other_operating_2")
        total_incomes_1 = request.POST.get("total_incomes_1")
        total_incomes_2 = request.POST.get("total_incomes_2")
        expenses_salaries_wages_bonus_1 = request.POST.get(
            "expenses_salaries_wages_bonus_1"
        )
        expenses_salaries_wages_bonus_2 = request.POST.get(
            "expenses_salaries_wages_bonus_2"
        )
        expenses_interests_1 = request.POST.get("expenses_interests_1")
        expenses_interests_2 = request.POST.get("expenses_interests_2")
        expenses_rent_1 = request.POST.get("expenses_rent_1")
        expenses_rent_2 = request.POST.get("expenses_rent_2")
        expenses_depreciation_1 = request.POST.get("expenses_depreciation_1")
        expenses_depreciation_2 = request.POST.get("expenses_depreciation_2")
        expenses_donations_1 = request.POST.get("expenses_donations_1")
        expenses_donations_2 = request.POST.get("expenses_donations_2")
        expenses_sales_taxes_1 = request.POST.get("expenses_sales_taxes_1")
        expenses_sales_taxes_2 = request.POST.get("expenses_sales_taxes_2")
        expenses_purchases_machinery_1 = request.POST.get(
            "expenses_purchases_machinery_1"
        )
        expenses_purchases_machinery_2 = request.POST.get(
            "expenses_purchases_machinery_2"
        )
        expenses_other_purchases_1 = request.POST.get("expenses_other_purchases_1")
        expenses_other_purchases_2 = request.POST.get("expenses_other_purchases_2")
        expenses_licenses_1 = request.POST.get("expenses_licenses_1")
        expenses_licenses_2 = request.POST.get("expenses_licenses_2")
        expenses_other_operating_1 = request.POST.get("expenses_other_operating_1")
        expenses_other_operating_2 = request.POST.get("expenses_other_operating_2")
        total_expenses_1 = request.POST.get("total_expenses_1")
        total_expenses_2 = request.POST.get("total_expenses_2")
        net_profit_1 = request.POST.get("net_profit_1")
        net_profit_2 = request.POST.get("net_profit_2")
        profit_income_tax_1 = request.POST.get("profit_income_tax_1")
        profit_income_tax_2 = request.POST.get("profit_income_tax_2")
        profit_after_income_tax_1 = request.POST.get("profit_after_income_tax_1")
        profit_after_income_tax_2 = request.POST.get("profit_after_income_tax_2")
        sales_tax_withheld_1 = request.POST.get("sales_tax_withheld_1")
        sales_tax_withheld_2 = request.POST.get("sales_tax_withheld_2")

        name = request.POST.get("name")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-540P.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "company_name",
                        "address",
                        "email",
                        "liaison_officer",
                        "ssn",
                        "tel",
                        "fax",
                        "legal_form",
                        "cfc",
                        "business_type",
                        "business_function",
                        "branches",
                        "branches_yes",
                        "closing_date",
                        "start_year",
                        "end_year",
                        "incomes_from_persons_1",
                        "incomes_from_persons_2",
                        "incomes_from_industries_and_businesses_1",
                        "incomes_from_industries_and_businesses_2",
                        "incomes_commissions_received_1",
                        "incomes_commissions_received_2",
                        "incomes_from_air_fare_1",
                        "incomes_from_air_fare_2",
                        "incomes_from_maritime_1",
                        "incomes_from_maritime_2",
                        "incomes_rent_1",
                        "incomes_rent_2",
                        "incomes_interests_1",
                        "incomes_interests_2",
                        "incomes_capital_gain_loss_1",
                        "incomes_capital_gain_loss_2",
                        "incomes_other_operating_1",
                        "incomes_other_operating_2",
                        "total_incomes_1",
                        "total_incomes_2",
                        "expenses_salaries_wages_bonus_1",
                        "expenses_salaries_wages_bonus_2",
                        "expenses_interests_1",
                        "expenses_interests_2",
                        "expenses_rent_1",
                        "expenses_rent_2",
                        "expenses_depreciation_1",
                        "expenses_depreciation_2",
                        "expenses_donations_1",
                        "expenses_donations_2",
                        "expenses_sales_taxes_1",
                        "expenses_sales_taxes_2",
                        "expenses_purchases_machinery_1",
                        "expenses_purchases_machinery_2",
                        "expenses_other_purchases_1",
                        "expenses_other_purchases_2",
                        "expenses_licenses_1",
                        "expenses_licenses_2",
                        "expenses_other_operating_1",
                        "expenses_other_operating_2",
                        "total_expenses_1",
                        "total_expenses_2",
                        "net_profit_1",
                        "net_profit_2",
                        "profit_income_tax_1",
                        "profit_income_tax_2",
                        "profit_after_income_tax_1",
                        "profit_after_income_tax_2",
                        "sales_tax_withheld_1",
                        "sales_tax_withheld_2",
                        "name",
                        "rank",
                    ]
                )

            writer.writerow(
                [
                    company_name,
                    address,
                    email,
                    liaison_officer,
                    ssn,
                    tel,
                    fax,
                    legal_form,
                    cfc,
                    business_type,
                    business_function,
                    branches,
                    branches_yes,
                    closing_date,
                    start_year,
                    end_year,
                    incomes_from_persons_1,
                    incomes_from_persons_2,
                    incomes_from_industries_and_businesses_1,
                    incomes_from_industries_and_businesses_2,
                    incomes_commissions_received_1,
                    incomes_commissions_received_2,
                    incomes_from_air_fare_1,
                    incomes_from_air_fare_2,
                    incomes_from_maritime_1,
                    incomes_from_maritime_2,
                    incomes_rent_1,
                    incomes_rent_2,
                    incomes_interests_1,
                    incomes_interests_2,
                    incomes_capital_gain_loss_1,
                    incomes_capital_gain_loss_2,
                    incomes_other_operating_1,
                    incomes_other_operating_2,
                    total_incomes_1,
                    total_incomes_2,
                    expenses_salaries_wages_bonus_1,
                    expenses_salaries_wages_bonus_2,
                    expenses_interests_1,
                    expenses_interests_2,
                    expenses_rent_1,
                    expenses_rent_2,
                    expenses_depreciation_1,
                    expenses_depreciation_2,
                    expenses_donations_1,
                    expenses_donations_2,
                    expenses_sales_taxes_1,
                    expenses_sales_taxes_2,
                    expenses_purchases_machinery_1,
                    expenses_purchases_machinery_2,
                    expenses_other_purchases_1,
                    expenses_other_purchases_2,
                    expenses_licenses_1,
                    expenses_licenses_2,
                    expenses_other_operating_1,
                    expenses_other_operating_2,
                    total_expenses_1,
                    total_expenses_2,
                    net_profit_1,
                    net_profit_2,
                    profit_income_tax_1,
                    profit_income_tax_2,
                    profit_after_income_tax_1,
                    profit_after_income_tax_2,
                    sales_tax_withheld_1,
                    sales_tax_withheld_2,
                    name,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-540P.csv",
            dtypes={
                "company_name": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "ssn": str,
                "tel": str,
                "fax": str,
                "legal_form": str,
                "cfc": str,
                "business_type": str,
                "business_function": str,
                "branches": str,
                "branches_yes": str,
                "closing_date": str,
                "start_year": int,
                "end_year": int,
                "incomes_from_persons_1": float,
                "incomes_from_persons_2": float,
                "incomes_from_industries_and_businesses_1": float,
                "incomes_from_industries_and_businesses_2": float,
                "incomes_commissions_received_1": float,
                "incomes_commissions_received_2": float,
                "incomes_from_air_fare_1": float,
                "incomes_from_air_fare_2": float,
                "incomes_from_maritime_1": float,
                "incomes_from_maritime_2": float,
                "incomes_rent_1": float,
                "incomes_rent_2": float,
                "incomes_interests_1": float,
                "incomes_interests_2": float,
                "incomes_capital_gain_loss_1": float,
                "incomes_capital_gain_loss_2": float,
                "incomes_other_operating_1": float,
                "incomes_other_operating_2": float,
                "total_incomes_1": float,
                "total_incomes_2": float,
                "expenses_salaries_wages_bonus_1": float,
                "expenses_salaries_wages_bonus_2": float,
                "expenses_interests_1": float,
                "expenses_interests_2": float,
                "expenses_rent_1": float,
                "expenses_rent_2": float,
                "expenses_depreciation_1": float,
                "expenses_depreciation_2": float,
                "expenses_donations_1": float,
                "expenses_donations_2": float,
                "expenses_sales_taxes_1": float,
                "expenses_sales_taxes_2": float,
                "expenses_purchases_machinery_1": float,
                "expenses_purchases_machinery_2": float,
                "expenses_other_purchases_1": float,
                "expenses_other_purchases_2": float,
                "expenses_licenses_1": float,
                "expenses_licenses_2": float,
                "expenses_other_operating_1": float,
                "expenses_other_operating_2": float,
                "total_expenses_1": float,
                "total_expenses_2": float,
                "net_profit_1": float,
                "net_profit_2": float,
                "profit_income_tax_1": float,
                "profit_income_tax_2": float,
                "profit_after_income_tax_1": float,
                "profit_after_income_tax_2": float,
                "sales_tax_withheld_1": float,
                "sales_tax_withheld_2": float,
                "name": str,
                "rank": str,
            },
            table_name="IP_540P",
            table_id=20,
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-540P.html")


def IP_540S(request):

    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get("company_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")
        legal_form = request.POST.get("legal_form")
        cfc = request.POST.get("cfc")
        business_type = request.POST.get("business_type")
        business_function = request.POST.get("business_function")
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        incomes_from_persons_1 = request.POST.get("incomes_from_persons_1")
        incomes_from_persons_2 = request.POST.get("incomes_from_persons_2")
        incomes_from_industries_and_businesses_1 = request.POST.get(
            "incomes_from_industries_and_businesses_1"
        )
        incomes_from_industries_and_businesses_2 = request.POST.get(
            "incomes_from_industries_and_businesses_2"
        )
        expenses_newspapers_1 = request.POST.get("expenses_newspapers_1")
        expenses_newspapers_2 = request.POST.get("expenses_newspapers_2")
        expenses_radio_1 = request.POST.get("expenses_radio_1")
        expenses_radio_2 = request.POST.get("expenses_radio_2")
        expenses_other_1 = request.POST.get("expenses_other_1")
        expenses_other_2 = request.POST.get("expenses_other_2")
        gross_profit_1 = request.POST.get("gross_profit_1")
        gross_profit_2 = request.POST.get("gross_profit_2")
        gross_other_income_1 = request.POST.get("gross_other_income_1")
        gross_other_income_2 = request.POST.get("gross_other_income_2")
        gross_interests_1 = request.POST.get("gross_interests_1")
        gross_interests_2 = request.POST.get("gross_interests_2")
        gross_rent_land_1 = request.POST.get("gross_rent_land_1")
        gross_rent_land_2 = request.POST.get("gross_rent_land_2")
        gross_capital_gain_1 = request.POST.get("gross_capital_gain_1")
        gross_capital_gain_2 = request.POST.get("gross_capital_gain_2")
        gross_other_1 = request.POST.get("gross_other_1")
        gross_other_2 = request.POST.get("gross_other_2")
        income_total_income_1 = request.POST.get("income_total_income_1")
        income_total_income_2 = request.POST.get("income_total_income_2")
        income_total_expenses_1 = request.POST.get("income_total_expenses_1")
        income_total_expenses_2 = request.POST.get("income_total_expenses_2")
        expenses_salaries_wages_bonus_1 = request.POST.get(
            "expenses_salaries_wages_bonus_1"
        )
        expenses_salaries_wages_bonus_2 = request.POST.get(
            "expenses_salaries_wages_bonus_2"
        )
        expenses_interests_1 = request.POST.get("expenses_interests_1")
        expenses_interests_2 = request.POST.get("expenses_interests_2")
        expenses_rent_1 = request.POST.get("expenses_rent_1")
        expenses_rent_2 = request.POST.get("expenses_rent_2")
        expenses_depreciation_1 = request.POST.get("expenses_depreciation_1")
        expenses_depreciation_2 = request.POST.get("expenses_depreciation_2")
        expenses_other_taxes_1 = request.POST.get("expenses_other_taxes_1")
        expenses_other_taxes_2 = request.POST.get("expenses_other_taxes_2")
        expenses_donations_1 = request.POST.get("expenses_donations_1")
        expenses_donations_2 = request.POST.get("expenses_donations_2")
        expenses_sales_taxes_1 = request.POST.get("expenses_sales_taxes_1")
        expenses_sales_taxes_2 = request.POST.get("expenses_sales_taxes_2")
        expenses_purchases_machinery_1 = request.POST.get(
            "expenses_purchases_machinery_1"
        )
        expenses_purchases_machinery_2 = request.POST.get(
            "expenses_purchases_machinery_2"
        )
        expenses_other_purchases_1 = request.POST.get("expenses_other_purchases_1")
        expenses_other_purchases_2 = request.POST.get("expenses_other_purchases_2")
        expenses_licenses_1 = request.POST.get("expenses_licenses_1")
        expenses_licenses_2 = request.POST.get("expenses_licenses_2")
        expenses_other_operation_1 = request.POST.get("expenses_other_operation_1")
        expenses_other_operation_2 = request.POST.get("expenses_other_operation_2")
        net_profit_1 = request.POST.get("net_profit_1")
        net_profit_2 = request.POST.get("net_profit_2")
        profit_income_tax_1 = request.POST.get("profit_income_tax_1")
        profit_income_tax_2 = request.POST.get("profit_income_tax_2")
        profit_after_income_tax_1 = request.POST.get("profit_after_income_tax_1")
        profit_after_income_tax_2 = request.POST.get("profit_after_income_tax_2")
        sales_tax_withheld_1 = request.POST.get("sales_tax_withheld_1")
        sales_tax_withheld_2 = request.POST.get("sales_tax_withheld_2")
        name = request.POST.get("name")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-540S.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "company_name",
                        "address",
                        "email",
                        "liaison_officer",
                        "ssn",
                        "tel",
                        "fax",
                        "legal_form",
                        "cfc",
                        "business_type",
                        "business_function",
                        "closing_date",
                        "start_year",
                        "end_year",
                        "incomes_from_persons_1",
                        "incomes_from_persons_2",
                        "incomes_from_industries_and_businesses_1",
                        "incomes_from_industries_and_businesses_2",
                        "expenses_newspapers_1",
                        "expenses_newspapers_2",
                        "expenses_radio_1",
                        "expenses_radio_2",
                        "expenses_other_1",
                        "expenses_other_2",
                        "gross_profit_1",
                        "gross_profit_2",
                        "gross_other_income_1",
                        "gross_other_income_2",
                        "gross_interests_1",
                        "gross_interests_2",
                        "gross_rent_land_1",
                        "gross_rent_land_2",
                        "gross_capital_gain_1",
                        "gross_capital_gain_2",
                        "gross_other_1",
                        "gross_other_2",
                        "income_total_income_1",
                        "income_total_income_2",
                        "income_total_expenses_1",
                        "income_total_expenses_2",
                        "expenses_salaries_wages_bonus_1",
                        "expenses_salaries_wages_bonus_2",
                        "expenses_interests_1",
                        "expenses_interests_2",
                        "expenses_rent_1",
                        "expenses_rent_2",
                        "expenses_depreciation_1",
                        "expenses_depreciation_2",
                        "expenses_other_taxes_1",
                        "expenses_other_taxes_2",
                        "expenses_donations_1",
                        "expenses_donations_2",
                        "expenses_sales_taxes_1",
                        "expenses_sales_taxes_2",
                        "expenses_purchases_machinery_1",
                        "expenses_purchases_machinery_2",
                        "expenses_other_purchases_1",
                        "expenses_other_purchases_2",
                        "expenses_licenses_1",
                        "expenses_licenses_2",
                        "expenses_other_operation_1",
                        "expenses_other_operation_2",
                        "net_profit_1",
                        "net_profit_2",
                        "profit_income_tax_1",
                        "profit_income_tax_2",
                        "profit_after_income_tax_1",
                        "profit_after_income_tax_2",
                        "sales_tax_withheld_1",
                        "sales_tax_withheld_2",
                        "name",
                        "rank",
                    ]
                )

            writer.writerow(
                [
                    company_name,
                    address,
                    email,
                    liaison_officer,
                    ssn,
                    tel,
                    fax,
                    legal_form,
                    cfc,
                    business_type,
                    business_function,
                    closing_date,
                    start_year,
                    end_year,
                    incomes_from_persons_1,
                    incomes_from_persons_2,
                    incomes_from_industries_and_businesses_1,
                    incomes_from_industries_and_businesses_2,
                    expenses_newspapers_1,
                    expenses_newspapers_2,
                    expenses_radio_1,
                    expenses_radio_2,
                    expenses_other_1,
                    expenses_other_2,
                    gross_profit_1,
                    gross_profit_2,
                    gross_other_income_1,
                    gross_other_income_2,
                    gross_interests_1,
                    gross_interests_2,
                    gross_rent_land_1,
                    gross_rent_land_2,
                    gross_capital_gain_1,
                    gross_capital_gain_2,
                    gross_other_1,
                    gross_other_2,
                    income_total_income_1,
                    income_total_income_2,
                    income_total_expenses_1,
                    income_total_expenses_2,
                    expenses_salaries_wages_bonus_1,
                    expenses_salaries_wages_bonus_2,
                    expenses_interests_1,
                    expenses_interests_2,
                    expenses_rent_1,
                    expenses_rent_2,
                    expenses_depreciation_1,
                    expenses_depreciation_2,
                    expenses_other_taxes_1,
                    expenses_other_taxes_2,
                    expenses_donations_1,
                    expenses_donations_2,
                    expenses_sales_taxes_1,
                    expenses_sales_taxes_2,
                    expenses_purchases_machinery_1,
                    expenses_purchases_machinery_2,
                    expenses_other_purchases_1,
                    expenses_other_purchases_2,
                    expenses_licenses_1,
                    expenses_licenses_2,
                    expenses_other_operation_1,
                    expenses_other_operation_2,
                    net_profit_1,
                    net_profit_2,
                    profit_income_tax_1,
                    profit_income_tax_2,
                    profit_after_income_tax_1,
                    profit_after_income_tax_2,
                    sales_tax_withheld_1,
                    sales_tax_withheld_2,
                    name,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-540S.csv",
            dtypes={
                "company_name": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "ssn": str,
                "tel": str,
                "fax": str,
                "legal_form": str,
                "cfc": str,
                "business_type": str,
                "business_function": str,
                "closing_date": str,
                "start_year": int,
                "end_year": int,
                "incomes_from_persons_1": float,
                "incomes_from_persons_2": float,
                "incomes_from_industries_and_businesses_1": float,
                "incomes_from_industries_and_businesses_2": float,
                "expenses_newspapers_1": float,
                "expenses_newspapers_2": float,
                "expenses_radio_1": float,
                "expenses_radio_2": float,
                "expenses_other_1": float,
                "expenses_other_2": float,
                "gross_profit_1": float,
                "gross_profit_2": float,
                "gross_other_income_1": float,
                "gross_other_income_2": float,
                "gross_interests_1": float,
                "gross_interests_2": float,
                "gross_rent_land_1": float,
                "gross_rent_land_2": float,
                "gross_capital_gain_1": float,
                "gross_capital_gain_2": float,
                "gross_other_1": float,
                "gross_other_2": float,
                "income_total_income_1": float,
                "income_total_income_2": float,
                "income_total_expenses_1": float,
                "income_total_expenses_2": float,
                "expenses_salaries_wages_bonus_1": float,
                "expenses_salaries_wages_bonus_2": float,
                "expenses_interests_1": float,
                "expenses_interests_2": float,
                "expenses_rent_1": float,
                "expenses_rent_2": float,
                "expenses_depreciation_1": float,
                "expenses_depreciation_2": float,
                "expenses_other_taxes_1": float,
                "expenses_other_taxes_2": float,
                "expenses_donations_1": float,
                "expenses_donations_2": float,
                "expenses_sales_taxes_1": float,
                "expenses_sales_taxes_2": float,
                "expenses_purchases_machinery_1": float,
                "expenses_purchases_machinery_2": float,
                "expenses_other_purchases_1": float,
                "expenses_other_purchases_2": float,
                "expenses_licenses_1": float,
                "expenses_licenses_2": float,
                "expenses_other_operation_1": float,
                "expenses_other_operation_2": float,
                "net_profit_1": float,
                "net_profit_2": float,
                "profit_income_tax_1": float,
                "profit_income_tax_2": float,
                "profit_after_income_tax_1": float,
                "profit_after_income_tax_2": float,
                "sales_tax_withheld_1": float,
                "sales_tax_withheld_2": float,
                "name": str,
                "rank": str,
            },
            table_name="IP_540S",
            table_id=16,
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-540S.html")


def IP_540a(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get("company_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")
        legal_form = request.POST.get("legal_form")
        cfc = request.POST.get("cfc")
        business_type = request.POST.get("business_type")
        business_function = request.POST.get("business_function")
        closing_date = request.POST.get("closing_date")

        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")

        billing_1 = request.POST.get("billing_1")
        billing_2 = request.POST.get("billing_2")
        incomes_from_persons_1 = request.POST.get("incomes_from_persons_1")
        incomes_from_persons_2 = request.POST.get("incomes_from_persons_2")
        incomes_from_industries_and_businesses_1 = request.POST.get(
            "incomes_from_industries_and_businesses_1"
        )
        incomes_from_industries_and_businesses_2 = request.POST.get(
            "incomes_from_industries_and_businesses_2"
        )

        billing_expenses_1 = request.POST.get("billing_expenses_1")
        billing_expenses_2 = request.POST.get("billing_expenses_2")
        expenses_newspapers_1 = request.POST.get("expenses_newspapers_1")
        expenses_newspapers_2 = request.POST.get("expenses_newspapers_2")
        expenses_radio_television_1 = request.POST.get("expenses_radio_television_1")
        expenses_radio_television_2 = request.POST.get("expenses_radio_television_2")
        expenses_others_1 = request.POST.get("expenses_others_1")
        expenses_others_2 = request.POST.get("expenses_others_2")

        gross_profit_1 = request.POST.get("gross_profit_1")
        gross_profit_2 = request.POST.get("gross_profit_2")

        other_incomes_1 = request.POST.get("other_incomes_1")
        other_incomes_2 = request.POST.get("other_incomes_2")
        other_interests_1 = request.POST.get("other_interests_1")
        other_interests_2 = request.POST.get("other_interests_2")
        rent_of_land_1 = request.POST.get("rent_of_land_1")
        rent_of_land_2 = request.POST.get("rent_of_land_2")
        capital_1 = request.POST.get("capital_1")
        capital_2 = request.POST.get("capital_2")
        others_1 = request.POST.get("others_1")
        others_2 = request.POST.get("others_2")

        total_incomes_1 = request.POST.get("total_incomes_1")
        total_incomes_2 = request.POST.get("total_incomes_2")

        total_expenses_1 = request.POST.get("total_expenses_1")
        total_expenses_2 = request.POST.get("total_expenses_2")
        expenses_salaries_bonus_1 = request.POST.get("expenses_salaries_bonus_1")
        expenses_salaries_bonus_2 = request.POST.get("expenses_salaries_bonus_2")
        expenses_interests_1 = request.POST.get("expenses_interests_1")
        expenses_interests_2 = request.POST.get("expenses_interests_2")
        expenses_rent_1 = request.POST.get("expenses_rent_1")
        expenses_rent_2 = request.POST.get("expenses_rent_2")
        expenses_depreciation_1 = request.POST.get("expenses_depreciation_1")
        expenses_depreciation_2 = request.POST.get("expenses_depreciation_2")
        expenses_other_donations_1 = request.POST.get("expenses_other_donations_1")
        expenses_other_donations_2 = request.POST.get("expenses_other_donations_2")
        expenses_donations_1 = request.POST.get("expenses_donations_1")
        expenses_donations_2 = request.POST.get("expenses_donations_2")
        expenses_sales_taxes_1 = request.POST.get("expenses_sales_taxes_1")
        expenses_sales_taxes_2 = request.POST.get("expenses_sales_taxes_2")
        expenses_purchases_machinery_1 = request.POST.get(
            "expenses_purchases_machinery_1"
        )
        expenses_purchases_machinery_2 = request.POST.get(
            "expenses_purchases_machinery_2"
        )
        expenses_other_purchases_1 = request.POST.get("expenses_other_purchases_1")
        expenses_other_purchases_2 = request.POST.get("expenses_other_purchases_2")
        expenses_licenses_1 = request.POST.get("expenses_licenses_1")
        expenses_licenses_2 = request.POST.get("expenses_licenses_2")
        expenses_other_operationg_1 = request.POST.get("expenses_other_operationg_1")
        expenses_other_operationg_2 = request.POST.get("expenses_other_operationg_2")

        net_profit_1 = request.POST.get("net_profit_1")
        net_profit_2 = request.POST.get("net_profit_2")
        profit_income_tax_1 = request.POST.get("profit_income_tax_1")
        profit_income_tax_2 = request.POST.get("profit_income_tax_2")
        profit_after_income_tax_1 = request.POST.get("profit_after_income_tax_1")
        profit_after_income_tax_2 = request.POST.get("profit_after_income_tax_2")

        sales_tax_withheld_1 = request.POST.get("sales_tax_withheld_1")
        sales_tax_withheld_2 = request.POST.get("sales_tax_withheld_2")

        name = request.POST.get("name")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-540a.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "company_name",
                        "address",
                        "email",
                        "liaison_officer",
                        "ssn",
                        "tel",
                        "fax",
                        "legal_form",
                        "cfc",
                        "business_type",
                        "business_function",
                        "closing_date",
                        "start_year",
                        "end_year",
                        "billing_1",
                        "billing_2",
                        "incomes_from_persons_1",
                        "incomes_from_persons_2",
                        "incomes_from_industries_and_businesses_1",
                        "incomes_from_industries_and_businesses_2",
                        "billing_expenses_1",
                        "billing_expenses_2",
                        "expenses_newspapers_1",
                        "expenses_newspapers_2",
                        "expenses_radio_television_1",
                        "expenses_radio_television_2",
                        "expenses_others_1",
                        "expenses_others_2",
                        "gross_profit_1",
                        "gross_profit_2",
                        "other_incomes_1",
                        "other_incomes_2",
                        "other_interests_1",
                        "other_interests_2",
                        "rent_of_land_1",
                        "rent_of_land_2",
                        "capital_1",
                        "capital_2",
                        "others_1",
                        "others_2",
                        "total_incomes_1",
                        "total_incomes_2",
                        "total_expenses_1",
                        "total_expenses_2",
                        "expenses_salaries_bonus_1",
                        "expenses_salaries_bonus_2",
                        "expenses_interests_1",
                        "expenses_interests_2",
                        "expenses_rent_1",
                        "expenses_rent_2",
                        "expenses_depreciation_1",
                        "expenses_depreciation_2",
                        "expenses_other_donations_1",
                        "expenses_other_donations_2",
                        "expenses_donations_1",
                        "expenses_donations_2",
                        "expenses_sales_taxes_1",
                        "expenses_sales_taxes_2",
                        "expenses_purchases_machinery_1",
                        "expenses_purchases_machinery_2",
                        "expenses_other_purchases_1",
                        "expenses_other_purchases_2",
                        "expenses_licenses_1",
                        "expenses_licenses_2",
                        "expenses_other_operationg_1",
                        "expenses_other_operationg_2",
                        "net_profit_1",
                        "net_profit_2",
                        "profit_income_tax_1",
                        "profit_income_tax_2",
                        "profit_after_income_tax_1",
                        "profit_after_income_tax_2",
                        "sales_tax_withheld_1",
                        "sales_tax_withheld_2",
                        "name",
                        "rank",
                    ]
                )

            writer.writerow(
                [
                    company_name,
                    address,
                    email,
                    liaison_officer,
                    ssn,
                    tel,
                    fax,
                    legal_form,
                    cfc,
                    business_type,
                    business_function,
                    closing_date,
                    start_year,
                    end_year,
                    billing_1,
                    billing_2,
                    incomes_from_persons_1,
                    incomes_from_persons_2,
                    incomes_from_industries_and_businesses_1,
                    incomes_from_industries_and_businesses_2,
                    billing_expenses_1,
                    billing_expenses_2,
                    expenses_newspapers_1,
                    expenses_newspapers_2,
                    expenses_radio_television_1,
                    expenses_radio_television_2,
                    expenses_others_1,
                    expenses_others_2,
                    gross_profit_1,
                    gross_profit_2,
                    other_incomes_1,
                    other_incomes_2,
                    other_interests_1,
                    other_interests_2,
                    rent_of_land_1,
                    rent_of_land_2,
                    capital_1,
                    capital_2,
                    others_1,
                    others_2,
                    total_incomes_1,
                    total_incomes_2,
                    total_expenses_1,
                    total_expenses_2,
                    expenses_salaries_bonus_1,
                    expenses_salaries_bonus_2,
                    expenses_interests_1,
                    expenses_interests_2,
                    expenses_rent_1,
                    expenses_rent_2,
                    expenses_depreciation_1,
                    expenses_depreciation_2,
                    expenses_other_donations_1,
                    expenses_other_donations_2,
                    expenses_donations_1,
                    expenses_donations_2,
                    expenses_sales_taxes_1,
                    expenses_sales_taxes_2,
                    expenses_purchases_machinery_1,
                    expenses_purchases_machinery_2,
                    expenses_other_purchases_1,
                    expenses_other_purchases_2,
                    expenses_licenses_1,
                    expenses_licenses_2,
                    expenses_other_operationg_1,
                    expenses_other_operationg_2,
                    net_profit_1,
                    net_profit_2,
                    profit_income_tax_1,
                    profit_income_tax_2,
                    profit_after_income_tax_1,
                    profit_after_income_tax_2,
                    sales_tax_withheld_1,
                    sales_tax_withheld_2,
                    name,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-540a.csv",
            dtypes={
                "company_name": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "ssn": str,
                "tel": str,
                "fax": str,
                "legal_form": str,
                "cfc": str,
                "business_type": str,
                "business_function": str,
                "closing_date": str,
                "start_year": int,
                "end_year": int,
                "billing_1": float,
                "billing_2": float,
                "incomes_from_persons_1": float,
                "incomes_from_persons_2": float,
                "incomes_from_industries_and_businesses_1": float,
                "incomes_from_industries_and_businesses_2": float,
                "billing_expenses_1": float,
                "billing_expenses_2": float,
                "expenses_newspapers_1": float,
                "expenses_newspapers_2": float,
                "expenses_radio_television_1": float,
                "expenses_radio_television_2": float,
                "expenses_others_1": float,
                "expenses_others_2": float,
                "gross_profit_1": float,
                "gross_profit_2": float,
                "other_incomes_1": float,
                "other_incomes_2": float,
                "other_interests_1": float,
                "other_interests_2": float,
                "rent_of_land_1": float,
                "rent_of_land_2": float,
                "capital_1": float,
                "capital_2": float,
                "others_1": float,
                "others_2": float,
                "total_incomes_1": float,
                "total_incomes_2": float,
                "total_expenses_1": float,
                "total_expenses_2": float,
                "expenses_salaries_bonus_1": float,
                "expenses_salaries_bonus_2": float,
                "expenses_interests_1": float,
                "expenses_interests_2": float,
                "expenses_rent_1": float,
                "expenses_rent_2": float,
                "expenses_depreciation_1": float,
                "expenses_depreciation_2": float,
                "expenses_other_donations_1": float,
                "expenses_other_donations_2": float,
                "expenses_donations_1": float,
                "expenses_donations_2": float,
                "expenses_sales_taxes_1": float,
                "expenses_sales_taxes_2": float,
                "expenses_purchases_machinery_1": float,
                "expenses_purchases_machinery_2": float,
                "expenses_other_purchases_1": float,
                "expenses_other_purchases_2": float,
                "expenses_licenses_1": float,
                "expenses_licenses_2": float,
                "expenses_other_operationg_1": float,
                "expenses_other_operationg_2": float,
                "net_profit_1": float,
                "net_profit_2": float,
                "profit_income_tax_1": float,
                "profit_income_tax_2": float,
                "profit_after_income_tax_1": float,
                "profit_after_income_tax_2": float,
                "sales_tax_withheld_1": float,
                "sales_tax_withheld_2": float,
                "name": str,
                "rank": str,
            },
            table_name="IP_540a",
            table_id=14,
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-540a.html")


def IP_540v(request):

    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get("company_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")
        legal_form = request.POST.get("legal_form")
        cfc = request.POST.get("cfc")
        business_type = request.POST.get("business_type")
        business_function = request.POST.get("business_function")
        branches = request.POST.get("branches")
        branches_yes = request.POST.get("branches_yes")
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        incomes_services_rendered_1 = request.POST.get("incomes_services_rendered_1")
        incomes_services_rendered_2 = request.POST.get("incomes_services_rendered_2")
        incomes_to_business_1 = request.POST.get("incomes_to_business_1")
        incomes_to_business_2 = request.POST.get("incomes_to_business_2")
        incomes_to_personal_pets_1 = request.POST.get("incomes_to_personal_pets_1")
        incomes_to_personal_pets_2 = request.POST.get("incomes_to_personal_pets_2")
        incomes_sale_merchandise_1 = request.POST.get("incomes_sale_merchandise_1")
        incomes_sale_merchandise_2 = request.POST.get("incomes_sale_merchandise_2")
        incomes_rent_of_land_and_building_1 = request.POST.get(
            "incomes_rent_of_land_and_building_1"
        )
        incomes_rent_of_land_and_building_2 = request.POST.get(
            "incomes_rent_of_land_and_building_2"
        )
        incomes_interests_1 = request.POST.get("incomes_interests_1")
        incomes_interests_2 = request.POST.get("incomes_interests_2")
        incomes_capital_gain_or_loss_1 = request.POST.get(
            "incomes_capital_gain_or_loss_1"
        )
        incomes_capital_gain_or_loss_2 = request.POST.get(
            "incomes_capital_gain_or_loss_2"
        )
        incomes_other_operating_income_1 = request.POST.get(
            "incomes_other_operating_income_1"
        )
        incomes_other_operating_income_2 = request.POST.get(
            "incomes_other_operating_income_2"
        )
        incomes_total_1 = request.POST.get("incomes_total_1")
        incomes_total_2 = request.POST.get("incomes_total_2")
        total_expenses_1 = request.POST.get("total_expenses_1")
        total_expenses_2 = request.POST.get("total_expenses_2")
        expenses_salaries_wages_bonus_1 = request.POST.get(
            "expenses_salaries_wages_bonus_1"
        )
        expenses_salaries_wages_bonus_2 = request.POST.get(
            "expenses_salaries_wages_bonus_2"
        )
        expenses_interests_1 = request.POST.get("expenses_interests_1")
        expenses_interests_2 = request.POST.get("expenses_interests_2")
        expenses_rent_1 = request.POST.get("expenses_rent_1")
        expenses_rent_2 = request.POST.get("expenses_rent_2")
        expenses_depreciation_1 = request.POST.get("expenses_depreciation_1")
        expenses_depreciation_2 = request.POST.get("expenses_depreciation_2")
        expenses_bad_debts_1 = request.POST.get("expenses_bad_debts_1")
        expenses_bad_debts_2 = request.POST.get("expenses_bad_debts_2")
        expenses_donations_1 = request.POST.get("expenses_donations_1")
        expenses_donations_2 = request.POST.get("expenses_donations_2")
        expenses_sales_taxes_1 = request.POST.get("expenses_sales_taxes_1")
        expenses_sales_taxes_2 = request.POST.get("expenses_sales_taxes_2")
        expenses_purchases_machinery_1 = request.POST.get(
            "expenses_purchases_machinery_1"
        )
        expenses_purchases_machinery_2 = request.POST.get(
            "expenses_purchases_machinery_2"
        )
        expenses_other_purchases_1 = request.POST.get("expenses_other_purchases_1")
        expenses_other_purchases_2 = request.POST.get("expenses_other_purchases_2")
        expenses_licenses_1 = request.POST.get("expenses_licenses_1")
        expenses_licenses_2 = request.POST.get("expenses_licenses_2")
        expenses_other_operating_1 = request.POST.get("expenses_other_operating_1")
        expenses_other_operating_2 = request.POST.get("expenses_other_operating_2")
        expenses_total_expenses_1 = request.POST.get("expenses_total_expenses_1")
        expenses_total_expenses_2 = request.POST.get("expenses_total_expenses_2")
        net_profit_1 = request.POST.get("net_profit_1")
        net_profit_2 = request.POST.get("net_profit_2")
        profit_income_tax_1 = request.POST.get("profit_income_tax_1")
        profit_income_tax_2 = request.POST.get("profit_income_tax_2")
        profit_after_income_tax_1 = request.POST.get("profit_after_income_tax_1")
        profit_after_income_tax_2 = request.POST.get("profit_after_income_tax_2")
        sales_tax_withheld_1 = request.POST.get("sales_tax_withheld_1")
        sales_tax_withheld_2 = request.POST.get("sales_tax_withheld_2")
        name = request.POST.get("name")
        rank = request.POST.get("name")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-540v.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "company_name",
                        "address",
                        "email",
                        "liaison_officer",
                        "ssn",
                        "tel",
                        "fax",
                        "legal_form",
                        "cfc",
                        "business_type",
                        "business_function",
                        "branches",
                        "branches_yes",
                        "closing_date",
                        "start_year",
                        "end_year",
                        "incomes_services_rendered_1",
                        "incomes_services_rendered_2",
                        "incomes_to_business_1",
                        "incomes_to_business_2",
                        "incomes_to_personal_pets_1",
                        "incomes_to_personal_pets_2",
                        "incomes_sale_merchandise_1",
                        "incomes_sale_merchandise_2",
                        "incomes_rent_of_land_and_building_1",
                        "incomes_rent_of_land_and_building_2",
                        "incomes_interests_1",
                        "incomes_interests_2",
                        "incomes_capital_gain_or_loss_1",
                        "incomes_capital_gain_or_loss_2",
                        "incomes_other_operating_income_1",
                        "incomes_other_operating_income_2",
                        "incomes_total_1",
                        "incomes_total_2",
                        "total_expenses_1",
                        "total_expenses_2",
                        "expenses_salaries_wages_bonus_1",
                        "expenses_salaries_wages_bonus_2",
                        "expenses_interests_1",
                        "expenses_interests_2",
                        "expenses_rent_1",
                        "expenses_rent_2",
                        "expenses_depreciation_1",
                        "expenses_depreciation_2",
                        "expenses_bad_debts_1",
                        "expenses_bad_debts_2",
                        "expenses_donations_1",
                        "expenses_donations_2",
                        "expenses_sales_taxes_1",
                        "expenses_sales_taxes_2",
                        "expenses_purchases_machinery_1",
                        "expenses_purchases_machinery_2",
                        "expenses_other_purchases_1",
                        "expenses_other_purchases_2",
                        "expenses_licenses_1",
                        "expenses_licenses_2",
                        "expenses_other_operating_1",
                        "expenses_other_operating_2",
                        "expenses_total_expenses_1",
                        "expenses_total_expenses_2",
                        "net_profit_1",
                        "net_profit_2",
                        "profit_income_tax_1",
                        "profit_income_tax_2",
                        "profit_after_income_tax_1",
                        "profit_after_income_tax_2",
                        "sales_tax_withheld_1",
                        "sales_tax_withheld_2",
                        "name",
                        "rank",
                    ]
                )

            writer.writerow(
                [
                    company_name,
                    address,
                    email,
                    liaison_officer,
                    ssn,
                    tel,
                    fax,
                    legal_form,
                    cfc,
                    business_type,
                    business_function,
                    branches,
                    branches_yes,
                    closing_date,
                    start_year,
                    end_year,
                    incomes_services_rendered_1,
                    incomes_services_rendered_2,
                    incomes_to_business_1,
                    incomes_to_business_2,
                    incomes_to_personal_pets_1,
                    incomes_to_personal_pets_2,
                    incomes_sale_merchandise_1,
                    incomes_sale_merchandise_2,
                    incomes_rent_of_land_and_building_1,
                    incomes_rent_of_land_and_building_2,
                    incomes_interests_1,
                    incomes_interests_2,
                    incomes_capital_gain_or_loss_1,
                    incomes_capital_gain_or_loss_2,
                    incomes_other_operating_income_1,
                    incomes_other_operating_income_2,
                    incomes_total_1,
                    incomes_total_2,
                    total_expenses_1,
                    total_expenses_2,
                    expenses_salaries_wages_bonus_1,
                    expenses_salaries_wages_bonus_2,
                    expenses_interests_1,
                    expenses_interests_2,
                    expenses_rent_1,
                    expenses_rent_2,
                    expenses_depreciation_1,
                    expenses_depreciation_2,
                    expenses_bad_debts_1,
                    expenses_bad_debts_2,
                    expenses_donations_1,
                    expenses_donations_2,
                    expenses_sales_taxes_1,
                    expenses_sales_taxes_2,
                    expenses_purchases_machinery_1,
                    expenses_purchases_machinery_2,
                    expenses_other_purchases_1,
                    expenses_other_purchases_2,
                    expenses_licenses_1,
                    expenses_licenses_2,
                    expenses_other_operating_1,
                    expenses_other_operating_2,
                    expenses_total_expenses_1,
                    expenses_total_expenses_2,
                    net_profit_1,
                    net_profit_2,
                    profit_income_tax_1,
                    profit_income_tax_2,
                    profit_after_income_tax_1,
                    profit_after_income_tax_2,
                    sales_tax_withheld_1,
                    sales_tax_withheld_2,
                    name,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-540v.csv",
            dtypes={
                "company_name": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "ssn": str,
                "tel": str,
                "fax": str,
                "legal_form": str,
                "cfc": str,
                "business_type": str,
                "business_function": str,
                "branches": str,
                "branches_yes": str,
                "closing_date": str,
                "start_year": int,
                "end_year": int,
                "incomes_services_rendered_1": float,
                "incomes_services_rendered_2": float,
                "incomes_to_business_1": float,
                "incomes_to_business_2": float,
                "incomes_to_personal_pets_1": float,
                "incomes_to_personal_pets_2": float,
                "incomes_sale_merchandise_1": float,
                "incomes_sale_merchandise_2": float,
                "incomes_rent_of_land_and_building_1": float,
                "incomes_rent_of_land_and_building_2": float,
                "incomes_interests_1": float,
                "incomes_interests_2": float,
                "incomes_capital_gain_or_loss_1": float,
                "incomes_capital_gain_or_loss_2": float,
                "incomes_other_operating_income_1": float,
                "incomes_other_operating_income_2": float,
                "incomes_total_1": float,
                "incomes_total_2": float,
                "total_expenses_1": float,
                "total_expenses_2": float,
                "expenses_salaries_wages_bonus_1": float,
                "expenses_salaries_wages_bonus_2": float,
                "expenses_interests_1": float,
                "expenses_interests_2": float,
                "expenses_rent_1": float,
                "expenses_rent_2": float,
                "expenses_depreciation_1": float,
                "expenses_depreciation_2": float,
                "expenses_bad_debts_1": float,
                "expenses_bad_debts_2": float,
                "expenses_donations_1": float,
                "expenses_donations_2": float,
                "expenses_sales_taxes_1": float,
                "expenses_sales_taxes_2": float,
                "expenses_purchases_machinery_1": float,
                "expenses_purchases_machinery_2": float,
                "expenses_other_purchases_1": float,
                "expenses_other_purchases_2": float,
                "expenses_licenses_1": float,
                "expenses_licenses_2": float,
                "expenses_other_operating_1": float,
                "expenses_other_operating_2": float,
                "expenses_total_expenses_1": float,
                "expenses_total_expenses_2": float,
                "net_profit_1": float,
                "net_profit_2": float,
                "profit_income_tax_1": float,
                "profit_income_tax_2": float,
                "profit_after_income_tax_1": float,
                "profit_after_income_tax_2": float,
                "sales_tax_withheld_1": float,
                "sales_tax_withheld_2": float,
                "name": str,
                "rank": str,
            },
            table_name="IP_540v",
            table_id=12,
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-540v.html")


def IP_720(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get("company_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")

        legal_form = request.POST.get("legal_form")
        cfc = request.POST.get("cfc")
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")

        total_incomes_1 = request.POST.get("total_incomes_1")
        total_incomes_2 = request.POST.get("total_incomes_2")
        incomes_from_persons_1 = request.POST.get("incomes_from_persons_1")
        incomes_from_persons_2 = request.POST.get("incomes_from_persons_2")
        incomes_from_industries_1 = request.POST.get("incomes_from_industries_1")
        incomes_from_industries_2 = request.POST.get("incomes_from_industries_2")
        incomes_room_rental_1 = request.POST.get("incomes_room_rental_1")
        incomes_room_rental_2 = request.POST.get("incomes_room_rental_2")
        incomes_casino_1 = request.POST.get("incomes_casino_1")
        incomes_casino_2 = request.POST.get("incomes_casino_2")
        incomes_less_prizes_1 = request.POST.get("incomes_less_prizes_1")
        incomes_less_prizes_2 = request.POST.get("incomes_less_prizes_2")
        incomes_food_beverages_1 = request.POST.get("incomes_food_beverages_1")
        incomes_food_beverages_2 = request.POST.get("incomes_food_beverages_2")
        incomes_interests_1 = request.POST.get("incomes_interests_1")
        incomes_interests_2 = request.POST.get("incomes_interests_2")
        incomes_rent_1 = request.POST.get("incomes_rent_1")
        incomes_rent_2 = request.POST.get("incomes_rent_2")
        incomes_capital_gain_loss_1 = request.POST.get("incomes_capital_gain_loss_1")
        incomes_capital_gain_loss_2 = request.POST.get("incomes_capital_gain_loss_2")
        other_incomes_1 = request.POST.get("other_incomes_1")
        other_incomes_2 = request.POST.get("other_incomes_2")
        total_expenses_1 = request.POST.get("total_expenses_1")
        total_expenses_2 = request.POST.get("total_expenses_2")
        expenses_food_beverages_1 = request.POST.get("expenses_food_beverages_1")
        expenses_food_beverages_2 = request.POST.get("expenses_food_beverages_2")
        expenses_food_1 = request.POST.get("expenses_food_1")
        expenses_food_2 = request.POST.get("expenses_food_2")
        expenses_beverages_1 = request.POST.get("expenses_beverages_1")
        expenses_beverages_2 = request.POST.get("expenses_beverages_2")
        expenses_music_entertainment_1 = request.POST.get(
            "expenses_music_entertainment_1"
        )
        expenses_music_entertainment_2 = request.POST.get(
            "expenses_music_entertainment_2"
        )
        expenses_salaries_wages_bonus_1 = request.POST.get(
            "expenses_salaries_wages_bonus_1"
        )
        expenses_salaries_wages_bonus_2 = request.POST.get(
            "expenses_salaries_wages_bonus_2"
        )
        expenses_uniform_1 = request.POST.get("expenses_uniform_1")
        expenses_uniform_2 = request.POST.get("expenses_uniform_2")
        expenses_interests_1 = request.POST.get("expenses_interests_1")
        expenses_interests_2 = request.POST.get("expenses_interests_2")
        expenses_rent_1 = request.POST.get("expenses_rent_1")
        expenses_rent_2 = request.POST.get("expenses_rent_2")
        expenses_depreciation_1 = request.POST.get("expenses_depreciation_1")
        expenses_depreciation_2 = request.POST.get("expenses_depreciation_2")
        expenses_bad_debts_1 = request.POST.get("expenses_bad_debts_1")
        expenses_bad_debts_2 = request.POST.get("expenses_bad_debts_2")
        expenses_donations_1 = request.POST.get("expenses_donations_1")
        expenses_donations_2 = request.POST.get("expenses_donations_2")
        expenses_free_food_employees_1 = request.POST.get(
            "expenses_free_food_employees_1"
        )
        expenses_free_food_employees_2 = request.POST.get(
            "expenses_free_food_employees_2"
        )
        expenses_sales_tax_1 = request.POST.get("expenses_sales_tax_1")
        expenses_sales_tax_2 = request.POST.get("expenses_sales_tax_2")
        expenses_purchases_machinery_1 = request.POST.get(
            "expenses_purchases_machinery_1"
        )
        expenses_purchases_machinery_2 = request.POST.get(
            "expenses_purchases_machinery_2"
        )
        expenses_other_purchases_1 = request.POST.get("expenses_other_purchases_1")
        expenses_other_purchases_2 = request.POST.get("expenses_other_purchases_2")
        expenses_licenses_1 = request.POST.get("expenses_licenses_1")
        expenses_licenses_2 = request.POST.get("expenses_licenses_2")
        other_expenses_1 = request.POST.get("other_expenses_1")
        other_expenses_2 = request.POST.get("other_expenses_2")
        net_profit_loss_1 = request.POST.get("net_profit_loss_1")
        net_profit_loss_2 = request.POST.get("net_profit_loss_2")
        profit_incomes_tax_1 = request.POST.get("profit_incomes_tax_1")
        profit_incomes_tax_2 = request.POST.get("profit_incomes_tax_2")
        profit_after_income_tax_1 = request.POST.get("profit_after_income_tax_1")
        profit_after_income_tax_2 = request.POST.get("profit_after_income_tax_2")
        sales_tax_withheld_1 = request.POST.get("sales_tax_withheld_1")
        sales_tax_withheld_2 = request.POST.get("sales_tax_withheld_2")
        name = request.POST.get("name")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-720.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "company_name",
                        "address",
                        "email",
                        "liaison_officer",
                        "ssn",
                        "tel",
                        "fax",
                        "legal_form",
                        "cfc",
                        "closing_date",
                        "start_year",
                        "end_year",
                        "total_incomes_1",
                        "total_incomes_2",
                        "incomes_from_persons_1",
                        "incomes_from_persons_2",
                        "incomes_from_industries_1",
                        "incomes_from_industries_2",
                        "incomes_room_rental_1",
                        "incomes_room_rental_2",
                        "incomes_casino_1",
                        "incomes_casino_2",
                        "incomes_less_prizes_1",
                        "incomes_less_prizes_2",
                        "incomes_food_beverages_1",
                        "incomes_food_beverages_2",
                        "incomes_interests_1",
                        "incomes_interests_2",
                        "incomes_rent_1",
                        "incomes_rent_2",
                        "incomes_capital_gain_loss_1",
                        "incomes_capital_gain_loss_2",
                        "other_incomes_1",
                        "other_incomes_2",
                        "total_expenses_1",
                        "total_expenses_2",
                        "expenses_food_beverages_1",
                        "expenses_food_beverages_2",
                        "expenses_food_1",
                        "expenses_food_2",
                        "expenses_beverages_1",
                        "expenses_beverages_2",
                        "expenses_music_entertainment_1",
                        "expenses_music_entertainment_2",
                        "expenses_salaries_wages_bonus_1",
                        "expenses_salaries_wages_bonus_2",
                        "expenses_uniform_1",
                        "expenses_uniform_2",
                        "expenses_interests_1",
                        "expenses_interests_2",
                        "expenses_rent_1",
                        "expenses_rent_2",
                        "expenses_depreciation_1",
                        "expenses_depreciation_2",
                        "expenses_bad_debts_1",
                        "expenses_bad_debts_2",
                        "expenses_donations_1",
                        "expenses_donations_2",
                        "expenses_free_food_employees_1",
                        "expenses_free_food_employees_2",
                        "expenses_sales_tax_1",
                        "expenses_sales_tax_2",
                        "expenses_purchases_machinery_1",
                        "expenses_purchases_machinery_2",
                        "expenses_other_purchases_1",
                        "expenses_other_purchases_2",
                        "expenses_licenses_1",
                        "expenses_licenses_2",
                        "other_expenses_1",
                        "other_expenses_2",
                        "net_profit_loss_1",
                        "net_profit_loss_2",
                        "profit_incomes_tax_1",
                        "profit_incomes_tax_2",
                        "profit_after_income_tax_1",
                        "profit_after_income_tax_2",
                        "sales_tax_withheld_1",
                        "sales_tax_withheld_2",
                        "name",
                        "rank",
                    ]
                )

            writer.writerow(
                [
                    company_name,
                    address,
                    email,
                    liaison_officer,
                    ssn,
                    tel,
                    fax,
                    legal_form,
                    cfc,
                    closing_date,
                    start_year,
                    end_year,
                    total_incomes_1,
                    total_incomes_2,
                    incomes_from_persons_1,
                    incomes_from_persons_2,
                    incomes_from_industries_1,
                    incomes_from_industries_2,
                    incomes_room_rental_1,
                    incomes_room_rental_2,
                    incomes_casino_1,
                    incomes_casino_2,
                    incomes_less_prizes_1,
                    incomes_less_prizes_2,
                    incomes_food_beverages_1,
                    incomes_food_beverages_2,
                    incomes_interests_1,
                    incomes_interests_2,
                    incomes_rent_1,
                    incomes_rent_2,
                    incomes_capital_gain_loss_1,
                    incomes_capital_gain_loss_2,
                    other_incomes_1,
                    other_incomes_2,
                    total_expenses_1,
                    total_expenses_2,
                    expenses_food_beverages_1,
                    expenses_food_beverages_2,
                    expenses_food_1,
                    expenses_food_2,
                    expenses_beverages_1,
                    expenses_beverages_2,
                    expenses_music_entertainment_1,
                    expenses_music_entertainment_2,
                    expenses_salaries_wages_bonus_1,
                    expenses_salaries_wages_bonus_2,
                    expenses_uniform_1,
                    expenses_uniform_2,
                    expenses_interests_1,
                    expenses_interests_2,
                    expenses_rent_1,
                    expenses_rent_2,
                    expenses_depreciation_1,
                    expenses_depreciation_2,
                    expenses_bad_debts_1,
                    expenses_bad_debts_2,
                    expenses_donations_1,
                    expenses_donations_2,
                    expenses_free_food_employees_1,
                    expenses_free_food_employees_2,
                    expenses_sales_tax_1,
                    expenses_sales_tax_2,
                    expenses_purchases_machinery_1,
                    expenses_purchases_machinery_2,
                    expenses_other_purchases_1,
                    expenses_other_purchases_2,
                    expenses_licenses_1,
                    expenses_licenses_2,
                    other_expenses_1,
                    other_expenses_2,
                    net_profit_loss_1,
                    net_profit_loss_2,
                    profit_incomes_tax_1,
                    profit_incomes_tax_2,
                    profit_after_income_tax_1,
                    profit_after_income_tax_2,
                    sales_tax_withheld_1,
                    sales_tax_withheld_2,
                    name,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-720.csv",
            dtypes={
                "company_name": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "ssn": str,
                "tel": str,
                "fax": str,
                "legal_form": str,
                "cfc": str,
                "closing_date": str,
                "start_year": int,
                "end_year": int,
                "total_incomes_1": float,
                "total_incomes_2": float,
                "incomes_from_persons_1": float,
                "incomes_from_persons_2": float,
                "incomes_from_industries_1": float,
                "incomes_from_industries_2": float,
                "incomes_room_rental_1": float,
                "incomes_room_rental_2": float,
                "incomes_casino_1": float,
                "incomes_casino_2": float,
                "incomes_less_prizes_1": float,
                "incomes_less_prizes_2": float,
                "incomes_food_beverages_1": float,
                "incomes_food_beverages_2": float,
                "incomes_interests_1": float,
                "incomes_interests_2": float,
                "incomes_rent_1": float,
                "incomes_rent_2": float,
                "incomes_capital_gain_loss_1": float,
                "incomes_capital_gain_loss_2": float,
                "other_incomes_1": float,
                "other_incomes_2": float,
                "total_expenses_1": float,
                "total_expenses_2": float,
                "expenses_food_beverages_1": float,
                "expenses_food_beverages_2": float,
                "expenses_food_1": float,
                "expenses_food_2": float,
                "expenses_beverages_1": float,
                "expenses_beverages_2": float,
                "expenses_music_entertainment_1": float,
                "expenses_music_entertainment_2": float,
                "expenses_salaries_wages_bonus_1": float,
                "expenses_salaries_wages_bonus_2": float,
                "expenses_uniform_1": float,
                "expenses_uniform_2": float,
                "expenses_interests_1": float,
                "expenses_interests_2": float,
                "expenses_rent_1": float,
                "expenses_rent_2": float,
                "expenses_depreciation_1": float,
                "expenses_depreciation_2": float,
                "expenses_bad_debts_1": float,
                "expenses_bad_debts_2": float,
                "expenses_donations_1": float,
                "expenses_donations_2": float,
                "expenses_free_food_employees_1": float,
                "expenses_free_food_employees_2": float,
                "expenses_sales_tax_1": float,
                "expenses_sales_tax_2": float,
                "expenses_purchases_machinery_1": float,
                "expenses_purchases_machinery_2": float,
                "expenses_other_purchases_1": float,
                "expenses_other_purchases_2": float,
                "expenses_licenses_1": float,
                "expenses_licenses_2": float,
                "other_expenses_1": float,
                "other_expenses_2": float,
                "net_profit_loss_1": float,
                "net_profit_loss_2": float,
                "profit_incomes_tax_1": float,
                "profit_incomes_tax_2": float,
                "profit_after_income_tax_1": float,
                "profit_after_income_tax_2": float,
                "sales_tax_withheld_1": float,
                "sales_tax_withheld_2": float,
                "name": str,
                "rank": str,
            },
            table_name="IP_720",
            table_id=10,
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-720.html")


def IP_810(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get("company_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")
        legal_form = request.POST.get("legal_form")
        cfc = request.POST.get("cfc")
        business_type = request.POST.get("business_type")
        business_function = request.POST.get("business_function")
        branches = request.POST.get("branches")
        branches_yes = request.POST.get("branches_yes")
        closing_date = request.POST.get("closing_date")

        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")

        total_income_1 = request.POST.get("total_income_1")
        total_income_2 = request.POST.get("total_income_2")
        services_rendered_1 = request.POST.get("services_rendered_1")
        services_rendered_2 = request.POST.get("services_rendered_2")
        from_persons_1 = request.POST.get("from_persons_1")
        from_persons_2 = request.POST.get("from_persons_2")
        industries_businesses_1 = request.POST.get("industries_businesses_1")
        industries_businesses_2 = request.POST.get("industries_businesses_2")
        sales_1 = request.POST.get("sales_1")
        sales_2 = request.POST.get("sales_2")
        rent_machinery_1 = request.POST.get("rent_machinery_1")
        rent_machinery_2 = request.POST.get("rent_machinery_2")
        rent_land_1 = request.POST.get("rent_land_1")
        rent_land_2 = request.POST.get("rent_land_2")
        interest_1 = request.POST.get("interest_1")
        interest_2 = request.POST.get("interest_2")
        capitan_gain_loss_1 = request.POST.get("capitan_gain_loss_1")
        capitan_gain_loss_2 = request.POST.get("capitan_gain_loss_2")

        total_expenses_1 = request.POST.get("total_expenses_1")
        total_expenses_2 = request.POST.get("total_expenses_2")
        salaries_1 = request.POST.get("salaries_1")
        salaries_2 = request.POST.get("salaries_2")
        expenses_interests_1 = request.POST.get("expenses_interests_1")
        expenses_interests_2 = request.POST.get("expenses_interests_2")
        expenses_rents_1 = request.POST.get("expenses_rents_1")
        expenses_rents_2 = request.POST.get("expenses_rents_2")
        depreciation_1 = request.POST.get("depreciation_1")
        depreciation_2 = request.POST.get("depreciation_2")
        bad_debts_1 = request.POST.get("bad_debts_1")
        bad_debts_2 = request.POST.get("bad_debts_2")
        donations_1 = request.POST.get("donations_1")
        donations_2 = request.POST.get("donations_2")
        other_operating_expenses_1 = request.POST.get("other_operating_expenses_1")
        other_operating_expenses_2 = request.POST.get("other_operating_expenses_2")
        sales_tax_1 = request.POST.get("sales_tax_1")
        sales_tax_2 = request.POST.get("sales_tax_2")
        purchases_1 = request.POST.get("purchases_1")
        purchases_2 = request.POST.get("purchases_2")
        other_purchases_1 = request.POST.get("other_purchases_1")
        other_purchases_2 = request.POST.get("other_purchases_2")
        licenses_patents_1 = request.POST.get("licenses_patents_1")
        licenses_patents_2 = request.POST.get("licenses_patents_2")

        net_profit_loss_1 = request.POST.get("net_profit_loss_1")
        net_profit_loss_2 = request.POST.get("net_profit_loss_2")
        income_tax_1 = request.POST.get("income_tax_1")
        income_tax_2 = request.POST.get("income_tax_2")
        profit_after_tax_1 = request.POST.get("profit_after_tax_1")
        profit_after_tax_2 = request.POST.get("profit_after_tax_2")

        withheld_tax_1 = request.POST.get("withheld_tax_1")
        withheld_tax_2 = request.POST.get("withheld_tax_2")

        name = request.POST.get("name")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-810.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "company_name",
                        "address",
                        "email",
                        "liaison_officer",
                        "ssn",
                        "tel",
                        "fax",
                        "legal_form",
                        "cfc",
                        "business_type",
                        "business_function",
                        "branches",
                        "branches_yes",
                        "closing_date",
                        "start_year",
                        "end_year",
                        "total_income_1",
                        "total_income_2",
                        "services_rendered_1",
                        "services_rendered_2",
                        "from_persons_1",
                        "from_persons_2",
                        "industries_businesses_1",
                        "industries_businesses_2",
                        "sales_1",
                        "sales_2",
                        "rent_machinery_1",
                        "rent_machinery_2",
                        "rent_land_1",
                        "rent_land_2",
                        "interest_1",
                        "interest_2",
                        "capitan_gain_loss_1",
                        "capitan_gain_loss_2",
                        "total_expenses_1",
                        "total_expenses_2",
                        "salaries_1",
                        "salaries_2",
                        "expenses_interests_1",
                        "expenses_interests_2",
                        "expenses_rents_1",
                        "expenses_rents_2",
                        "depreciation_1",
                        "depreciation_2",
                        "bad_debts_1",
                        "bad_debts_2",
                        "donations_1",
                        "donations_2",
                        "other_operating_expenses_1",
                        "other_operating_expenses_2",
                        "sales_tax_1",
                        "sales_tax_2",
                        "purchases_1",
                        "purchases_2",
                        "other_purchases_1",
                        "other_purchases_2",
                        "licenses_patents_1",
                        "licenses_patents_2",
                        "net_profit_loss_1",
                        "net_profit_loss_2",
                        "income_tax_1",
                        "income_tax_2",
                        "profit_after_tax_1",
                        "profit_after_tax_2",
                        "withheld_tax_1",
                        "withheld_tax_2",
                        "name",
                        "rank",
                    ]
                )

            writer.writerow(
                [
                    company_name,
                    address,
                    email,
                    liaison_officer,
                    ssn,
                    tel,
                    fax,
                    legal_form,
                    cfc,
                    business_type,
                    business_function,
                    branches,
                    branches_yes,
                    closing_date,
                    start_year,
                    end_year,
                    total_income_1,
                    total_income_2,
                    services_rendered_1,
                    services_rendered_2,
                    from_persons_1,
                    from_persons_2,
                    industries_businesses_1,
                    industries_businesses_2,
                    sales_1,
                    sales_2,
                    rent_machinery_1,
                    rent_machinery_2,
                    rent_land_1,
                    rent_land_2,
                    interest_1,
                    interest_2,
                    capitan_gain_loss_1,
                    capitan_gain_loss_2,
                    total_expenses_1,
                    total_expenses_2,
                    salaries_1,
                    salaries_2,
                    expenses_interests_1,
                    expenses_interests_2,
                    expenses_rents_1,
                    expenses_rents_2,
                    depreciation_1,
                    depreciation_2,
                    bad_debts_1,
                    bad_debts_2,
                    donations_1,
                    donations_2,
                    other_operating_expenses_1,
                    other_operating_expenses_2,
                    sales_tax_1,
                    sales_tax_2,
                    purchases_1,
                    purchases_2,
                    other_purchases_1,
                    other_purchases_2,
                    licenses_patents_1,
                    licenses_patents_2,
                    net_profit_loss_1,
                    net_profit_loss_2,
                    income_tax_1,
                    income_tax_2,
                    profit_after_tax_1,
                    profit_after_tax_2,
                    withheld_tax_1,
                    withheld_tax_2,
                    name,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-810.csv",
            dtypes={
                "company_name": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "ssn": str,
                "tel": str,
                "fax": str,
                "legal_form": str,
                "cfc": str,
                "business_type": str,
                "business_function": str,
                "branches": str,
                "branches_yes": str,
                "closing_date": str,
                "start_year": int,
                "end_year": int,
                "total_income_1": float,
                "total_income_2": float,
                "services_rendered_1": float,
                "services_rendered_2": float,
                "from_persons_1": float,
                "from_persons_2": float,
                "industries_businesses_1": float,
                "industries_businesses_2": float,
                "sales_1": float,
                "sales_2": float,
                "rent_machinery_1": float,
                "rent_machinery_2": float,
                "rent_land_1": float,
                "rent_land_2": float,
                "interest_1": float,
                "interest_2": float,
                "capitan_gain_loss_1": float,
                "capitan_gain_loss_2": float,
                "total_expenses_1": float,
                "total_expenses_2": float,
                "salaries_1": float,
                "salaries_2": float,
                "expenses_interests_1": float,
                "expenses_interests_2": float,
                "expenses_rents_1": float,
                "expenses_rents_2": float,
                "depreciation_1": float,
                "depreciation_2": float,
                "bad_debts_1": float,
                "bad_debts_2": float,
                "donations_1": float,
                "donations_2": float,
                "other_operating_expenses_1": float,
                "other_operating_expenses_2": float,
                "sales_tax_1": float,
                "sales_tax_2": float,
                "purchases_1": float,
                "purchases_2": float,
                "other_purchases_1": float,
                "other_purchases_2": float,
                "licenses_patents_1": float,
                "licenses_patents_2": float,
                "net_profit_loss_1": float,
                "net_profit_loss_2": float,
                "income_tax_1": float,
                "income_tax_2": float,
                "profit_after_tax_1": float,
                "profit_after_tax_2": float,
                "withheld_tax_1": float,
                "withheld_tax_2": float,
                "name": str,
                "rank": str,
            },
            table_name="IP_810",
            table_id=8,
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-810.html")


def JP_547(request):
    if request.method == "POST":
        # Retrieve form data
        agency_form = request.POST.get("agency_form")
        agency_to = request.POST.get("agency_to")

        salaries_wages = request.POST.get("salaries_wages")
        civil_service = request.POST.get("civil_service")
        federal_employee_retirement = request.POST.get("federal_employee_retirement")
        thrift_savings_disbursements = request.POST.get("thrift_savings_disbursements")
        social_security = request.POST.get("social_security")
        life_insurance_health_disbursements = request.POST.get(
            "life_insurance_health_disbursements"
        )
        other_disbursements = request.POST.get("other_disbursements")
        construction_contracts = request.POST.get("construction_contracts")
        rent_disbursements = request.POST.get("rent_disbursements")
        other_purchases = request.POST.get("other_purchases")
        equipment_supplies = request.POST.get("equipment_supplies")
        rent_sales = request.POST.get("rent_sales")
        other_sales = request.POST.get("other_sales")
        income_tax = request.POST.get("income_tax")
        other_taxes_licenses = request.POST.get("other_taxes_licenses")
        fines_penalties = request.POST.get("fines_penalties")
        interest = request.POST.get("interest")
        other_collections_1 = request.POST.get("other_collections_1")
        other_collections_amount_1 = request.POST.get("other_collections_amount_1")
        other_collections_2 = request.POST.get("other_collections_2")
        other_collections_amount_2 = request.POST.get("other_collections_amount_2")
        other_collections_3 = request.POST.get("other_collections_3")
        other_collections_amount_3 = request.POST.get("other_collections_amount_3")
        civil_service_2 = request.POST.get("civil_service_2")
        federal_employee = request.POST.get("federal_employee")
        thrift_saving_deductions = request.POST.get("thrift_saving_deductions")
        social_security_deductions = request.POST.get("social_security_deductions")
        life_insurance_health_deductions = request.POST.get(
            "life_insurance_health_deductions"
        )
        income_tax_deductions = request.POST.get("income_tax_deductions")
        saving_bonds = request.POST.get("saving_bonds")
        other_deductions = request.POST.get("other_deductions")
        other_deductions_amount = request.POST.get("other_deductions_amount")
        commonwealth = request.POST.get("commonwealth")
        municipal = request.POST.get("municipal")
        individuals_private_institutions = request.POST.get(
            "individuals_private_institutions"
        )
        death_disability = request.POST.get("death_disability")
        other_payments_1 = request.POST.get("other_payments_1")
        other_payments_amount_1 = request.POST.get("other_payments_amount_1")
        other_payments_2 = request.POST.get("other_payments_2")
        other_payments_amount_2 = request.POST.get("other_payments_amount_2")
        loans_advances = request.POST.get("loans_advances")
        repayments_loans = request.POST.get("repayments_loans")
        total_loans_amount = request.POST.get("total_loans_amount")
        loans_cancelled = request.POST.get("loans_cancelled")
        other_credits = request.POST.get("other_credits")
        loans_and_advances = request.POST.get("loans_and_advances")
        loans_and_advances_amount = request.POST.get("loans_and_advances_amount")
        interest_collected = request.POST.get("interest_collected")
        forgiveness_credit = request.POST.get("forgiveness_credit")

        reporting_agency = request.POST.get("reporting_agency")

        csv_file_path = "data/cuestionarios/balanza_de_pagos/JP-547.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "agency_form",
                        "agency_to",
                        "salaries_wages",
                        "civil_service",
                        "federal_employee_retirement",
                        "thrift_savings_disbursements",
                        "social_security",
                        "life_insurance_health_disbursements",
                        "other_disbursements",
                        "construction_contracts",
                        "rent_disbursements",
                        "other_purchases",
                        "equipment_supplies",
                        "rent_sales",
                        "other_sales",
                        "income_tax",
                        "other_taxes_licenses",
                        "fines_penalties",
                        "interest",
                        "other_collections_1",
                        "other_collections_amount_1",
                        "other_collections_2",
                        "other_collections_amount_2",
                        "other_collections_3",
                        "other_collections_amount_3",
                        "civil_service_2",
                        "federal_employee",
                        "thrift_saving_deductions",
                        "social_security_deductions",
                        "life_insurance_health_deductions",
                        "income_tax_deductions",
                        "saving_bonds",
                        "other_deductions",
                        "other_deductions_amount",
                        "commonwealth",
                        "municipal",
                        "individuals_private_institutions",
                        "death_disability",
                        "other_payments_1",
                        "other_payments_amount_1",
                        "other_payments_2",
                        "other_payments_amount_2",
                        "loans_advances",
                        "repayments_loans",
                        "total_loans_amount",
                        "loans_cancelled",
                        "other_credits",
                        "loans_and_advances",
                        "loans_and_advances_amount",
                        "interest_collected",
                        "forgiveness_credit",
                        "reporting_agency",
                    ]
                )

            writer.writerow(
                [
                    agency_form,
                    agency_to,
                    salaries_wages,
                    civil_service,
                    federal_employee_retirement,
                    thrift_savings_disbursements,
                    social_security,
                    life_insurance_health_disbursements,
                    other_disbursements,
                    construction_contracts,
                    rent_disbursements,
                    other_purchases,
                    equipment_supplies,
                    rent_sales,
                    other_sales,
                    income_tax,
                    other_taxes_licenses,
                    fines_penalties,
                    interest,
                    other_collections_1,
                    other_collections_amount_1,
                    other_collections_2,
                    other_collections_amount_2,
                    other_collections_3,
                    other_collections_amount_3,
                    civil_service_2,
                    federal_employee,
                    thrift_saving_deductions,
                    social_security_deductions,
                    life_insurance_health_deductions,
                    income_tax_deductions,
                    saving_bonds,
                    other_deductions,
                    other_deductions_amount,
                    commonwealth,
                    municipal,
                    individuals_private_institutions,
                    death_disability,
                    other_payments_1,
                    other_payments_amount_1,
                    other_payments_2,
                    other_payments_amount_2,
                    loans_advances,
                    repayments_loans,
                    total_loans_amount,
                    loans_cancelled,
                    other_credits,
                    loans_and_advances,
                    loans_and_advances_amount,
                    interest_collected,
                    forgiveness_credit,
                    reporting_agency,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/balanza_de_pagos/JP-547.csv",
            dtypes={
                "agency_form": str,
                "agency_to": str,
                "salaries_wages": float,
                "civil_service": float,
                "federal_employee_retirement": float,
                "thrift_savings_disbursements": float,
                "social_security": float,
                "life_insurance_health_disbursements": float,
                "other_disbursements": float,
                "construction_contracts": float,
                "rent_disbursements": float,
                "other_purchases": float,
                "equipment_supplies": float,
                "rent_sales": float,
                "other_sales": float,
                "income_tax": float,
                "other_taxes_licenses": float,
                "fines_penalties": float,
                "interest": float,
                "other_collections_1": str,
                "other_collections_amount_1": float,
                "other_collections_2": str,
                "other_collections_amount_2": float,
                "other_collections_3": str,
                "other_collections_amount_3": float,
                "civil_service_2": float,
                "federal_employee": float,
                "thrift_saving_deductions": float,
                "social_security_deductions": float,
                "life_insurance_health_deductions": float,
                "income_tax_deductions": float,
                "saving_bonds": float,
                "other_deductions": str,
                "other_deductions_amount": float,
                "commonwealth": float,
                "municipal": float,
                "individuals_private_institutions": float,
                "death_disability": float,
                "other_payments_1": str,
                "other_payments_amount_1": float,
                "other_payments_2": str,
                "other_payments_amount_2": float,
                "loans_advances": float,
                "repayments_loans": float,
                "total_loans_amount": float,
                "loans_cancelled": float,
                "other_credits": float,
                "loans_and_advances": float,
                "loans_and_advances_amount": float,
                "interest_collected": float,
                "forgiveness_credit": float,
                "reporting_agency": str,
            },
            table_name="JP_547",
            table_id=6,
            debug=False,
        )
        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/balanza_de_pagos/JP-547.html")
