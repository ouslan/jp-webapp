from calendar import month
import polars as pl
import plotly.express as px
from ..jp_imports.src.jp_imports.data_process import DataProcess
from django.shortcuts import render

def web_app_imports_exports(request):
    df1 = DataProcess(saving_dir="data/", instance="jp_instetute", debug=True).process_int_jp(time="yearly", types="country")
    df2 = DataProcess(saving_dir="data/", instance="jp_instetute", debug=True).process_int_jp(time="monthly", types="country")
    df3 = DataProcess(saving_dir="data/", instance="jp_instetute", debug=True).process_int_jp(time="qrt", types="country")
    
    df1 = df1.with_columns(data=pl.col("imports"))
    years = df1['year'].unique().to_list()
    
    df2 = df2.with_columns(data=pl.col("imports"))
    months = df2['month'].unique().to_list()
    
    df3 = df3.with_columns(data=pl.col("imports"))
    qrts = df3['qrt'].unique().to_list()

    fig = px.pie(df1, values='data', names='country')

    fig.update_traces(textposition='inside', textinfo='percent+label')
    
    frequency = ["yearly", "monthly", "qtr"]
    
    buttons = [
        dict(
            args=[{"data": [df1.to_dicts(), df2.to_dicts(), df3.to_dicts()][frequency.index(freq)], "frequency": freq}],
            label={"yearly": "Yearly", "monthly": "Monthly", "qtr": "Qtr"}[freq],
            method="update"
        ) for freq in frequency
    ]
    
    
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
