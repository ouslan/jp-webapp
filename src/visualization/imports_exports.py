import polars as pl
import plotly.express as px
from django.shortcuts import render

def web_app_imports_exports(request):
    df = pl.read_parquet("data/external/temporero.parquet")
    years = df['year'].unique().to_list()

    fig = px.pie(df, values='data', names='country')

    fig.update_traces(textposition='inside', textinfo='percent+label')

    buttons = [
        dict(
            args=[{"x": [df.filter(pl.col("year") == year)["data"].to_list()], "labels": [df.filter(pl.col("year") == year)["country"].to_list()]}],
            label=str(year),
            method="update"
        )
        for year in years
    ]

    buttons.insert(0, dict(
        args=[{"x": [df["data"].to_list()], "labels": [df["country"].to_list()]}],
        label="Annual",
        method="update"
    ))

    fig.update_layout(
        annotations=[
            dict(
                x=0.75,
                y=1.11,
                xref='paper',
                yref='paper',
                text="",
                showarrow=False,
                font=dict(
                    family='Arial',
                    size=18,
                    color='black'
                ),
                xanchor='left',
                yanchor='top'
            ),
        ],
        updatemenus=[
            dict(
                buttons=buttons,
                direction="down",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.05,
                xanchor="left",
                y=1.14,
                yanchor="top"
            ),
        ]
    )

    imports_and_exports = fig.to_html(full_html=False, default_height=500, default_width=700)

    context = {
        "imports_and_exports": imports_and_exports
    }

    return render(request, "imports_exports.html", context)
