import polars as pl
import plotly.express as px
from django.shortcuts import render
from dotenv import load_dotenv
import requests
import pandas as pd

API_URL = "https://api.econlabs.net"

def fetch_trade_data(agg, time_start, time_end, trade_type="country"):
    url = f"{API_URL}/data/trade/jp/?agg={agg}&types={trade_type}&time={time_start}+{time_end}"
    response = requests.get(url).json()
    return pd.DataFrame(response)

def generate_pie_chart(data, value_column, name_column, title):
    fig = px.pie(data, values=value_column, names=name_column, title=title)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(title={'x': 0.5, 'font': {'color': 'black'}})
    return fig.to_html(full_html=False, default_height=500, default_width=700)

def get_time_range(frequency, year, month=None):
    if frequency == "Yearly":
        return f"{year}-01-01", f"{int(year)+1}-01-01"
    elif frequency == "Monthly" and month:
        return f"2010-01-01", f"2010-02-01"
    elif frequency == "Quarterly" and month:
        return f"{year}-{month}", f"{year}-{int(month)+3}"
    return "2009-01-01", "2010-01-01"  # Default range

def web_app_imports_exports(request):

    df1_imports = requests.get("https://api.econlabs.net/data/trade/jp/?time=yearly&types=country&agg=none&agr=false&group=false&datetime=2009").json()
    df1_imports = pd.DataFrame(df1_imports)

    # IMPORTS GRAPH 
    fig = px.pie(df1_imports, values='imports', names='country_name')
    fig.update_traces(textposition='inside', textinfo='percent+label')

    if request.method == "POST":
        imports_params = {
            "frequency": request.POST.get("frequency", frequency_defaults["frequency"]),
            "second_dropdown": request.POST.get("second_dropdown", frequency_defaults["second_dropdown"]),
            "third_dropdown": request.POST.get("third_dropdown", frequency_defaults["third_dropdown"])
        }
    else:
        imports_params = frequency_defaults

    imports_time_start, imports_time_end = get_time_range(imports_params["frequency"], imports_params["second_dropdown"], imports_params["third_dropdown"])
    
    imports_data = fetch_trade_data(
        agg=imports_params["frequency"].lower(), 
        time_start=imports_time_start,
        time_end=imports_time_end
    )
    imports_chart = generate_pie_chart(imports_data, "imports", "country_name", f"{imports_params['frequency']} / {imports_params['second_dropdown']} / {imports_params['third_dropdown']}")

    # Initialize Exports Data and Graph
    if request.method == "POST":
        frequency_2 = request.POST.get("frequency_2")
        second_dropdown_2 = request.POST.get("second_dropdown_2")
        third_dropdown_2 = request.POST.get("third_dropdown_2")
        exports_params = {
            "frequency": frequency_2 if frequency_2 else frequency_defaults["frequency"],
            "second_dropdown": second_dropdown_2 if second_dropdown_2 else frequency_defaults["second_dropdown"],
            "third_dropdown": third_dropdown_2 if third_dropdown_2 else frequency_defaults["third_dropdown"]
        }
    else:
        exports_params = frequency_defaults

    exports_time_start, exports_time_end = get_time_range(exports_params["frequency"], exports_params["second_dropdown"], exports_params["third_dropdown"])
    exports_data = fetch_trade_data(
        agg=exports_params["frequency"].lower(), 
        time_start=exports_time_start, 
        time_end=exports_time_end
    )
    exports_chart = generate_pie_chart(exports_data, "exports", "country_name", f"{exports_params['frequency']} / {exports_params['second_dropdown']}")

    context = {
        "imports": imports_chart,
        "exports": exports_chart
    }
    return render(request, "imports_exports.html", context)
