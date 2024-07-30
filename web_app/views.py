import pandas as pd
from django.shortcuts import render
from .models import *
from web_app import graphics_function as gf
import csv
from django.shortcuts import render, redirect
from django.http import HttpResponse
from src.dao.data_db_dao import DAO
import os


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


def JP_304(request):
    if request.method == "POST":
        # Retrieve form data
        start_month = request.POST.get("start_month")
        end_month = request.POST.get("end_month")
        year = request.POST.get("year")
        name = request.POST.get("name")
        direction = request.POST.get("direction")
        liaison_officer = request.POST.get("liaison_officer")
        title = request.POST.get("title")
        tel = request.POST.get("tel")

        nombre_agencia_federal_1 = request.POST.get("nombre_agencia_federal_1")
        catalogo_federal_1 = request.POST.get("catalogo_federal_1")
        sai_federal_1 = request.POST.get("sai_federal_1")
        titulo_federal_1 = request.POST.get("titulo_federal_1")
        aportacion_aprobada_federal_1 = request.POST.get(
            "aportacion_aprobada_federal_1"
        )
        fecha_aprobacion_federal_1 = request.POST.get("fecha_aprobacion_federal_1")
        aportacion_recibida_federal_1 = request.POST.get(
            "aportacion_recibida_federal_1"
        )
        fecha_recibo_federal_1 = request.POST.get("fecha_recibo_federal_1")
        aportacion_gastada_federal_1 = request.POST.get("aportacion_gastada_federal_1")
        fecha_gasto_federal_1 = request.POST.get("fecha_gasto_federal_1")

        nombre_agencia_federal_2 = request.POST.get("nombre_agencia_federal_2")
        catalogo_federal_2 = request.POST.get("catalogo_federal_2")
        sai_federal_2 = request.POST.get("sai_federal_2")
        titulo_federal_2 = request.POST.get("titulo_federal_2")
        aportacion_aprobada_federal_2 = request.POST.get(
            "aportacion_aprobada_federal_2"
        )
        fecha_aprobacion_federal_2 = request.POST.get("fecha_aprobacion_federal_2")
        aportacion_recibida_federal_2 = request.POST.get(
            "aportacion_recibida_federal_2"
        )
        fecha_recibo_federal_2 = request.POST.get("fecha_recibo_federal_2")
        aportacion_gastada_federal_2 = request.POST.get("aportacion_gastada_federal_2")
        fecha_gasto_federal_2 = request.POST.get("fecha_gasto_federal_2")

        nombre_agencia_federal_3 = request.POST.get("nombre_agencia_federal_3")
        catalogo_federal_3 = request.POST.get("catalogo_federal_3")
        sai_federal_3 = request.POST.get("sai_federal_3")
        titulo_federal_3 = request.POST.get("titulo_federal_3")
        aportacion_aprobada_federal_3 = request.POST.get(
            "aportacion_aprobada_federal_3"
        )
        fecha_aprobacion_federal_3 = request.POST.get("fecha_aprobacion_federal_3")
        aportacion_recibida_federal_3 = request.POST.get(
            "aportacion_recibida_federal_3"
        )
        fecha_recibo_federal_3 = request.POST.get("fecha_recibo_federal_3")
        aportacion_gastada_federal_3 = request.POST.get("aportacion_gastada_federal_3")
        fecha_gasto_federal_3 = request.POST.get("fecha_gasto_federal_3")

        nombre_agencia_federal_4 = request.POST.get("nombre_agencia_federal_4")
        catalogo_federal_4 = request.POST.get("catalogo_federal_4")
        sai_federal_4 = request.POST.get("sai_federal_4")
        titulo_federal_4 = request.POST.get("titulo_federal_4")
        aportacion_aprobada_federal_4 = request.POST.get(
            "aportacion_aprobada_federal_4"
        )
        fecha_aprobacion_federal_4 = request.POST.get("fecha_aprobacion_federal_4")
        aportacion_recibida_federal_4 = request.POST.get(
            "aportacion_recibida_federal_4"
        )
        fecha_recibo_federal_4 = request.POST.get("fecha_recibo_federal_4")
        aportacion_gastada_federal_4 = request.POST.get("aportacion_gastada_federal_4")
        fecha_gasto_federal_4 = request.POST.get("fecha_gasto_federal_4")

        nombre_agencia_federal_5 = request.POST.get("nombre_agencia_federal_5")
        catalogo_federal_5 = request.POST.get("catalogo_federal_5")
        sai_federal_5 = request.POST.get("sai_federal_5")
        titulo_federal_5 = request.POST.get("titulo_federal_5")
        aportacion_aprobada_federal_5 = request.POST.get(
            "aportacion_aprobada_federal_5"
        )
        fecha_aprobacion_federal_5 = request.POST.get("fecha_aprobacion_federal_5")
        aportacion_recibida_federal_5 = request.POST.get(
            "aportacion_recibida_federal_5"
        )
        fecha_recibo_federal_5 = request.POST.get("fecha_recibo_federal_5")
        aportacion_gastada_federal_5 = request.POST.get("aportacion_gastada_federal_5")
        fecha_gasto_federal_5 = request.POST.get("fecha_gasto_federal_5")

        agencia_local_table_box_1 = request.POST.get("agencia_local_table_box_1")
        catalogo_local_1 = request.POST.get("catalogo_local_1")
        programa_local_1 = request.POST.get("programa_local_1")
        aportacion_federal_aprobada_local_1 = request.POST.get(
            "aportacion_federal_aprobada_local_1"
        )
        fecha_aprobacion_local_1 = request.POST.get("fecha_aprobacion_local_1")
        aportacion_federal_recibida_local_1 = request.POST.get(
            "aportacion_federal_recibida_local_1"
        )
        fecha_recibo_local_1 = request.POST.get("fecha_recibo_local_1")
        aportacion_federal_gastada_local_1 = request.POST.get(
            "aportacion_federal_gastada_local_1"
        )
        fecha_gasto_local_1 = request.POST.get("fecha_gasto_local_1")
        numero_cuenta_local_1 = request.POST.get("numero_cuenta_local_1")

        agencia_local_table_box_2 = request.POST.get("agencia_local_table_box_2")
        catalogo_local_2 = request.POST.get("catalogo_local_2")
        programa_local_2 = request.POST.get("programa_local_2")
        aportacion_federal_aprobada_local_2 = request.POST.get(
            "aportacion_federal_aprobada_local_2"
        )
        fecha_aprobacion_local_2 = request.POST.get("fecha_aprobacion_local_2")
        aportacion_federal_recibida_local_2 = request.POST.get(
            "aportacion_federal_recibida_local_2"
        )
        fecha_recibo_local_2 = request.POST.get("fecha_recibo_local_2")
        aportacion_federal_gastada_local_2 = request.POST.get(
            "aportacion_federal_gastada_local_2"
        )
        fecha_gasto_local_2 = request.POST.get("fecha_gasto_local_2")
        numero_cuenta_local_2 = request.POST.get("numero_cuenta_local_2")

        agencia_local_table_box_3 = request.POST.get("agencia_local_table_box_3")
        catalogo_local_3 = request.POST.get("catalogo_local_3")
        programa_local_3 = request.POST.get("programa_local_3")
        aportacion_federal_aprobada_local_3 = request.POST.get(
            "aportacion_federal_aprobada_local_3"
        )
        fecha_aprobacion_local_3 = request.POST.get("fecha_aprobacion_local_3")
        aportacion_federal_recibida_local_3 = request.POST.get(
            "aportacion_federal_recibida_local_3"
        )
        fecha_recibo_local_3 = request.POST.get("fecha_recibo_local_3")
        aportacion_federal_gastada_local_3 = request.POST.get(
            "aportacion_federal_gastada_local_3"
        )
        fecha_gasto_local_3 = request.POST.get("fecha_gasto_local_3")
        numero_cuenta_local_3 = request.POST.get("numero_cuenta_local_3")

        agencia_local_table_box_4 = request.POST.get("agencia_local_table_box_4")
        catalogo_local_4 = request.POST.get("catalogo_local_4")
        programa_local_4 = request.POST.get("programa_local_4")
        aportacion_federal_aprobada_local_4 = request.POST.get(
            "aportacion_federal_aprobada_local_4"
        )
        fecha_aprobacion_local_4 = request.POST.get("fecha_aprobacion_local_4")
        aportacion_federal_recibida_local_4 = request.POST.get(
            "aportacion_federal_recibida_local_4"
        )
        fecha_recibo_local_4 = request.POST.get("fecha_recibo_local_4")
        aportacion_federal_gastada_local_4 = request.POST.get(
            "aportacion_federal_gastada_local_4"
        )
        fecha_gasto_local_4 = request.POST.get("fecha_gasto_local_4")
        numero_cuenta_local_4 = request.POST.get("numero_cuenta_local_4")

        agencia_local_table_box_5 = request.POST.get("agencia_local_table_box_5")
        catalogo_local_5 = request.POST.get("catalogo_local_5")
        programa_local_5 = request.POST.get("programa_local_5")
        aportacion_federal_aprobada_local_5 = request.POST.get(
            "aportacion_federal_aprobada_local_5"
        )
        fecha_aprobacion_local_5 = request.POST.get("fecha_aprobacion_local_5")
        aportacion_federal_recibida_local_5 = request.POST.get(
            "aportacion_federal_recibida_local_5"
        )
        fecha_recibo_local_5 = request.POST.get("fecha_recibo_local_5")
        aportacion_federal_gastada_local_5 = request.POST.get(
            "aportacion_federal_gastada_local_5"
        )
        fecha_gasto_local_5 = request.POST.get("fecha_gasto_local_5")
        numero_cuenta_local_5 = request.POST.get("numero_cuenta_local_5")

        csv_file_path = "data/cuestionarios/balanza_de_pagos/JP-304.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "start_month",
                        "end_month",
                        "year",
                        "name",
                        "direction",
                        "liaison_officer",
                        "title",
                        "tel",
                        "nombre_agencia_federal_1",
                        "catalogo_federal_1",
                        "sai_federal_1",
                        "titulo_federal_1",
                        "aportacion_aprobada_federal_1",
                        "fecha_aprobacion_federal_1",
                        "aportacion_recibida_federal_1",
                        "fecha_recibo_federal_1",
                        "aportacion_gastada_federal_1",
                        "fecha_gasto_federal_1",
                        "nombre_agencia_federal_2",
                        "catalogo_federal_2",
                        "sai_federal_2",
                        "titulo_federal_2",
                        "aportacion_aprobada_federal_2",
                        "fecha_aprobacion_federal_2",
                        "aportacion_recibida_federal_2",
                        "fecha_recibo_federal_2",
                        "aportacion_gastada_federal_2",
                        "fecha_gasto_federal_2",
                        "nombre_agencia_federal_3",
                        "catalogo_federal_3",
                        "sai_federal_3",
                        "titulo_federal_3",
                        "aportacion_aprobada_federal_3",
                        "fecha_aprobacion_federal_3",
                        "aportacion_recibida_federal_3",
                        "fecha_recibo_federal_3",
                        "aportacion_gastada_federal_3",
                        "fecha_gasto_federal_3",
                        "nombre_agencia_federal_4",
                        "catalogo_federal_4",
                        "sai_federal_4",
                        "titulo_federal_4",
                        "aportacion_aprobada_federal_4",
                        "fecha_aprobacion_federal_4",
                        "aportacion_recibida_federal_4",
                        "fecha_recibo_federal_4",
                        "aportacion_gastada_federal_4",
                        "fecha_gasto_federal_4",
                        "nombre_agencia_federal_5",
                        "catalogo_federal_5",
                        "sai_federal_5",
                        "titulo_federal_5",
                        "aportacion_aprobada_federal_5",
                        "fecha_aprobacion_federal_5",
                        "aportacion_recibida_federal_5",
                        "fecha_recibo_federal_5",
                        "aportacion_gastada_federal_5",
                        "fecha_gasto_federal_5",
                        "agencia_local_table_box_1",
                        "catalogo_local_1",
                        "programa_local_1",
                        "aportacion_federal_aprobada_local_1",
                        "fecha_aprobacion_local_1",
                        "aportacion_federal_recibida_local_1",
                        "fecha_recibo_local_1",
                        "aportacion_federal_gastada_local_1",
                        "fecha_gasto_local_1",
                        "numero_cuenta_local_1",
                        "agencia_local_table_box_2",
                        "catalogo_local_2",
                        "programa_local_2",
                        "aportacion_federal_aprobada_local_2",
                        "fecha_aprobacion_local_2",
                        "aportacion_federal_recibida_local_2",
                        "fecha_recibo_local_2",
                        "aportacion_federal_gastada_local_2",
                        "fecha_gasto_local_2",
                        "numero_cuenta_local_2",
                        "agencia_local_table_box_3",
                        "catalogo_local_3",
                        "programa_local_3",
                        "aportacion_federal_aprobada_local_3",
                        "fecha_aprobacion_local_3",
                        "aportacion_federal_recibida_local_3",
                        "fecha_recibo_local_3",
                        "aportacion_federal_gastada_local_3",
                        "fecha_gasto_local_3",
                        "numero_cuenta_local_3",
                        "agencia_local_table_box_4",
                        "catalogo_local_4",
                        "programa_local_4",
                        "aportacion_federal_aprobada_local_4",
                        "fecha_aprobacion_local_4",
                        "aportacion_federal_recibida_local_4",
                        "fecha_recibo_local_4",
                        "aportacion_federal_gastada_local_4",
                        "fecha_gasto_local_4",
                        "numero_cuenta_local_4",
                        "agencia_local_table_box_5",
                        "catalogo_local_5",
                        "programa_local_5",
                        "aportacion_federal_aprobada_local_5",
                        "fecha_aprobacion_local_5",
                        "aportacion_federal_recibida_local_5",
                        "fecha_recibo_local_5",
                        "aportacion_federal_gastada_local_5",
                        "fecha_gasto_local_5",
                        "numero_cuenta_local_5",
                    ]
                )

            writer.writerow(
                [
                    start_month,
                    end_month,
                    year,
                    name,
                    direction,
                    liaison_officer,
                    title,
                    tel,
                    nombre_agencia_federal_1,
                    catalogo_federal_1,
                    sai_federal_1,
                    titulo_federal_1,
                    aportacion_aprobada_federal_1,
                    fecha_aprobacion_federal_1,
                    aportacion_recibida_federal_1,
                    fecha_recibo_federal_1,
                    aportacion_gastada_federal_1,
                    fecha_gasto_federal_1,
                    nombre_agencia_federal_2,
                    catalogo_federal_2,
                    sai_federal_2,
                    titulo_federal_2,
                    aportacion_aprobada_federal_2,
                    fecha_aprobacion_federal_2,
                    aportacion_recibida_federal_2,
                    fecha_recibo_federal_2,
                    aportacion_gastada_federal_2,
                    fecha_gasto_federal_2,
                    nombre_agencia_federal_3,
                    catalogo_federal_3,
                    sai_federal_3,
                    titulo_federal_3,
                    aportacion_aprobada_federal_3,
                    fecha_aprobacion_federal_3,
                    aportacion_recibida_federal_3,
                    fecha_recibo_federal_3,
                    aportacion_gastada_federal_3,
                    fecha_gasto_federal_3,
                    nombre_agencia_federal_4,
                    catalogo_federal_4,
                    sai_federal_4,
                    titulo_federal_4,
                    aportacion_aprobada_federal_4,
                    fecha_aprobacion_federal_4,
                    aportacion_recibida_federal_4,
                    fecha_recibo_federal_4,
                    aportacion_gastada_federal_4,
                    fecha_gasto_federal_4,
                    nombre_agencia_federal_5,
                    catalogo_federal_5,
                    sai_federal_5,
                    titulo_federal_5,
                    aportacion_aprobada_federal_5,
                    fecha_aprobacion_federal_5,
                    aportacion_recibida_federal_5,
                    fecha_recibo_federal_5,
                    aportacion_gastada_federal_5,
                    fecha_gasto_federal_5,
                    agencia_local_table_box_1,
                    catalogo_local_1,
                    programa_local_1,
                    aportacion_federal_aprobada_local_1,
                    fecha_aprobacion_local_1,
                    aportacion_federal_recibida_local_1,
                    fecha_recibo_local_1,
                    aportacion_federal_gastada_local_1,
                    fecha_gasto_local_1,
                    numero_cuenta_local_1,
                    agencia_local_table_box_2,
                    catalogo_local_2,
                    programa_local_2,
                    aportacion_federal_aprobada_local_2,
                    fecha_aprobacion_local_2,
                    aportacion_federal_recibida_local_2,
                    fecha_recibo_local_2,
                    aportacion_federal_gastada_local_2,
                    fecha_gasto_local_2,
                    numero_cuenta_local_2,
                    agencia_local_table_box_3,
                    catalogo_local_3,
                    programa_local_3,
                    aportacion_federal_aprobada_local_3,
                    fecha_aprobacion_local_3,
                    aportacion_federal_recibida_local_3,
                    fecha_recibo_local_3,
                    aportacion_federal_gastada_local_3,
                    fecha_gasto_local_3,
                    numero_cuenta_local_3,
                    agencia_local_table_box_4,
                    catalogo_local_4,
                    programa_local_4,
                    aportacion_federal_aprobada_local_4,
                    fecha_aprobacion_local_4,
                    aportacion_federal_recibida_local_4,
                    fecha_recibo_local_4,
                    aportacion_federal_gastada_local_4,
                    fecha_gasto_local_4,
                    numero_cuenta_local_4,
                    agencia_local_table_box_5,
                    catalogo_local_5,
                    programa_local_5,
                    aportacion_federal_aprobada_local_5,
                    fecha_aprobacion_local_5,
                    aportacion_federal_recibida_local_5,
                    fecha_recibo_local_5,
                    aportacion_federal_gastada_local_5,
                    fecha_gasto_local_5,
                    numero_cuenta_local_5,
                ]
            )

        return render(request, "forms/succesfull.html")

    return render(request, "forms/quaterly/balanza_de_pagos/JP-304.html")


def JP_361(request):
    if request.method == "POST":
        # Retrieve form data
        income_expenses_year_1 = request.POST.get("income_expenses_year_1")
        income_expenses_year_2 = request.POST.get("income_expenses_year_2")
        income_life_1 = request.POST.get("income_life_1")
        income_life_2 = request.POST.get("income_life_2")
        income_disability_1 = request.POST.get("income_disability_1")
        income_disability_2 = request.POST.get("income_disability_2")
        income_auto_1 = request.POST.get("income_auto_1")
        income_auto_2 = request.POST.get("income_auto_2")
        income_other_1 = request.POST.get("income_other_1")
        income_other_2 = request.POST.get("income_other_2")
        income_interest_1 = request.POST.get("income_interest_1")
        income_interest_2 = request.POST.get("income_interest_2")
        income_rent_1 = request.POST.get("income_rent_1")
        income_rent_2 = request.POST.get("income_rent_2")
        income_other_2_1 = request.POST.get("income_other_2_1")
        income_other_2_2 = request.POST.get("income_other_2_2")
        total_income_1 = request.POST.get("total_income_1")
        total_income_2 = request.POST.get("total_income_2")
        expenses_life_1 = request.POST.get("expenses_life_1")
        expenses_life_2 = request.POST.get("expenses_life_2")
        expenses_disability_1 = request.POST.get("expenses_disability_1")
        expenses_disability_2 = request.POST.get("expenses_disability_2")
        expenses_auto_1 = request.POST.get("expenses_auto_1")
        expenses_auto_2 = request.POST.get("expenses_auto_2")
        expenses_other_1 = request.POST.get("expenses_other_1")
        expenses_other_2 = request.POST.get("expenses_other_2")
        expenses_salaries_1 = request.POST.get("expenses_salaries_1")
        expenses_salaries_2 = request.POST.get("expenses_salaries_2")
        expenses_interes_1 = request.POST.get("expenses_interes_1")
        expenses_interes_2 = request.POST.get("expenses_interes_2")
        expenses_rent_1 = request.POST.get("expenses_rent_1")
        expenses_rent_2 = request.POST.get("expenses_rent_2")
        expenses_depreciation_1 = request.POST.get("expenses_depreciation_1")
        expenses_depreciation_2 = request.POST.get("expenses_depreciation_2")
        expenses_donations_1 = request.POST.get("expenses_donations_1")
        expenses_donations_2 = request.POST.get("expenses_donations_2")
        expenses_commissions_1 = request.POST.get("expenses_commissions_1")
        expenses_commissions_2 = request.POST.get("expenses_commissions_2")
        expenses_employees_1 = request.POST.get("expenses_employees_1")
        expenses_employees_2 = request.POST.get("expenses_employees_2")
        expenses_brokers_1 = request.POST.get("expenses_brokers_1")
        expenses_brokers_2 = request.POST.get("expenses_brokers_2")
        expenses_other_operational_1 = request.POST.get("expenses_other_operational_1")
        expenses_other_operational_2 = request.POST.get("expenses_other_operational_2")
        total_expenses_1 = request.POST.get("total_expenses_1")
        total_expenses_2 = request.POST.get("total_expenses_2")
        net_profit_1 = request.POST.get("net_profit_1")
        net_profit_2 = request.POST.get("net_profit_2")
        balance_year_1 = request.POST.get("balance_year_1")
        balance_year_2 = request.POST.get("balance_year_2")
        guaranteed_1 = request.POST.get("guaranteed_1")
        guaranteed_2 = request.POST.get("guaranteed_2")
        guaranteed_3 = request.POST.get("guaranteed_3")
        guaranteed_4 = request.POST.get("guaranteed_4")
        veterans_1 = request.POST.get("veterans_1")
        veterans_2 = request.POST.get("veterans_2")
        veterans_3 = request.POST.get("veterans_3")
        veterans_4 = request.POST.get("veterans_4")
        conventional_1 = request.POST.get("conventional_1")
        conventional_2 = request.POST.get("conventional_2")
        conventional_3 = request.POST.get("conventional_3")
        conventional_4 = request.POST.get("conventional_4")
        other_1 = request.POST.get("other_1")
        other_2 = request.POST.get("other_2")
        other_3 = request.POST.get("other_3")
        other_4 = request.POST.get("other_4")
        policy_loans_1 = request.POST.get("policy_loans_1")
        policy_loans_2 = request.POST.get("policy_loans_2")
        policy_loans_3 = request.POST.get("policy_loans_3")
        policy_loans_4 = request.POST.get("policy_loans_4")
        other_specify_1 = request.POST.get("other_specify_1")
        other_specify_2 = request.POST.get("other_specify_2")
        other_specify_3 = request.POST.get("other_specify_3")
        other_specify_4 = request.POST.get("other_specify_4")
        policy_reserves_1 = request.POST.get("policy_reserves_1")
        policy_reserves_2 = request.POST.get("policy_reserves_2")
        accrued_dividends_1 = request.POST.get("accrued_dividends_1")
        accrued_dividends_2 = request.POST.get("accrued_dividends_2")
        signature = request.POST.get("signature")
        date = request.POST.get("date")
        phone = request.POST.get("phone")
        position = request.POST.get("position")

        csv_file_path = "data/cuestionarios/balanza_de_pagos/JP-361.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "income_expenses_year_1",
                        "income_expenses_year_2",
                        "income_life_1",
                        "income_life_2",
                        "income_disability_1",
                        "income_disability_2",
                        "income_auto_1",
                        "income_auto_2",
                        "income_other_1",
                        "income_other_2",
                        "income_interest_1",
                        "income_interest_2",
                        "income_rent_1",
                        "income_rent_2",
                        "income_other_2_1",
                        "income_other_2_2",
                        "total_income_1",
                        "total_income_2",
                        "expenses_life_1",
                        "expenses_life_2",
                        "expenses_disability_1",
                        "expenses_disability_2",
                        "expenses_auto_1",
                        "expenses_auto_2",
                        "expenses_other_1",
                        "expenses_other_2",
                        "expenses_salaries_1",
                        "expenses_salaries_2",
                        "expenses_interes_1",
                        "expenses_interes_2",
                        "expenses_rent_1",
                        "expenses_rent_2",
                        "expenses_depreciation_1",
                        "expenses_depreciation_2",
                        "expenses_donations_1",
                        "expenses_donations_2",
                        "expenses_commissions_1",
                        "expenses_commissions_2",
                        "expenses_employees_1",
                        "expenses_employees_2",
                        "expenses_brokers_1",
                        "expenses_brokers_2",
                        "expenses_other_operational_1",
                        "expenses_other_operational_2",
                        "total_expenses_1",
                        "total_expenses_2",
                        "net_profit_1",
                        "net_profit_2",
                        "balance_year_1",
                        "balance_year_2",
                        "guaranteed_1",
                        "guaranteed_2",
                        "guaranteed_3",
                        "guaranteed_4",
                        "veterans_1",
                        "veterans_2",
                        "veterans_3",
                        "veterans_4",
                        "conventional_1",
                        "conventional_2",
                        "conventional_3",
                        "conventional_4",
                        "other_1",
                        "other_2",
                        "other_3",
                        "other_4",
                        "policy_loans_1",
                        "policy_loans_2",
                        "policy_loans_3",
                        "policy_loans_4",
                        "other_specify_1",
                        "other_specify_2",
                        "other_specify_3",
                        "other_specify_4",
                        "policy_reserves_1",
                        "policy_reserves_2",
                        "accrued_dividends_1",
                        "accrued_dividends_2",
                        "signature",
                        "date",
                        "phone",
                        "position",
                    ]
                )

            writer.writerow(
                [
                    income_expenses_year_1,
                    income_expenses_year_2,
                    income_life_1,
                    income_life_2,
                    income_disability_1,
                    income_disability_2,
                    income_auto_1,
                    income_auto_2,
                    income_other_1,
                    income_other_2,
                    income_interest_1,
                    income_interest_2,
                    income_rent_1,
                    income_rent_2,
                    income_other_2_1,
                    income_other_2_2,
                    total_income_1,
                    total_income_2,
                    expenses_life_1,
                    expenses_life_2,
                    expenses_disability_1,
                    expenses_disability_2,
                    expenses_auto_1,
                    expenses_auto_2,
                    expenses_other_1,
                    expenses_other_2,
                    expenses_salaries_1,
                    expenses_salaries_2,
                    expenses_interes_1,
                    expenses_interes_2,
                    expenses_rent_1,
                    expenses_rent_2,
                    expenses_depreciation_1,
                    expenses_depreciation_2,
                    expenses_donations_1,
                    expenses_donations_2,
                    expenses_commissions_1,
                    expenses_commissions_2,
                    expenses_employees_1,
                    expenses_employees_2,
                    expenses_brokers_1,
                    expenses_brokers_2,
                    expenses_other_operational_1,
                    expenses_other_operational_2,
                    total_expenses_1,
                    total_expenses_2,
                    net_profit_1,
                    net_profit_2,
                    balance_year_1,
                    balance_year_2,
                    guaranteed_1,
                    guaranteed_2,
                    guaranteed_3,
                    guaranteed_4,
                    veterans_1,
                    veterans_2,
                    veterans_3,
                    veterans_4,
                    conventional_1,
                    conventional_2,
                    conventional_3,
                    conventional_4,
                    other_1,
                    other_2,
                    other_3,
                    other_4,
                    policy_loans_1,
                    policy_loans_2,
                    policy_loans_3,
                    policy_loans_4,
                    other_specify_1,
                    other_specify_2,
                    other_specify_3,
                    other_specify_4,
                    policy_reserves_1,
                    policy_reserves_2,
                    accrued_dividends_1,
                    accrued_dividends_2,
                    signature,
                    date,
                    phone,
                    position,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/balanza_de_pagos/JP-361.csv",
            dtypes={
                "income_expenses_year_1": int,
                "income_expenses_year_2": int,
                "income_life_1": float,
                "income_life_2": float,
                "income_disability_1": float,
                "income_disability_2": float,
                "income_auto_1": float,
                "income_auto_2": float,
                "income_other_1": float,
                "income_other_2": float,
                "income_interest_1": float,
                "income_interest_2": float,
                "income_rent_1": float,
                "income_rent_2": float,
                "income_other_2_1": float,
                "income_other_2_2": float,
                "total_income_1": float,
                "total_income_2": float,
                "expenses_life_1": float,
                "expenses_life_2": float,
                "expenses_disability_1": float,
                "expenses_disability_2": float,
                "expenses_auto_1": float,
                "expenses_auto_2": float,
                "expenses_other_1": float,
                "expenses_other_2": float,
                "expenses_salaries_1": float,
                "expenses_salaries_2": float,
                "expenses_interes_1": float,
                "expenses_interes_2": float,
                "expenses_rent_1": float,
                "expenses_rent_2": float,
                "expenses_depreciation_1": float,
                "expenses_depreciation_2": float,
                "expenses_donations_1": float,
                "expenses_donations_2": float,
                "expenses_commissions_1": float,
                "expenses_commissions_2": float,
                "expenses_employees_1": float,
                "expenses_employees_2": float,
                "expenses_brokers_1": float,
                "expenses_brokers_2": float,
                "expenses_other_operational_1": float,
                "expenses_other_operational_2": float,
                "total_expenses_1": float,
                "total_expenses_2": float,
                "net_profit_1": float,
                "net_profit_2": float,
                "balance_year_1": int,
                "balance_year_2": int,
                "guaranteed_1": float,
                "guaranteed_2": float,
                "guaranteed_3": float,
                "guaranteed_4": float,
                "veterans_1": float,
                "veterans_2": float,
                "veterans_3": float,
                "veterans_4": float,
                "conventional_1": float,
                "conventional_2": float,
                "conventional_3": float,
                "conventional_4": float,
                "other_1": float,
                "other_2": float,
                "other_3": float,
                "other_4": float,
                "policy_loans_1": float,
                "policy_loans_2": float,
                "policy_loans_3": float,
                "policy_loans_4": float,
                "other_specify_1": float,
                "other_specify_2": float,
                "other_specify_3": float,
                "other_specify_4": float,
                "policy_reserves_1": float,
                "policy_reserves_2": float,
                "accrued_dividends_1": float,
                "accrued_dividends_2": float,
                "signature": str,
                "date": str,
                "phone": str,
                "position": str,
            },
            table_name="JP_361",
            table_id="2",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/balanza_de_pagos/JP-361.html")


def JP_362(request):
    if request.method == "POST":
        # Retrieve form data
        year_1 = request.POST.get("year_1")
        year_2 = request.POST.get("year_2")

        company_name = request.POST.get("company_name")

        debts_balance = request.POST.get("debts_balance")
        debts_emision = request.POST.get("debts_emision")
        debts_amortizacion = request.POST.get("debts_amortizacion")
        debts_final = request.POST.get("debts_final")
        debts_interes = request.POST.get("debts_interes")
        debts_acreedor = request.POST.get("debts_acreedor")

        debts_bond_balance = request.POST.get("debts_bond_balance")
        debts_bond_emision = request.POST.get("debts_bond_emision")
        debts_bond_amortizacion = request.POST.get("debts_bond_amortizacion")
        debts_bond_final = request.POST.get("debts_bond_final")
        debts_bond_interes = request.POST.get("debts_bond_interes")
        debts_bond_acreedor = request.POST.get("debts_bond_acreedor")

        debts_promossory_notes_balance = request.POST.get(
            "debts_promossory_notes_balance"
        )
        debts_promossory_notes_emision = request.POST.get(
            "debts_promossory_notes_emision"
        )
        debts_promossory_notes_amortizacion = request.POST.get(
            "debts_promossory_notes_amortizacion"
        )
        debts_promossory_notes_final = request.POST.get("debts_promossory_notes_final")
        debts_promossory_notes_interes = request.POST.get(
            "debts_promossory_notes_interes"
        )
        debts_promossory_notes_acreedor = request.POST.get(
            "debts_promossory_notes_acreedor"
        )

        debts_others_balance = request.POST.get("debts_others_balance")
        debts_others_emision = request.POST.get("debts_others_emision")
        debts_others_amortizacion = request.POST.get("debts_others_amortizacion")
        debts_others_final = request.POST.get("debts_others_final")
        debts_others_interes = request.POST.get("debts_others_interes")
        debts_others_acreedor = request.POST.get("debts_others_acreedor")

        short_promossory_balance = request.POST.get("short_promossory_balance")
        short_promossory_emision = request.POST.get("short_promossory_emision")
        short_promossory_amortizacion = request.POST.get(
            "short_promossory_amortizacion"
        )
        short_promossory_final = request.POST.get("short_promossory_final")
        short_promossory_interes = request.POST.get("short_promossory_interes")
        short_promossory_acreedor = request.POST.get("short_promossory_acreedor")

        short_account_balance = request.POST.get("short_account_balance")
        short_account_emision = request.POST.get("short_account_emision")
        short_account_amortizacion = request.POST.get("short_account_amortizacion")
        short_account_final = request.POST.get("short_account_final")
        short_account_interes = request.POST.get("short_account_interes")
        short_account_acreedor = request.POST.get("short_account_acreedor")

        short_others_balance = request.POST.get("short_others_balance")
        short_others_emision = request.POST.get("short_others_emision")
        short_others_amortizacion = request.POST.get("short_others_amortizacion")
        short_others_final = request.POST.get("short_others_final")
        short_others_interes = request.POST.get("short_others_interes")
        short_others_acreedor = request.POST.get("short_others_acreedor")

        short_term_balance = request.POST.get("short_term_balance")
        short_term_emision = request.POST.get("short_term_emision")
        short_term_amortizacion = request.POST.get("short_term_amortizacion")
        short_term_final = request.POST.get("short_term_final")
        short_term_interes = request.POST.get("short_term_interes")
        short_term_acreedor = request.POST.get("short_term_acreedor")

        assets_balance = request.POST.get("assets_balance")
        assets_emision = request.POST.get("assets_emision")
        assets_amortizacion = request.POST.get("assets_amortizacion")
        assets_final = request.POST.get("assets_final")
        assets_interes = request.POST.get("assets_interes")

        assets_values_balance = request.POST.get("assets_values_balance")
        assets_values_emision = request.POST.get("assets_values_emision")
        assets_values_amortizacion = request.POST.get("assets_values_amortizacion")
        assets_values_final = request.POST.get("assets_values_final")
        assets_values_interes = request.POST.get("assets_values_interes")

        assets_others_balance = request.POST.get("assets_others_balance")
        assets_others_emision = request.POST.get("assets_others_emision")
        assets_others_amortizacion = request.POST.get("assets_others_amortizacion")
        assets_others_final = request.POST.get("assets_others_final")
        assets_others_interes = request.POST.get("assets_others_interes")

        short_balance = request.POST.get("short_balance")
        short_emision = request.POST.get("short_emision")
        short_amortizacion = request.POST.get("short_amortizacion")
        short_final = request.POST.get("short_final")
        short_interes = request.POST.get("short_interes")

        short_balance_balance = request.POST.get("short_balance_balance")
        short_balance_emision = request.POST.get("short_balance_emision")
        short_balance_amortizacion = request.POST.get("short_balance_amortizacion")
        short_balance_final = request.POST.get("short_balance_final")
        short_balance_interes = request.POST.get("short_balance_interes")

        short_accouts_balance = request.POST.get("short_accouts_balance")
        short_accouts_emision = request.POST.get("short_accouts_emision")
        short_accouts_amortizacion = request.POST.get("short_accouts_amortizacion")
        short_accouts_final = request.POST.get("short_accouts_final")
        short_accouts_interes = request.POST.get("short_accouts_interes")

        short_others_balance_2 = request.POST.get("short_others_balance_2")
        short_others_emision_2 = request.POST.get("short_others_emision_2")
        short_others_amortizacion_2 = request.POST.get("short_others_amortizacion_2")
        short_others_final_2 = request.POST.get("short_others_final_2")
        short_others_interes_2 = request.POST.get("short_others_interes_2")

        signature = request.POST.get("signature")
        position = request.POST.get("position")
        date = request.POST.get("date")
        phone = request.POST.get("phone")

        csv_file_path = "data/cuestionarios/balanza_de_pagos/JP-362.csv"
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
                        "company_name",
                        "debts_balance",
                        "debts_emision",
                        "debts_amortizacion",
                        "debts_final",
                        "debts_interes",
                        "debts_acreedor",
                        "debts_bond_balance",
                        "debts_bond_emision",
                        "debts_bond_amortizacion",
                        "debts_bond_final",
                        "debts_bond_interes",
                        "debts_bond_acreedor",
                        "debts_promossory_notes_balance",
                        "debts_promossory_notes_emision",
                        "debts_promossory_notes_amortizacion",
                        "debts_promossory_notes_final",
                        "debts_promossory_notes_interes",
                        "debts_promossory_notes_acreedor",
                        "debts_others_balance",
                        "debts_others_emision",
                        "debts_others_amortizacion",
                        "debts_others_final",
                        "debts_others_interes",
                        "debts_others_acreedor",
                        "short_term_balance",
                        "short_term_emision",
                        "short_term_amortizacion",
                        "short_term_final",
                        "short_term_interes",
                        "short_term_acreedor",
                        "short_promossory_balance",
                        "short_promossory_emision",
                        "short_promossory_amortizacion",
                        "short_promossory_final",
                        "short_promossory_interes",
                        "short_promossory_acreedor",
                        "short_account_balance",
                        "short_account_emision",
                        "short_account_amortizacion",
                        "short_account_final",
                        "short_account_interes",
                        "short_account_acreedor",
                        "short_others_balance",
                        "short_others_emision",
                        "short_others_amortizacion",
                        "short_others_final",
                        "short_others_interes",
                        "short_others_acreedor",
                        "assets_balance",
                        "assets_emision",
                        "assets_amortizacion",
                        "assets_final",
                        "assets_interes",
                        "assets_values_balance",
                        "assets_values_emision",
                        "assets_values_amortizacion",
                        "assets_values_final",
                        "assets_values_interes",
                        "assets_others_balance",
                        "assets_others_emision",
                        "assets_others_amortizacion",
                        "assets_others_final",
                        "assets_others_interes",
                        "short_balance",
                        "short_emision",
                        "short_amortizacion",
                        "short_final",
                        "short_interes",
                        "short_balance_balance",
                        "short_balance_emision",
                        "short_balance_amortizacion",
                        "short_balance_final",
                        "short_balance_interes",
                        "short_accouts_balance",
                        "short_accouts_emision",
                        "short_accouts_amortizacion",
                        "short_accouts_final",
                        "short_accouts_interes",
                        "short_others_balance_2",
                        "short_others_emision_2",
                        "short_others_amortizacion_2",
                        "short_others_final_2",
                        "short_others_interes_2",
                        "signature",
                        "position",
                        "date",
                        "phone",
                    ]
                )

            writer.writerow(
                [
                    year_1,
                    year_2,
                    company_name,
                    debts_balance,
                    debts_emision,
                    debts_amortizacion,
                    debts_final,
                    debts_interes,
                    debts_acreedor,
                    debts_bond_balance,
                    debts_bond_emision,
                    debts_bond_amortizacion,
                    debts_bond_final,
                    debts_bond_interes,
                    debts_bond_acreedor,
                    debts_promossory_notes_balance,
                    debts_promossory_notes_emision,
                    debts_promossory_notes_amortizacion,
                    debts_promossory_notes_final,
                    debts_promossory_notes_interes,
                    debts_promossory_notes_acreedor,
                    debts_others_balance,
                    debts_others_emision,
                    debts_others_amortizacion,
                    debts_others_final,
                    debts_others_interes,
                    debts_others_acreedor,
                    short_term_balance,
                    short_term_emision,
                    short_term_amortizacion,
                    short_term_final,
                    short_term_interes,
                    short_term_acreedor,
                    short_promossory_balance,
                    short_promossory_emision,
                    short_promossory_amortizacion,
                    short_promossory_final,
                    short_promossory_interes,
                    short_promossory_acreedor,
                    short_account_balance,
                    short_account_emision,
                    short_account_amortizacion,
                    short_account_final,
                    short_account_interes,
                    short_account_acreedor,
                    short_others_balance,
                    short_others_emision,
                    short_others_amortizacion,
                    short_others_final,
                    short_others_interes,
                    short_others_acreedor,
                    assets_balance,
                    assets_emision,
                    assets_amortizacion,
                    assets_final,
                    assets_interes,
                    assets_values_balance,
                    assets_values_emision,
                    assets_values_amortizacion,
                    assets_values_final,
                    assets_values_interes,
                    assets_others_balance,
                    assets_others_emision,
                    assets_others_amortizacion,
                    assets_others_final,
                    assets_others_interes,
                    short_balance,
                    short_emision,
                    short_amortizacion,
                    short_final,
                    short_interes,
                    short_balance_balance,
                    short_balance_emision,
                    short_balance_amortizacion,
                    short_balance_final,
                    short_balance_interes,
                    short_accouts_balance,
                    short_accouts_emision,
                    short_accouts_amortizacion,
                    short_accouts_final,
                    short_accouts_interes,
                    short_others_balance_2,
                    short_others_emision_2,
                    short_others_amortizacion_2,
                    short_others_final_2,
                    short_others_interes_2,
                    signature,
                    position,
                    date,
                    phone,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/balanza_de_pagos/JP-362.csv",
            dtypes={
                "year_1": int,
                "year_2": int,
                "company_name": str,
                "debts_balance": float,
                "debts_emision": float,
                "debts_amortizacion": float,
                "debts_final": float,
                "debts_interes": float,
                "debts_acreedor": str,
                "debts_bond_balance": float,
                "debts_bond_emision": float,
                "debts_bond_amortizacion": float,
                "debts_bond_final": float,
                "debts_bond_interes": float,
                "debts_bond_acreedor": str,
                "debts_promossory_notes_balance": float,
                "debts_promossory_notes_emision": float,
                "debts_promossory_notes_amortizacion": float,
                "debts_promossory_notes_final": float,
                "debts_promossory_notes_interes": float,
                "debts_promossory_notes_acreedor": str,
                "debts_others_balance": float,
                "debts_others_emision": float,
                "debts_others_amortizacion": float,
                "debts_others_final": float,
                "debts_others_interes": float,
                "debts_others_acreedor": str,
                "short_term_balance": float,
                "short_term_emision": float,
                "short_term_amortizacion": float,
                "short_term_final": float,
                "short_term_interes": float,
                "short_term_acreedor": str,
                "short_promossory_balance": float,
                "short_promossory_emision": float,
                "short_promossory_amortizacion": float,
                "short_promossory_final": float,
                "short_promossory_interes": float,
                "short_promossory_acreedor": str,
                "short_account_balance": float,
                "short_account_emision": float,
                "short_account_amortizacion": float,
                "short_account_final": float,
                "short_account_interes": float,
                "short_account_acreedor": str,
                "short_others_balance": float,
                "short_others_emision": float,
                "short_others_amortizacion": float,
                "short_others_final": float,
                "short_others_interes": float,
                "short_others_acreedor": str,
                "assets_balance": float,
                "assets_emision": float,
                "assets_amortizacion": float,
                "assets_final": float,
                "assets_interes": float,
                "assets_values_balance": float,
                "assets_values_emision": float,
                "assets_values_amortizacion": float,
                "assets_values_final": float,
                "assets_values_interes": float,
                "assets_others_balance": float,
                "assets_others_emision": float,
                "assets_others_amortizacion": float,
                "assets_others_final": float,
                "assets_others_interes": float,
                "short_balance": float,
                "short_emision": float,
                "short_amortizacion": float,
                "short_final": float,
                "short_interes": float,
                "short_balance_balance": float,
                "short_balance_emision": float,
                "short_balance_amortizacion": float,
                "short_balance_final": float,
                "short_balance_interes": float,
                "short_accouts_balance": float,
                "short_accouts_emision": float,
                "short_accouts_amortizacion": float,
                "short_accouts_final": float,
                "short_accouts_interes": float,
                "short_others_balance_2": float,
                "short_others_emision_2": float,
                "short_others_amortizacion_2": float,
                "short_others_final_2": float,
                "short_others_interes_2": float,
                "signature": str,
                "position": str,
                "date": str,
                "phone": str,
            },
            table_name="JP_362",
            table_id="3",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/balanza_de_pagos/JP-362.html")


def JP_364(request):
    if request.method == "POST":
        # Retrieve form data
        year_bono1 = request.POST.get("year_bono1")
        year_bono2 = request.POST.get("year_bono2")
        year_paga1 = request.POST.get("year_paga1")
        year_paga2 = request.POST.get("year_paga2")
        ELA_bono1 = request.POST.get("ELA_bono1")
        ELA_bono2 = request.POST.get("ELA_bono2")
        ELA_paga1 = request.POST.get("ELA_paga1")
        ELA_paga2 = request.POST.get("ELA_paga2")
        ELA_agente = request.POST.get("ELA_agente")
        municipio_bono1 = request.POST.get("municipio_bono1")
        municipio_bono2 = request.POST.get("municipio_bono2")
        municipio_paga1 = request.POST.get("municipio_paga1")
        municipio_paga2 = request.POST.get("municipio_paga2")
        municipio_agente = request.POST.get("municipio_agente")
        corp_publicas_bono1 = request.POST.get("corp_publicas_bono1")
        corp_publicas_bono2 = request.POST.get("corp_publicas_bono2")
        corp_publicas_paga1 = request.POST.get("corp_publicas_paga1")
        corp_publicas_paga2 = request.POST.get("corp_publicas_paga2")
        corp_publicas_agente = request.POST.get("corp_publicas_agente")
        AEE_bono1 = request.POST.get("AEE_bono1")
        AEE_bono2 = request.POST.get("AEE_bono2")
        AEE_paga1 = request.POST.get("AEE_paga1")
        AEE_paga2 = request.POST.get("AEE_paga2")
        AEE_agente = request.POST.get("AEE_agente")
        Acarreteras_bono1 = request.POST.get("Acarreteras_bono1")
        Acarreteras_bono2 = request.POST.get("Acarreteras_bono2")
        Acarreteras_paga1 = request.POST.get("Acarreteras_paga1")
        Acarreteras_paga2 = request.POST.get("Acarreteras_paga2")
        Acarreteras_agente = request.POST.get("Acarreteras_agente")
        AAA_bono1 = request.POST.get("AAA_bono1")
        AAA_bono2 = request.POST.get("AAA_bono2")
        AAA_paga1 = request.POST.get("AAA_paga1")
        AAA_paga2 = request.POST.get("AAA_paga2")
        AAA_agente = request.POST.get("AAA_agente")
        AEP_bono1 = request.POST.get("AEP_bono1")
        AEP_bono2 = request.POST.get("AEP_bono2")
        AEP_paga1 = request.POST.get("AEP_paga1")
        AEP_paga2 = request.POST.get("AEP_paga2")
        AEP_agente = request.POST.get("AEP_agente")
        AP_bono1 = request.POST.get("AP_bono1")
        AP_bono2 = request.POST.get("AP_bono2")
        AP_paga1 = request.POST.get("AP_paga1")
        AP_paga2 = request.POST.get("AP_paga2")
        AP_agente = request.POST.get("AP_agente")
        AT_bono1 = request.POST.get("AT_bono1")
        AT_bono2 = request.POST.get("AT_bono2")
        AT_paga1 = request.POST.get("AT_paga1")
        AT_paga2 = request.POST.get("AT_paga2")
        AT_agente = request.POST.get("AT_agente")
        CFI_bono1 = request.POST.get("CFI_bono1")
        CFI_bono2 = request.POST.get("CFI_bono2")
        CFI_paga1 = request.POST.get("CFI_paga1")
        CFI_paga2 = request.POST.get("CFI_paga2")
        CFI_agente = request.POST.get("CFI_agente")
        BGF_bono1 = request.POST.get("BGF_bono1")
        BGF_bono2 = request.POST.get("BGF_bono2")
        BGF_paga1 = request.POST.get("BGF_paga1")
        BGF_paga2 = request.POST.get("BGF_paga2")
        BGF_agente = request.POST.get("BGF_agente")
        CFV_bono1 = request.POST.get("CFV_bono1")
        CFV_bono2 = request.POST.get("CFV_bono2")
        CFV_paga1 = request.POST.get("CFV_paga1")
        CFV_paga2 = request.POST.get("CFV_paga2")
        CFV_agente = request.POST.get("CFV_agente")
        otherk_title = request.POST.get("otherk_title")
        otherk_bono1 = request.POST.get("otherk_bono1")
        otherk_bono2 = request.POST.get("otherk_bono2")
        otherk_paga1 = request.POST.get("otherk_paga1")
        otherk_paga2 = request.POST.get("otherk_paga2")
        otherk_agente = request.POST.get("otherk_agente")
        otherl_title = request.POST.get("otherl_title")
        otherl_bono1 = request.POST.get("otherl_bono1")
        otherl_bono2 = request.POST.get("otherl_bono2")
        otherl_paga1 = request.POST.get("otherl_paga1")
        otherl_paga2 = request.POST.get("otherl_paga2")
        otherl_agente = request.POST.get("otherl_agente")
        otherm_title = request.POST.get("otherm_title")
        otherm_bono1 = request.POST.get("otherm_bono1")
        otherm_bono2 = request.POST.get("otherm_bono2")
        otherm_paga1 = request.POST.get("otherm_paga1")
        otherm_paga2 = request.POST.get("otherm_paga2")
        otherm_agente = request.POST.get("otherm_agente")

        year_balance1 = request.POST.get("year_balance1")
        year_balance2 = request.POST.get("year_balance2")
        FHA_balance1 = request.POST.get("FHA_balance1")
        FHA_balance2 = request.POST.get("FHA_balance2")
        FHA_agente = request.POST.get("FHA_agente")
        GAV_balance1 = request.POST.get("GAV_balance1")
        GAV_balance2 = request.POST.get("GAV_balance2")
        GAV_agente = request.POST.get("GAV_agente")
        convencionales_balance1 = request.POST.get("convencionales_balance1")
        convencionales_balance2 = request.POST.get("convencionales_balance2")
        convencionales_agente = request.POST.get("convencionales_agente")
        otras_instituciones_balance1 = request.POST.get("otras_instituciones_balance1")
        otras_instituciones_balance2 = request.POST.get("otras_instituciones_balance2")
        otras_instituciones_agente = request.POST.get("otras_instituciones_agente")
        prestamos_hipo_balance1 = request.POST.get("prestamos_hipo_balance1")
        prestamos_hipo_balance2 = request.POST.get("prestamos_hipo_balance2")
        prestamos_hipo_agente = request.POST.get("prestamos_hipo_agente")
        prestamos_comerciales_industriales_balance1 = request.POST.get(
            "prestamos_comerciales_industriales_balance1"
        )
        prestamos_comerciales_industriales_balance2 = request.POST.get(
            "prestamos_comerciales_industriales_balance2"
        )
        prestamos_comerciales_industriales_agente = request.POST.get(
            "prestamos_comerciales_industriales_agente"
        )
        prestamos_poliza_balance1 = request.POST.get("prestamos_poliza_balance1")
        prestamos_poliza_balance2 = request.POST.get("prestamos_poliza_balance2")
        prestamos_poliza_agente = request.POST.get("prestamos_poliza_agente")
        reservas_poliza_balance1 = request.POST.get("reservas_poliza_balance1")
        reservas_poliza_balance2 = request.POST.get("reservas_poliza_balance2")
        reservas_poliza_agente = request.POST.get("reservas_poliza_agente")
        dividendos_poliza_balance1 = request.POST.get("dividendos_poliza_balance1")
        dividendos_poliza_balance2 = request.POST.get("dividendos_poliza_balance2")
        dividendos_poliza_agente = request.POST.get("dividendos_poliza_agente")
        signature = request.POST.get("nombre_firma")
        phone = request.POST.get("phone")
        nombre_persona = request.POST.get("nombre_persona")

        csv_file_path = "data/cuestionarios/balanza_de_pagos/JP-364.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "year_bono1",
                        "year_bono2",
                        "year_paga1",
                        "year_paga2",
                        "ELA_bono1",
                        "ELA_bono2",
                        "ELA_paga1",
                        "ELA_paga2",
                        "ELA_agente",
                        "municipio_bono1",
                        "municipio_bono2",
                        "municipio_paga1",
                        "municipio_paga2",
                        "municipio_agente",
                        "corp_publicas_bono1",
                        "corp_publicas_bono2",
                        "corp_publicas_paga1",
                        "corp_publicas_paga2",
                        "corp_publicas_agente",
                        "AEE_bono1",
                        "AEE_bono2",
                        "AEE_paga1",
                        "AEE_paga2",
                        "AEE_agente",
                        "Acarreteras_bono1",
                        "Acarreteras_bono2",
                        "Acarreteras_paga1",
                        "Acarreteras_paga2",
                        "Acarreteras_agente",
                        "AAA_bono1",
                        "AAA_bono2",
                        "AAA_paga1",
                        "AAA_paga2",
                        "AAA_agente",
                        "AEP_bono1",
                        "AEP_bono2",
                        "AEP_paga1",
                        "AEP_paga2",
                        "AEP_agente",
                        "AP_bono1",
                        "AP_bono2",
                        "AP_paga1",
                        "AP_paga2",
                        "AP_agente",
                        "AT_bono1",
                        "AT_bono2",
                        "AT_paga1",
                        "AT_paga2",
                        "AT_agente",
                        "CFI_bono1",
                        "CFI_bono2",
                        "CFI_paga1",
                        "CFI_paga2",
                        "CFI_agente",
                        "BGF_bono1",
                        "BGF_bono2",
                        "BGF_paga1",
                        "BGF_paga2",
                        "BGF_agente",
                        "CFV_bono1",
                        "CFV_bono2",
                        "CFV_paga1",
                        "CFV_paga2",
                        "CFV_agente",
                        "otherk_title",
                        "otherk_bono1",
                        "otherk_bono2",
                        "otherk_paga1",
                        "otherk_paga2",
                        "otherk_agente",
                        "otherl_title",
                        "otherl_bono1",
                        "otherl_bono2",
                        "otherl_paga1",
                        "otherl_paga2",
                        "otherl_agente",
                        "otherm_title",
                        "otherm_bono1",
                        "otherm_bono2",
                        "otherm_paga1",
                        "otherm_paga2",
                        "otherm_agente",
                        "year_balance1",
                        "year_balance2",
                        "FHA_balance1",
                        "FHA_balance2",
                        "FHA_agente",
                        "GAV_balance1",
                        "GAV_balance2",
                        "GAV_agente",
                        "convencionales_balance1",
                        "convencionales_balance2",
                        "convencionales_agente",
                        "otras_instituciones_balance1",
                        "otras_instituciones_balance2",
                        "otras_instituciones_agente",
                        "prestamos_hipo_balance1",
                        "prestamos_hipo_balance2",
                        "prestamos_hipo_agente",
                        "prestamos_comerciales_industriales_balance1",
                        "prestamos_comerciales_industriales_balance2",
                        "prestamos_comerciales_industriales_agente",
                        "prestamos_poliza_balance1",
                        "prestamos_poliza_balance2",
                        "prestamos_poliza_agente",
                        "reservas_poliza_balance1",
                        "reservas_poliza_balance2",
                        "reservas_poliza_agente",
                        "dividendos_poliza_balance1",
                        "dividendos_poliza_balance2",
                        "dividendos_poliza_agente",
                        "signature",
                        "phone",
                        "nombre_persona",
                    ]
                )

            writer.writerow(
                [
                    year_bono1,
                    year_bono2,
                    year_paga1,
                    year_paga2,
                    ELA_bono1,
                    ELA_bono2,
                    ELA_paga1,
                    ELA_paga2,
                    ELA_agente,
                    municipio_bono1,
                    municipio_bono2,
                    municipio_paga1,
                    municipio_paga2,
                    municipio_agente,
                    corp_publicas_bono1,
                    corp_publicas_bono2,
                    corp_publicas_paga1,
                    corp_publicas_paga2,
                    corp_publicas_agente,
                    AEE_bono1,
                    AEE_bono2,
                    AEE_paga1,
                    AEE_paga2,
                    AEE_agente,
                    Acarreteras_bono1,
                    Acarreteras_bono2,
                    Acarreteras_paga1,
                    Acarreteras_paga2,
                    Acarreteras_agente,
                    AAA_bono1,
                    AAA_bono2,
                    AAA_paga1,
                    AAA_paga2,
                    AAA_agente,
                    AEP_bono1,
                    AEP_bono2,
                    AEP_paga1,
                    AEP_paga2,
                    AEP_agente,
                    AP_bono1,
                    AP_bono2,
                    AP_paga1,
                    AP_paga2,
                    AP_agente,
                    AT_bono1,
                    AT_bono2,
                    AT_paga1,
                    AT_paga2,
                    AT_agente,
                    CFI_bono1,
                    CFI_bono2,
                    CFI_paga1,
                    CFI_paga2,
                    CFI_agente,
                    BGF_bono1,
                    BGF_bono2,
                    BGF_paga1,
                    BGF_paga2,
                    BGF_agente,
                    CFV_bono1,
                    CFV_bono2,
                    CFV_paga1,
                    CFV_paga2,
                    CFV_agente,
                    otherk_title,
                    otherk_bono1,
                    otherk_bono2,
                    otherk_paga1,
                    otherk_paga2,
                    otherk_agente,
                    otherl_title,
                    otherl_bono1,
                    otherl_bono2,
                    otherl_paga1,
                    otherl_paga2,
                    otherl_agente,
                    otherm_title,
                    otherm_bono1,
                    otherm_bono2,
                    otherm_paga1,
                    otherm_paga2,
                    otherm_agente,
                    year_balance1,
                    year_balance2,
                    FHA_balance1,
                    FHA_balance2,
                    FHA_agente,
                    GAV_balance1,
                    GAV_balance2,
                    GAV_agente,
                    convencionales_balance1,
                    convencionales_balance2,
                    convencionales_agente,
                    otras_instituciones_balance1,
                    otras_instituciones_balance2,
                    otras_instituciones_agente,
                    prestamos_hipo_balance1,
                    prestamos_hipo_balance2,
                    prestamos_hipo_agente,
                    prestamos_comerciales_industriales_balance1,
                    prestamos_comerciales_industriales_balance2,
                    prestamos_comerciales_industriales_agente,
                    prestamos_poliza_balance1,
                    prestamos_poliza_balance2,
                    prestamos_poliza_agente,
                    reservas_poliza_balance1,
                    reservas_poliza_balance2,
                    reservas_poliza_agente,
                    dividendos_poliza_balance1,
                    dividendos_poliza_balance2,
                    dividendos_poliza_agente,
                    signature,
                    phone,
                    nombre_persona,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/balanza_de_pagos/JP-364.csv",
            dtypes={
                "year_bono1": int,
                "year_bono2": int,
                "year_paga1": int,
                "year_paga2": int,
                "ELA_bono1": float,
                "ELA_bono2": float,
                "ELA_paga1": float,
                "ELA_paga2": float,
                "ELA_agente": str,
                "municipio_bono1": float,
                "municipio_bono2": float,
                "municipio_paga1": float,
                "municipio_paga2": float,
                "municipio_agente": str,
                "corp_publicas_bono1": float,
                "corp_publicas_bono2": float,
                "corp_publicas_paga1": float,
                "corp_publicas_paga2": float,
                "corp_publicas_agente": str,
                "AEE_bono1": float,
                "AEE_bono2": float,
                "AEE_paga1": float,
                "AEE_paga2": float,
                "AEE_agente": str,
                "Acarreteras_bono1": float,
                "Acarreteras_bono2": float,
                "Acarreteras_paga1": float,
                "Acarreteras_paga2": float,
                "Acarreteras_agente": str,
                "AAA_bono1": float,
                "AAA_bono2": float,
                "AAA_paga1": float,
                "AAA_paga2": float,
                "AAA_agente": str,
                "AEP_bono1": float,
                "AEP_bono2": float,
                "AEP_paga1": float,
                "AEP_paga2": float,
                "AEP_agente": str,
                "AP_bono1": float,
                "AP_bono2": float,
                "AP_paga1": float,
                "AP_paga2": float,
                "AP_agente": str,
                "AT_bono1": float,
                "AT_bono2": float,
                "AT_paga1": float,
                "AT_paga2": float,
                "AT_agente": str,
                "CFI_bono1": float,
                "CFI_bono2": float,
                "CFI_paga1": float,
                "CFI_paga2": float,
                "CFI_agente": str,
                "BGF_bono1": float,
                "BGF_bono2": float,
                "BGF_paga1": float,
                "BGF_paga2": float,
                "BGF_agente": str,
                "CFV_bono1": float,
                "CFV_bono2": float,
                "CFV_paga1": float,
                "CFV_paga2": float,
                "CFV_agente": str,
                "otherk_title": str,
                "otherk_bono1": float,
                "otherk_bono2": float,
                "otherk_paga1": float,
                "otherk_paga2": float,
                "otherk_agente": str,
                "otherl_title": str,
                "otherl_bono1": float,
                "otherl_bono2": float,
                "otherl_paga1": float,
                "otherl_paga2": float,
                "otherl_agente": str,
                "otherm_title": str,
                "otherm_bono1": float,
                "otherm_bono2": float,
                "otherm_paga1": float,
                "otherm_paga2": float,
                "otherm_agente": str,
                "year_balance1": int,
                "year_balance2": int,
                "FHA_balance1": float,
                "FHA_balance2": float,
                "FHA_agente": str,
                "GAV_balance1": float,
                "GAV_balance2": float,
                "GAV_agente": str,
                "convencionales_balance1": float,
                "convencionales_balance2": float,
                "convencionales_agente": str,
                "otras_instituciones_balance1": float,
                "otras_instituciones_balance2": float,
                "otras_instituciones_agente": str,
                "prestamos_hipo_balance1": float,
                "prestamos_hipo_balance2": float,
                "prestamos_hipo_agente": str,
                "prestamos_comerciales_industriales_balance1": float,
                "prestamos_comerciales_industriales_balance2": float,
                "prestamos_comerciales_industriales_agente": str,
                "prestamos_poliza_balance1": float,
                "prestamos_poliza_balance2": float,
                "prestamos_poliza_agente": str,
                "reservas_poliza_balance1": float,
                "reservas_poliza_balance2": float,
                "reservas_poliza_agente": str,
                "dividendos_poliza_balance1": float,
                "dividendos_poliza_balance2": float,
                "dividendos_poliza_agente": str,
                "signature": str,
                "phone": str,
                "nombre_persona": str,
            },
            table_name="JP_364",
            table_id="4",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/balanza_de_pagos/JP-364.html")


def JP_529(request):
    if request.method == "POST":
        # Retrieve form data
        # header
        year1 = request.POST.get("year1")
        year2 = request.POST.get("year2")
        company = request.POST.get("company")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")
        tel = request.POST.get("tel")

        choice = request.POST.get("choice")

        # tabla 1
        agencia_a1 = request.POST.get("agencia_a1")
        federal_program_a1 = request.POST.get("federal_program_a1")
        quantity_a1 = request.POST.get("quantity_a1")
        date_a1 = request.POST.get("date_a1")

        agencia_a2 = request.POST.get("agencia_a2")
        federal_program_a2 = request.POST.get("federal_program_a2")
        quantity_a2 = request.POST.get("quantity_a2")
        date_a2 = request.POST.get("date_a2")

        agencia_a3 = request.POST.get("agencia_a3")
        federal_program_a3 = request.POST.get("federal_program_a3")
        quantity_a3 = request.POST.get("quantity_a3")
        date_a3 = request.POST.get("date_a3")

        agencia_a4 = request.POST.get("agencia_a4")
        federal_program_a4 = request.POST.get("federal_program_a4")
        quantity_a4 = request.POST.get("quantity_a4")
        date_a4 = request.POST.get("date_a4")

        agencia_a5 = request.POST.get("agencia_a5")
        federal_program_a5 = request.POST.get("federal_program_a5")
        quantity_a5 = request.POST.get("quantity_a5")
        date_a5 = request.POST.get("date_a5")

        agencia_a6 = request.POST.get("agencia_a6")
        federal_program_a6 = request.POST.get("federal_program_a6")
        quantity_a6 = request.POST.get("quantity_a6")
        date_a6 = request.POST.get("date_a6")

        agencia_a7 = request.POST.get("agencia_a7")
        federal_program_a7 = request.POST.get("federal_program_a7")
        quantity_a7 = request.POST.get("quantity_a7")
        date_a7 = request.POST.get("date_a7")

        agencia_a8 = request.POST.get("agencia_a8")
        federal_program_a8 = request.POST.get("federal_program_a8")
        quantity_a8 = request.POST.get("quantity_a8")
        date_a8 = request.POST.get("date_a8")

        # tabla 2
        agencia_b1 = request.POST.get("agencia_b1")
        federal_program_b1 = request.POST.get("federal_program_b1")
        quantity_b1 = request.POST.get("quantity_b1")
        date_b1 = request.POST.get("date_b1")

        agencia_b2 = request.POST.get("agencia_b2")
        federal_program_b2 = request.POST.get("federal_program_b2")
        quantity_b2 = request.POST.get("quantity_b2")
        date_b2 = request.POST.get("date_b2")

        agencia_b3 = request.POST.get("agencia_b3")
        federal_program_b3 = request.POST.get("federal_program_b3")
        quantity_b3 = request.POST.get("quantity_b3")
        date_b3 = request.POST.get("date_b3")

        agencia_b4 = request.POST.get("agencia_b4")
        federal_program_b4 = request.POST.get("federal_program_b4")
        quantity_b4 = request.POST.get("quantity_b4")
        date_b4 = request.POST.get("date_b4")

        agencia_b5 = request.POST.get("agencia_b5")
        federal_program_b5 = request.POST.get("federal_program_b5")
        quantity_b5 = request.POST.get("quantity_b5")
        date_b5 = request.POST.get("date_b5")

        agencia_b6 = request.POST.get("agencia_b6")
        federal_program_b6 = request.POST.get("federal_program_b6")
        quantity_b6 = request.POST.get("quantity_b6")
        date_b6 = request.POST.get("date_b6")

        agencia_b7 = request.POST.get("agencia_b7")
        federal_program_b7 = request.POST.get("federal_program_b7")
        quantity_b7 = request.POST.get("quantity_b7")
        date_b7 = request.POST.get("date_b7")

        agencia_b8 = request.POST.get("agencia_b8")
        federal_program_b8 = request.POST.get("federal_program_b8")
        quantity_b8 = request.POST.get("quantity_b8")
        date_b8 = request.POST.get("date_b8")

        # section2
        # tabla 1
        instuition1 = request.POST.get("instuition1")
        money1 = request.POST.get("money1")
        date1 = request.POST.get("date1")

        # tabla 2
        instuition2 = request.POST.get("instuition2")
        money2 = request.POST.get("money2")
        date2 = request.POST.get("date2")

        # tabla 3
        instuition3 = request.POST.get("instuition3")
        money3 = request.POST.get("money3")
        date3 = request.POST.get("date3")

        # tabla 4
        instuition4 = request.POST.get("instuition4")
        money4 = request.POST.get("money4")
        date4 = request.POST.get("date4")

        # tabla 5
        instuition5 = request.POST.get("instuition5")
        money5 = request.POST.get("money5")
        date5 = request.POST.get("date5")

        # tabla 6
        instuition6 = request.POST.get("instuition6")
        money6 = request.POST.get("money6")
        date6 = request.POST.get("date6")

        # tabla 7
        instuition7 = request.POST.get("instuition7")
        money7 = request.POST.get("money7")
        date7 = request.POST.get("date7")

        # tabla 8
        instuition8 = request.POST.get("instuition8")
        money8 = request.POST.get("money8")
        date8 = request.POST.get("date8")

        # tabla 9
        instuition9 = request.POST.get("instuition9")
        money9 = request.POST.get("money9")
        date9 = request.POST.get("date9")

        # tabla 10
        instuition10 = request.POST.get("instuition10")
        money10 = request.POST.get("money10")
        date10 = request.POST.get("date10")

        # footer
        name = request.POST.get("name")
        puesto = request.POST.get("puesto")
        date = request.POST.get("date")

        csv_file_path = "data/cuestionarios/balanza_de_pagos/JP-529.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "year1",
                        "year2",
                        "company",
                        "address",
                        "email",
                        "liaison_officer",
                        "tel",
                        "choice",
                        "agencia_a1",
                        "federal_program_a1",
                        "quantity_a1",
                        "date_a1",
                        "agencia_a2",
                        "federal_program_a2",
                        "quantity_a2",
                        "date_a2",
                        "agencia_a3",
                        "federal_program_a3",
                        "quantity_a3",
                        "date_a3",
                        "agencia_a4",
                        "federal_program_a4",
                        "quantity_a4",
                        "date_a4",
                        "agencia_a5",
                        "federal_program_a5",
                        "quantity_a5",
                        "date_a5",
                        "agencia_a6",
                        "federal_program_a6",
                        "quantity_a6",
                        "date_a6",
                        "agencia_a7",
                        "federal_program_a7",
                        "quantity_a7",
                        "date_a7",
                        "agencia_a8",
                        "federal_program_a8",
                        "quantity_a8",
                        "date_a8",
                        "agencia_b1",
                        "federal_program_b1",
                        "quantity_b1",
                        "date_b1",
                        "agencia_b2",
                        "federal_program_b2",
                        "quantity_b2",
                        "date_b2",
                        "agencia_b3",
                        "federal_program_b3",
                        "quantity_b3",
                        "date_b3",
                        "agencia_b4",
                        "federal_program_b4",
                        "quantity_b4",
                        "date_b4",
                        "agencia_b5",
                        "federal_program_b5",
                        "quantity_b5",
                        "date_b5",
                        "agencia_b6",
                        "federal_program_b6",
                        "quantity_b6",
                        "date_b6",
                        "agencia_b7",
                        "federal_program_b7",
                        "quantity_b7",
                        "date_b7",
                        "agencia_b8",
                        "federal_program_b8",
                        "quantity_b8",
                        "date_b8",
                        "instuition1",
                        "money1",
                        "date1",
                        "instuition2",
                        "money2",
                        "date2",
                        "instuition3",
                        "money3",
                        "date3",
                        "instuition4",
                        "money4",
                        "date4",
                        "instuition5",
                        "money5",
                        "date5",
                        "instuition6",
                        "money6",
                        "date6",
                        "instuition7",
                        "money7",
                        "date7",
                        "instuition8",
                        "money8",
                        "date8",
                        "instuition9",
                        "money9",
                        "date9",
                        "instuition10",
                        "money10",
                        "date10",
                        "name",
                        "puesto",
                        "date",
                    ]
                )

            writer.writerow(
                [
                    year1,
                    year2,
                    company,
                    address,
                    email,
                    liaison_officer,
                    tel,
                    choice,
                    agencia_a1,
                    federal_program_a1,
                    quantity_a1,
                    date_a1,
                    agencia_a2,
                    federal_program_a2,
                    quantity_a2,
                    date_a2,
                    agencia_a3,
                    federal_program_a3,
                    quantity_a3,
                    date_a3,
                    agencia_a4,
                    federal_program_a4,
                    quantity_a4,
                    date_a4,
                    agencia_a5,
                    federal_program_a5,
                    quantity_a5,
                    date_a5,
                    agencia_a6,
                    federal_program_a6,
                    quantity_a6,
                    date_a6,
                    agencia_a7,
                    federal_program_a7,
                    quantity_a7,
                    date_a7,
                    agencia_a8,
                    federal_program_a8,
                    quantity_a8,
                    date_a8,
                    agencia_b1,
                    federal_program_b1,
                    quantity_b1,
                    date_b1,
                    agencia_b2,
                    federal_program_b2,
                    quantity_b2,
                    date_b2,
                    agencia_b3,
                    federal_program_b3,
                    quantity_b3,
                    date_b3,
                    agencia_b4,
                    federal_program_b4,
                    quantity_b4,
                    date_b4,
                    agencia_b5,
                    federal_program_b5,
                    quantity_b5,
                    date_b5,
                    agencia_b6,
                    federal_program_b6,
                    quantity_b6,
                    date_b6,
                    agencia_b7,
                    federal_program_b7,
                    quantity_b7,
                    date_b7,
                    agencia_b8,
                    federal_program_b8,
                    quantity_b8,
                    date_b8,
                    instuition1,
                    money1,
                    date1,
                    instuition2,
                    money2,
                    date2,
                    instuition3,
                    money3,
                    date3,
                    instuition4,
                    money4,
                    date4,
                    instuition5,
                    money5,
                    date5,
                    instuition6,
                    money6,
                    date6,
                    instuition7,
                    money7,
                    date7,
                    instuition8,
                    money8,
                    date8,
                    instuition9,
                    money9,
                    date9,
                    instuition10,
                    money10,
                    date10,
                    name,
                    puesto,
                    date,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/balanza_de_pagos/JP-529.csv",
            dtypes={
                "year1": int,
                "year2": int,
                "company": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "tel": str,
                "choice": str,
                "agencia_a1": str,
                "federal_program_a1": str,
                "quantity_a1": float,
                "date_a1": str,
                "agencia_a2": str,
                "federal_program_a2": str,
                "quantity_a2": float,
                "date_a2": str,
                "agencia_a3": str,
                "federal_program_a3": str,
                "quantity_a3": float,
                "date_a3": str,
                "agencia_a4": str,
                "federal_program_a4": str,
                "quantity_a4": float,
                "date_a4": str,
                "agencia_a5": str,
                "federal_program_a5": str,
                "quantity_a5": float,
                "date_a5": str,
                "agencia_a6": str,
                "federal_program_a6": str,
                "quantity_a6": float,
                "date_a6": str,
                "agencia_a7": str,
                "federal_program_a7": str,
                "quantity_a7": float,
                "date_a7": str,
                "agencia_a8": str,
                "federal_program_a8": str,
                "quantity_a8": float,
                "date_a8": str,
                "agencia_b1": str,
                "federal_program_b1": str,
                "quantity_b1": float,
                "date_b1": str,
                "agencia_b2": str,
                "federal_program_b2": str,
                "quantity_b2": float,
                "date_b2": str,
                "agencia_b3": str,
                "federal_program_b3": str,
                "quantity_b3": float,
                "date_b3": str,
                "agencia_b4": str,
                "federal_program_b4": str,
                "quantity_b4": float,
                "date_b4": str,
                "agencia_b5": str,
                "federal_program_b5": str,
                "quantity_b5": float,
                "date_b5": str,
                "agencia_b6": str,
                "federal_program_b6": str,
                "quantity_b6": float,
                "date_b6": str,
                "agencia_b7": str,
                "federal_program_b7": str,
                "quantity_b7": float,
                "date_b7": str,
                "agencia_b8": str,
                "federal_program_b8": str,
                "quantity_b8": float,
                "date_b8": str,
                "instuition1": str,
                "money1": float,
                "date1": str,
                "instuition2": str,
                "money2": float,
                "date2": str,
                "instuition3": str,
                "money3": float,
                "date3": str,
                "instuition4": str,
                "money4": float,
                "date4": str,
                "instuition5": str,
                "money5": float,
                "date5": str,
                "instuition6": str,
                "money6": float,
                "date6": str,
                "instuition7": str,
                "money7": float,
                "date7": str,
                "instuition8": str,
                "money8": float,
                "date8": str,
                "instuition9": str,
                "money9": float,
                "date9": str,
                "instuition10": str,
                "money10": float,
                "date10": str,
                "name": str,
                "puesto": str,
                "date": str,
            },
            table_name="JP_529",
            table_id="5",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/balanza_de_pagos/JP-529.html")


def IP_110(request):
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
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        incomes_services_revenues_1 = request.POST.get("incomes_services_revenues_1")
        incomes_services_revenues_2 = request.POST.get("incomes_services_revenues_2")
        incomes_industries_1 = request.POST.get("incomes_industries_1")
        incomes_industries_2 = request.POST.get("incomes_industries_2")
        incomes_persons_1 = request.POST.get("incomes_persons_1")
        incomes_persons_2 = request.POST.get("incomes_persons_2")
        incomes_sale_merchandise_1 = request.POST.get("incomes_sale_merchandise_1")
        incomes_sale_merchandise_2 = request.POST.get("incomes_sale_merchandise_2")
        incomes_rents_1 = request.POST.get("incomes_rents_1")
        incomes_rents_2 = request.POST.get("incomes_rents_2")
        incomes_interests_1 = request.POST.get("incomes_interests_1")
        incomes_interests_2 = request.POST.get("incomes_interests_2")
        incomes_capital_gain_loss_1 = request.POST.get("incomes_capital_gain_loss_1")
        incomes_capital_gain_loss_2 = request.POST.get("incomes_capital_gain_loss_2")
        others_incomes_1 = request.POST.get("others_incomes_1")
        others_incomes_2 = request.POST.get("others_incomes_2")
        total_income_1 = request.POST.get("total_income_1")
        total_income_2 = request.POST.get("total_income_2")
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
        expenses_rents_1 = request.POST.get("expenses_rents_1")
        expenses_rents_2 = request.POST.get("expenses_rents_2")
        expenses_depreciation_1 = request.POST.get("expenses_depreciation_1")
        expenses_depreciation_2 = request.POST.get("expenses_depreciation_2")
        expenses_bad_debts_1 = request.POST.get("expenses_bad_debts_1")
        expenses_bad_debts_2 = request.POST.get("expenses_bad_debts_2")
        expenses_donation_1 = request.POST.get("expenses_donation_1")
        expenses_donation_2 = request.POST.get("expenses_donation_2")
        expenses_sales_tax_1 = request.POST.get("expenses_sales_tax_1")
        expenses_sales_tax_2 = request.POST.get("expenses_sales_tax_2")
        expenses_machinery_1 = request.POST.get("expenses_machinery_1")
        expenses_machinery_2 = request.POST.get("expenses_machinery_2")
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
        net_profit_income_tax_1 = request.POST.get("net_profit_income_tax_1")
        net_profit_income_tax_2 = request.POST.get("net_profit_income_tax_2")
        profit_after_tax_1 = request.POST.get("profit_after_tax_1")
        profit_after_tax_2 = request.POST.get("profit_after_tax_2")
        withheld_tax_1 = request.POST.get("withheld_tax_1")
        withheld_tax_2 = request.POST.get("withheld_tax_2")
        signature = request.POST.get("signature")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-110.csv"
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
                        "closing_date",
                        "start_year",
                        "end_year",
                        "incomes_services_revenues_1",
                        "incomes_services_revenues_2",
                        "incomes_industries_1",
                        "incomes_industries_2",
                        "incomes_persons_1",
                        "incomes_persons_2",
                        "incomes_sale_merchandise_1",
                        "incomes_sale_merchandise_2",
                        "incomes_rents_1",
                        "incomes_rents_2",
                        "incomes_interests_1",
                        "incomes_interests_2",
                        "incomes_capital_gain_loss_1",
                        "incomes_capital_gain_loss_2",
                        "others_incomes_1",
                        "others_incomes_2",
                        "total_income_1",
                        "total_income_2",
                        "expenses_1",
                        "expenses_2",
                        "expenses_salaries_wages_bonus_1",
                        "expenses_salaries_wages_bonus_2",
                        "expenses_interests_1",
                        "expenses_interests_2",
                        "expenses_rents_1",
                        "expenses_rents_2",
                        "expenses_depreciation_1",
                        "expenses_depreciation_2",
                        "expenses_bad_debts_1",
                        "expenses_bad_debts_2",
                        "expenses_donation_1",
                        "expenses_donation_2",
                        "expenses_sales_tax_1",
                        "expenses_sales_tax_2",
                        "expenses_machinery_1",
                        "expenses_machinery_2",
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
                        "net_profit_income_tax_1",
                        "net_profit_income_tax_2",
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
                    closing_date,
                    start_year,
                    end_year,
                    incomes_services_revenues_1,
                    incomes_services_revenues_2,
                    incomes_industries_1,
                    incomes_industries_2,
                    incomes_persons_1,
                    incomes_persons_2,
                    incomes_sale_merchandise_1,
                    incomes_sale_merchandise_2,
                    incomes_rents_1,
                    incomes_rents_2,
                    incomes_interests_1,
                    incomes_interests_2,
                    incomes_capital_gain_loss_1,
                    incomes_capital_gain_loss_2,
                    others_incomes_1,
                    others_incomes_2,
                    total_income_1,
                    total_income_2,
                    expenses_1,
                    expenses_2,
                    expenses_salaries_wages_bonus_1,
                    expenses_salaries_wages_bonus_2,
                    expenses_interests_1,
                    expenses_interests_2,
                    expenses_rents_1,
                    expenses_rents_2,
                    expenses_depreciation_1,
                    expenses_depreciation_2,
                    expenses_bad_debts_1,
                    expenses_bad_debts_2,
                    expenses_donation_1,
                    expenses_donation_2,
                    expenses_sales_tax_1,
                    expenses_sales_tax_2,
                    expenses_machinery_1,
                    expenses_machinery_2,
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
                    net_profit_income_tax_1,
                    net_profit_income_tax_2,
                    profit_after_tax_1,
                    profit_after_tax_2,
                    withheld_tax_1,
                    withheld_tax_2,
                    signature,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-110.csv",
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
                "closing_date": str,
                "start_year": str,
                "end_year": str,
                "incomes_services_revenues_1": float,
                "incomes_services_revenues_2": float,
                "incomes_industries_1": float,
                "incomes_industries_2": float,
                "incomes_persons_1": float,
                "incomes_persons_2": float,
                "incomes_sale_merchandise_1": float,
                "incomes_sale_merchandise_2": float,
                "incomes_rents_1": float,
                "incomes_rents_2": float,
                "incomes_interests_1": float,
                "incomes_interests_2": float,
                "incomes_capital_gain_loss_1": float,
                "incomes_capital_gain_loss_2": float,
                "others_incomes_1": float,
                "others_incomes_2": float,
                "total_income_1": float,
                "total_income_2": float,
                "expenses_1": float,
                "expenses_2": float,
                "expenses_salaries_wages_bonus_1": float,
                "expenses_salaries_wages_bonus_2": float,
                "expenses_interests_1": float,
                "expenses_interests_2": float,
                "expenses_rents_1": float,
                "expenses_rents_2": float,
                "expenses_depreciation_1": float,
                "expenses_depreciation_2": float,
                "expenses_bad_debts_1": float,
                "expenses_bad_debts_2": float,
                "expenses_donation_1": float,
                "expenses_donation_2": float,
                "expenses_sales_tax_1": float,
                "expenses_sales_tax_2": float,
                "expenses_machinery_1": float,
                "expenses_machinery_2": float,
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
                "net_profit_income_tax_1": float,
                "net_profit_income_tax_2": float,
                "profit_after_tax_1": float,
                "profit_after_tax_2": float,
                "withheld_tax_1": float,
                "withheld_tax_2": float,
                "signature": str,
                "rank": str,
            },
            table_name="IP_110",
            table_id="15",
            debug=False,
        )

        return render(request, "forms/succesfull.html")

    return render(request, "forms/yearly/ingreso_neto/IP-110.html")


def JP_541(request):
    if request.method == "POST":
        # Retrieve form data

        # TABLE 1
        encuesta_1 = request.POST.get("encuesta_1")
        fiscal_year_1 = request.POST.get("fiscal_year_1")
        company_name_1 = request.POST.get("company_name_1")
        liaison_officer_1 = request.POST.get("liaison_officer_1")
        tel_1 = request.POST.get("tel_1")
        project_1 = request.POST.get("project_1")
        branches_1 = request.POST.get("branches_1")

        project_name_1_1 = request.POST.get("project_name_1_1")
        city_1_1 = request.POST.get("city_1_1")
        total_number_project_1_1 = request.POST.get("total_number_project_1_1")
        total_cost_1_1 = request.POST.get("total_cost_1_1")
        start_date_1_1 = request.POST.get("start_date_1_1")
        end_date_1_1 = request.POST.get("end_date_1_1")
        value_first_trimester_1_1 = request.POST.get("value_first_trimester_1_1")
        value_second_trimester_1_1 = request.POST.get("value_second_trimester_1_1")
        value_third_trimester_1_1 = request.POST.get("value_third_trimester_1_1")
        value_fourth_trimester_1_1 = request.POST.get("value_fourth_trimester_1_1")

        project_name_1_2 = request.POST.get("project_name_1_2")
        city_1_2 = request.POST.get("city_1_2")
        total_number_project_1_2 = request.POST.get("total_number_project_1_2")
        total_cost_1_2 = request.POST.get("total_cost_1_2")
        start_date_1_2 = request.POST.get("start_date_1_2")
        end_date_1_2 = request.POST.get("end_date_1_2")
        value_first_trimester_1_2 = request.POST.get("value_first_trimester_1_2")
        value_second_trimester_1_2 = request.POST.get("value_second_trimester_1_2")
        value_third_trimester_1_2 = request.POST.get("value_third_trimester_1_2")
        value_fourth_trimester_1_2 = request.POST.get("value_fourth_trimester_1_2")

        project_name_1_3 = request.POST.get("project_name_1_3")
        city_1_3 = request.POST.get("city_1_3")
        total_number_project_1_3 = request.POST.get("total_number_project_1_3")
        total_cost_1_3 = request.POST.get("total_cost_1_3")
        start_date_1_3 = request.POST.get("start_date_1_3")
        end_date_1_3 = request.POST.get("end_date_1_3")
        value_first_trimester_1_3 = request.POST.get("value_first_trimester_1_3")
        value_second_trimester_1_3 = request.POST.get("value_second_trimester_1_3")
        value_third_trimester_1_3 = request.POST.get("value_third_trimester_1_3")
        value_fourth_trimester_1_3 = request.POST.get("value_fourth_trimester_1_3")

        project_name_1_4 = request.POST.get("project_name_1_4")
        city_1_4 = request.POST.get("city_1_4")
        total_number_project_1_4 = request.POST.get("total_number_project_1_4")
        total_cost_1_4 = request.POST.get("total_cost_1_4")
        start_date_1_4 = request.POST.get("start_date_1_4")
        end_date_1_4 = request.POST.get("end_date_1_4")
        value_first_trimester_1_4 = request.POST.get("value_first_trimester_1_4")
        value_second_trimester_1_4 = request.POST.get("value_second_trimester_1_4")
        value_third_trimester_1_4 = request.POST.get("value_third_trimester_1_4")
        value_fourth_trimester_1_4 = request.POST.get("value_fourth_trimester_1_4")

        project_name_1_5 = request.POST.get("project_name_1_5")
        city_1_5 = request.POST.get("city_1_5")
        total_number_project_1_5 = request.POST.get("total_number_project_1_5")
        total_cost_1_5 = request.POST.get("total_cost_1_5")
        start_date_1_5 = request.POST.get("start_date_1_5")
        end_date_1_5 = request.POST.get("end_date_1_5")
        value_first_trimester_1_5 = request.POST.get("value_first_trimester_1_5")
        value_second_trimester_1_5 = request.POST.get("value_second_trimester_1_5")
        value_third_trimester_1_5 = request.POST.get("value_third_trimester_1_5")
        value_fourth_trimester_1_5 = request.POST.get("value_fourth_trimester_1_5")

        project_name_1_6 = request.POST.get("project_name_1_6")
        city_1_6 = request.POST.get("city_1_6")
        total_number_project_1_6 = request.POST.get("total_number_project_1_6")
        total_cost_1_6 = request.POST.get("total_cost_1_6")
        start_date_1_6 = request.POST.get("start_date_1_6")
        end_date_1_6 = request.POST.get("end_date_1_6")
        value_first_trimester_1_6 = request.POST.get("value_first_trimester_1_6")
        value_second_trimester_1_6 = request.POST.get("value_second_trimester_1_6")
        value_third_trimester_1_6 = request.POST.get("value_third_trimester_1_6")
        value_fourth_trimester_1_6 = request.POST.get("value_fourth_trimester_1_6")

        project_name_1_7 = request.POST.get("project_name_1_7")
        city_1_7 = request.POST.get("city_1_7")
        total_number_project_1_7 = request.POST.get("total_number_project_1_7")
        total_cost_1_7 = request.POST.get("total_cost_1_7")
        start_date_1_7 = request.POST.get("start_date_1_7")
        end_date_1_7 = request.POST.get("end_date_1_7")
        value_first_trimester_1_7 = request.POST.get("value_first_trimester_1_7")
        value_second_trimester_1_7 = request.POST.get("value_second_trimester_1_7")
        value_third_trimester_1_7 = request.POST.get("value_third_trimester_1_7")
        value_fourth_trimester_1_7 = request.POST.get("value_fourth_trimester_1_7")

        project_name_1_8 = request.POST.get("project_name_1_8")
        city_1_8 = request.POST.get("city_1_8")
        total_number_project_1_8 = request.POST.get("total_number_project_1_8")
        total_cost_1_8 = request.POST.get("total_cost_1_8")
        start_date_1_8 = request.POST.get("start_date_1_8")
        end_date_1_8 = request.POST.get("end_date_1_8")
        value_first_trimester_1_8 = request.POST.get("value_first_trimester_1_8")
        value_second_trimester_1_8 = request.POST.get("value_second_trimester_1_8")
        value_third_trimester_1_8 = request.POST.get("value_third_trimester_1_8")
        value_fourth_trimester_1_8 = request.POST.get("value_fourth_trimester_1_8")

        project_name_1_9 = request.POST.get("project_name_1_9")
        city_1_9 = request.POST.get("city_1_9")
        total_number_project_1_9 = request.POST.get("total_number_project_1_9")
        total_cost_1_9 = request.POST.get("total_cost_1_9")
        start_date_1_9 = request.POST.get("start_date_1_9")
        end_date_1_9 = request.POST.get("end_date_1_9")
        value_first_trimester_1_9 = request.POST.get("value_first_trimester_1_9")
        value_second_trimester_1_9 = request.POST.get("value_second_trimester_1_9")
        value_third_trimester_1_9 = request.POST.get("value_third_trimester_1_9")
        value_fourth_trimester_1_9 = request.POST.get("value_fourth_trimester_1_9")

        project_name_1_10 = request.POST.get("project_name_1_10")
        city_1_10 = request.POST.get("city_1_10")
        total_number_project_1_10 = request.POST.get("total_number_project_1_10")
        total_cost_1_10 = request.POST.get("total_cost_1_10")
        start_date_1_10 = request.POST.get("start_date_1_10")
        end_date_1_10 = request.POST.get("end_date_1_10")
        value_first_trimester_1_10 = request.POST.get("value_first_trimester_1_10")
        value_second_trimester_1_10 = request.POST.get("value_second_trimester_1_10")
        value_third_trimester_1_10 = request.POST.get("value_third_trimester_1_10")
        value_fourth_trimester_1_10 = request.POST.get("value_fourth_trimester_1_10")

        # TABLE 2
        encuesta_2 = request.POST.get("encuesta_2")
        fiscal_year_2 = request.POST.get("fiscal_year_2")
        company_name_2 = request.POST.get("company_name_2")
        liaison_officer_2 = request.POST.get("liaison_officer_2")
        tel_2 = request.POST.get("tel_2")
        project_2 = request.POST.get("project_2")
        branches_2 = request.POST.get("branches_2")

        project_name_2_1 = request.POST.get("project_name_2_1")
        city_2_1 = request.POST.get("city_2_1")
        total_number_project_2_1 = request.POST.get("total_number_project_2_1")
        total_cost_2_1 = request.POST.get("total_cost_2_1")
        start_date_2_1 = request.POST.get("start_date_2_1")
        end_date_2_1 = request.POST.get("end_date_2_1")
        value_first_trimester_2_1 = request.POST.get("value_first_trimester_2_1")
        value_second_trimester_2_1 = request.POST.get("value_second_trimester_2_1")
        value_third_trimester_2_1 = request.POST.get("value_third_trimester_2_1")
        value_fourth_trimester_2_1 = request.POST.get("value_fourth_trimester_2_1")

        project_name_2_2 = request.POST.get("project_name_2_2")
        city_2_2 = request.POST.get("city_2_2")
        total_number_project_2_2 = request.POST.get("total_number_project_2_2")
        total_cost_2_2 = request.POST.get("total_cost_2_2")
        start_date_2_2 = request.POST.get("start_date_2_2")
        end_date_2_2 = request.POST.get("end_date_2_2")
        value_first_trimester_2_2 = request.POST.get("value_first_trimester_2_2")
        value_second_trimester_2_2 = request.POST.get("value_second_trimester_2_2")
        value_third_trimester_2_2 = request.POST.get("value_third_trimester_2_2")
        value_fourth_trimester_2_2 = request.POST.get("value_fourth_trimester_2_2")

        project_name_2_3 = request.POST.get("project_name_2_3")
        city_2_3 = request.POST.get("city_2_3")
        total_number_project_2_3 = request.POST.get("total_number_project_2_3")
        total_cost_2_3 = request.POST.get("total_cost_2_3")
        start_date_2_3 = request.POST.get("start_date_2_3")
        end_date_2_3 = request.POST.get("end_date_2_3")
        value_first_trimester_2_3 = request.POST.get("value_first_trimester_2_3")
        value_second_trimester_2_3 = request.POST.get("value_second_trimester_2_3")
        value_third_trimester_2_3 = request.POST.get("value_third_trimester_2_3")
        value_fourth_trimester_2_3 = request.POST.get("value_fourth_trimester_2_3")

        project_name_2_4 = request.POST.get("project_name_2_4")
        city_2_4 = request.POST.get("city_2_4")
        total_number_project_2_4 = request.POST.get("total_number_project_2_4")
        total_cost_2_4 = request.POST.get("total_cost_2_4")
        start_date_2_4 = request.POST.get("start_date_2_4")
        end_date_2_4 = request.POST.get("end_date_2_4")
        value_first_trimester_2_4 = request.POST.get("value_first_trimester_2_4")
        value_second_trimester_2_4 = request.POST.get("value_second_trimester_2_4")
        value_third_trimester_2_4 = request.POST.get("value_third_trimester_2_4")
        value_fourth_trimester_2_4 = request.POST.get("value_fourth_trimester_2_4")

        project_name_2_5 = request.POST.get("project_name_2_5")
        city_2_5 = request.POST.get("city_2_5")
        total_number_project_2_5 = request.POST.get("total_number_project_2_5")
        total_cost_2_5 = request.POST.get("total_cost_2_5")
        start_date_2_5 = request.POST.get("start_date_2_5")
        end_date_2_5 = request.POST.get("end_date_2_5")
        value_first_trimester_2_5 = request.POST.get("value_first_trimester_2_5")
        value_second_trimester_2_5 = request.POST.get("value_second_trimester_2_5")
        value_third_trimester_2_5 = request.POST.get("value_third_trimester_2_5")
        value_fourth_trimester_2_5 = request.POST.get("value_fourth_trimester_2_5")

        project_name_2_6 = request.POST.get("project_name_2_6")
        city_2_6 = request.POST.get("city_2_6")
        total_number_project_2_6 = request.POST.get("total_number_project_2_6")
        total_cost_2_6 = request.POST.get("total_cost_2_6")
        start_date_2_6 = request.POST.get("start_date_2_6")
        end_date_2_6 = request.POST.get("end_date_2_6")
        value_first_trimester_2_6 = request.POST.get("value_first_trimester_2_6")
        value_second_trimester_2_6 = request.POST.get("value_second_trimester_2_6")
        value_third_trimester_2_6 = request.POST.get("value_third_trimester_2_6")
        value_fourth_trimester_2_6 = request.POST.get("value_fourth_trimester_2_6")

        project_name_2_7 = request.POST.get("project_name_2_7")
        city_2_7 = request.POST.get("city_2_7")
        total_number_project_2_7 = request.POST.get("total_number_project_2_7")
        total_cost_2_7 = request.POST.get("total_cost_2_7")
        start_date_2_7 = request.POST.get("start_date_2_7")
        end_date_2_7 = request.POST.get("end_date_2_7")
        value_first_trimester_2_7 = request.POST.get("value_first_trimester_2_7")
        value_second_trimester_2_7 = request.POST.get("value_second_trimester_2_7")
        value_third_trimester_2_7 = request.POST.get("value_third_trimester_2_7")
        value_fourth_trimester_2_7 = request.POST.get("value_fourth_trimester_2_7")

        project_name_2_8 = request.POST.get("project_name_2_8")
        city_2_8 = request.POST.get("city_2_8")
        total_number_project_2_8 = request.POST.get("total_number_project_2_8")
        total_cost_2_8 = request.POST.get("total_cost_2_8")
        start_date_2_8 = request.POST.get("start_date_2_8")
        end_date_2_8 = request.POST.get("end_date_2_8")
        value_first_trimester_2_8 = request.POST.get("value_first_trimester_2_8")
        value_second_trimester_2_8 = request.POST.get("value_second_trimester_2_8")
        value_third_trimester_2_8 = request.POST.get("value_third_trimester_2_8")
        value_fourth_trimester_2_8 = request.POST.get("value_fourth_trimester_2_8")

        project_name_2_9 = request.POST.get("project_name_2_9")
        city_2_9 = request.POST.get("city_2_9")
        total_number_project_2_9 = request.POST.get("total_number_project_2_9")
        total_cost_2_9 = request.POST.get("total_cost_2_9")
        start_date_2_9 = request.POST.get("start_date_2_9")
        end_date_2_9 = request.POST.get("end_date_2_9")
        value_first_trimester_2_9 = request.POST.get("value_first_trimester_2_9")
        value_second_trimester_2_9 = request.POST.get("value_second_trimester_2_9")
        value_third_trimester_2_9 = request.POST.get("value_third_trimester_2_9")
        value_fourth_trimester_2_9 = request.POST.get("value_fourth_trimester_2_9")

        project_name_2_10 = request.POST.get("project_name_2_10")
        city_2_10 = request.POST.get("city_2_10")
        total_number_project_2_10 = request.POST.get("total_number_project_2_10")
        total_cost_2_10 = request.POST.get("total_cost_2_10")
        start_date_2_10 = request.POST.get("start_date_2_10")
        end_date_2_10 = request.POST.get("end_date_2_10")
        value_first_trimester_2_10 = request.POST.get("value_first_trimester_2_10")
        value_second_trimester_2_10 = request.POST.get("value_second_trimester_2_10")
        value_third_trimester_2_10 = request.POST.get("value_third_trimester_2_10")
        value_fourth_trimester_2_10 = request.POST.get("value_fourth_trimester_2_10")

        # TABLE 3
        encuesta_3 = request.POST.get("encuesta_3")
        fiscal_year_3 = request.POST.get("fiscal_year_3")
        company_name_3 = request.POST.get("company_name_3")
        liaison_officer_3 = request.POST.get("liaison_officer_3")
        tel_3 = request.POST.get("tel_3")
        project_3 = request.POST.get("project_3")
        branches_3 = request.POST.get("branches_3")

        project_name_3_1 = request.POST.get("project_name_3_1")
        city_3_1 = request.POST.get("city_3_1")
        total_number_project_3_1 = request.POST.get("total_number_project_3_1")
        total_cost_3_1 = request.POST.get("total_cost_3_1")
        start_date_3_1 = request.POST.get("start_date_3_1")
        end_date_3_1 = request.POST.get("end_date_3_1")
        value_first_trimester_3_1 = request.POST.get("value_first_trimester_3_1")
        value_second_trimester_3_1 = request.POST.get("value_second_trimester_3_1")
        value_third_trimester_3_1 = request.POST.get("value_third_trimester_3_1")
        value_fourth_trimester_3_1 = request.POST.get("value_fourth_trimester_3_1")

        project_name_3_2 = request.POST.get("project_name_3_2")
        city_3_2 = request.POST.get("city_3_2")
        total_number_project_3_2 = request.POST.get("total_number_project_3_2")
        total_cost_3_2 = request.POST.get("total_cost_3_2")
        start_date_3_2 = request.POST.get("start_date_3_2")
        end_date_3_2 = request.POST.get("end_date_3_2")
        value_first_trimester_3_2 = request.POST.get("value_first_trimester_3_2")
        value_second_trimester_3_2 = request.POST.get("value_second_trimester_3_2")
        value_third_trimester_3_2 = request.POST.get("value_third_trimester_3_2")
        value_fourth_trimester_3_2 = request.POST.get("value_fourth_trimester_3_2")

        project_name_3_3 = request.POST.get("project_name_3_3")
        city_3_3 = request.POST.get("city_3_3")
        total_number_project_3_3 = request.POST.get("total_number_project_3_3")
        total_cost_3_3 = request.POST.get("total_cost_3_3")
        start_date_3_3 = request.POST.get("start_date_3_3")
        end_date_3_3 = request.POST.get("end_date_3_3")
        value_first_trimester_3_3 = request.POST.get("value_first_trimester_3_3")
        value_second_trimester_3_3 = request.POST.get("value_second_trimester_3_3")
        value_third_trimester_3_3 = request.POST.get("value_third_trimester_3_3")
        value_fourth_trimester_3_3 = request.POST.get("value_fourth_trimester_3_3")

        project_name_3_4 = request.POST.get("project_name_3_4")
        city_3_4 = request.POST.get("city_3_4")
        total_number_project_3_4 = request.POST.get("total_number_project_3_4")
        total_cost_3_4 = request.POST.get("total_cost_3_4")
        start_date_3_4 = request.POST.get("start_date_3_4")
        end_date_3_4 = request.POST.get("end_date_3_4")
        value_first_trimester_3_4 = request.POST.get("value_first_trimester_3_4")
        value_second_trimester_3_4 = request.POST.get("value_second_trimester_3_4")
        value_third_trimester_3_4 = request.POST.get("value_third_trimester_3_4")
        value_fourth_trimester_3_4 = request.POST.get("value_fourth_trimester_3_4")

        project_name_3_5 = request.POST.get("project_name_3_5")
        city_3_5 = request.POST.get("city_3_5")
        total_number_project_3_5 = request.POST.get("total_number_project_3_5")
        total_cost_3_5 = request.POST.get("total_cost_3_5")
        start_date_3_5 = request.POST.get("start_date_3_5")
        end_date_3_5 = request.POST.get("end_date_3_5")
        value_first_trimester_3_5 = request.POST.get("value_first_trimester_3_5")
        value_second_trimester_3_5 = request.POST.get("value_second_trimester_3_5")
        value_third_trimester_3_5 = request.POST.get("value_third_trimester_3_5")
        value_fourth_trimester_3_5 = request.POST.get("value_fourth_trimester_3_5")

        project_name_3_6 = request.POST.get("project_name_3_6")
        city_3_6 = request.POST.get("city_3_6")
        total_number_project_3_6 = request.POST.get("total_number_project_3_6")
        total_cost_3_6 = request.POST.get("total_cost_3_6")
        start_date_3_6 = request.POST.get("start_date_3_6")
        end_date_3_6 = request.POST.get("end_date_3_6")
        value_first_trimester_3_6 = request.POST.get("value_first_trimester_3_6")
        value_second_trimester_3_6 = request.POST.get("value_second_trimester_3_6")
        value_third_trimester_3_6 = request.POST.get("value_third_trimester_3_6")
        value_fourth_trimester_3_6 = request.POST.get("value_fourth_trimester_3_6")

        project_name_3_7 = request.POST.get("project_name_3_7")
        city_3_7 = request.POST.get("city_3_7")
        total_number_project_3_7 = request.POST.get("total_number_project_3_7")
        total_cost_3_7 = request.POST.get("total_cost_3_7")
        start_date_3_7 = request.POST.get("start_date_3_7")
        end_date_3_7 = request.POST.get("end_date_3_7")
        value_first_trimester_3_7 = request.POST.get("value_first_trimester_3_7")
        value_second_trimester_3_7 = request.POST.get("value_second_trimester_3_7")
        value_third_trimester_3_7 = request.POST.get("value_third_trimester_3_7")
        value_fourth_trimester_3_7 = request.POST.get("value_fourth_trimester_3_7")

        project_name_3_8 = request.POST.get("project_name_3_8")
        city_3_8 = request.POST.get("city_3_8")
        total_number_project_3_8 = request.POST.get("total_number_project_3_8")
        total_cost_3_8 = request.POST.get("total_cost_3_8")
        start_date_3_8 = request.POST.get("start_date_3_8")
        end_date_3_8 = request.POST.get("end_date_3_8")
        value_first_trimester_3_8 = request.POST.get("value_first_trimester_3_8")
        value_second_trimester_3_8 = request.POST.get("value_second_trimester_3_8")
        value_third_trimester_3_8 = request.POST.get("value_third_trimester_3_8")
        value_fourth_trimester_3_8 = request.POST.get("value_fourth_trimester_3_8")

        project_name_3_9 = request.POST.get("project_name_3_9")
        city_3_9 = request.POST.get("city_3_9")
        total_number_project_3_9 = request.POST.get("total_number_project_3_9")
        total_cost_3_9 = request.POST.get("total_cost_3_9")
        start_date_3_9 = request.POST.get("start_date_3_9")
        end_date_3_9 = request.POST.get("end_date_3_9")
        value_first_trimester_3_9 = request.POST.get("value_first_trimester_3_9")
        value_second_trimester_3_9 = request.POST.get("value_second_trimester_3_9")
        value_third_trimester_3_9 = request.POST.get("value_third_trimester_3_9")
        value_fourth_trimester_3_9 = request.POST.get("value_fourth_trimester_3_9")

        project_name_3_10 = request.POST.get("project_name_3_10")
        city_3_10 = request.POST.get("city_3_10")
        total_number_project_3_10 = request.POST.get("total_number_project_3_10")
        total_cost_3_10 = request.POST.get("total_cost_3_10")
        start_date_3_10 = request.POST.get("start_date_3_10")
        end_date_3_10 = request.POST.get("end_date_3_10")
        value_first_trimester_3_10 = request.POST.get("value_first_trimester_3_10")
        value_second_trimester_3_10 = request.POST.get("value_second_trimester_3_10")
        value_third_trimester_3_10 = request.POST.get("value_third_trimester_3_10")
        value_fourth_trimester_3_10 = request.POST.get("value_fourth_trimester_3_10")

        # TABLE 4
        encuesta_4 = request.POST.get("encuesta_4")
        fiscal_year_4 = request.POST.get("fiscal_year_4")
        company_name_4 = request.POST.get("company_name_4")
        liaison_officer_4 = request.POST.get("liaison_officer_4")
        tel_4 = request.POST.get("tel_4")
        project_4 = request.POST.get("project_4")
        branches_4 = request.POST.get("branches_4")

        project_name_4_1 = request.POST.get("project_name_4_1")
        city_4_1 = request.POST.get("city_4_1")
        total_number_project_4_1 = request.POST.get("total_number_project_4_1")
        total_cost_4_1 = request.POST.get("total_cost_4_1")
        start_date_4_1 = request.POST.get("start_date_4_1")
        end_date_4_1 = request.POST.get("end_date_4_1")
        value_first_trimester_4_1 = request.POST.get("value_first_trimester_4_1")
        value_second_trimester_4_1 = request.POST.get("value_second_trimester_4_1")
        value_third_trimester_4_1 = request.POST.get("value_third_trimester_4_1")
        value_fourth_trimester_4_1 = request.POST.get("value_fourth_trimester_4_1")

        project_name_4_2 = request.POST.get("project_name_4_2")
        city_4_2 = request.POST.get("city_4_2")
        total_number_project_4_2 = request.POST.get("total_number_project_4_2")
        total_cost_4_2 = request.POST.get("total_cost_4_2")
        start_date_4_2 = request.POST.get("start_date_4_2")
        end_date_4_2 = request.POST.get("end_date_4_2")
        value_first_trimester_4_2 = request.POST.get("value_first_trimester_4_2")
        value_second_trimester_4_2 = request.POST.get("value_second_trimester_4_2")
        value_third_trimester_4_2 = request.POST.get("value_third_trimester_4_2")
        value_fourth_trimester_4_2 = request.POST.get("value_fourth_trimester_4_2")

        project_name_4_3 = request.POST.get("project_name_4_3")
        city_4_3 = request.POST.get("city_4_3")
        total_number_project_4_3 = request.POST.get("total_number_project_4_3")
        total_cost_4_3 = request.POST.get("total_cost_4_3")
        start_date_4_3 = request.POST.get("start_date_4_3")
        end_date_4_3 = request.POST.get("end_date_4_3")
        value_first_trimester_4_3 = request.POST.get("value_first_trimester_4_3")
        value_second_trimester_4_3 = request.POST.get("value_second_trimester_4_3")
        value_third_trimester_4_3 = request.POST.get("value_third_trimester_4_3")
        value_fourth_trimester_4_3 = request.POST.get("value_fourth_trimester_4_3")

        project_name_4_4 = request.POST.get("project_name_4_4")
        city_4_4 = request.POST.get("city_4_4")
        total_number_project_4_4 = request.POST.get("total_number_project_4_4")
        total_cost_4_4 = request.POST.get("total_cost_4_4")
        start_date_4_4 = request.POST.get("start_date_4_4")
        end_date_4_4 = request.POST.get("end_date_4_4")
        value_first_trimester_4_4 = request.POST.get("value_first_trimester_4_4")
        value_second_trimester_4_4 = request.POST.get("value_second_trimester_4_4")
        value_third_trimester_4_4 = request.POST.get("value_third_trimester_4_4")
        value_fourth_trimester_4_4 = request.POST.get("value_fourth_trimester_4_4")

        project_name_4_5 = request.POST.get("project_name_4_5")
        city_4_5 = request.POST.get("city_4_5")
        total_number_project_4_5 = request.POST.get("total_number_project_4_5")
        total_cost_4_5 = request.POST.get("total_cost_4_5")
        start_date_4_5 = request.POST.get("start_date_4_5")
        end_date_4_5 = request.POST.get("end_date_4_5")
        value_first_trimester_4_5 = request.POST.get("value_first_trimester_4_5")
        value_second_trimester_4_5 = request.POST.get("value_second_trimester_4_5")
        value_third_trimester_4_5 = request.POST.get("value_third_trimester_4_5")
        value_fourth_trimester_4_5 = request.POST.get("value_fourth_trimester_4_5")

        project_name_4_6 = request.POST.get("project_name_4_6")
        city_4_6 = request.POST.get("city_4_6")
        total_number_project_4_6 = request.POST.get("total_number_project_4_6")
        total_cost_4_6 = request.POST.get("total_cost_4_6")
        start_date_4_6 = request.POST.get("start_date_4_6")
        end_date_4_6 = request.POST.get("end_date_4_6")
        value_first_trimester_4_6 = request.POST.get("value_first_trimester_4_6")
        value_second_trimester_4_6 = request.POST.get("value_second_trimester_4_6")
        value_third_trimester_4_6 = request.POST.get("value_third_trimester_4_6")
        value_fourth_trimester_4_6 = request.POST.get("value_fourth_trimester_4_6")

        project_name_4_7 = request.POST.get("project_name_4_7")
        city_4_7 = request.POST.get("city_4_7")
        total_number_project_4_7 = request.POST.get("total_number_project_4_7")
        total_cost_4_7 = request.POST.get("total_cost_4_7")
        start_date_4_7 = request.POST.get("start_date_4_7")
        end_date_4_7 = request.POST.get("end_date_4_7")
        value_first_trimester_4_7 = request.POST.get("value_first_trimester_4_7")
        value_second_trimester_4_7 = request.POST.get("value_second_trimester_4_7")
        value_third_trimester_4_7 = request.POST.get("value_third_trimester_4_7")
        value_fourth_trimester_4_7 = request.POST.get("value_fourth_trimester_4_7")

        project_name_4_8 = request.POST.get("project_name_4_8")
        city_4_8 = request.POST.get("city_4_8")
        total_number_project_4_8 = request.POST.get("total_number_project_4_8")
        total_cost_4_8 = request.POST.get("total_cost_4_8")
        start_date_4_8 = request.POST.get("start_date_4_8")
        end_date_4_8 = request.POST.get("end_date_4_8")
        value_first_trimester_4_8 = request.POST.get("value_first_trimester_4_8")
        value_second_trimester_4_8 = request.POST.get("value_second_trimester_4_8")
        value_third_trimester_4_8 = request.POST.get("value_third_trimester_4_8")
        value_fourth_trimester_4_8 = request.POST.get("value_fourth_trimester_4_8")

        project_name_4_9 = request.POST.get("project_name_4_9")
        city_4_9 = request.POST.get("city_4_9")
        total_number_project_4_9 = request.POST.get("total_number_project_4_9")
        total_cost_4_9 = request.POST.get("total_cost_4_9")
        start_date_4_9 = request.POST.get("start_date_4_9")
        end_date_4_9 = request.POST.get("end_date_4_9")
        value_first_trimester_4_9 = request.POST.get("value_first_trimester_4_9")
        value_second_trimester_4_9 = request.POST.get("value_second_trimester_4_9")
        value_third_trimester_4_9 = request.POST.get("value_third_trimester_4_9")
        value_fourth_trimester_4_9 = request.POST.get("value_fourth_trimester_4_9")

        project_name_4_10 = request.POST.get("project_name_4_10")
        city_4_10 = request.POST.get("city_4_10")
        total_number_project_4_10 = request.POST.get("total_number_project_4_10")
        total_cost_4_10 = request.POST.get("total_cost_4_10")
        start_date_4_10 = request.POST.get("start_date_4_10")
        end_date_4_10 = request.POST.get("end_date_4_10")
        value_first_trimester_4_10 = request.POST.get("value_first_trimester_4_10")
        value_second_trimester_4_10 = request.POST.get("value_second_trimester_4_10")
        value_third_trimester_4_10 = request.POST.get("value_third_trimester_4_10")
        value_fourth_trimester_4_10 = request.POST.get("value_fourth_trimester_4_10")

        csv_file_path = "data/cuestionarios/construcción/JP-541.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, "a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "encuesta_1",
                        "fiscal_year_1",
                        "company_name_1",
                        "liaison_officer_1",
                        "tel_1",
                        "project_1",
                        "branches_1",
                        "project_name_1_1",
                        "city_1_1",
                        "total_number_project_1_1",
                        "total_cost_1_1",
                        "start_date_1_1",
                        "end_date_1_1",
                        "value_first_trimester_1_1",
                        "value_second_trimester_1_1",
                        "value_third_trimester_1_1",
                        "value_fourth_trimester_1_1",
                        "project_name_1_2",
                        "city_1_2",
                        "total_number_project_1_2",
                        "total_cost_1_2",
                        "start_date_1_2",
                        "end_date_1_2",
                        "value_first_trimester_1_2",
                        "value_second_trimester_1_2",
                        "value_third_trimester_1_2",
                        "value_fourth_trimester_1_2",
                        "project_name_1_3",
                        "city_1_3",
                        "total_number_project_1_3",
                        "total_cost_1_3",
                        "start_date_1_3",
                        "end_date_1_3",
                        "value_first_trimester_1_3",
                        "value_second_trimester_1_3",
                        "value_third_trimester_1_3",
                        "value_fourth_trimester_1_3",
                        "project_name_1_4",
                        "city_1_4",
                        "total_number_project_1_4",
                        "total_cost_1_4",
                        "start_date_1_4",
                        "end_date_1_4",
                        "value_first_trimester_1_4",
                        "value_second_trimester_1_4",
                        "value_third_trimester_1_4",
                        "value_fourth_trimester_1_4",
                        "project_name_1_5",
                        "city_1_5",
                        "total_number_project_1_5",
                        "total_cost_1_5",
                        "start_date_1_5",
                        "end_date_1_5",
                        "value_first_trimester_1_5",
                        "value_second_trimester_1_5",
                        "value_third_trimester_1_5",
                        "value_fourth_trimester_1_5",
                        "project_name_1_6",
                        "city_1_6",
                        "total_number_project_1_6",
                        "total_cost_1_6",
                        "start_date_1_6",
                        "end_date_1_6",
                        "value_first_trimester_1_6",
                        "value_second_trimester_1_6",
                        "value_third_trimester_1_6",
                        "value_fourth_trimester_1_6",
                        "project_name_1_7",
                        "city_1_7",
                        "total_number_project_1_7",
                        "total_cost_1_7",
                        "start_date_1_7",
                        "end_date_1_7",
                        "value_first_trimester_1_7",
                        "value_second_trimester_1_7",
                        "value_third_trimester_1_7",
                        "value_fourth_trimester_1_7",
                        "project_name_1_8",
                        "city_1_8",
                        "total_number_project_1_8",
                        "total_cost_1_8",
                        "start_date_1_8",
                        "end_date_1_8",
                        "value_first_trimester_1_8",
                        "value_second_trimester_1_8",
                        "value_third_trimester_1_8",
                        "value_fourth_trimester_1_8",
                        "project_name_1_9",
                        "city_1_9",
                        "total_number_project_1_9",
                        "total_cost_1_9",
                        "start_date_1_9",
                        "end_date_1_9",
                        "value_first_trimester_1_9",
                        "value_second_trimester_1_9",
                        "value_third_trimester_1_9",
                        "value_fourth_trimester_1_9",
                        "project_name_1_10",
                        "city_1_10",
                        "total_number_project_1_10",
                        "total_cost_1_10",
                        "start_date_1_10",
                        "end_date_1_10",
                        "value_first_trimester_1_10",
                        "value_second_trimester_1_10",
                        "value_third_trimester_1_10",
                        "value_fourth_trimester_1_10",
                        "encuesta_2",
                        "fiscal_year_2",
                        "company_name_2",
                        "liaison_officer_2",
                        "tel_2",
                        "project_2",
                        "branches_2",
                        "project_name_2_1",
                        "city_2_1",
                        "total_number_project_2_1",
                        "total_cost_2_1",
                        "start_date_2_1",
                        "end_date_2_1",
                        "value_first_trimester_2_1",
                        "value_second_trimester_2_1",
                        "value_third_trimester_2_1",
                        "value_fourth_trimester_2_1",
                        "project_name_2_2",
                        "city_2_2",
                        "total_number_project_2_2",
                        "total_cost_2_2",
                        "start_date_2_2",
                        "end_date_2_2",
                        "value_first_trimester_2_2",
                        "value_second_trimester_2_2",
                        "value_third_trimester_2_2",
                        "value_fourth_trimester_2_2",
                        "project_name_2_3",
                        "city_2_3",
                        "total_number_project_2_3",
                        "total_cost_2_3",
                        "start_date_2_3",
                        "end_date_2_3",
                        "value_first_trimester_2_3",
                        "value_second_trimester_2_3",
                        "value_third_trimester_2_3",
                        "value_fourth_trimester_2_3",
                        "project_name_2_4",
                        "city_2_4",
                        "total_number_project_2_4",
                        "total_cost_2_4",
                        "start_date_2_4",
                        "end_date_2_4",
                        "value_first_trimester_2_4",
                        "value_second_trimester_2_4",
                        "value_third_trimester_2_4",
                        "value_fourth_trimester_2_4",
                        "project_name_2_5",
                        "city_2_5",
                        "total_number_project_2_5",
                        "total_cost_2_5",
                        "start_date_2_5",
                        "end_date_2_5",
                        "value_first_trimester_2_5",
                        "value_second_trimester_2_5",
                        "value_third_trimester_2_5",
                        "value_fourth_trimester_2_5",
                        "project_name_2_6",
                        "city_2_6",
                        "total_number_project_2_6",
                        "total_cost_2_6",
                        "start_date_2_6",
                        "end_date_2_6",
                        "value_first_trimester_2_6",
                        "value_second_trimester_2_6",
                        "value_third_trimester_2_6",
                        "value_fourth_trimester_2_6",
                        "project_name_2_7",
                        "city_2_7",
                        "total_number_project_2_7",
                        "total_cost_2_7",
                        "start_date_2_7",
                        "end_date_2_7",
                        "value_first_trimester_2_7",
                        "value_second_trimester_2_7",
                        "value_third_trimester_2_7",
                        "value_fourth_trimester_2_7",
                        "project_name_2_8",
                        "city_2_8",
                        "total_number_project_2_8",
                        "total_cost_2_8",
                        "start_date_2_8",
                        "end_date_2_8",
                        "value_first_trimester_2_8",
                        "value_second_trimester_2_8",
                        "value_third_trimester_2_8",
                        "value_fourth_trimester_2_8",
                        "project_name_2_9",
                        "city_2_9",
                        "total_number_project_2_9",
                        "total_cost_2_9",
                        "start_date_2_9",
                        "end_date_2_9",
                        "value_first_trimester_2_9",
                        "value_second_trimester_2_9",
                        "value_third_trimester_2_9",
                        "value_fourth_trimester_2_9",
                        "project_name_2_10",
                        "city_2_10",
                        "total_number_project_2_10",
                        "total_cost_2_10",
                        "start_date_2_10",
                        "end_date_2_10",
                        "value_first_trimester_2_10",
                        "value_second_trimester_2_10",
                        "value_third_trimester_2_10",
                        "value_fourth_trimester_2_10",
                        "encuesta_3",
                        "fiscal_year_3",
                        "company_name_3",
                        "liaison_officer_3",
                        "tel_3",
                        "project_3",
                        "branches_3",
                        "project_name_3_1",
                        "city_3_1",
                        "total_number_project_3_1",
                        "total_cost_3_1",
                        "start_date_3_1",
                        "end_date_3_1",
                        "value_first_trimester_3_1",
                        "value_second_trimester_3_1",
                        "value_third_trimester_3_1",
                        "value_fourth_trimester_3_1",
                        "project_name_3_2",
                        "city_3_2",
                        "total_number_project_3_2",
                        "total_cost_3_2",
                        "start_date_3_2",
                        "end_date_3_2",
                        "value_first_trimester_3_2",
                        "value_second_trimester_3_2",
                        "value_third_trimester_3_2",
                        "value_fourth_trimester_3_2",
                        "project_name_3_3",
                        "city_3_3",
                        "total_number_project_3_3",
                        "total_cost_3_3",
                        "start_date_3_3",
                        "end_date_3_3",
                        "value_first_trimester_3_3",
                        "value_second_trimester_3_3",
                        "value_third_trimester_3_3",
                        "value_fourth_trimester_3_3",
                        "project_name_3_4",
                        "city_3_4",
                        "total_number_project_3_4",
                        "total_cost_3_4",
                        "start_date_3_4",
                        "end_date_3_4",
                        "value_first_trimester_3_4",
                        "value_second_trimester_3_4",
                        "value_third_trimester_3_4",
                        "value_fourth_trimester_3_4",
                        "project_name_3_5",
                        "city_3_5",
                        "total_number_project_3_5",
                        "total_cost_3_5",
                        "start_date_3_5",
                        "end_date_3_5",
                        "value_first_trimester_3_5",
                        "value_second_trimester_3_5",
                        "value_third_trimester_3_5",
                        "value_fourth_trimester_3_5",
                        "project_name_3_6",
                        "city_3_6",
                        "total_number_project_3_6",
                        "total_cost_3_6",
                        "start_date_3_6",
                        "end_date_3_6",
                        "value_first_trimester_3_6",
                        "value_second_trimester_3_6",
                        "value_third_trimester_3_6",
                        "value_fourth_trimester_3_6",
                        "project_name_3_7",
                        "city_3_7",
                        "total_number_project_3_7",
                        "total_cost_3_7",
                        "start_date_3_7",
                        "end_date_3_7",
                        "value_first_trimester_3_7",
                        "value_second_trimester_3_7",
                        "value_third_trimester_3_7",
                        "value_fourth_trimester_3_7",
                        "project_name_3_8",
                        "city_3_8",
                        "total_number_project_3_8",
                        "total_cost_3_8",
                        "start_date_3_8",
                        "end_date_3_8",
                        "value_first_trimester_3_8",
                        "value_second_trimester_3_8",
                        "value_third_trimester_3_8",
                        "value_fourth_trimester_3_8",
                        "project_name_3_9",
                        "city_3_9",
                        "total_number_project_3_9",
                        "total_cost_3_9",
                        "start_date_3_9",
                        "end_date_3_9",
                        "value_first_trimester_3_9",
                        "value_second_trimester_3_9",
                        "value_third_trimester_3_9",
                        "value_fourth_trimester_3_9",
                        "project_name_3_10",
                        "city_3_10",
                        "total_number_project_3_10",
                        "total_cost_3_10",
                        "start_date_3_10",
                        "end_date_3_10",
                        "value_first_trimester_3_10",
                        "value_second_trimester_3_10",
                        "value_third_trimester_3_10",
                        "value_fourth_trimester_3_10",
                        "encuesta_4",
                        "trimestre_4",
                        "company_name_4",
                        "liaison_officer_4",
                        "tel_4",
                        "project_4",
                        "branches_4",
                        "project_name_4_1",
                        "city_4_1",
                        "total_number_project_4_1",
                        "total_cost_4_1",
                        "start_date_4_1",
                        "end_date_4_1",
                        "value_first_trimester_4_1",
                        "value_second_trimester_4_1",
                        "value_third_trimester_4_1",
                        "value_fourth_trimester_4_1",
                        "project_name_4_2",
                        "city_4_2",
                        "total_number_project_4_2",
                        "total_cost_4_2",
                        "start_date_4_2",
                        "end_date_4_2",
                        "value_first_trimester_4_2",
                        "value_second_trimester_4_2",
                        "value_third_trimester_4_2",
                        "value_fourth_trimester_4_2",
                        "project_name_4_3",
                        "city_4_3",
                        "total_number_project_4_3",
                        "total_cost_4_3",
                        "start_date_4_3",
                        "end_date_4_3",
                        "value_first_trimester_4_3",
                        "value_second_trimester_4_3",
                        "value_third_trimester_4_3",
                        "value_fourth_trimester_4_3",
                        "project_name_4_4",
                        "city_4_4",
                        "total_number_project_4_4",
                        "total_cost_4_4",
                        "start_date_4_4",
                        "end_date_4_4",
                        "value_first_trimester_4_4",
                        "value_second_trimester_4_4",
                        "value_third_trimester_4_4",
                        "value_fourth_trimester_4_4",
                        "project_name_4_5",
                        "city_4_5",
                        "total_number_project_4_5",
                        "total_cost_4_5",
                        "start_date_4_5",
                        "end_date_4_5",
                        "value_first_trimester_4_5",
                        "value_second_trimester_4_5",
                        "value_third_trimester_4_5",
                        "value_fourth_trimester_4_5",
                        "project_name_4_6",
                        "city_4_6",
                        "total_number_project_4_6",
                        "total_cost_4_6",
                        "start_date_4_6",
                        "end_date_4_6",
                        "value_first_trimester_4_6",
                        "value_second_trimester_4_6",
                        "value_third_trimester_4_6",
                        "value_fourth_trimester_4_6",
                        "project_name_4_7",
                        "city_4_7",
                        "total_number_project_4_7",
                        "total_cost_4_7",
                        "start_date_4_7",
                        "end_date_4_7",
                        "value_first_trimester_4_7",
                        "value_second_trimester_4_7",
                        "value_third_trimester_4_7",
                        "value_fourth_trimester_4_7",
                        "project_name_4_8",
                        "city_4_8",
                        "total_number_project_4_8",
                        "total_cost_4_8",
                        "start_date_4_8",
                        "end_date_4_8",
                        "value_first_trimester_4_8",
                        "value_second_trimester_4_8",
                        "value_third_trimester_4_8",
                        "value_fourth_trimester_4_8",
                        "project_name_4_9",
                        "city_4_9",
                        "total_number_project_4_9",
                        "total_cost_4_9",
                        "start_date_4_9",
                        "end_date_4_9",
                        "value_first_trimester_4_9",
                        "value_second_trimester_4_9",
                        "value_third_trimester_4_9",
                        "value_fourth_trimester_4_9",
                        "project_name_4_10",
                        "city_4_10",
                        "total_number_project_4_10",
                        "total_cost_4_10",
                        "start_date_4_10",
                        "end_date_4_10",
                        "value_first_trimester_4_10",
                        "value_second_trimester_4_10",
                        "value_third_trimester_4_10",
                        "value_fourth_trimester_4_10",
                    ]
                )

            writer.writerow(
                [
                    encuesta_1,
                    fiscal_year_1,
                    company_name_1,
                    liaison_officer_1,
                    tel_1,
                    project_1,
                    branches_1,
                    project_name_1_1,
                    city_1_1,
                    total_number_project_1_1,
                    total_cost_1_1,
                    start_date_1_1,
                    end_date_1_1,
                    value_first_trimester_1_1,
                    value_second_trimester_1_1,
                    value_third_trimester_1_1,
                    value_fourth_trimester_1_1,
                    project_name_1_2,
                    city_1_2,
                    total_number_project_1_2,
                    total_cost_1_2,
                    start_date_1_2,
                    end_date_1_2,
                    value_first_trimester_1_2,
                    value_second_trimester_1_2,
                    value_third_trimester_1_2,
                    value_fourth_trimester_1_2,
                    project_name_1_3,
                    city_1_3,
                    total_number_project_1_3,
                    total_cost_1_3,
                    start_date_1_3,
                    end_date_1_3,
                    value_first_trimester_1_3,
                    value_second_trimester_1_3,
                    value_third_trimester_1_3,
                    value_fourth_trimester_1_3,
                    project_name_1_4,
                    city_1_4,
                    total_number_project_1_4,
                    total_cost_1_4,
                    start_date_1_4,
                    end_date_1_4,
                    value_first_trimester_1_4,
                    value_second_trimester_1_4,
                    value_third_trimester_1_4,
                    value_fourth_trimester_1_4,
                    project_name_1_5,
                    city_1_5,
                    total_number_project_1_5,
                    total_cost_1_5,
                    start_date_1_5,
                    end_date_1_5,
                    value_first_trimester_1_5,
                    value_second_trimester_1_5,
                    value_third_trimester_1_5,
                    value_fourth_trimester_1_5,
                    project_name_1_6,
                    city_1_6,
                    total_number_project_1_6,
                    total_cost_1_6,
                    start_date_1_6,
                    end_date_1_6,
                    value_first_trimester_1_6,
                    value_second_trimester_1_6,
                    value_third_trimester_1_6,
                    value_fourth_trimester_1_6,
                    project_name_1_7,
                    city_1_7,
                    total_number_project_1_7,
                    total_cost_1_7,
                    start_date_1_7,
                    end_date_1_7,
                    value_first_trimester_1_7,
                    value_second_trimester_1_7,
                    value_third_trimester_1_7,
                    value_fourth_trimester_1_7,
                    project_name_1_8,
                    city_1_8,
                    total_number_project_1_8,
                    total_cost_1_8,
                    start_date_1_8,
                    end_date_1_8,
                    value_first_trimester_1_8,
                    value_second_trimester_1_8,
                    value_third_trimester_1_8,
                    value_fourth_trimester_1_8,
                    project_name_1_9,
                    city_1_9,
                    total_number_project_1_9,
                    total_cost_1_9,
                    start_date_1_9,
                    end_date_1_9,
                    value_first_trimester_1_9,
                    value_second_trimester_1_9,
                    value_third_trimester_1_9,
                    value_fourth_trimester_1_9,
                    project_name_1_10,
                    city_1_10,
                    total_number_project_1_10,
                    total_cost_1_10,
                    start_date_1_10,
                    end_date_1_10,
                    value_first_trimester_1_10,
                    value_second_trimester_1_10,
                    value_third_trimester_1_10,
                    value_fourth_trimester_1_10,
                    encuesta_2,
                    fiscal_year_2,
                    company_name_2,
                    liaison_officer_2,
                    tel_2,
                    project_2,
                    branches_2,
                    project_name_2_1,
                    city_2_1,
                    total_number_project_2_1,
                    total_cost_2_1,
                    start_date_2_1,
                    end_date_2_1,
                    value_first_trimester_2_1,
                    value_second_trimester_2_1,
                    value_third_trimester_2_1,
                    value_fourth_trimester_2_1,
                    project_name_2_2,
                    city_2_2,
                    total_number_project_2_2,
                    total_cost_2_2,
                    start_date_2_2,
                    end_date_2_2,
                    value_first_trimester_2_2,
                    value_second_trimester_2_2,
                    value_third_trimester_2_2,
                    value_fourth_trimester_2_2,
                    project_name_2_3,
                    city_2_3,
                    total_number_project_2_3,
                    total_cost_2_3,
                    start_date_2_3,
                    end_date_2_3,
                    value_first_trimester_2_3,
                    value_second_trimester_2_3,
                    value_third_trimester_2_3,
                    value_fourth_trimester_2_3,
                    project_name_2_4,
                    city_2_4,
                    total_number_project_2_4,
                    total_cost_2_4,
                    start_date_2_4,
                    end_date_2_4,
                    value_first_trimester_2_4,
                    value_second_trimester_2_4,
                    value_third_trimester_2_4,
                    value_fourth_trimester_2_4,
                    project_name_2_5,
                    city_2_5,
                    total_number_project_2_5,
                    total_cost_2_5,
                    start_date_2_5,
                    end_date_2_5,
                    value_first_trimester_2_5,
                    value_second_trimester_2_5,
                    value_third_trimester_2_5,
                    value_fourth_trimester_2_5,
                    project_name_2_6,
                    city_2_6,
                    total_number_project_2_6,
                    total_cost_2_6,
                    start_date_2_6,
                    end_date_2_6,
                    value_first_trimester_2_6,
                    value_second_trimester_2_6,
                    value_third_trimester_2_6,
                    value_fourth_trimester_2_6,
                    project_name_2_7,
                    city_2_7,
                    total_number_project_2_7,
                    total_cost_2_7,
                    start_date_2_7,
                    end_date_2_7,
                    value_first_trimester_2_7,
                    value_second_trimester_2_7,
                    value_third_trimester_2_7,
                    value_fourth_trimester_2_7,
                    project_name_2_8,
                    city_2_8,
                    total_number_project_2_8,
                    total_cost_2_8,
                    start_date_2_8,
                    end_date_2_8,
                    value_first_trimester_2_8,
                    value_second_trimester_2_8,
                    value_third_trimester_2_8,
                    value_fourth_trimester_2_8,
                    project_name_2_9,
                    city_2_9,
                    total_number_project_2_9,
                    total_cost_2_9,
                    start_date_2_9,
                    end_date_2_9,
                    value_first_trimester_2_9,
                    value_second_trimester_2_9,
                    value_third_trimester_2_9,
                    value_fourth_trimester_2_9,
                    project_name_2_10,
                    city_2_10,
                    total_number_project_2_10,
                    total_cost_2_10,
                    start_date_2_10,
                    end_date_2_10,
                    value_first_trimester_2_10,
                    value_second_trimester_2_10,
                    value_third_trimester_2_10,
                    value_fourth_trimester_2_10,
                    encuesta_3,
                    fiscal_year_3,
                    company_name_3,
                    liaison_officer_3,
                    tel_3,
                    project_3,
                    branches_3,
                    project_name_3_1,
                    city_3_1,
                    total_number_project_3_1,
                    total_cost_3_1,
                    start_date_3_1,
                    end_date_3_1,
                    value_first_trimester_3_1,
                    value_second_trimester_3_1,
                    value_third_trimester_3_1,
                    value_fourth_trimester_3_1,
                    project_name_3_2,
                    city_3_2,
                    total_number_project_3_2,
                    total_cost_3_2,
                    start_date_3_2,
                    end_date_3_2,
                    value_first_trimester_3_2,
                    value_second_trimester_3_2,
                    value_third_trimester_3_2,
                    value_fourth_trimester_3_2,
                    project_name_3_3,
                    city_3_3,
                    total_number_project_3_3,
                    total_cost_3_3,
                    start_date_3_3,
                    end_date_3_3,
                    value_first_trimester_3_3,
                    value_second_trimester_3_3,
                    value_third_trimester_3_3,
                    value_fourth_trimester_3_3,
                    project_name_3_4,
                    city_3_4,
                    total_number_project_3_4,
                    total_cost_3_4,
                    start_date_3_4,
                    end_date_3_4,
                    value_first_trimester_3_4,
                    value_second_trimester_3_4,
                    value_third_trimester_3_4,
                    value_fourth_trimester_3_4,
                    project_name_3_5,
                    city_3_5,
                    total_number_project_3_5,
                    total_cost_3_5,
                    start_date_3_5,
                    end_date_3_5,
                    value_first_trimester_3_5,
                    value_second_trimester_3_5,
                    value_third_trimester_3_5,
                    value_fourth_trimester_3_5,
                    project_name_3_6,
                    city_3_6,
                    total_number_project_3_6,
                    total_cost_3_6,
                    start_date_3_6,
                    end_date_3_6,
                    value_first_trimester_3_6,
                    value_second_trimester_3_6,
                    value_third_trimester_3_6,
                    value_fourth_trimester_3_6,
                    project_name_3_7,
                    city_3_7,
                    total_number_project_3_7,
                    total_cost_3_7,
                    start_date_3_7,
                    end_date_3_7,
                    value_first_trimester_3_7,
                    value_second_trimester_3_7,
                    value_third_trimester_3_7,
                    value_fourth_trimester_3_7,
                    project_name_3_8,
                    city_3_8,
                    total_number_project_3_8,
                    total_cost_3_8,
                    start_date_3_8,
                    end_date_3_8,
                    value_first_trimester_3_8,
                    value_second_trimester_3_8,
                    value_third_trimester_3_8,
                    value_fourth_trimester_3_8,
                    project_name_3_9,
                    city_3_9,
                    total_number_project_3_9,
                    total_cost_3_9,
                    start_date_3_9,
                    end_date_3_9,
                    value_first_trimester_3_9,
                    value_second_trimester_3_9,
                    value_third_trimester_3_9,
                    value_fourth_trimester_3_9,
                    project_name_3_10,
                    city_3_10,
                    total_number_project_3_10,
                    total_cost_3_10,
                    start_date_3_10,
                    end_date_3_10,
                    value_first_trimester_3_10,
                    value_second_trimester_3_10,
                    value_third_trimester_3_10,
                    value_fourth_trimester_3_10,
                    encuesta_4,
                    fiscal_year_4,
                    company_name_4,
                    liaison_officer_4,
                    tel_4,
                    project_4,
                    branches_4,
                    project_name_4_1,
                    city_4_1,
                    total_number_project_4_1,
                    total_cost_4_1,
                    start_date_4_1,
                    end_date_4_1,
                    value_first_trimester_4_1,
                    value_second_trimester_4_1,
                    value_third_trimester_4_1,
                    value_fourth_trimester_4_1,
                    project_name_4_2,
                    city_4_2,
                    total_number_project_4_2,
                    total_cost_4_2,
                    start_date_4_2,
                    end_date_4_2,
                    value_first_trimester_4_2,
                    value_second_trimester_4_2,
                    value_third_trimester_4_2,
                    value_fourth_trimester_4_2,
                    project_name_4_3,
                    city_4_3,
                    total_number_project_4_3,
                    total_cost_4_3,
                    start_date_4_3,
                    end_date_4_3,
                    value_first_trimester_4_3,
                    value_second_trimester_4_3,
                    value_third_trimester_4_3,
                    value_fourth_trimester_4_3,
                    project_name_4_4,
                    city_4_4,
                    total_number_project_4_4,
                    total_cost_4_4,
                    start_date_4_4,
                    end_date_4_4,
                    value_first_trimester_4_4,
                    value_second_trimester_4_4,
                    value_third_trimester_4_4,
                    value_fourth_trimester_4_4,
                    project_name_4_5,
                    city_4_5,
                    total_number_project_4_5,
                    total_cost_4_5,
                    start_date_4_5,
                    end_date_4_5,
                    value_first_trimester_4_5,
                    value_second_trimester_4_5,
                    value_third_trimester_4_5,
                    value_fourth_trimester_4_5,
                    project_name_4_6,
                    city_4_6,
                    total_number_project_4_6,
                    total_cost_4_6,
                    start_date_4_6,
                    end_date_4_6,
                    value_first_trimester_4_6,
                    value_second_trimester_4_6,
                    value_third_trimester_4_6,
                    value_fourth_trimester_4_6,
                    project_name_4_7,
                    city_4_7,
                    total_number_project_4_7,
                    total_cost_4_7,
                    start_date_4_7,
                    end_date_4_7,
                    value_first_trimester_4_7,
                    value_second_trimester_4_7,
                    value_third_trimester_4_7,
                    value_fourth_trimester_4_7,
                    project_name_4_8,
                    city_4_8,
                    total_number_project_4_8,
                    total_cost_4_8,
                    start_date_4_8,
                    end_date_4_8,
                    value_first_trimester_4_8,
                    value_second_trimester_4_8,
                    value_third_trimester_4_8,
                    value_fourth_trimester_4_8,
                    project_name_4_9,
                    city_4_9,
                    total_number_project_4_9,
                    total_cost_4_9,
                    start_date_4_9,
                    end_date_4_9,
                    value_first_trimester_4_9,
                    value_second_trimester_4_9,
                    value_third_trimester_4_9,
                    value_fourth_trimester_4_9,
                    project_name_4_10,
                    city_4_10,
                    total_number_project_4_10,
                    total_cost_4_10,
                    start_date_4_10,
                    end_date_4_10,
                    value_first_trimester_4_10,
                    value_second_trimester_4_10,
                    value_third_trimester_4_10,
                    value_fourth_trimester_4_10,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/construcción/JP-541.csv",
            dtypes={
                "encuesta_1": str,
                "fiscal_year_1": str,
                "company_name_1": str,
                "liaison_officer_1": str,
                "tel_1": str,
                "project_1": str,
                "branches_1": str,
                "project_name_1_1": str,
                "city_1_1": str,
                "total_number_project_1_1": str,
                "total_cost_1_1": str,
                "start_date_1_1": str,
                "end_date_1_1": str,
                "value_first_trimester_1_1": str,
                "value_second_trimester_1_1": str,
                "value_third_trimester_1_1": str,
                "value_fourth_trimester_1_1": str,
                "project_name_1_2": str,
                "city_1_2": str,
                "total_number_project_1_2": str,
                "total_cost_1_2": str,
                "start_date_1_2": str,
                "end_date_1_2": str,
                "value_first_trimester_1_2": str,
                "value_second_trimester_1_2": str,
                "value_third_trimester_1_2": str,
                "value_fourth_trimester_1_2": str,
                "project_name_1_3": str,
                "city_1_3": str,
                "total_number_project_1_3": str,
                "total_cost_1_3": str,
                "start_date_1_3": str,
                "end_date_1_3": str,
                "value_first_trimester_1_3": str,
                "value_second_trimester_1_3": str,
                "value_third_trimester_1_3": str,
                "value_fourth_trimester_1_3": str,
                "project_name_1_4": str,
                "city_1_4": str,
                "total_number_project_1_4": str,
                "total_cost_1_4": str,
                "start_date_1_4": str,
                "end_date_1_4": str,
                "value_first_trimester_1_4": str,
                "value_second_trimester_1_4": str,
                "value_third_trimester_1_4": str,
                "value_fourth_trimester_1_4": str,
                "project_name_1_5": str,
                "city_1_5": str,
                "total_number_project_1_5": str,
                "total_cost_1_5": str,
                "start_date_1_5": str,
                "end_date_1_5": str,
                "value_first_trimester_1_5": str,
                "value_second_trimester_1_5": str,
                "value_third_trimester_1_5": str,
                "value_fourth_trimester_1_5": str,
                "project_name_1_6": str,
                "city_1_6": str,
                "total_number_project_1_6": str,
                "total_cost_1_6": str,
                "start_date_1_6": str,
                "end_date_1_6": str,
                "value_first_trimester_1_6": str,
                "value_second_trimester_1_6": str,
                "value_third_trimester_1_6": str,
                "value_fourth_trimester_1_6": str,
                "project_name_1_7": str,
                "city_1_7": str,
                "total_number_project_1_7": str,
                "total_cost_1_7": str,
                "start_date_1_7": str,
                "end_date_1_7": str,
                "value_first_trimester_1_7": str,
                "value_second_trimester_1_7": str,
                "value_third_trimester_1_7": str,
                "value_fourth_trimester_1_7": str,
                "project_name_1_8": str,
                "city_1_8": str,
                "total_number_project_1_8": str,
                "total_cost_1_8": str,
                "start_date_1_8": str,
                "end_date_1_8": str,
                "value_first_trimester_1_8": str,
                "value_second_trimester_1_8": str,
                "value_third_trimester_1_8": str,
                "value_fourth_trimester_1_8": str,
                "project_name_1_9": str,
                "city_1_9": str,
                "total_number_project_1_9": str,
                "total_cost_1_9": str,
                "start_date_1_9": str,
                "end_date_1_9": str,
                "value_first_trimester_1_9": str,
                "value_second_trimester_1_9": str,
                "value_third_trimester_1_9": str,
                "value_fourth_trimester_1_9": str,
                "project_name_1_10": str,
                "city_1_10": str,
                "total_number_project_1_10": str,
                "total_cost_1_10": str,
                "start_date_1_10": str,
                "end_date_1_10": str,
                "value_first_trimester_1_10": str,
                "value_second_trimester_1_10": str,
                "value_third_trimester_1_10": str,
                "value_fourth_trimester_1_10": str,
                "encuesta_2": str,
                "fiscal_year_2": str,
                "company_name_2": str,
                "liaison_officer_2": str,
                "tel_2": str,
                "project_2": str,
                "branches_2": str,
                "project_name_2_1": str,
                "city_2_1": str,
                "total_number_project_2_1": str,
                "total_cost_2_1": str,
                "start_date_2_1": str,
                "end_date_2_1": str,
                "value_first_trimester_2_1": str,
                "value_second_trimester_2_1": str,
                "value_third_trimester_2_1": str,
                "value_fourth_trimester_2_1": str,
                "project_name_2_2": str,
                "city_2_2": str,
                "total_number_project_2_2": str,
                "total_cost_2_2": str,
                "start_date_2_2": str,
                "end_date_2_2": str,
                "value_first_trimester_2_2": str,
                "value_second_trimester_2_2": str,
                "value_third_trimester_2_2": str,
                "value_fourth_trimester_2_2": str,
                "project_name_2_3": str,
                "city_2_3": str,
                "total_number_project_2_3": str,
                "total_cost_2_3": str,
                "start_date_2_3": str,
                "end_date_2_3": str,
                "value_first_trimester_2_3": str,
                "value_second_trimester_2_3": str,
                "value_third_trimester_2_3": str,
                "value_fourth_trimester_2_3": str,
                "project_name_2_4": str,
                "city_2_4": str,
                "total_number_project_2_4": str,
                "total_cost_2_4": str,
                "start_date_2_4": str,
                "end_date_2_4": str,
                "value_first_trimester_2_4": str,
                "value_second_trimester_2_4": str,
                "value_third_trimester_2_4": str,
                "value_fourth_trimester_2_4": str,
                "project_name_2_5": str,
                "city_2_5": str,
                "total_number_project_2_5": str,
                "total_cost_2_5": str,
                "start_date_2_5": str,
                "end_date_2_5": str,
                "value_first_trimester_2_5": str,
                "value_second_trimester_2_5": str,
                "value_third_trimester_2_5": str,
                "value_fourth_trimester_2_5": str,
                "project_name_2_6": str,
                "city_2_6": str,
                "total_number_project_2_6": str,
                "total_cost_2_6": str,
                "start_date_2_6": str,
                "end_date_2_6": str,
                "value_first_trimester_2_6": str,
                "value_second_trimester_2_6": str,
                "value_third_trimester_2_6": str,
                "value_fourth_trimester_2_6": str,
                "project_name_2_7": str,
                "city_2_7": str,
                "total_number_project_2_7": str,
                "total_cost_2_7": str,
                "start_date_2_7": str,
                "end_date_2_7": str,
                "value_first_trimester_2_7": str,
                "value_second_trimester_2_7": str,
                "value_third_trimester_2_7": str,
                "value_fourth_trimester_2_7": str,
                "project_name_2_8": str,
                "city_2_8": str,
                "total_number_project_2_8": str,
                "total_cost_2_8": str,
                "start_date_2_8": str,
                "end_date_2_8": str,
                "value_first_trimester_2_8": str,
                "value_second_trimester_2_8": str,
                "value_third_trimester_2_8": str,
                "value_fourth_trimester_2_8": str,
                "project_name_2_9": str,
                "city_2_9": str,
                "total_number_project_2_9": str,
                "total_cost_2_9": str,
                "start_date_2_9": str,
                "end_date_2_9": str,
                "value_first_trimester_2_9": str,
                "value_second_trimester_2_9": str,
                "value_third_trimester_2_9": str,
                "value_fourth_trimester_2_9": str,
                "project_name_2_10": str,
                "city_2_10": str,
                "total_number_project_2_10": str,
                "total_cost_2_10": str,
                "start_date_2_10": str,
                "end_date_2_10": str,
                "value_first_trimester_2_10": str,
                "value_second_trimester_2_10": str,
                "value_third_trimester_2_10": str,
                "value_fourth_trimester_2_10": str,
                "encuesta_3": str,
                "fiscal_year_3": str,
                "company_name_3": str,
                "liaison_officer_3": str,
                "tel_3": str,
                "project_3": str,
                "branches_3": str,
                "project_name_3_1": str,
                "city_3_1": str,
                "total_number_project_3_1": str,
                "total_cost_3_1": str,
                "start_date_3_1": str,
                "end_date_3_1": str,
                "value_first_trimester_3_1": str,
                "value_second_trimester_3_1": str,
                "value_third_trimester_3_1": str,
                "value_fourth_trimester_3_1": str,
                "project_name_3_2": str,
                "city_3_2": str,
                "total_number_project_3_2": str,
                "total_cost_3_2": str,
                "start_date_3_2": str,
                "end_date_3_2": str,
                "value_first_trimester_3_2": str,
                "value_second_trimester_3_2": str,
                "value_third_trimester_3_2": str,
                "value_fourth_trimester_3_2": str,
                "project_name_3_3": str,
                "city_3_3": str,
                "total_number_project_3_3": str,
                "total_cost_3_3": str,
                "start_date_3_3": str,
                "end_date_3_3": str,
                "value_first_trimester_3_3": str,
                "value_second_trimester_3_3": str,
                "value_third_trimester_3_3": str,
                "value_fourth_trimester_3_3": str,
                "project_name_3_4": str,
                "city_3_4": str,
                "total_number_project_3_4": str,
                "total_cost_3_4": str,
                "start_date_3_4": str,
                "end_date_3_4": str,
                "value_first_trimester_3_4": str,
                "value_second_trimester_3_4": str,
                "value_third_trimester_3_4": str,
                "value_fourth_trimester_3_4": str,
                "project_name_3_5": str,
                "city_3_5": str,
                "total_number_project_3_5": str,
                "total_cost_3_5": str,
                "start_date_3_5": str,
                "end_date_3_5": str,
                "value_first_trimester_3_5": str,
                "value_second_trimester_3_5": str,
                "value_third_trimester_3_5": str,
                "value_fourth_trimester_3_5": str,
                "project_name_3_6": str,
                "city_3_6": str,
                "total_number_project_3_6": str,
                "total_cost_3_6": str,
                "start_date_3_6": str,
                "end_date_3_6": str,
                "value_first_trimester_3_6": str,
                "value_second_trimester_3_6": str,
                "value_third_trimester_3_6": str,
                "value_fourth_trimester_3_6": str,
                "project_name_3_7": str,
                "city_3_7": str,
                "total_number_project_3_7": str,
                "total_cost_3_7": str,
                "start_date_3_7": str,
                "end_date_3_7": str,
                "value_first_trimester_3_7": str,
                "value_second_trimester_3_7": str,
                "value_third_trimester_3_7": str,
                "value_fourth_trimester_3_7": str,
                "project_name_3_8": str,
                "city_3_8": str,
                "total_number_project_3_8": str,
                "total_cost_3_8": str,
                "start_date_3_8": str,
                "end_date_3_8": str,
                "value_first_trimester_3_8": str,
                "value_second_trimester_3_8": str,
                "value_third_trimester_3_8": str,
                "value_fourth_trimester_3_8": str,
                "project_name_3_9": str,
                "city_3_9": str,
                "total_number_project_3_9": str,
                "total_cost_3_9": str,
                "start_date_3_9": str,
                "end_date_3_9": str,
                "value_first_trimester_3_9": str,
                "value_second_trimester_3_9": str,
                "value_third_trimester_3_9": str,
                "value_fourth_trimester_3_9": str,
                "project_name_3_10": str,
                "city_3_10": str,
                "total_number_project_3_10": str,
                "total_cost_3_10": str,
                "start_date_3_10": str,
                "end_date_3_10": str,
                "value_first_trimester_3_10": str,
                "value_second_trimester_3_10": str,
                "value_third_trimester_3_10": str,
                "value_fourth_trimester_3_10": str,
                "encuesta_4": str,
                "trimestre_4": str,
                "company_name_4": str,
                "liaison_officer_4": str,
                "tel_4": str,
                "project_4": str,
                "branches_4": str,
                "project_name_4_1": str,
                "city_4_1": str,
                "total_number_project_4_1": str,
                "total_cost_4_1": str,
                "start_date_4_1": str,
                "end_date_4_1": str,
                "value_first_trimester_4_1": str,
                "value_second_trimester_4_1": str,
                "value_third_trimester_4_1": str,
                "value_fourth_trimester_4_1": str,
                "project_name_4_2": str,
                "city_4_2": str,
                "total_number_project_4_2": str,
                "total_cost_4_2": str,
                "start_date_4_2": str,
                "end_date_4_2": str,
                "value_first_trimester_4_2": str,
                "value_second_trimester_4_2": str,
                "value_third_trimester_4_2": str,
                "value_fourth_trimester_4_2": str,
                "project_name_4_3": str,
                "city_4_3": str,
                "total_number_project_4_3": str,
                "total_cost_4_3": str,
                "start_date_4_3": str,
                "end_date_4_3": str,
                "value_first_trimester_4_3": str,
                "value_second_trimester_4_3": str,
                "value_third_trimester_4_3": str,
                "value_fourth_trimester_4_3": str,
                "project_name_4_4": str,
                "city_4_4": str,
                "total_number_project_4_4": str,
                "total_cost_4_4": str,
                "start_date_4_4": str,
                "end_date_4_4": str,
                "value_first_trimester_4_4": str,
                "value_second_trimester_4_4": str,
                "value_third_trimester_4_4": str,
                "value_fourth_trimester_4_4": str,
                "project_name_4_5": str,
                "city_4_5": str,
                "total_number_project_4_5": str,
                "total_cost_4_5": str,
                "start_date_4_5": str,
                "end_date_4_5": str,
                "value_first_trimester_4_5": str,
                "value_second_trimester_4_5": str,
                "value_third_trimester_4_5": str,
                "value_fourth_trimester_4_5": str,
                "project_name_4_6": str,
                "city_4_6": str,
                "total_number_project_4_6": str,
                "total_cost_4_6": str,
                "start_date_4_6": str,
                "end_date_4_6": str,
                "value_first_trimester_4_6": str,
                "value_second_trimester_4_6": str,
                "value_third_trimester_4_6": str,
                "value_fourth_trimester_4_6": str,
                "project_name_4_7": str,
                "city_4_7": str,
                "total_number_project_4_7": str,
                "total_cost_4_7": str,
                "start_date_4_7": str,
                "end_date_4_7": str,
                "value_first_trimester_4_7": str,
                "value_second_trimester_4_7": str,
                "value_third_trimester_4_7": str,
                "value_fourth_trimester_4_7": str,
                "project_name_4_8": str,
                "city_4_8": str,
                "total_number_project_4_8": str,
                "total_cost_4_8": str,
                "start_date_4_8": str,
                "end_date_4_8": str,
                "value_first_trimester_4_8": str,
                "value_second_trimester_4_8": str,
                "value_third_trimester_4_8": str,
                "value_fourth_trimester_4_8": str,
                "project_name_4_9": str,
                "city_4_9": str,
                "total_number_project_4_9": str,
                "total_cost_4_9": str,
                "start_date_4_9": str,
                "end_date_4_9": str,
                "value_first_trimester_4_9": str,
                "value_second_trimester_4_9": str,
                "value_third_trimester_4_9": str,
                "value_fourth_trimester_4_9": str,
                "project_name_4_10": str,
                "city_4_10": str,
                "total_number_project_4_10": str,
                "total_cost_4_10": str,
                "start_date_4_10": str,
                "end_date_4_10": str,
                "value_first_trimester_4_10": str,
                "value_second_trimester_4_10": str,
                "value_third_trimester_4_10": str,
                "value_fourth_trimester_4_10": str,
            },
            table_name="JP_541",
            table_id="7",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/quaterly/construcción/JP-541.html")


def JP_363(request):
    if request.method == "POST":
        # Retrieve form data
        bonds_year_left = request.POST.get("bonds_year_left")
        bonds_year_right = request.POST.get("bonds_year_right")
        notes_year_left = request.POST.get("notes_year_left")
        notes_year_right = request.POST.get("notes_year_right")
        CG_bonds_left = request.POST.get("CG_bonds_left")
        CG_bonds_right = request.POST.get("CG_bonds_right")
        CG_notes_left = request.POST.get("CG_notes_left")
        CG_notes_right = request.POST.get("CG_notes_right")
        CG_name_service = request.POST.get("CG_name_service")
        town_bonds_left = request.POST.get("town_bonds_left")
        town_bonds_right = request.POST.get("town_bonds_right")
        town_notes_left = request.POST.get("town_notes_left")
        town_notes_right = request.POST.get("town_notes_right")
        town_name_service = request.POST.get("town_name_service")
        PC_bonds_left = request.POST.get("PC_bonds_left")
        PC_bonds_right = request.POST.get("PC_bonds_right")
        PC_notes_left = request.POST.get("PC_notes_left")
        PC_notes_right = request.POST.get("PC_notes_right")
        PC_name_service = request.POST.get("PC_name_service")
        EPA_bonds_left = request.POST.get("EPA_bonds_left")
        EPA_bonds_right = request.POST.get("EPA_bonds_right")
        EPA_notes_left = request.POST.get("EPA_notes_left")
        EPA_notes_right = request.POST.get("EPA_notes_right")
        EPA_name_service = request.POST.get("EPA_name_service")
        HA_bonds_left = request.POST.get("HA_bonds_left")
        HA_bonds_right = request.POST.get("HA_bonds_right")
        HA_notes_left = request.POST.get("HA_notes_left")
        HA_notes_right = request.POST.get("HA_notes_right")
        HA_name_service = request.POST.get("HA_name_service")
        ASA_bonds_left = request.POST.get("ASA_bonds_left")
        ASA_bonds_right = request.POST.get("ASA_bonds_right")
        ASA_notes_left = request.POST.get("ASA_notes_left")
        ASA_notes_right = request.POST.get("ASA_notes_right")
        ASA_name_service = request.POST.get("ASA_name_service")
        PBA_bonds_left = request.POST.get("PBA_bonds_left")
        PBA_bonds_right = request.POST.get("PBA_bonds_right")
        PBA_notes_left = request.POST.get("PBA_notes_left")
        PBA_notes_right = request.POST.get("PBA_notes_right")
        PBA_name_service = request.POST.get("PBA_name_service")
        PA_bonds_left = request.POST.get("PA_bonds_left")
        PA_bonds_right = request.POST.get("PA_bonds_right")
        PA_notes_left = request.POST.get("PA_notes_left")
        PA_notes_right = request.POST.get("PA_notes_right")
        PA_name_service = request.POST.get("PA_name_service")
        TA_bonds_left = request.POST.get("TA_bonds_left")
        TA_bonds_right = request.POST.get("TA_bonds_right")
        TA_notes_left = request.POST.get("TA_notes_left")
        TA_notes_right = request.POST.get("TA_notes_right")
        TA_name_service = request.POST.get("TA_name_service")
        IDC_bonds_left = request.POST.get("IDC_bonds_left")
        IDC_bonds_right = request.POST.get("IDC_bonds_right")
        IDC_notes_left = request.POST.get("IDC_notes_left")
        IDC_notes_right = request.POST.get("IDC_notes_right")
        IDC_name_service = request.POST.get("IDC_name_service")
        GDB_bonds_left = request.POST.get("GDB_bonds_left")
        GDB_bonds_right = request.POST.get("GDB_bonds_right")
        GDB_notes_left = request.POST.get("GDB_notes_left")
        GDB_notes_right = request.POST.get("GDB_notes_right")
        GDB_name_service = request.POST.get("GDB_name_service")
        HFC_bonds_left = request.POST.get("HFC_bonds_left")
        HFC_bonds_right = request.POST.get("HFC_bonds_right")
        HFC_notes_left = request.POST.get("HFC_notes_left")
        HFC_notes_right = request.POST.get("HFC_notes_right")
        HFC_name_service = request.POST.get("HFC_name_service")
        other = request.POST.get("other")
        other_bonds_left = request.POST.get("other_bonds_left")
        other_bonds_right = request.POST.get("other_bonds_right")
        other_notes_left = request.POST.get("other_notes_left")
        other_notes_right = request.POST.get("other_notes_right")
        other_name_service = request.POST.get("other_name_service")
        other_PC_1 = request.POST.get("other_PC_1")
        other_PC_1_bonds_left = request.POST.get("other_PC_1_bonds_left")
        other_PC_1_bonds_right = request.POST.get("other_PC_1_bonds_right")
        other_PC_1_notes_left = request.POST.get("other_PC_1_notes_left")
        other_PC_1_notes_right = request.POST.get("other_PC_1_notes_right")
        other_PC_1_name_service = request.POST.get("other_PC_1_name_service")
        other_PC_2 = request.POST.get("other_PC_2")
        other_PC_2_bonds_left = request.POST.get("other_PC_2_bonds_left")
        other_PC_2_bonds_right = request.POST.get("other_PC_2_bonds_right")
        other_PC_2_notes_left = request.POST.get("other_PC_2_notes_left")
        other_PC_2_notes_right = request.POST.get("other_PC_2_notes_right")
        other_PC_2_name_service = request.POST.get("other_PC_2_name_service")
        GNMA_bonds_left = request.POST.get("GNMA_bonds_left")
        GNMA_bonds_right = request.POST.get("GNMA_bonds_right")
        GNMA_notes_left = request.POST.get("GNMA_notes_left")
        GNMA_notes_right = request.POST.get("GNMA_notes_right")
        GNMA_name_service = request.POST.get("GNMA_name_service")
        other5 = request.POST.get("other5")
        other5_bonds_left = request.POST.get("other5_bonds_left")
        other5_bonds_right = request.POST.get("other5_bonds_right")
        other5_notes_left = request.POST.get("other5_notes_left")
        other5_notes_right = request.POST.get("other5_notes_right")
        other5_name_service = request.POST.get("other5_name_service")
        signature = request.POST.get("signature")
        position = request.POST.get("position")
        date = request.POST.get("date")
        phone = request.POST.get("phone")

        csv_file_path = "data/cuestionarios/balanza_de_pagos/JP-363.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "bonds_year_left",
                        "bonds_year_right",
                        "notes_year_left",
                        "notes_year_right",
                        "CG_bonds_left",
                        "CG_bonds_right",
                        "CG_notes_left",
                        "CG_notes_right",
                        "CG_name_service",
                        "town_bonds_left",
                        "town_bonds_right",
                        "town_notes_left",
                        "town_notes_right",
                        "town_name_service",
                        "PC_bonds_left",
                        "PC_bonds_right",
                        "PC_notes_left",
                        "PC_notes_right",
                        "PC_name_service",
                        "EPA_bonds_left",
                        "EPA_bonds_right",
                        "EPA_notes_left",
                        "EPA_notes_right",
                        "EPA_name_service",
                        "HA_bonds_left",
                        "HA_bonds_right",
                        "HA_notes_left",
                        "HA_notes_right",
                        "HA_name_service",
                        "ASA_bonds_left",
                        "ASA_bonds_right",
                        "ASA_notes_left",
                        "ASA_notes_right",
                        "ASA_name_service",
                        "PBA_bonds_left",
                        "PBA_bonds_right",
                        "PBA_notes_left",
                        "PBA_notes_right",
                        "PBA_name_service",
                        "PA_bonds_left",
                        "PA_bonds_right",
                        "PA_notes_left",
                        "PA_notes_right",
                        "PA_name_service",
                        "TA_bonds_left",
                        "TA_bonds_right",
                        "TA_notes_left",
                        "TA_notes_right",
                        "TA_name_service",
                        "IDC_bonds_left",
                        "IDC_bonds_right",
                        "IDC_notes_left",
                        "IDC_notes_right",
                        "IDC_name_service",
                        "GDB_bonds_left",
                        "GDB_bonds_right",
                        "GDB_notes_left",
                        "GDB_notes_right",
                        "GDB_name_service",
                        "HFC_bonds_left",
                        "HFC_bonds_right",
                        "HFC_notes_left",
                        "HFC_notes_right",
                        "HFC_name_service",
                        "other",
                        "other_bonds_left",
                        "other_bonds_right",
                        "other_notes_left",
                        "other_notes_right",
                        "other_name_service",
                        "other_PC_1",
                        "other_PC_1_bonds_left",
                        "other_PC_1_bonds_right",
                        "other_PC_1_notes_left",
                        "other_PC_1_notes_right",
                        "other_PC_1_name_service",
                        "other_PC_2",
                        "other_PC_2_bonds_left",
                        "other_PC_2_bonds_right",
                        "other_PC_2_notes_left",
                        "other_PC_2_notes_right",
                        "other_PC_2_name_service",
                        "GNMA_bonds_left",
                        "GN",
                        "GNMA_notes_left",
                        "GNMA_notes_right",
                        "GNMA_name_service",
                        "other5",
                        "other5_bonds_left",
                        "other5_bonds_right",
                        "other5_notes_left",
                        "other5_notes_right",
                        "other5_name_service",
                        "signature",
                        "position",
                        "date",
                        "phone",
                    ]
                )

            writer.writerow(
                [
                    bonds_year_left,
                    bonds_year_right,
                    notes_year_left,
                    notes_year_right,
                    CG_bonds_left,
                    CG_bonds_right,
                    CG_notes_left,
                    CG_notes_right,
                    CG_name_service,
                    town_bonds_left,
                    town_bonds_right,
                    town_notes_left,
                    town_notes_right,
                    town_name_service,
                    PC_bonds_left,
                    PC_bonds_right,
                    PC_notes_left,
                    PC_notes_right,
                    PC_name_service,
                    EPA_bonds_left,
                    EPA_bonds_right,
                    EPA_notes_left,
                    EPA_notes_right,
                    EPA_name_service,
                    HA_bonds_left,
                    HA_bonds_right,
                    HA_notes_left,
                    HA_notes_right,
                    HA_name_service,
                    ASA_bonds_left,
                    ASA_bonds_right,
                    ASA_notes_left,
                    ASA_notes_right,
                    ASA_name_service,
                    PBA_bonds_left,
                    PBA_bonds_right,
                    PBA_notes_left,
                    PBA_notes_right,
                    PBA_name_service,
                    PA_bonds_left,
                    PA_bonds_right,
                    PA_notes_left,
                    PA_notes_right,
                    PA_name_service,
                    TA_bonds_left,
                    TA_bonds_right,
                    TA_notes_left,
                    TA_notes_right,
                    TA_name_service,
                    IDC_bonds_left,
                    IDC_bonds_right,
                    IDC_notes_left,
                    IDC_notes_right,
                    IDC_name_service,
                    GDB_bonds_left,
                    GDB_bonds_right,
                    GDB_notes_left,
                    GDB_notes_right,
                    GDB_name_service,
                    HFC_bonds_left,
                    HFC_bonds_right,
                    HFC_notes_left,
                    HFC_notes_right,
                    HFC_name_service,
                    other,
                    other_bonds_left,
                    other_bonds_right,
                    other_notes_left,
                    other_notes_right,
                    other_name_service,
                    other_PC_1,
                    other_PC_1_bonds_left,
                    other_PC_1_bonds_right,
                    other_PC_1_notes_left,
                    other_PC_1_notes_right,
                    other_PC_1_name_service,
                    other_PC_2,
                    other_PC_2_bonds_left,
                    other_PC_2_bonds_right,
                    other_PC_2_notes_left,
                    other_PC_2_notes_right,
                    other_PC_2_name_service,
                    GNMA_bonds_left,
                    GNMA_bonds_right,
                    GNMA_notes_left,
                    GNMA_notes_right,
                    GNMA_name_service,
                    other5,
                    other5_bonds_left,
                    other5_bonds_right,
                    other5_notes_left,
                    other5_notes_right,
                    other5_name_service,
                    signature,
                    position,
                    date,
                    phone,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/balanza_de_pagos/JP-363.csv",
            dtypes={
                "bonds_year_left": int,
                "bonds_year_right": int,
                "notes_year_left": int,
                "notes_year_right": int,
                "CG_bonds_left": float,
                "CG_bonds_right": float,
                "CG_notes_left": float,
                "CG_notes_right": float,
                "CG_name_service": str,
                "town_bonds_left": float,
                "town_bonds_right": float,
                "town_notes_left": float,
                "town_notes_right": float,
                "town_name_service": str,
                "PC_bonds_left": float,
                "PC_bonds_right": float,
                "PC_notes_left": float,
                "PC_notes_right": float,
                "PC_name_service": str,
                "EPA_bonds_left": float,
                "EPA_bonds_right": float,
                "EPA_notes_left": float,
                "EPA_notes_right": float,
                "EPA_name_service": str,
                "HA_bonds_left": float,
                "HA_bonds_right": float,
                "HA_notes_left": float,
                "HA_notes_right": float,
                "HA_name_service": str,
                "ASA_bonds_left": float,
                "ASA_bonds_right": float,
                "ASA_notes_left": float,
                "ASA_notes_right": float,
                "ASA_name_service": str,
                "PBA_bonds_left": float,
                "PBA_bonds_right": float,
                "PBA_notes_left": float,
                "PBA_notes_right": float,
                "PBA_name_service": str,
                "PA_bonds_left": float,
                "PA_bonds_right": float,
                "PA_notes_left": float,
                "PA_notes_right": float,
                "PA_name_service": str,
                "TA_bonds_left": float,
                "TA_bonds_right": float,
                "TA_notes_left": float,
                "TA_notes_right": float,
                "TA_name_service": str,
                "IDC_bonds_left": float,
                "IDC_bonds_right": float,
                "IDC_notes_left": float,
                "IDC_notes_right": float,
                "IDC_name_service": str,
                "GDB_bonds_left": float,
                "GDB_bonds_right": float,
                "GDB_notes_left": float,
                "GDB_notes_right": float,
                "GDB_name_service": str,
                "HFC_bonds_left": float,
                "HFC_bonds_right": float,
                "HFC_notes_left": float,
                "HFC_notes_right": float,
                "HFC_name_service": str,
                "other": str,
                "other_bonds_left": float,
                "other_bonds_right": float,
                "other_notes_left": float,
                "other_notes_right": float,
                "other_name_service": str,
                "other_PC_1": str,
                "other_PC_1_bonds_left": float,
                "other_PC_1_bonds_right": float,
                "other_PC_1_notes_left": float,
                "other_PC_1_notes_right": float,
                "other_PC_1_name_service": str,
                "other_PC_2": str,
                "other_PC_2_bonds_left": float,
                "other_PC_2_bonds_right": float,
                "other_PC_2_notes_left": float,
                "other_PC_2_notes_right": float,
                "other_PC_2_name_service": str,
                "GNMA_bonds_left": float,
                "GN": str,
                "GNMA_notes_left": float,
                "GNMA_notes_right": float,
                "GNMA_name_service": str,
                "other5": str,
                "other5_bonds_left": float,
                "other5_bonds_right": float,
                "other5_notes_left": float,
                "other5_notes_right": float,
                "other5_name_service": str,
                "signature": str,
                "position": str,
                "date": str,
                "phone": str,
            },
            table_name="JP_363",
            table_id="11",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/balanza_de_pagos/JP-363.html")


def succesfull_page(request):
    return render(request, "forms/succesfull.html")


def Forms(request):
    return render(request, "forms/forms.html")


def JP_560_63110(request):
    if request.method == "POST":
        # Retrieve form data
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")
        sales_1 = request.POST.get("sales_1")
        sales_2 = request.POST.get("sales_2")
        disability_1 = request.POST.get("disability_1")
        disability_2 = request.POST.get("disability_2")
        life_1 = request.POST.get("life_1")
        life_2 = request.POST.get("life_2")
        interest_1 = request.POST.get("interest_1")
        interest_2 = request.POST.get("interest_2")
        other_income_1 = request.POST.get("other_income_1")
        other_income_2 = request.POST.get("other_income_2")
        total_income_1 = request.POST.get("total_income_1")
        total_income_2 = request.POST.get("total_income_2")
        interest_paid_1 = request.POST.get("interest_paid_1")
        interest_paid_2 = request.POST.get("interest_paid_2")
        disability_paid_1 = request.POST.get("disability_paid_1")
        disability_paid_2 = request.POST.get("disability_paid_2")
        life_paid_1 = request.POST.get("life_paid_1")
        life_paid_2 = request.POST.get("life_paid_2")
        other_expenditures_1 = request.POST.get("other_expenditures_1")
        other_expenditures_2 = request.POST.get("other_expenditures_2")
        total_expenditures_1 = request.POST.get("total_expenditures_1")
        total_expenditures_2 = request.POST.get("total_expenditures_2")
        net_profit_1 = request.POST.get("net_profit_1")
        net_profit_2 = request.POST.get("net_profit_2")
        initial_inventory_1 = request.POST.get("initial_inventory_1")
        initial_inventory_2 = request.POST.get("initial_inventory_2")
        final_inventory_1 = request.POST.get("final_inventory_1")
        final_inventory_2 = request.POST.get("final_inventory_2")
        signature = request.POST.get("signature")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/JP-560-63110.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "ssn",
                        "tel",
                        "fax",
                        "sales_1",
                        "sales_2",
                        "disability_1",
                        "disability_2",
                        "life_1",
                        "life_2",
                        "interest_1",
                        "interest_2",
                        "other_income_1",
                        "other_income_2",
                        "total_income_1",
                        "total_income_2",
                        "interest_paid_1",
                        "interest_paid_2",
                        "disability_paid_1",
                        "disability_paid_2",
                        "life_paid_1",
                        "life_paid_2",
                        "other_expenditures_1",
                        "other_expenditures_2",
                        "total_expenditures_1",
                        "total_expenditures_2",
                        "net_profit_1",
                        "net_profit_2",
                        "initial_inventory_1",
                        "initial_inventory_2",
                        "final_inventory_1",
                        "final_inventory_2",
                        "signature",
                        "rank",
                    ]
                )

            writer.writerow(
                [
                    ssn,
                    tel,
                    fax,
                    sales_1,
                    sales_2,
                    disability_1,
                    disability_2,
                    life_1,
                    life_2,
                    interest_1,
                    interest_2,
                    other_income_1,
                    other_income_2,
                    total_income_1,
                    total_income_2,
                    interest_paid_1,
                    interest_paid_2,
                    disability_paid_1,
                    disability_paid_2,
                    life_paid_1,
                    life_paid_2,
                    other_expenditures_1,
                    other_expenditures_2,
                    total_expenditures_1,
                    total_expenditures_2,
                    net_profit_1,
                    net_profit_2,
                    initial_inventory_1,
                    initial_inventory_2,
                    final_inventory_1,
                    final_inventory_2,
                    signature,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/JP-560-63110.csv",
            dtypes={
                "ssn": str,
                "tel": str,
                "fax": str,
                "sales_1": float,
                "sales_2": float,
                "disability_1": float,
                "disability_2": float,
                "life_1": float,
                "life_2": float,
                "interest_1": float,
                "interest_2": float,
                "other_income_1": float,
                "other_income_2": float,
                "total_income_1": float,
                "total_income_2": float,
                "interest_paid_1": float,
                "interest_paid_2": float,
                "disability_paid_1": float,
                "disability_paid_2": float,
                "life_paid_1": float,
                "life_paid_2": float,
                "other_expenditures_1": float,
                "other_expenditures_2": float,
                "total_expenditures_1": float,
                "total_expenditures_2": float,
                "net_profit_1": float,
                "net_profit_2": float,
                "initial_inventory_1": float,
                "initial_inventory_2": float,
                "final_inventory_1": float,
                "final_inventory_2": float,
                "signature": str,
                "rank": str,
            },
            table_name="JP_560_63110",
            table_id="9",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/JP-560-63110.html")


def IP_210(request):
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
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        income_operations_12 = request.POST.get("income_operations_12")
        income_operations_13 = request.POST.get("income_operations_13")
        income_interests_12 = request.POST.get("income_interests_12")
        income_interests_13 = request.POST.get("income_interests_13")
        incomes_rents_12 = request.POST.get("incomes_rents_12")
        incomes_rents_13 = request.POST.get("incomes_rents_13")
        income_rent_land_12 = request.POST.get("income_rent_land_12")
        income_rent_land_13 = request.POST.get("income_rent_land_13")
        other_income_12 = request.POST.get("other_income_12")
        other_income_13 = request.POST.get("other_income_13")
        total_incomes_12 = request.POST.get("total_incomes_12")
        total_incomes_13 = request.POST.get("total_incomes_13")
        total_income_12 = request.POST.get("total_income_12")
        total_income_13 = request.POST.get("total_income_13")

        salaries_2012 = request.POST.get("salaries_2012")
        salaries_2013 = request.POST.get("salaries_2013")
        expenses_interests_12 = request.POST.get("expenses_interests_12")
        expenses_interests_13 = request.POST.get("expenses_interests_13")
        depreciation_12 = request.POST.get("depreciation_12")
        depreciation_13 = request.POST.get("depreciation_13")
        expenses_rent_12 = request.POST.get("expenses_rent_12")
        expenses_rent_13 = request.POST.get("expenses_rent_13")
        bad_debts_12 = request.POST.get("bad_debts_12")
        bad_debts_13 = request.POST.get("bad_debts_13")
        donations_12 = request.POST.get("donations_12")
        donations_13 = request.POST.get("donations_13")
        sales_tax_12 = request.POST.get("sales_tax_12")
        sales_tax_13 = request.POST.get("sales_tax_13")
        machinery_12 = request.POST.get("machinery_12")
        machinery_13 = request.POST.get("machinery_13")
        other_purchases_12 = request.POST.get("other_purchases_12")
        other_purchases_13 = request.POST.get("other_purchases_13")
        licenses_12 = request.POST.get("licenses_12")
        licenses_13 = request.POST.get("licenses_13")
        other_expenses_12 = request.POST.get("other_expenses_12")
        other_expenses_13 = request.POST.get("other_expenses_13")
        total_expenses_12 = request.POST.get("total_expenses_12")
        total_expenses_13 = request.POST.get("total_expenses_13")
        net_profit_12 = request.POST.get("net_profit_12")
        net_profit_13 = request.POST.get("net_profit_13")
        income_tax_12 = request.POST.get("income_tax_12")
        income_tax_13 = request.POST.get("income_tax_13")
        profit_after_tax_12 = request.POST.get("profit_after_tax_12")
        profit_after_tax_13 = request.POST.get("profit_after_tax_13")
        withheld_tax_12 = request.POST.get("withheld_tax_12")
        withheld_tax_13 = request.POST.get("withheld_tax_13")
        signature = request.POST.get("signature")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-210.csv"
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
                        "closing_date",
                        "start_year",
                        "end_year",
                        "income_operations_12",
                        "income_operations_13",
                        "income_interests_12",
                        "income_interests_13",
                        "incomes_rents_12",
                        "incomes_rents_13",
                        "income_rent_land_12",
                        "income_rent_land_13",
                        "other_income_12",
                        "other_income_13",
                        "total_incomes_12",
                        "total_incomes_13",
                        "total_income_12",
                        "total_income_13",
                        "salaries_2012",
                        "salaries_2013",
                        "expenses_interests_12",
                        "expenses_interests_13",
                        "depreciation_12",
                        "depreciation_13",
                        "bad_debts_12",
                        "bad_debts_13",
                        "expenses_rent_12",
                        "expenses_rent_13",
                        "donations_12",
                        "donations_13",
                        "sales_tax_12",
                        "sales_tax_13",
                        "machinery_12",
                        "machinery_13",
                        "other_purchases_12",
                        "other_purchases_13",
                        "licenses_12",
                        "licenses_13",
                        "other_expenses_12",
                        "other_expenses_13",
                        "total_expenses_12",
                        "total_expenses_13",
                        "net_profit_12",
                        "net_profit_13",
                        "income_tax_12",
                        "income_tax_13",
                        "profit_after_tax_12",
                        "profit_after_tax_13",
                        "withheld_tax_12",
                        "withheld_tax_13",
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
                    closing_date,
                    start_year,
                    end_year,
                    income_operations_12,
                    income_operations_13,
                    income_interests_12,
                    income_interests_13,
                    incomes_rents_12,
                    incomes_rents_13,
                    income_rent_land_12,
                    income_rent_land_13,
                    other_income_12,
                    other_income_13,
                    total_incomes_12,
                    total_incomes_13,
                    total_income_12,
                    total_income_13,
                    salaries_2012,
                    salaries_2013,
                    expenses_interests_12,
                    expenses_interests_13,
                    depreciation_12,
                    depreciation_13,
                    expenses_rent_12,
                    expenses_rent_13,
                    bad_debts_12,
                    bad_debts_13,
                    donations_12,
                    donations_13,
                    sales_tax_12,
                    sales_tax_13,
                    machinery_12,
                    machinery_13,
                    other_purchases_12,
                    other_purchases_13,
                    licenses_12,
                    licenses_13,
                    other_expenses_12,
                    other_expenses_13,
                    total_expenses_12,
                    total_expenses_13,
                    net_profit_12,
                    net_profit_13,
                    income_tax_12,
                    income_tax_13,
                    profit_after_tax_12,
                    profit_after_tax_13,
                    withheld_tax_12,
                    withheld_tax_13,
                    signature,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-210.csv",
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
                "closing_date": str,
                "start_year": int,
                "end_year": int,
                "income_operations_12": float,
                "income_operations_13": float,
                "income_interests_12": float,
                "income_interests_13": float,
                "incomes_rents_12": float,
                "incomes_rents_13": float,
                "income_rent_land_12": float,
                "income_rent_land_13": float,
                "other_income_12": float,
                "other_income_13": float,
                "total_incomes_12": float,
                "total_incomes_13": float,
                "total_income_12": float,
                "total_income_13": float,
                "salaries_2012": float,
                "salaries_2013": float,
                "expenses_interests_12": float,
                "expenses_interests_13": float,
                "depreciation_12": float,
                "depreciation_13": float,
                "bad_debts_12": float,
                "bad_debts_13": float,
                "expenses_rent_12": float,
                "expenses_rent_13": float,
                "donations_12": float,
                "donations_13": float,
                "sales_tax_12": float,
                "sales_tax_13": float,
                "machinery_12": float,
                "machinery_13": float,
                "other_purchases_12": float,
                "other_purchases_13": float,
                "licenses_12": float,
                "licenses_13": float,
                "other_expenses_12": float,
                "other_expenses_13": float,
                "total_expenses_12": float,
                "total_expenses_13": float,
                "net_profit_12": float,
                "net_profit_13": float,
                "income_tax_12": float,
                "income_tax_13": float,
                "profit_after_tax_12": float,
                "profit_after_tax_13": float,
                "withheld_tax_12": float,
                "withheld_tax_13": float,
                "signature": str,
                "rank": str,
            },
            table_name="IP_210",
            table_id="13",
            debug=False,
        )

        return render(request, "forms/succesfull.html")

    return render(request, "forms/yearly/ingreso_neto/IP-210.html")


def IP_220(request):
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
        services_revenues_12 = request.POST.get("services_revenues_12")
        services_revenues_13 = request.POST.get("services_revenues_13")
        residential_consumers_12 = request.POST.get("residential_consumers_12")
        residential_consumers_13 = request.POST.get("residential_consumers_13")
        other_consumers_12 = request.POST.get("other_consumers_12")
        other_consumers_13 = request.POST.get("other_consumers_13")
        incomes_rents_12 = request.POST.get("incomes_rents_12")
        incomes_rents_13 = request.POST.get("incomes_rents_13")
        incomes_interests_12 = request.POST.get("incomes_interests_12")
        incomes_interests_13 = request.POST.get("incomes_interests_13")
        dividends_12 = request.POST.get("dividends_12")
        dividends_13 = request.POST.get("dividends_13")
        others_incomes_12 = request.POST.get("others_incomes_12")
        others_incomes_13 = request.POST.get("others_incomes_13")
        total_income_12 = request.POST.get("total_income_12")
        total_income_13 = request.POST.get("total_income_13")
        salaries_2012 = request.POST.get("salaries_2012")
        salaries_2013 = request.POST.get("salaries_2013")
        expenses_interests_12 = request.POST.get("expenses_interests_12")
        expenses_interests_13 = request.POST.get("expenses_interests_13")
        expenses_rents_12 = request.POST.get("expenses_rents_12")
        expenses_rents_13 = request.POST.get("expenses_rents_13")
        depreciation_12 = request.POST.get("depreciation_12")
        depreciation_13 = request.POST.get("depreciation_13")
        bad_debts_12 = request.POST.get("bad_debts_12")
        bad_debts_13 = request.POST.get("bad_debts_13")
        donations_12 = request.POST.get("donations_12")
        donations_13 = request.POST.get("donations_13")
        sales_tax_12 = request.POST.get("sales_tax_12")
        sales_tax_13 = request.POST.get("sales_tax_13")
        machinery_12 = request.POST.get("machinery_12")
        machinery_13 = request.POST.get("machinery_13")
        other_purchases_12 = request.POST.get("other_purchases_12")
        other_purchases_13 = request.POST.get("other_purchases_13")
        licenses_12 = request.POST.get("licenses_12")
        licenses_13 = request.POST.get("licenses_13")
        other_expenses_12 = request.POST.get("other_expenses_12")
        other_expenses_13 = request.POST.get("other_expenses_13")
        total_expenses_12 = request.POST.get("total_expenses_12")
        total_expenses_13 = request.POST.get("total_expenses_13")
        net_profit_12 = request.POST.get("net_profit_12")
        net_profit_13 = request.POST.get("net_profit_13")
        income_tax_12 = request.POST.get("income_tax_12")
        income_tax_13 = request.POST.get("income_tax_13")
        profit_after_tax_12 = request.POST.get("profit_after_tax_12")
        profit_after_tax_13 = request.POST.get("profit_after_tax_13")
        withheld_tax_12 = request.POST.get("withheld_tax_12")
        withheld_tax_13 = request.POST.get("withheld_tax_13")
        signature = request.POST.get("signature")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-220.csv"
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
                        "services_revenues_12",
                        "services_revenues_13",
                        "residential_consumers_12",
                        "residential_consumers_13",
                        "other_consumers_12",
                        "other_consumers_13",
                        "incomes_rents_12",
                        "incomes_rents_13",
                        "incomes_interests_12",
                        "incomes_interests_13",
                        "dividends_12",
                        "dividends_13",
                        "others_incomes_12",
                        "others_incomes_13",
                        "total_income_12",
                        "total_income_13",
                        "salaries_2012",
                        "salaries_2013",
                        "expenses_interests_12",
                        "expenses_interests_13",
                        "expenses_rents_12",
                        "expenses_rents_13",
                        "depreciation_12",
                        "depreciation_13",
                        "bad_debts_12",
                        "bad_debts_13",
                        "donations_12",
                        "donations_13",
                        "sales_tax_12",
                        "sales_tax_13",
                        "machinery_12",
                        "machinery_13",
                        "other_purchases_12",
                        "other_purchases_13",
                        "licenses_12",
                        "licenses_13",
                        "other_expenses_12",
                        "other_expenses_13",
                        "total_expenses_12",
                        "total_expenses_13",
                        "net_profit_12",
                        "net_profit_13",
                        "income_tax_12",
                        "income_tax_13",
                        "profit_after_tax_12",
                        "profit_after_tax_13",
                        "withheld_tax_12",
                        "withheld_tax_13",
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
                    services_revenues_12,
                    services_revenues_13,
                    residential_consumers_12,
                    residential_consumers_13,
                    other_consumers_12,
                    other_consumers_13,
                    incomes_rents_12,
                    incomes_rents_13,
                    incomes_interests_12,
                    incomes_interests_13,
                    dividends_12,
                    dividends_13,
                    others_incomes_12,
                    others_incomes_13,
                    total_income_12,
                    total_income_13,
                    salaries_2012,
                    salaries_2013,
                    expenses_interests_12,
                    expenses_interests_13,
                    expenses_rents_12,
                    expenses_rents_13,
                    depreciation_12,
                    depreciation_13,
                    bad_debts_12,
                    bad_debts_13,
                    donations_12,
                    donations_13,
                    sales_tax_12,
                    sales_tax_13,
                    machinery_12,
                    machinery_13,
                    other_purchases_12,
                    other_purchases_13,
                    licenses_12,
                    licenses_13,
                    other_expenses_12,
                    other_expenses_13,
                    total_expenses_12,
                    total_expenses_13,
                    net_profit_12,
                    net_profit_13,
                    income_tax_12,
                    income_tax_13,
                    profit_after_tax_12,
                    profit_after_tax_13,
                    withheld_tax_12,
                    withheld_tax_13,
                    signature,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-220.csv",
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
                "services_revenues_12": float,
                "services_revenues_13": float,
                "residential_consumers_12": float,
                "residential_consumers_13": float,
                "other_consumers_12": float,
                "other_consumers_13": float,
                "incomes_rents_12": float,
                "incomes_rents_13": float,
                "incomes_interests_12": float,
                "incomes_interests_13": float,
                "dividends_12": float,
                "dividends_13": float,
                "others_incomes_12": float,
                "others_incomes_13": float,
                "total_income_12": float,
                "total_income_13": float,
                "salaries_2012": float,
                "salaries_2013": float,
                "expenses_interests_12": float,
                "expenses_interests_13": float,
                "expenses_rents_12": float,
                "expenses_rents_13": float,
                "depreciation_12": float,
                "depreciation_13": float,
                "bad_debts_12": float,
                "bad_debts_13": float,
                "donations_12": float,
                "donations_13": float,
                "sales_tax_12": float,
                "sales_tax_13": float,
                "machinery_12": float,
                "machinery_13": float,
                "other_purchases_12": float,
                "other_purchases_13": float,
                "licenses_12": float,
                "licenses_13": float,
                "other_expenses_12": float,
                "other_expenses_13": float,
                "total_expenses_12": float,
                "total_expenses_13": float,
                "net_profit_12": float,
                "net_profit_13": float,
                "income_tax_12": float,
                "income_tax_13": float,
                "profit_after_tax_12": float,
                "profit_after_tax_13": float,
                "withheld_tax_12": float,
                "withheld_tax_13": float,
                "signature": str,
                "rank": str,
            },
            table_name="IP_220",
            table_id="17",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-220.html")


def JP_560_63111(request):

    if request.method == "POST":
        # Retrieve form data
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")
        sales_1 = request.POST.get("sales_1")
        sales_2 = request.POST.get("sales_2")
        premiums_1 = request.POST.get("premiums_1")
        premiums_2 = request.POST.get("premiums_2")
        interest_received_1 = request.POST.get("interest_received_1")
        interest_received_2 = request.POST.get("interest_received_2")
        other_income_1 = request.POST.get("other_income_1")
        other_income_2 = request.POST.get("other_income_2")
        total_income_1 = request.POST.get("total_income_1")
        total_income_2 = request.POST.get("total_income_2")
        interest_paid_1 = request.POST.get("interest_paid_1")
        interest_paid_2 = request.POST.get("interest_paid_2")
        claims_paid_1 = request.POST.get("claims_paid_1")
        claims_paid_2 = request.POST.get("claims_paid_2")
        other_expenditures_1 = request.POST.get("other_expenditures_1")
        other_expenditures_2 = request.POST.get("other_expenditures_2")
        total_expenditures_1 = request.POST.get("total_expenditures_1")
        total_expenditures_2 = request.POST.get("total_expenditures_2")
        net_profit_loss_1 = request.POST.get("net_profit_loss_1")
        net_profit_loss_2 = request.POST.get("net_profit_loss_2")
        initial_inventory_1 = request.POST.get("initial_inventory_1")
        initial_inventory_2 = request.POST.get("initial_inventory_2")
        final_inventory_1 = request.POST.get("final_inventory_1")
        final_inventory_2 = request.POST.get("final_inventory_2")
        signature = request.POST.get("signature")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/JP-560-63111.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "ssn",
                        "tel",
                        "fax",
                        "sales_1",
                        "sales_2",
                        "premiums_1",
                        "premiums_2",
                        "interest_received_1",
                        "interest_received_2",
                        "other_income_1",
                        "other_income_2",
                        "total_income_1",
                        "total_income_2",
                        "interest_paid_1",
                        "interest_paid_2",
                        "claims_paid_1",
                        "claims_paid_2",
                        "other_expenditures_1",
                        "other_expenditures_2",
                        "total_expenditures_1",
                        "total_expenditures_2",
                        "net_profit_loss_1",
                        "net_profit_loss_2",
                        "initial_inventory_1",
                        "initial_inventory_2",
                        "final_inventory_1",
                        "final_inventory_2",
                        "signature",
                        "rank",
                    ]
                )

            writer.writerow(
                [
                    ssn,
                    tel,
                    fax,
                    sales_1,
                    sales_2,
                    premiums_1,
                    premiums_2,
                    interest_received_1,
                    interest_received_2,
                    other_income_1,
                    other_income_2,
                    total_income_1,
                    total_income_2,
                    interest_paid_1,
                    interest_paid_2,
                    claims_paid_1,
                    claims_paid_2,
                    other_expenditures_1,
                    other_expenditures_2,
                    total_expenditures_1,
                    total_expenditures_2,
                    net_profit_loss_1,
                    net_profit_loss_2,
                    initial_inventory_1,
                    initial_inventory_2,
                    final_inventory_1,
                    final_inventory_2,
                    signature,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/JP-560-63111.csv",
            dtypes={
                "ssn": str,
                "tel": str,
                "fax": str,
                "sales_1": float,
                "sales_2": float,
                "premiums_1": float,
                "premiums_2": float,
                "interest_received_1": float,
                "interest_received_2": float,
                "other_income_1": float,
                "other_income_2": float,
                "total_income_1": float,
                "total_income_2": float,
                "interest_paid_1": float,
                "interest_paid_2": float,
                "claims_paid_1": float,
                "claims_paid_2": float,
                "other_expenditures_1": float,
                "other_expenditures_2": float,
                "total_expenditures_1": float,
                "total_expenditures_2": float,
                "net_profit_loss_1": float,
                "net_profit_loss_2": float,
                "initial_inventory_1": float,
                "initial_inventory_2": float,
                "final_inventory_1": float,
                "final_inventory_2": float,
                "signature": str,
                "rank": str,
            },
            table_name="JP_560_63111",
            table_id="19",
            debug=False,
        )

        return render(request, "forms/succesfull.html")

    return render(request, "forms/yearly/ingreso_neto/JP-560-63111.html")


def IP_230(request):
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
        income_project_A_12 = request.POST.get("income_project_A_12")
        income_project_A_13 = request.POST.get("income_project_A_13")
        people_A_12 = request.POST.get("people_A_12")
        people_A_13 = request.POST.get("people_A_13")
        industries_businesses_A_12 = request.POST.get("industries_businesses_A_12")
        industries_businesses_A_13 = request.POST.get("industries_businesses_A_13")
        direct_indirect_B_12 = request.POST.get("direct_indirect_B_12")
        direct_indirect_B_13 = request.POST.get("direct_indirect_B_13")
        direct_christmas_vacation_B_12 = request.POST.get(
            "direct_christmas_vacation_B_12"
        )
        direct_christmas_vacation_B_13 = request.POST.get(
            "direct_christmas_vacation_B_13"
        )
        rent_land_building_B_12 = request.POST.get("rent_land_building_B_12")
        rent_land_building_B_13 = request.POST.get("rent_land_building_B_13")
        rent_equipment_B_12 = request.POST.get("rent_equipment_B_12")
        rent_equipment_B_13 = request.POST.get("rent_equipment_B_13")
        depreciation_B_12 = request.POST.get("depreciation_B_12")
        depreciation_B_13 = request.POST.get("depreciation_B_13")
        sales_tax_B_12 = request.POST.get("sales_tax_B_12")
        sales_tax_B_13 = request.POST.get("sales_tax_B_13")
        purchases_machinery_equipment_B_12 = request.POST.get(
            "purchases_machinery_equipment_B_12"
        )
        purchases_machinery_equipment_B_13 = request.POST.get(
            "purchases_machinery_equipment_B_13"
        )
        other_purchases_B_12 = request.POST.get("other_purchases_B_12")
        other_purchases_B_13 = request.POST.get("other_purchases_B_13")
        licenses_patent_B_12 = request.POST.get("licenses_patent_B_12")
        licenses_patent_B_13 = request.POST.get("licenses_patent_B_13")
        other_costs_direct_indirect_B_12 = request.POST.get(
            "other_costs_direct_indirect_B_12"
        )
        other_costs_direct_indirect_B_13 = request.POST.get(
            "other_costs_direct_indirect_B_13"
        )
        gross_profit_C_12 = request.POST.get("gross_profit_C_12")
        gross_profit_C_13 = request.POST.get("gross_profit_C_13")
        other_income_D_12 = request.POST.get("other_income_D_12")
        other_income_D_13 = request.POST.get("other_income_D_13")
        interest_D_12 = request.POST.get("interest_D_12")
        interest_D_13 = request.POST.get("interest_D_13")
        rent_land_building_D_12 = request.POST.get("rent_land_building_D_12")
        rent_land_building_D_13 = request.POST.get("rent_land_building_D_13")
        gain_loss_D_12 = request.POST.get("gain_loss_D_12")
        gain_loss_D_13 = request.POST.get("gain_loss_D_13")
        other_D_12 = request.POST.get("other_D_12")
        other_D_13 = request.POST.get("other_D_13")
        gross_profit_E_12 = request.POST.get("gross_profit_E_12")
        gross_profit_E_13 = request.POST.get("gross_profit_E_13")
        administrative_F_12 = request.POST.get("administrative_F_12")
        administrative_F_13 = request.POST.get("administrative_F_13")
        salaries_wages_bonus_commissions_F_12 = request.POST.get(
            "salaries_wages_bonus_commissions_F_12"
        )
        salaries_wages_bonus_commissions_F_13 = request.POST.get(
            "salaries_wages_bonus_commissions_F_13"
        )
        interest_F_12 = request.POST.get("interest_F_12")
        interest_F_13 = request.POST.get("interest_F_13")
        rent_land_building_F_12 = request.POST.get("rent_land_building_F_12")
        rent_land_building_F_13 = request.POST.get("rent_land_building_F_13")
        depreciation_F_12 = request.POST.get("depreciation_F_12")
        depreciation_F_13 = request.POST.get("depreciation_F_13")
        bad_debts_F_12 = request.POST.get("bad_debts_F_12")
        bad_debts_F_13 = request.POST.get("bad_debts_F_13")
        donation_F_12 = request.POST.get("donation_F_12")
        donation_F_13 = request.POST.get("donation_F_13")
        other_expenses_F_12 = request.POST.get("other_expenses_F_12")
        other_expenses_F_13 = request.POST.get("other_expenses_F_13")
        net_profit_G_12 = request.POST.get("net_profit_G_12")
        net_profit_G_13 = request.POST.get("net_profit_G_13")
        income_tax_G_12 = request.POST.get("income_tax_G_12")
        income_tax_G_13 = request.POST.get("income_tax_G_13")
        profit_after_tax_G_12 = request.POST.get("profit_after_tax_G_12")
        profit_after_tax_G_13 = request.POST.get("profit_after_tax_G_13")
        sales_tax_H_12 = request.POST.get("sales_tax_H_12")
        sales_tax_H_13 = request.POST.get("sales_tax_H_13")
        beginning_year_HA = request.POST.get("beginning_year_HA")
        end_year_HB = request.POST.get("end_year_HB")
        beginning_year_HC = request.POST.get("beginning_year_HC")
        end_year_HD = request.POST.get("end_year_HD")
        signature = request.POST.get("signature")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-230.csv"
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
                        "income_project_A_12",
                        "income_project_A_13",
                        "people_A_12",
                        "people_A_13",
                        "industries_businesses_A_12",
                        "industries_businesses_A_13",
                        "direct_indirect_B_12",
                        "direct_indirect_B_13",
                        "direct_christmas_vacation_B_12",
                        "direct_christmas_vacation_B_13",
                        "rent_land_building_B_12",
                        "rent_land_building_B_13",
                        "rent_equipment_B_12",
                        "rent_equipment_B_13",
                        "depreciation_B_12",
                        "depreciation_B_13",
                        "sales_tax_B_12",
                        "sales_tax_B_13",
                        "purchases_machinery_equipment_B_12",
                        "purchases_machinery_equipment_B_13",
                        "other_purchases_B_12",
                        "other_purchases_B_13",
                        "licenses_patent_B_12",
                        "licenses_patent_B_13",
                        "other_costs_direct_indirect_B_12",
                        "other_costs_direct_indirect_B_13",
                        "gross_profit_C_12",
                        "gross_profit_C_13",
                        "other_income_D_12",
                        "other_income_D_13",
                        "interest_D_12",
                        "interest_D_13",
                        "rent_land_building_D_12",
                        "rent_land_building_D_13",
                        "gain_loss_D_12",
                        "gain_loss_D_13",
                        "other_D_12",
                        "other_D_13",
                        "gross_profit_E_12",
                        "gross_profit_E_13",
                        "administrative_F_12",
                        "administrative_F_13",
                        "salaries_wages_bonus_commissions_F_12",
                        "salaries_wages_bonus_commissions_F_13",
                        "interest_F_12",
                        "interest_F_13",
                        "rent_land_building_F_12",
                        "rent_land_building_F_13",
                        "depreciation_F_12",
                        "depreciation_F_13",
                        "bad_debts_F_12",
                        "bad_debts_F_13",
                        "donation_F_12",
                        "donation_F_13",
                        "other_expenses_F_12",
                        "other_expenses_F_13",
                        "net_profit_G_12",
                        "net_profit_G_13",
                        "income_tax_G_12",
                        "income_tax_G_13",
                        "profit_after_tax_G_12",
                        "profit_after_tax_G_13",
                        "sales_tax_H_12",
                        "sales_tax_H_13",
                        "beginning_year_HA",
                        "end_year_HB",
                        "beginning_year_HC",
                        "end_year_HD",
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
                    income_project_A_12,
                    income_project_A_13,
                    people_A_12,
                    people_A_13,
                    industries_businesses_A_12,
                    industries_businesses_A_13,
                    direct_indirect_B_12,
                    direct_indirect_B_13,
                    direct_christmas_vacation_B_12,
                    direct_christmas_vacation_B_13,
                    rent_land_building_B_12,
                    rent_land_building_B_13,
                    rent_equipment_B_12,
                    rent_equipment_B_13,
                    depreciation_B_12,
                    depreciation_B_13,
                    sales_tax_B_12,
                    sales_tax_B_13,
                    purchases_machinery_equipment_B_12,
                    purchases_machinery_equipment_B_13,
                    other_purchases_B_12,
                    other_purchases_B_13,
                    licenses_patent_B_12,
                    licenses_patent_B_13,
                    other_costs_direct_indirect_B_12,
                    other_costs_direct_indirect_B_13,
                    gross_profit_C_12,
                    gross_profit_C_13,
                    other_income_D_12,
                    other_income_D_13,
                    interest_D_12,
                    interest_D_13,
                    rent_land_building_D_12,
                    rent_land_building_D_13,
                    gain_loss_D_12,
                    gain_loss_D_13,
                    other_D_12,
                    other_D_13,
                    gross_profit_E_12,
                    gross_profit_E_13,
                    administrative_F_12,
                    administrative_F_13,
                    salaries_wages_bonus_commissions_F_12,
                    salaries_wages_bonus_commissions_F_13,
                    interest_F_12,
                    interest_F_13,
                    rent_land_building_F_12,
                    rent_land_building_F_13,
                    depreciation_F_12,
                    depreciation_F_13,
                    bad_debts_F_12,
                    bad_debts_F_13,
                    donation_F_12,
                    donation_F_13,
                    other_expenses_F_12,
                    other_expenses_F_13,
                    net_profit_G_12,
                    net_profit_G_13,
                    income_tax_G_12,
                    income_tax_G_13,
                    profit_after_tax_G_12,
                    profit_after_tax_G_13,
                    sales_tax_H_12,
                    sales_tax_H_13,
                    beginning_year_HA,
                    end_year_HB,
                    beginning_year_HC,
                    end_year_HD,
                    signature,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-230.csv",
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
                "income_project_A_12": float,
                "income_project_A_13": float,
                "people_A_12": float,
                "people_A_13": float,
                "industries_businesses_A_12": float,
                "industries_businesses_A_13": float,
                "direct_indirect_B_12": float,
                "direct_indirect_B_13": float,
                "direct_christmas_vacation_B_12": float,
                "direct_christmas_vacation_B_13": float,
                "rent_land_building_B_12": float,
                "rent_land_building_B_13": float,
                "rent_equipment_B_12": float,
                "rent_equipment_B_13": float,
                "depreciation_B_12": float,
                "depreciation_B_13": float,
                "sales_tax_B_12": float,
                "sales_tax_B_13": float,
                "purchases_machinery_equipment_B_12": float,
                "purchases_machinery_equipment_B_13": float,
                "other_purchases_B_12": float,
                "other_purchases_B_13": float,
                "licenses_patent_B_12": float,
                "licenses_patent_B_13": float,
                "other_costs_direct_indirect_B_12": float,
                "other_costs_direct_indirect_B_13": float,
                "gross_profit_C_12": float,
                "gross_profit_C_13": float,
                "other_income_D_12": float,
                "other_income_D_13": float,
                "interest_D_12": float,
                "interest_D_13": float,
                "rent_land_building_D_12": float,
                "rent_land_building_D_13": float,
                "gain_loss_D_12": float,
                "gain_loss_D_13": float,
                "other_D_12": float,
                "other_D_13": float,
                "gross_profit_E_12": float,
                "gross_profit_E_13": float,
                "administrative_F_12": float,
                "administrative_F_13": float,
                "salaries_wages_bonus_commissions_F_12": float,
                "salaries_wages_bonus_commissions_F_13": float,
                "interest_F_12": float,
                "interest_F_13": float,
                "rent_land_building_F_12": float,
                "rent_land_building_F_13": float,
                "depreciation_F_12": float,
                "depreciation_F_13": float,
                "bad_debts_F_12": float,
                "bad_debts_F_13": float,
                "donation_F_12": float,
                "donation_F_13": float,
                "other_expenses_F_12": float,
                "other_expenses_F_13": float,
                "net_profit_G_12": float,
                "net_profit_G_13": float,
                "income_tax_G_12": float,
                "income_tax_G_13": float,
                "profit_after_tax_G_12": float,
                "profit_after_tax_G_13": float,
                "sales_tax_H_12": float,
                "sales_tax_H_13": float,
                "beginning_year_HA": int,
                "end_year_HB": int,
                "beginning_year_HC": int,
                "end_year_HD": int,
                "signature": str,
                "rank": str,
            },
            table_name="IP_230",
            table_id="21",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-230.html")


def JP_560_63210(request):
    if request.method == "POST":
        # Retrieve form data
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")
        sales_1 = request.POST.get("sales_1")
        sales_2 = request.POST.get("sales_2")
        premiums_1 = request.POST.get("premiums_1")
        premiums_2 = request.POST.get("premiums_2")
        disability_A_1 = request.POST.get("disability_A_1")
        disability_A_2 = request.POST.get("disability_A_2")
        cars_A_1 = request.POST.get("cars_A_1")
        cars_A_2 = request.POST.get("cars_A_2")
        other_A_1 = request.POST.get("other_A_1")
        other_A_2 = request.POST.get("other_A_2")
        interest_received_1 = request.POST.get("interest_received_1")
        interest_received_2 = request.POST.get("interest_received_2")
        other_income_1 = request.POST.get("other_income_1")
        other_income_2 = request.POST.get("other_income_2")
        total_income_1 = request.POST.get("total_income_1")
        total_income_2 = request.POST.get("total_income_2")
        interest_paid_1 = request.POST.get("interest_paid_1")
        interest_paid_2 = request.POST.get("interest_paid_2")
        claims_paid_1 = request.POST.get("claims_paid_1")
        claims_paid_2 = request.POST.get("claims_paid_2")
        disability_B_1 = request.POST.get("disability_B_1")
        disability_B_2 = request.POST.get("disability_B_2")
        cars_B_1 = request.POST.get("cars_B_1")
        cars_B_2 = request.POST.get("cars_B_2")
        other_B_1 = request.POST.get("other_B_1")
        other_B_2 = request.POST.get("other_B_2")
        other_expenditures_1 = request.POST.get("other_expenditures_1")
        other_expenditures_2 = request.POST.get("other_expenditures_2")
        total_expenditures_1 = request.POST.get("total_expenditures_1")
        total_expenditures_2 = request.POST.get("total_expenditures_2")
        net_profit_loss_1 = request.POST.get("net_profit_loss_1")
        net_profit_loss_2 = request.POST.get("net_profit_loss_2")
        initial_inventory_1 = request.POST.get("initial_inventory_1")
        initial_inventory_2 = request.POST.get("initial_inventory_2")
        final_inventory_1 = request.POST.get("final_inventory_1")
        final_inventory_2 = request.POST.get("final_inventory_2")
        signature = request.POST.get("signature")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/JP-560-63210.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "ssn",
                        "tel",
                        "fax",
                        "sales_1",
                        "sales_2",
                        "premiums_1",
                        "premiums_2",
                        "disability_A_1",
                        "disability_A_2",
                        "cars_A_1",
                        "cars_A_2",
                        "other_A_1",
                        "other_A_2",
                        "interest_received_1",
                        "interest_received_2",
                        "other_income_1",
                        "other_income_2",
                        "total_income_1",
                        "total_income_2",
                        "interest_paid_1",
                        "interest_paid_2",
                        "claims_paid_1",
                        "claims_paid_2",
                        "disability_B_1",
                        "disability_B_2",
                        "cars_B_1",
                        "cars_B_2",
                        "other_B_1",
                        "other_B_2",
                        "other_expenditures_1",
                        "other_expenditures_2",
                        "total_expenditures_1",
                        "total_expenditures_2",
                        "net_profit_loss_1",
                        "net_profit_loss_2",
                        "initial_inventory_1",
                        "initial_inventory_2",
                        "final_inventory_1",
                        "final_inventory_2",
                        "signature",
                        "rank",
                    ]
                )

            writer.writerow(
                [
                    ssn,
                    tel,
                    fax,
                    sales_1,
                    sales_2,
                    premiums_1,
                    premiums_2,
                    disability_A_1,
                    disability_A_2,
                    cars_A_1,
                    cars_A_2,
                    other_A_1,
                    other_A_2,
                    interest_received_1,
                    interest_received_2,
                    other_income_1,
                    other_income_2,
                    total_income_1,
                    total_income_2,
                    interest_paid_1,
                    interest_paid_2,
                    claims_paid_1,
                    claims_paid_2,
                    disability_B_1,
                    disability_B_2,
                    cars_B_1,
                    cars_B_2,
                    other_B_1,
                    other_B_2,
                    other_expenditures_1,
                    other_expenditures_2,
                    total_expenditures_1,
                    total_expenditures_2,
                    net_profit_loss_1,
                    net_profit_loss_2,
                    initial_inventory_1,
                    initial_inventory_2,
                    final_inventory_1,
                    final_inventory_2,
                    signature,
                    rank,
                ]
            )

            DAO().insert_forms(
                data_path="data/cuestionarios/ingreso_neto/JP-560-63210.csv",
                dtypes={
                    "ssn": str,
                    "tel": str,
                    "fax": str,
                    "sales_1": float,
                    "sales_2": float,
                    "premiums_1": float,
                    "premiums_2": float,
                    "disability_A_1": float,
                    "disability_A_2": float,
                    "cars_A_1": float,
                    "cars_A_2": float,
                    "other_A_1": float,
                    "other_A_2": float,
                    "interest_received_1": float,
                    "interest_received_2": float,
                    "other_income_1": float,
                    "other_income_2": float,
                    "total_income_1": float,
                    "total_income_2": float,
                    "interest_paid_1": float,
                    "interest_paid_2": float,
                    "claims_paid_1": float,
                    "claims_paid_2": float,
                    "disability_B_1": float,
                    "disability_B_2": float,
                    "cars_B_1": float,
                    "cars_B_2": float,
                    "other_B_1": float,
                    "other_B_2": float,
                    "other_expenditures_1": float,
                    "other_expenditures_2": float,
                    "total_expenditures_1": float,
                    "total_expenditures_2": float,
                    "net_profit_loss_1": float,
                    "net_profit_loss_2": float,
                    "initial_inventory_1": float,
                    "initial_inventory_2": float,
                    "final_inventory_1": float,
                    "final_inventory_2": float,
                    "signature": str,
                    "rank": str,
                },
                table_name="JP_560_63210",
                table_id="23",
                debug=False,
            )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/JP-560-63210.html")


def JP_560_2(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get("company_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")
        sales_1 = request.POST.get("sales_1")
        sales_2 = request.POST.get("sales_2")
        interest_received_1 = request.POST.get("interest_received_1")
        interest_received_2 = request.POST.get("interest_received_2")
        other_income_1 = request.POST.get("other_income_1")
        other_income_2 = request.POST.get("other_income_2")
        total_income_1 = request.POST.get("total_income_1")
        total_income_2 = request.POST.get("total_income_2")
        interest_paid_1 = request.POST.get("interest_paid_1")
        interest_paid_2 = request.POST.get("interest_paid_2")
        other_expenditures_1_1 = request.POST.get("other_expenditures_1_1")
        other_expenditures_2_1 = request.POST.get("other_expenditures_1_2")
        other_expenditures_1_2 = request.POST.get("other_expenditures_2_1")
        other_expenditures_2_2 = request.POST.get("other_expenditures_2_2")
        net_profit_loss_1 = request.POST.get("net_profit_loss_1")
        net_profit_loss_2 = request.POST.get("net_profit_loss_2")
        initial_inventory_1 = request.POST.get("initial_inventory_1")
        initial_inventory_2 = request.POST.get("initial_inventory_2")
        final_inventory_1 = request.POST.get("final_inventory_1")
        final_inventory_2 = request.POST.get("final_inventory_2")
        signature = request.POST.get("signature")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/JP-560-2.csv"
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
                        "sales_1",
                        "sales_2",
                        "interest_received_1",
                        "interest_received_2",
                        "other_income_1",
                        "other_income_2",
                        "total_income_1",
                        "total_income_2",
                        "interest_paid_1",
                        "interest_paid_2",
                        "other_expenditures_1_1",
                        "other_expenditures_2_1",
                        "other_expenditures_1_2",
                        "other_expenditures_2_2",
                        "net_profit_loss_1",
                        "net_profit_loss_2",
                        "initial_inventory_1",
                        "initial_inventory_2",
                        "final_inventory_1",
                        "final_inventory_2",
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
                    sales_1,
                    sales_2,
                    interest_received_1,
                    interest_received_2,
                    other_income_1,
                    other_income_2,
                    total_income_1,
                    total_income_2,
                    interest_paid_1,
                    interest_paid_2,
                    other_expenditures_1_1,
                    other_expenditures_2_1,
                    other_expenditures_1_2,
                    other_expenditures_2_2,
                    net_profit_loss_1,
                    net_profit_loss_2,
                    initial_inventory_1,
                    initial_inventory_2,
                    final_inventory_1,
                    final_inventory_2,
                    signature,
                    rank,
                ]
            )

        return render(request, "forms/succesfull.html")

    return render(request, "forms/yearly/ingreso_neto/JP-560-2.html")


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
                        "incomes_interest_1",
                        "incomes_interest_2",
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
                "federal_recieved_amount_7":  int,
                "federal_date_receipt_7": str,
                "federal_agency_name_8": str,
                "federal_program_8": str,
                "federal_recieved_amount_8":  int,
                "federal_date_receipt_8": str,
                "local_agency_name_1": str,
                "agency_program_1": str,
                "agency_recieved_amount_1":  int,
                "agency_date_receipt_1": str,
                "local_agency_name_2": str,
                "agency_program_2": str,
                "agency_recieved_amount_2":  int,
                "agency_date_receipt_2": str,
                "local_agency_name_3": str,
                "agency_program_3": str,
                "agency_recieved_amount_3":  int,
                "agency_date_receipt_3": str,
                "local_agency_name_4": str,
                "agency_program_4": str,
                "agency_recieved_amount_4":  int,
                "agency_date_receipt_4": str,
                "local_agency_name_5": str,
                "agency_program_5": str,
                "agency_recieved_amount_5":  int,
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
