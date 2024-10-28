from django.shortcuts import render
import pandas as pd
import requests
import plotly.express as px
import plotly.graph_objects as go
import polars as pl

def products_hts(request):
    # Default data for the graph
    url = "http://localhost:8051/data/trade/?time=yearly&types=hts&agr=false&group=false"
    r = requests.get(url).json()
    df = pd.DataFrame(r).sort_values(by="year")
    x_axis = df["year"]
    y_axis = df["qty_imports"]
    
    # Check if there's POST data to update the graph
    if request.method == "POST":
        frequency = request.POST.get("frequency")
        second_dropdown = request.POST.get("second_dropdown")
        third_dropdown = request.POST.get("third_dropdown")
        
        if frequency == "Yearly":
            url = "http://localhost:8051/data/trade/?time=yearly&types=hts&agr=false&group=false"
            y_axis = df["qty_imports"]
        elif frequency == "Monthly":
            url = "http://localhost:8051/data/trade/?time=monthly&types=hts&agr=false&group=false"
            y_axis = df.query("month == @second_dropdown and year == @third_dropdown")["qty_imports"]
        elif frequency == "Quarterly":
            url = "http://localhost:8051/data/trade/?time=qrtx&types=hts&agr=false&group=false"
            y_axis = df.query("qrt == @second_dropdown and year == @third_dropdown")["qty_imports"]
        else:
            url = "http://localhost:8051/data/trade/?time=yearly&types=hts&agr=false&group=false"
            y_axis = df["qty_imports"]

        # Get and process the data based on selected frequency
        r = requests.get(url).json()
        df = pd.DataFrame(r).sort_values(by="year")
        x_axis = df["year"] if frequency == "Yearly" else df["month"] if frequency == "Monthly" else df["qrt"]

    # Create the graph with the x and y axis
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
        margin=dict(l=0, r=0, t=0, b=0),
        plot_bgcolor='#F7F7F7',
        hovermode='x',
        showlegend=False,
        xaxis=dict(
            title="",
            color='black',
            showgrid=True,
            showticklabels=True,
            linecolor='black',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='black'
            ),
        ),
        yaxis=dict(
            title="",
            color='black',
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor='black',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='black'
            ),
        ),
        width=1380,
    )

    # Convert graph to HTML
    productos_hts__html = fig.to_html()

    # Pass the graph HTML to the context
    context = {
        "productos_hts__html": productos_hts__html,
    }
    
    return render(request, 'product_hts.html', context)
