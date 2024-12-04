import plotly.graph_objects as go
import pandas as pd
import requests
from django.shortcuts import render

def products_hts(request):
    # URLs for each frequency
    urls = {
        "yearly": "https://api.econlabs.net/data/trade/jp/?time=yearly&types=hts&agr=false&group=false",
        "monthly": "https://api.econlabs.net/data/trade/jp/?time=monthly&types=hts&agr=false&group=false",
        "quarterly": "https://api.econlabs.net/data/trade/jp/?time=qrt&types=hts&agr=false&group=false",
    }
    
    frequency = "Yearly"
    hts_code = "01"

    # Load data into the session to avoid repeated downloads
    if "yearly_data" not in request.session:
        response = requests.get(urls["yearly"]).json()
        request.session["yearly_data"] = response

    if "monthly_data" not in request.session:
        response = requests.get(urls["monthly"]).json()
        request.session["monthly_data"] = response

    if "quarterly_data" not in request.session:
        response = requests.get(urls["quarterly"]).json()
        request.session["quarterly_data"] = response

    # Convert session data into DataFrames
    df_yearly = pd.DataFrame(request.session["yearly_data"]).sort_values(by="year")
    df_monthly = pd.DataFrame(request.session["monthly_data"]).sort_values(by="year")
    df_quarterly = pd.DataFrame(request.session["quarterly_data"]).sort_values(by="year")
    
    # Create a new column for the first two digits of the hts_code
    df_yearly['hts_code_prefix'] = df_yearly['hts_code'].astype(str).str[:2]
    df_monthly['hts_code_prefix'] = df_monthly['hts_code'].astype(str).str[:2]
    df_quarterly['hts_code_prefix'] = df_quarterly['hts_code'].astype(str).str[:2]

    # Group by the new column and sum the qty_imports
    df_yearly_grouped = df_yearly.groupby(['year', 'hts_code_prefix'])['imports'].sum().reset_index()
    df_monthly_grouped = df_monthly.groupby(['month', 'hts_code_prefix'])['imports'].sum().reset_index()
    df_quarterly_grouped = df_quarterly.groupby(['qrt', 'hts_code_prefix'])['imports'].sum().reset_index()

    # Validate required columns
    required_columns = ["year", "month", "qty_imports"]
    for col in required_columns:
        if col not in df_monthly.columns:
            return render(request, 'product_hts.html', {"error": f"Missing column '{col}' in the dataset."})

    # Filter the data for the first time (Yearly with hts_code "01")
    df_filtered_yearly = df_yearly_grouped[df_yearly_grouped['hts_code_prefix'] == '01']
    x_axis = pd.Series(df_filtered_yearly["year"])
    y_axis = pd.Series(df_filtered_yearly["imports"])

    # Handle POST to change the frequency
    if request.method == "POST":
        frequency = request.POST.get("frequency")
        hts_code = request.POST.get("hts_code")

        if frequency == "Monthly":
            # Filter monthly data
            df_filtered = df_monthly_grouped[df_monthly_grouped["hts_code_prefix"] == hts_code]

            # Validate if filtered data exists
            if not df_filtered.empty:
                x_axis = pd.Series(df_filtered["month"])
                y_axis = pd.Series(df_filtered["imports"])
            else:
                x_axis = pd.Series([])
                y_axis = pd.Series([])

        elif frequency == "Quarterly":
            # Filter quarterly data
            df_filtered = df_quarterly_grouped[df_quarterly_grouped["hts_code_prefix"] == hts_code]

            # Validate if filtered data exists
            if not df_filtered.empty:
                x_axis = pd.Series(df_filtered["qrt"])
                y_axis = pd.Series(df_filtered["imports"])
            else:
                x_axis = pd.Series([])
                y_axis = pd.Series([])

        else:
            # Default to yearly data
            df_filtered_yearly = df_yearly_grouped[df_yearly_grouped['hts_code_prefix'] == hts_code]
            x_axis = pd.Series(df_filtered_yearly["year"])
            y_axis = pd.Series(df_filtered_yearly["imports"])
            
    # Add title to the graph
    title = f"Frequency: {frequency}    HTS Code: {hts_code}"

    # Create the graph with the x and y axis
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_axis, y=y_axis, mode='lines+markers'))

    fig.update_layout(title=title)

    # Render the template with the graph
    return render(request, 'product_hts.html', {'graph': fig.to_html()})
    