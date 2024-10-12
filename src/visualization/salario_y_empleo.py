from tkinter import Y
from django.shortcuts import render
import plotly.graph_objects as go
import polars as pl

def salary_and_employee(request):
    # Read the parquet file using Polars
    df = pl.read_parquet('data/processed/master_df.parquet')

    # Select only the relevant columns
    print(df.head())

    x_column = df['naics_code'].sort()
    y_columns = ['total_wages']

    # Create the graph using Plotly
    fig = go.Figure()

    for y_column in y_columns:
        fig.add_trace(go.Scatter(x=x_column, y=df[y_column], name=y_column))

    # Update the layout
    fig.update_layout(
        xaxis=dict(
            rangeslider=dict(visible=True),
            type="category"
        ),
        title="Salario y Empleo",
        xaxis_title="Fecha",
        yaxis_title=" ",
        width=1400,
        height=750
    )

    # Convert the graph to HTML
    graph_html = fig.to_html(full_html=False)

    context = {
        'graph': graph_html,
    }

    return render(request, "salario_y_empleo.html", context)