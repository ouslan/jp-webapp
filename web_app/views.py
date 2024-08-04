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
from src.formularios.form_jp_375 import JP_375
from src.formularios.form_ip_420 import IP_420
from src.formularios.form_ip_480 import IP_480
from src.formularios.form_ip_310 import IP_310
from src.formularios.form_jp_383 import JP_383
from src.formularios.form_ip_440 import IP_440
from src.formularios.form_ip_440g import IP_440g
from src.formularios.form_ip_310b import IP_310b
from src.formularios.form_ip_480a import IP_480a
from src.formularios.form_ip_490 import IP_490
from src.formularios.form_ip_520 import IP_520
from src.formularios.form_jp_536_2 import JP_536_2
from src.formularios.form_ip_510 import IP_510
from src.formularios.form_jp_544 import JP_544
from src.formularios.form_ip_520s import IP_520s
from src.formularios.form_ip_520a import IP_520a


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

def JP_544_1(request):
    return render(request, "forms/yearly/balanza_de_pagos/JP-544-1.html")

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
