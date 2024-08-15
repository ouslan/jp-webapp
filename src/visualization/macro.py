import pandas as pd
from django.shortcuts import render

import plotly.graph_objects as go
import plotly.express as px

def web_app_macro(request):
    df = pd.read_csv("data/processed/Series-Historicas-2001-2023_processes.csv").sort_values(by="PERIODO = AÑO FISCAL")

    y_axis_options = df.columns[1:]

    x_axis = df["PERIODO = AÑO FISCAL"]
    y_axis = df[y_axis_options[0]]

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
        width=1370
    )

    fig.update_layout(
        annotations=[
            dict(
                x=0.30,
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
                        args=[{"y": [df[col]]}],
                        label=col,
                        method="update"
                    ) for col in y_axis_options
                ],
                direction="down",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.35,
                xanchor="left",
                y=1.15,
                yanchor="top"
            )
        ]
    )

    macro_html = fig.to_html()

    context = {
        "macro": macro_html,
    }
    return render(request, "macro.html", context)
