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
from src.formularios.form_ip_230 import IP_230
from src.formularios.form_ip_540 import IP_540
from src.formularios.form_ip_540j import IP_540j
from src.formularios.form_jp_544_2 import JP_544_2
from src.formularios.form_ip_610 import IP_610
from src.formularios.form_ip_710 import IP_710
from src.formularios.form_ip_620 import IP_620
from src.formularios.form_ip_540p import IP_540p
from src.formularios.form_ip_540s import IP_540s
from src.formularios.form_ip_540v import IP_540v

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
