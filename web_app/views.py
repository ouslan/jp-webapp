import pandas as pd
from django.shortcuts import render
from web_app import graphics_function as gf
from plotly.subplots import make_subplots
import polars as pl
import plotly.graph_objects as go
from django.http import HttpResponse
from src.dao.data_db_dao import DAO
import plotly.express as px
from .models import *
import csv
import os
from src.visualization.indicadores import web_app_indicadores
from src.visualization.macro import web_app_macro
from src.visualization.imports_exports import web_app_imports_exports
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
from src.formularios.quaterly.form_jp_361_qrt import JP_361_qrt
from src.formularios.quaterly.form_jp_362_qtr import JP_362_qtr
from src.formularios.quaterly.form_jp_363_qtr import JP_363_qtr
from src.formularios.quaterly.form_jp_364_qtr import JP_364_qtr
from src.formularios.quaterly.form_jp_375_qtr import JP_375_qtr
from src.formularios.quaterly.form_jp_529_qtr import JP_529_qtr
from src.formularios.quaterly.form_jp_536_2_qtr import JP_536_2_qtr
from src.formularios.quaterly.form_jp_544_qtr import JP_544_qtr
from src.formularios.quaterly.ingreso_neto_qtr.form_ip_110_qtr import IP_110_qtr
from src.formularios.quaterly.ingreso_neto_qtr.form_ip_210_qtr import IP_210_qtr
from src.formularios.quaterly.ingreso_neto_qtr.form_ip_220_qtr import IP_220_qtr
from src.formularios.quaterly.ingreso_neto_qtr.form_ip_230_qtr import IP_230_qtr

def home(request):
    return render(request, "home.html")

def proyectos(request):
    return render(request, "proyectos.html")

def colaboradores(request):
    return render(request, "colaboradores.html")

def projection_annual_graph():
    # Read the CSV file
    df = pd.read_csv("data/external/yearly_idb.csv")
    
    # Extract column names
    columns = df.columns
    
    # The new column is the x-axis
    x_column = columns[0]
    
    # The rest of the columns are y-axes
    y_columns = columns[1:]
    
    # Create the graph
    fig = go.Figure()
    
    for y_column in y_columns:
        fig.add_trace(go.Scatter(x=df[x_column], y=df[y_column], name=y_column))
    
    # Update layout with range slider and selectors
    fig.update_layout(
        xaxis=dict(
            rangeslider=dict(visible=True),
            type="date"
        ),
        title="Gráfica Anual",
        xaxis_title=" ",
        yaxis_title=" ",
        width=1400,
        height=750
    )
    
    # Add Annotations (if needed, for now static)
    annotations = [
        dict(x="2022-01-01", y=100, xref="x", yref="y",
             text="Annotation Text", showarrow=True, arrowhead=1, ax=0, ay=-40)
    ]
    
    # Create the button options to toggle y-columns on or off
    update_menu = [
        dict(label=f"Show {y_column}",
             method="update",
             args=[{"visible": [i == idx or vis for idx, vis in enumerate([False] * len(y_columns))]},  # Make the selected trace visible
                   {"title": f"Showing {y_column}"}])
        for i, y_column in enumerate(y_columns)
    ]
    
    # Add a "Show All" button to display all traces
    update_menu.append(
        dict(label="Show All",
             method="update",
             args=[{"visible": [True] * len(y_columns)},  # Show all traces
                   {"title": "All Y-Axis Columns"}])
    )
    
    # Update layout with the updatemenus dropdown
    fig.update_layout(
        updatemenus=[
            dict(
                active=0,
                buttons=update_menu,
                direction="down",
                showactive=True
            )
        ]
    )
    
    # Convert the figure to HTML
    projection_annual_html = fig.to_html(full_html=False)
    
    return projection_annual_html

def projection_monthly_graph():
    # Read the CSV file
    df = pd.read_csv("data/external/monthly_idb.csv")
    
    # Extract column names
    columns = df.columns
    
    # The new column is the x-axis
    x_column = columns[0]
    
    # The rest of the columns are y-axes
    y_columns = columns[1:]
    
    # Create the graph
    fig = go.Figure()
    
    for y_column in y_columns:
        fig.add_trace(go.Scatter(x=df[x_column], y=df[y_column], name=y_column))
    
    # Update layout with range slider and selectors
    fig.update_layout(
        xaxis=dict(
            rangeslider=dict(visible=True),
            type="category"
        ),
        title="Gráfica Mensual",
        xaxis_title=" ",
        yaxis_title=" ",
        width=1400,
        height=750
    )
    
    # Add Annotations (if needed, for now static)
    annotations = [
        dict(x="2022-01-01", y=100, xref="x", yref="y",
             text="Annotation Text", showarrow=True, arrowhead=1, ax=0, ay=-40)
    ]
    
    # Create the button options to toggle y-columns on or off
    update_menu = [
        dict(label=f"Show {y_column}",
             method="update",
             args=[{"visible": [i == idx or vis for idx, vis in enumerate([False] * len(y_columns))]},  # Make the selected trace visible
                   {"title": f"Showing {y_column}"}])
        for i, y_column in enumerate(y_columns)
    ]
    
    # Add a "Show All" button to display all traces
    update_menu.append(
        dict(label="Show All",
             method="update",
             args=[{"visible": [True] * len(y_columns)},  # Show all traces
                   {"title": "All Y-Axis Columns"}])
    )
    
    # Update layout with the updatemenus dropdown
    fig.update_layout(
        updatemenus=[
            dict(
                active=0,
                buttons=update_menu,
                direction="down",
                showactive=True
            )
        ]
    )
    
    # Convert the figure to HTML
    projection_monthly_html = fig.to_html(full_html=False)
    
    return projection_monthly_html

def projection_fiscal_graph():
    # Read the CSV file
    df = pd.read_csv("data/external/fiscal_year_idb.csv")
    
    # Extract column names
    columns = df.columns
    
    # The new column is the x-axis
    x_column = columns[0]
    
    # The rest of the columns are y-axes
    y_columns = columns[1:5]
    
    # Create the graph
    fig = go.Figure()
    
    for y_column in y_columns:
        fig.add_trace(go.Scatter(x=df[x_column], y=df[y_column], name=y_column))
    
    # Update layout with range slider and selectors
    fig.update_layout(
        xaxis=dict(
            rangeslider=dict(visible=True),
            type="category"
        ),
        title="Gráfica Año Fiscal",
        xaxis_title=" ",
        yaxis_title=" ",
        width=1400,
        height=750
    )
    
    # Add Annotations (if needed, for now static)
    annotations = [
        dict(x="2022-01-01", y=100, xref="x", yref="y",
             text="Annotation Text", showarrow=True, arrowhead=1, ax=0, ay=-40)
    ]
    
    # Create the button options to toggle y-columns on or off
    update_menu = [
        dict(label=f"Show {y_column}",
             method="update",
             args=[{"visible": [i == idx or vis for idx, vis in enumerate([False] * len(y_columns))]},  # Make the selected trace visible
                   {"title": f"Showing {y_column}"}])
        for i, y_column in enumerate(y_columns)
    ]
    
    # Add a "Show All" button to display all traces
    update_menu.append(
        dict(label="Show All",
             method="update",
             args=[{"visible": [True] * len(y_columns)},  # Show all traces
                   {"title": "All Y-Axis Columns"}])
    )
    
    # Update layout with the updatemenus dropdown
    fig.update_layout(
        updatemenus=[
            dict(
                active=0,
                buttons=update_menu,
                direction="down",
                showactive=True
            )
        ]
    )
    
    # Convert the figure to HTML
    projection_fiscal_html = fig.to_html(full_html=False)
    
    return projection_fiscal_html

def projection_quarter_graph():
    # Read the CSV file
    df = pd.read_csv("data/external/quarterly_idb.csv")
    
    # Extract column names
    columns = df.columns
    
    # The new column is the x-axis
    x_column = columns[0]
    
    # The rest of the columns are y-axes
    y_columns = columns[1:]
    
    # Create the graph
    fig = go.Figure()
    
    for y_column in y_columns:
        fig.add_trace(go.Scatter(x=df[x_column], y=df[y_column], name=y_column))
    
    # Update layout with range slider and selectors
    fig.update_layout(
        xaxis=dict(
            rangeslider=dict(visible=True),
            type="category"
        ),
        title="Gráfica Trimestral",
        xaxis_title=" ",
        yaxis_title=" ",
        width=1400,
        height=750
    )
    
    # Add Annotations (if needed, for now static)
    # annotations = [
    #     dict(x="2022-01-01", y=100, xref="x", yref="y",
    #          text="Annotation Text", showarrow=True, arrowhead=1, ax=0, ay=-40)
    # ]
    
    # Create the button options to toggle y-columns on or off
    update_menu = [
        dict(label=f"Show {y_column}",
             method="update",
             args=[{"visible": [i == idx or vis for idx, vis in enumerate([False] * len(y_columns))]},  # Make the selected trace visible
                   {"title": f"Showing {y_column}"}])
        for i, y_column in enumerate(y_columns)
    ]
    
    # Add a "Show All" button to display all traces
    update_menu.append(
        dict(label="Show All",
             method="update",
             args=[{"visible": [True] * len(y_columns)},  # Show all traces
                   {"title": "All Y-Axis Columns"}])
    )
    
    # Update layout with the updatemenus dropdown
    fig.update_layout(
        updatemenus=[
            dict(
                active=0,
                buttons=update_menu,
                direction="down",
                showactive=True
            )
        ]
    )
    
    # Convert the figure to HTML
    projection_quarter_html = fig.to_html(full_html=False)
    
    return projection_quarter_html

def proyecciones_poblacionales(request):

    d_table = demographic_table(request)
    annual_graph = projection_annual_graph()
    monthly_graph = projection_monthly_graph()
    fiscal_graph = projection_fiscal_graph()
    quarter_graph = projection_quarter_graph()

    context = {
        "d_table": d_table,
        "annual_graph": annual_graph,
        "monthly_graph": monthly_graph,
        "fiscal_graph": fiscal_graph,
        "quarter_graph": quarter_graph
        }
    
    return render(request, "proyecciones.html", context)

def macro(request):
    return web_app_macro(request)
  
def imports_and_exports(request):
    return web_app_imports_exports(request)

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
    fig = go.Figure()
    
    for y_column in y_columns:
        fig.add_trace(go.Scatter(x=df[x_column], y=df[y_column], name=y_column))
    
    # Update layout with range slider and selectors
    fig.update_layout(
        xaxis=dict(
            rangeslider=dict(visible=True),
            type="date"
        ),
        title="Gráfica Anual",
        xaxis_title="Demográfico",
        yaxis_title=" ",
        width=1400,
        height=750
    )
    
    # Add Annotations (if needed, for now static)
    annotations = [
        dict(x="2022-01-01", y=100, xref="x", yref="y",
             text="Annotation Text", showarrow=True, arrowhead=1, ax=0, ay=-40)
    ]
    
    # Create the button options to toggle y-columns on or off
    update_menu = [
        dict(label=f"Show {y_column}",
             method="update",
             args=[{"visible": [i == idx or vis for idx, vis in enumerate([False] * len(y_columns))]},  # Make the selected trace visible
                   {"title": f"Showing {y_column}"}])
        for i, y_column in enumerate(y_columns)
    ]
    
    # Add a "Show All" button to display all traces
    update_menu.append(
        dict(label="Show All",
             method="update",
             args=[{"visible": [True] * len(y_columns)},  # Show all traces
                   {"title": "All Y-Axis Columns"}])
    )
    
    # Update layout with the updatemenus dropdown
    fig.update_layout(
        updatemenus=[
            dict(
                active=0,
                buttons=update_menu,
                direction="down",
                showactive=True
            )
        ]
    )
    
    # Convert the figure to HTML
    demographic_graph_html = fig.to_html(full_html=False)
    
    return demographic_graph_html


def trimestral_demographic_graph(selected_graph=1):
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

    # Create figure
    fig = go.Figure()

    # Add traces for each y-axis column
    for i, y_column in enumerate(y_columns):
        fig.add_trace(go.Scatter(x=df[x_column], y=df[y_column], name=y_column))

    # Create dropdown menu options to toggle traces on or off
    update_menu = [
        dict(label=f"Show {y_column}",
             method="update",
             args=[{"visible": [i == idx or False for idx in range(len(y_columns))]},  # Make the selected trace visible
                   {"title": f"Showing {y_column}"}])
        for i, y_column in enumerate(y_columns)
    ]

    # Add a "Show All" button to display all traces
    update_menu.append(
        dict(label="Show All",
             method="update",
             args=[{"visible": [True] * len(y_columns)},  # Show all traces
                   {"title": "All Y-Axis Columns"}])
    )

    # Update layout with the updatemenus dropdown and range slider
    fig.update_layout(
        updatemenus=[
            dict(
                buttons=update_menu,
                direction="down",
                showactive=True
            )
        ],
        xaxis=dict(
            rangeslider=dict(visible=True),
            type="category"  # Use "category" type for year-quarter format
        ),
        title="Gráfica Trimestral",
        xaxis_title="Trimestre",
        yaxis_title=" ",
        width=1500,
        height=750
    )

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

    # Create figure
    fig = go.Figure()

    # Add traces for each y-axis column
    for i, y_column in enumerate(y_columns):
        fig.add_trace(go.Scatter(x=df[x_column], y=df[y_column], name=y_column))

    # Create dropdown menu options to toggle traces on or off
    update_menu = [
        dict(label=f"Show {y_column}",
             method="update",
             args=[{"visible": [i == idx or False for idx in range(len(y_columns))]},  # Make the selected trace visible
                   {"title": f"Showing {y_column}"}])
        for i, y_column in enumerate(y_columns)
    ]

    # Add a "Show All" button to display all traces
    update_menu.append(
        dict(label="Show All",
             method="update",
             args=[{"visible": [True] * len(y_columns)},  # Show all traces
                   {"title": "All Y-Axis Columns"}])
    )

    # Update layout with the updatemenus dropdown and range slider
    fig.update_layout(
        updatemenus=[
            dict(
                buttons=update_menu,
                direction="down",
                showactive=True
            )
        ],
        xaxis=dict(
            rangeslider=dict(visible=True),
            type="category"  # Use "category" type for year-quarter format
        ),
        title="Gráfica Trimestral",
        xaxis_title="Mensual",
        yaxis_title=" ",
        width=1500,
        height=750
    )
    
    # Convert the figure to HTML
    monthly_demographic_graph_html = fig.to_html(full_html=False)
    return monthly_demographic_graph_html

def indice_desarrollo_humano(request):
    return render(request, "indice_desarrollo_humano.html")

def demographic_table(request):
    df = pd.read_parquet("data/processed/fiscal_year_idb.parquet")
    demographic_table = df.to_html(index=False, classes='table table-striped')
    return demographic_table

def datos_demograficos(request):
    # Generate the annual demographic graph
    graph_html = demographic_graph()
    t_graph_html = trimestral_demographic_graph()
    m_graph_html = monthly_demographic_graph()
    d_table = demographic_table(request)

    context = {
        "graph": graph_html,
        "t_graph": t_graph_html,
        "m_graph": m_graph_html,
        "d_table": d_table
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

def succesfull_page(request):
    return render(request, "forms/succesfull.html")

def Forms(request):
    return render(request, "forms/forms.html")

def JP_544_1(request):
    return render(request, "forms/yearly/balanza_de_pagos/JP-544-1.html")
