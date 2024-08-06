import pandas as pd
from django.shortcuts import render

import plotly.graph_objects as go
import plotly.express as px

def web_app_indicadores(request):
    df_monthly = pd.read_csv("data/processed/master.csv").sort_values(by="date")
    df_quarterly = pd.read_csv("data/processed/quarterly_master.csv").sort_values(by="quarter")
    df_annual = pd.read_csv("data/processed/annual_master.csv").sort_values(by="year")

    y_axis_monthly = df_monthly.columns[1:]
    y_axis_quarterly = df_quarterly.columns[1:]
    y_axis_annual = df_annual.columns[1:]

    x_axis = df_monthly["date"]
    y_axis = df_monthly[y_axis_monthly[0]]
    y_title = y_axis_monthly[0]

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
        margin=dict(l=30, r=30, t=25, b=25),
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
        width=1200,
        height=600
    )

    fig.update_layout(
        annotations=[
            dict(
                x=0.02,
                y=1.11,
                xref='paper',
                yref='paper',
                text='X:',
                showarrow=False,
                font=dict(
                    family='Arial',
                    size=18,
                    color='black'
                ),
                xanchor='left',
                yanchor='top'
            ),
            dict(
                x=0.40,
                y=1.11,
                xref='paper',
                yref='paper',
                text='Y:',
                showarrow=False,
                font=dict(
                    family='Arial',
                    size=18,
                    color='black'
                ),
                xanchor='left',
                yanchor='top'
            )
        ],
        updatemenus=[
            dict(
                buttons=[
                    dict(
                        args=[{"x": [df_monthly["date"]], "y": [df_monthly[y_axis_monthly[0]]]}],
                        label="Monthly",
                        method="update",
                        args2=[{"x": [df_quarterly["quarter"]], "y": [df_quarterly[y_axis_quarterly[0]]]}]
                    ),
                    dict(
                        args=[{"x": [df_quarterly["quarter"]], "y": [df_quarterly[y_axis_quarterly[0]]]}],
                        label="Quarterly",
                        method="update"
                    ),
                    dict(
                        args=[{"x": [df_annual["year"]], "y": [df_annual[y_axis_annual[0]]]}],
                        label="Annual",
                        method="update"
                    ),
                ],
                direction="down",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.05,
                xanchor="left",
                y=1.14,
                yanchor="top"
            ),
            dict(
                buttons=[
                    dict(
                        args=[{"y": [df_monthly[col]]}],
                        label=col,
                        method="update"
                    ) for col in y_axis_monthly
                ] + [
                    dict(
                        args=[{"y": [df_quarterly[col]]}],
                        label=col,
                        method="update"
                    ) for col in y_axis_quarterly
                ] + [
                    dict(
                        args=[{"y": [df_annual[col]]}],
                        label=col,
                        method="update"
                    ) for col in y_axis_annual
                ],
                direction="down",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.45,
                xanchor="left",
                y=1.14,
                yanchor="top"
            )
        ]
    )

    indicadores_html = fig.to_html()

    context = {
        "indicadores": indicadores_html,
    }
    return render(request, "indicadores.html", context)
