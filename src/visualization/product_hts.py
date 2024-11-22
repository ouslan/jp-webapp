from django.shortcuts import render
import pandas as pd
import requests
import plotly.express as px
import plotly.graph_objects as go

def products_hts(request):
    # URLs for each frequency
    urls = {
        "yearly": "https://api.econlabs.net/data/trade/jp/?time=yearly&types=hts&agr=false&group=false",
        "monthly": "https://api.econlabs.net/data/trade/jp/?time=monthly&types=hts&agr=false&group=false",
        "quarterly": "https://api.econlabs.net/data/trade/jp/?time=qrt&types=hts&agr=false&group=false",
    }

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

    # Validate required columns
    required_columns = ["year", "month", "qty_imports"]
    for col in required_columns:
        if col not in df_monthly.columns:
            return render(request, 'product_hts.html', {"error": f"Missing column '{col}' in the dataset."})

    # Default data for the graph (Yearly)
    x_axis = pd.Series(df_yearly["year"])
    y_axis = pd.Series(df_yearly["qty_imports"])

    # Handle POST to change the frequency
    if request.method == "POST":
        frequency = request.POST.get("frequency")
        second_dropdown = request.POST.get("second_dropdown")
        third_dropdown = request.POST.get("third_dropdown")

        if frequency == "Monthly":
            # Filter monthly data
            df_filtered = df_monthly[
                (df_monthly["month"] == int(second_dropdown)) & (df_monthly["year"] == int(third_dropdown))
            ]

            # Validate if filtered data exists
            if not df_filtered.empty:
                x_axis = pd.Series(df_filtered["month"])
                y_axis = pd.Series(df_filtered["qty_imports"])
            else:
                x_axis = pd.Series([])
                y_axis = pd.Series([])

        elif frequency == "Quarterly":
            # Filter quarterly data
            df_filtered = df_quarterly[
                (df_quarterly["qrt"] == int(second_dropdown)) & (df_quarterly["year"] == int(third_dropdown))
            ]
            
            # Validate if filtered data exists
            if not df_filtered.empty:
                x_axis = pd.Series(df_filtered["qrt"])
                y_axis = pd.Series(df_filtered["qty_imports"])
            else:
                x_axis = pd.Series([])
                y_axis = pd.Series([])

    # Create the graph
    if x_axis.empty or y_axis.empty:
        productos_hts__html = "<p>No data available for the selected filters.</p>"
    else:
        fig = px.scatter(x=x_axis, y=y_axis)
        fig.add_trace(go.Scatter(
            x=x_axis,
            y=y_axis,
            mode='lines+markers',
            line=dict(color='#FF2525', width=3),
            marker=dict(size=4, color='#00CDFF'),
            hoverinfo='text',
        ))

        fig.update_layout(
            title="HTS Data Visualization",
            margin=dict(l=0, r=0, t=40, b=0),
            plot_bgcolor='#F7F7F7',
            hovermode='x',
            showlegend=False,
            xaxis=dict(title="Month", color='black'),
            yaxis=dict(title="Quantity Imports", color='black'),
        )

        productos_hts__html = fig.to_html()

    # Pass the graph or error message to the context
    context = {
        "productos_hts__html": productos_hts__html,
    }

    return render(request, 'product_hts.html', context)
