from django.shortcuts import render
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import requests

def web_app_indicadores(request):
    df_monthly = pd.read_parquet("data/processed/indicadores_economicos.parquet").sort_values(by="date").reset_index()
    df_quarterly = pd.read_parquet("data/processed/indicadores_trimestrales.parquet").sort_values(by="quarter").reset_index()
    df_annual = pd.read_parquet("data/processed/indicadores_anuales.parquet").sort_values(by="year").reset_index()

    df_monthly["date"] = df_monthly["date"].astype(str)
    df_quarterly["quarter"] = df_quarterly["quarter"].astype(str)
    df_annual["year"] = df_annual["year"].astype(str)

    y_axis_options = df_monthly.columns[2:].sort_values()

    x_axis = df_monthly["date"]
    y_axis = df_monthly[y_axis_options[0]]

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
                        args=[{"x": [df_monthly["date"]], "y": [df_monthly[y_axis_options[0]]]}],
                        label="Monthly",
                        method="update",
                        args2=[{"x": [df_quarterly["quarter"]], "y": [df_quarterly[y_axis_options[0]]]}]
                    ),
                    dict(
                        args=[{"x": [df_quarterly["quarter"]], "y": [df_quarterly[y_axis_options[0]]]}],
                        label="Quarterly",
                        method="update"
                    ),
                    dict(
                        args=[{"x": [df_annual["year"]], "y": [df_annual[y_axis_options[0]]]}],
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
                        label=str(col).replace("_", " ").title(),
                        method="update"
                    ) for col in y_axis_options
                ] + [
                    dict(
                        args=[{"y": [df_quarterly[col]]}],
                        label=str(col).replace("_", " ").title(),
                        method="update"
                    ) for col in y_axis_options
                ] + [
                    dict(
                        args=[{"y": [df_annual[col]]}],
                        label=str(col).replace("_", " ").title(),
                        method="update"
                    ) for col in y_axis_options
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
