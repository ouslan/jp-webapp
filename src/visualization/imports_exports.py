from django.shortcuts import render
from env import get_db_credentials
import plotly.express as px
import pandas as pd
import requests

creds = get_db_credentials()
API_URL = creds[6]


def fetch_trade_data(agg, trade_type="country"):
    url = f"http://192.168.50.24:5551/data/trade/jp/?agg={agg}&types={trade_type}"
    response = requests.get(url).json()
    print(url)
    return pd.DataFrame(response)


def generate_pie_chart(data, value_column, name_column, title):
    fig = px.pie(data, values=value_column, names=name_column, title=title)
    fig.update_traces(textposition="inside", textinfo="percent+label")
    fig.update_layout(title={"x": 0.5, "font": {"color": "black"}})
    return fig.to_html(full_html=False, default_height=500, default_width=700)

def web_app_imports_exports(request):
    if request.method == "POST":
        frequency = request.POST.get("frequency")
        
        if frequency:
            if frequency == "Quarterly":
                frequency = "qrt"
            imports_data = fetch_trade_data(frequency.lower())
            if frequency == "qrt":
                frequency = "Quarterly"
        else:
            imports_data = fetch_trade_data("yearly")
            frequency = "Yearly"
        
        imports_chart = generate_pie_chart(imports_data, "imports", "country_name", f"{frequency}")
    else:
        imports_data = fetch_trade_data("yearly")
        imports_chart = generate_pie_chart(imports_data, "imports", "country_name", "Yearly")

    # Initialize Exports Data and Graph
    if request.method == "POST":
        frequency_2 = request.POST.get("frequency_2")
        
        if frequency_2:
            if frequency_2 == "Quarterly":
                frequency_2 = "qrt"
            exports_data = fetch_trade_data(frequency_2.lower())
            if frequency_2 == "qrt":
                frequency_2 = "Quarterly"
        else:
            exports_data = fetch_trade_data("yearly")
            frequency_2 = "Yearly"
        
        exports_chart = generate_pie_chart(exports_data, "exports", "country_name", f"{frequency_2}")
    else:
        exports_data = fetch_trade_data("yearly")
        exports_chart = generate_pie_chart(exports_data, "exports", "country_name", "Yearly")

    context = {"imports": imports_chart, "exports": exports_chart}

    return render(request, "imports_exports.html", context)
