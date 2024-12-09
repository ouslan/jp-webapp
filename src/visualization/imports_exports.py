from env import get_db_credentials
from django.shortcuts import render
import plotly.express as px
import pandas as pd
import requests

API_URL = "https://api.econlabs.net"


def web_app_imports_exports(request):

    df1_imports = requests.get(f"{API_URL}/data/trade/jp/?agg=yearly&types=country&time=2009-01-01+2010-01-01").json()
    df1_imports = pd.DataFrame(df1_imports)

    # IMPORTS GRAPH 
    fig = px.pie(df1_imports, values='imports', names='country_name')
    fig.update_traces(textposition='inside', textinfo='percent+label')

    if request.method == "POST":
        frequency = request.POST.get("frequency")
        second_dropdown = request.POST.get("second_dropdown")
        third_dropdown = request.POST.get("third_dropdown")

        if frequency == "Yearly":
            df1_imports = requests.get(f"{API_URL}/data/trade/jp/?agg=yearly&types=country&time={second_dropdown}-01-01+{int(second_dropdown)+1}-01-01").json()
            fig = px.pie(df1_imports, values='imports', names='country_name')
        elif frequency == "Monthly":
            df1_imports = requests.get(f"{API_URL}/data/trade/jp/?agg=monthly&types=country&time={second_dropdown}-{third_dropdown}+{second_dropdown}-{int(third_dropdown)+1}").json()
            fig = px.pie(df1_imports, values='imports', names='country_name')
        elif frequency == "Quarterly":
            df1_imports = requests.get(f"{API_URL}/data/trade/jp/?agg=qrt&types=country&time={second_dropdown}-{third_dropdown}+{second_dropdown}-{int(third_dropdown)+3}").json()
            fig = px.pie(df1_imports, values='imports', names='country_name')

        if frequency is None and second_dropdown is None:
            frequency = "Yearly"
            second_dropdown = 2009

        if third_dropdown is None:
            fig.update_layout(
                title={
                    'text': f"Time: {frequency} / {second_dropdown}",
                    'x': 0.5,
                    'font': {'color': 'black'}
                },
            )
        else:
            fig.update_layout(
                title={
                    'text': f"Time: {frequency} / {second_dropdown} / {third_dropdown}",
                    'x': 0.5,
                    'font': {'color': 'black'}
                },
            )

    fig.update_traces(textposition='inside', textinfo='percent+label')

    imports = fig.to_html(full_html=False, default_height=500, default_width=700)

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------

    # EXPORTS GRAPH

    df1_exports = requests.get(f"{API_URL}/data/trade/jp/?agg=yearly&types=country&time=2009-01-01+2010-01-01").json()
    df1_exports = pd.DataFrame(df1_exports)

    fig1 = px.pie(df1_exports, values='exports', names='country_name')
    fig1.update_traces(textposition='inside', textinfo='percent+label')

    if request.method == "POST":
        frequency_2 = request.POST.get("frequency_2")
        second_dropdown_2 = request.POST.get("second_dropdown_2")
        third_dropdown_2 = request.POST.get("third_dropdown_2")

        if frequency_2 == "Yearly":
            df1_exports = requests.get(f"{API_URL}/data/trade/jp/?agg=yearly&types=country&time={second_dropdown_2}-01-01+{int(second_dropdown_2)+1}-01-01").json()
            fig1 = px.pie(df1_exports, values='exports', names='country_name')
        elif frequency_2 == "Monthly":
            df1_exports = requests.get(f"{API_URL}/data/trade/jp/?agg=monthly&types=country&time={second_dropdown_2}-{third_dropdown_2}+{second_dropdown_2}-{int(third_dropdown_2)+1}").json()
            fig1 = px.pie(df1_exports, values='exports', names='country_name')
        elif frequency_2 == "Quarterly":
            df1_exports = requests.get(f"{API_URL}/data/trade/jp/?agg=qrt&types=country&time={second_dropdown_2}-{third_dropdown_2}+{second_dropdown_2}-{int(third_dropdown_2)+3}").json()
            fig1 = px.pie(df1_exports, values='exports', names='country_name')

        if frequency_2 is None and second_dropdown_2 is None:
            frequency_2 = "Yearly"
            second_dropdown_2 = 2009

        if third_dropdown_2 is None:
            fig1.update_layout(
                title={
                    'text': f"Time: {frequency_2} / {second_dropdown_2}",
                    'x': 0.5,
                    'font': {'color': 'black'}
                },
            )
        else:
            fig1.update_layout(
                title={
                    'text': f"Time: {frequency_2} / {second_dropdown_2} / {third_dropdown_2}",
                    'x': 0.5,
                    'font': {'color': 'black'}
                },
            )

    fig1.update_traces(textposition='inside', textinfo='percent+label')

    exports = fig1.to_html(full_html=False, default_height=500, default_width=700)

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------

    context = {
        "imports": imports,
        "exports": exports
    }

    return render(request, "imports_exports.html", context)
