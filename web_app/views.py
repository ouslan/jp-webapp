import pandas as pd
from django.shortcuts import render
from web_app import graphics_function as gf
from plotly.subplots import make_subplots
from django.http import HttpResponse
from src.dao.data_db_dao import DAO
import plotly.express as px
from .models import *
import csv
import os
from src.visualization.indicadores import web_app_indicadores
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
from src.formularios.form_ip_530 import IP_530
from src.formularios.form_ip_520s import IP_520s
from src.formularios.form_ip_520a import IP_520a
from src.formularios.form_ip_230 import IP_230
from src.formularios.form_ip_540 import IP_540
from src.formularios.form_ip_540j import IP_540J
from src.formularios.form_jp_544_2 import JP_544_2
from src.formularios.form_ip_610 import IP_610
from src.formularios.form_ip_710 import IP_710
from src.formularios.form_ip_620 import IP_620
from src.formularios.form_ip_540p import IP_540P
from src.formularios.form_ip_540s import IP_540S
from src.formularios.form_ip_540v import IP_540v
from src.formularios.form_ip_540a import IP_540a
from src.formularios.form_ip_720 import IP_720
from src.formularios.form_ip_810 import IP_810
from src.formularios.form_jp_547 import JP_547


def home(request):
    return render(request, "home.html")

def proyecciones_poblacionales(request):
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

    proyecciones = fig.to_html()

    context = {"proyecciones": proyecciones}
    return render(request, "proyecciones.html", context)


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


def demographic_graph():
    # Read the CSV file
    df = pd.read_csv("data/external/Anual_Historico.csv")

    # Extract column names
    columns = df.columns
    
    # The new column is the x-axis
    x_column = columns[0]
    
    # The rest of the columns are y-axes
    y_columns = columns[1:]

    # Create the graph
    fig = px.line(df, x=x_column, y=y_columns, title='Gráfica Anual', width=1400, height=750)

    # Convert the figure to HTML
    demographic_graph_html = fig.to_html(full_html=False)
    return demographic_graph_html


def trimestral_demographic_graph():
    # Read the new CSV file
    df = pd.read_csv("data/external/Trimestral_Historico.csv")

    # Extract column names
    columns = df.columns
    
    # Ensure the year and quarter columns are of correct type
    year= df[columns[0]].astype(str)
    qrt = df[columns[1]].astype(str)

    # Create a new column for the formatted x-axis
    df['YearQuarter'] = year + "Q" + qrt
    
    # The new column is the x-axis
    x_column = 'YearQuarter'
    
    # The rest of the columns are y-axes
    y_columns = columns[2:]

    # Create the graph
    fig = px.line(df, x=x_column, y=y_columns, title='Gráfica Trimestral', width=1500, height=750)
    # fig.update_traces(mode='markers+lines', marker=dict(size=8, symbol='x'))
    
    # Convert the figure to HTML
    trimestral_demographic_graph_html = fig.to_html(full_html=False)
    return trimestral_demographic_graph_html

def monthly_demographic_graph():
    # Read the new CSV file
    df = pd.read_csv("data/external/Mensual_Historico.csv")

    # Extract column names
    columns = df.columns
    
    # Ensure the year and quarter columns are of correct type
    year= df[columns[0]].astype(str)
    month = df[columns[1]].astype(str)

    # Create a new column for the formatted x-axis
    df['Year/Month'] = year + "M" + month
    
    # The new column is the x-axis
    x_column = 'Year/Month'
    
    # The rest of the columns are y-axes
    y_columns = columns[2:]

    # Create the graph
    fig = px.line(df, x=x_column, y=y_columns, title='Gráfica Mensual', width=1500, height=750)
    fig.show()
    
    # Convert the figure to HTML
    monthly_demographic_graph_html = fig.to_html(full_html=False)
    return monthly_demographic_graph_html



def datos_demograficos(request):
    # Generate the annual demographic graph
    graph_html = demographic_graph()
    t_graph_html = trimestral_demographic_graph()
    m_graph_html = monthly_demographic_graph()

    context = {
        "graph": graph_html,
        "t_graph": t_graph_html,
        "m_graph": m_graph_html
    }

    return render(request, "demograficos.html", context)

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
    return web_app_indicadores(request)

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

        DAO().insert_forms(
            data_path="data/cuestionarios/balanza_de_pagos/JP-304.csv",
            dtypes={
                "start_month": str,
                "end_month": str,
                "year": int,
                "name": str,
                "direction": str,
                "liaison_officer": str,
                "title": str,
                "tel": str,
                "nombre_agencia_federal_1": str,
                "catalogo_federal_1": str,
                "sai_federal_1": str,
                "titulo_federal_1": str,
                "aportacion_aprobada_federal_1": float,
                "fecha_aprobacion_federal_1": str,
                "aportacion_recibida_federal_1": float,
                "fecha_recibo_federal_1": str,
                "aportacion_gastada_federal_1": float,
                "fecha_gasto_federal_1": str,
                "nombre_agencia_federal_2": str,
                "catalogo_federal_2": str,
                "sai_federal_2": str,
                "titulo_federal_2": str,
                "aportacion_aprobada_federal_2": float,
                "fecha_aprobacion_federal_2": str,
                "aportacion_recibida_federal_2": float,
                "fecha_recibo_federal_2": str,
                "aportacion_gastada_federal_2": float,
                "fecha_gasto_federal_2": str,
                "nombre_agencia_federal_3": str,
                "catalogo_federal_3": str,
                "sai_federal_3": str,
                "titulo_federal_3": str,
                "aportacion_aprobada_federal_3": float,
                "fecha_aprobacion_federal_3": str,
                "aportacion_recibida_federal_3": float,
                "fecha_recibo_federal_3": str,
                "aportacion_gastada_federal_3": float,
                "fecha_gasto_federal_3": str,
                "nombre_agencia_federal_4": str,
                "catalogo_federal_4": str,
                "sai_federal_4": str,
                "titulo_federal_4": str,
                "aportacion_aprobada_federal_4": float,
                "fecha_aprobacion_federal_4": str,
                "aportacion_recibida_federal_4": float,
                "fecha_recibo_federal_4": str,
                "aportacion_gastada_federal_4": float,
                "fecha_gasto_federal_4": str,
                "nombre_agencia_federal_5": str,
                "catalogo_federal_5": str,
                "sai_federal_5": str,
                "titulo_federal_5": str,
                "aportacion_aprobada_federal_5": float,
                "fecha_aprobacion_federal_5": str,
                "aportacion_recibida_federal_5": str,
                "fecha_recibo_federal_5": str,
                "aportacion_gastada_federal_5": float,
                "fecha_gasto_federal_5": str,
                "agencia_local_table_box_1": str,
                "catalogo_local_1": str,
                "programa_local_1": str,
                "aportacion_federal_aprobada_local_1": float,
                "fecha_aprobacion_local_1": str,
                "aportacion_federal_recibida_local_1": float,
                "fecha_recibo_local_1": str,
                "aportacion_federal_gastada_local_1": float,
                "fecha_gasto_local_1": str,
                "numero_cuenta_local_1": str,
                "agencia_local_table_box_2": str,
                "catalogo_local_2": str,
                "programa_local_2": str,
                "aportacion_federal_aprobada_local_2": float,
                "fecha_aprobacion_local_2": str,
                "aportacion_federal_recibida_local_2": float,
                "fecha_recibo_local_2": str,
                "aportacion_federal_gastada_local_2": float,
                "fecha_gasto_local_2": str,
                "numero_cuenta_local_2": str,
                "agencia_local_table_box_3": str,
                "catalogo_local_3": str,
                "programa_local_3": str,
                "aportacion_federal_aprobada_local_3": float,
                "fecha_aprobacion_local_3": str,
                "aportacion_federal_recibida_local_3": float,
                "fecha_recibo_local_3": str,
                "aportacion_federal_gastada_local_3": float,
                "fecha_gasto_local_3": str,
                "numero_cuenta_local_3": str,
                "agencia_local_table_box_4": str,
                "catalogo_local_4": str,
                "programa_local_4": str,
                "aportacion_federal_aprobada_local_4": float,
                "fecha_aprobacion_local_4": str,
                "aportacion_federal_recibida_local_4": float,
                "fecha_recibo_local_4": str,
                "aportacion_federal_gastada_local_4": float,
                "fecha_gasto_local_4": str,
                "numero_cuenta_local_4": str,
                "agencia_local_table_box_5": str,
                "catalogo_local_5": str,
                "programa_local_5": str,
                "aportacion_federal_aprobada_local_5": float,
                "fecha_aprobacion_local_5": str,
                "aportacion_federal_recibida_local_5": float,
                "fecha_recibo_local_5": str,
                "aportacion_federal_gastada_local_5": float,
                "fecha_gasto_local_5": str,
                "numero_cuenta_local_5": str,
            },
            table_name="JP_304",
            table_id=44,
            debug=False,
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
                        "GNMA_bonds_right",
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
                "GNMA_bonds_right": float,
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

def JP_544_1(request):
    return render(request, "forms/yearly/balanza_de_pagos/JP-544-1.html")
