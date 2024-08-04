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
from src.formularios.form_ip_540a import IP_540a
from src.formularios.form_ip_720 import IP_720
from src.formularios.form_ip_810 import IP_810

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
