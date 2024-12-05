import plotly.graph_objects as go
import pandas as pd
import requests
from django.shortcuts import render

def productos_ranking(request):
    # URLs for each frequency
    response = requests.get("https://api.econlabs.net/data/trade/moving?agr=true").json()


    # Convert session data into DataFrames
    df = pd.DataFrame(response)

    # Find the last month in the DataFrame
    last_month = df['date'].max()

# Filter the data for the last month
    df_last_month = df[df['date'] == last_month]
    # Sort the DataFrame by export and import rank, then select the top 5 items
    top_exports = df_last_month.nlargest(5, 'moving_export_rank') 
    top_imports = df_last_month.nlargest(5, 'moving_import_rank')
    bottom_exports = df_last_month.nsmallest(5, 'moving_export_rank')
    bottom_imports = df_last_month.nsmallest(5, 'moving_import_rank')

    combined_exports = pd.concat([top_exports,bottom_exports])
    combined_imports = pd.concat([top_imports, bottom_imports])

    # Group by the new column and sum the qty_imports
    fig_export = go.Figure()
    fig_export.add_trace(go.Bar(
        x=combined_exports['moving_export_rank'],
        y=combined_exports['hs4'],
        orientation="h",
        textposition='auto',
        name="Top Exports"
    ))

    fig_export.update_layout(
        title="Top 5 Items by Export Rank",
        xaxis_title="HTS Code",
        yaxis_title="Export Rank",
        bargap=0.2
    )

    # Create histogram for top 5 import ranks
    fig_import = go.Figure()
    fig_import.add_trace(go.Bar(
        x=combined_imports['moving_import_rank'],
        y=combined_imports['hs4'],
        orientation="h",
        textposition='auto',
        name="Top Imports"
    ))
    fig_import.update_layout(
        title="Top 5 Items by Import Rank",
        xaxis_title="HTS Code",
        yaxis_title="Import Rank",
        bargap=0.2
    )

    # Validate required columns
    return render(request, 'productos_ranking.html', {
        'graph_export': fig_export.to_html(),
        'graph_import': fig_import.to_html()
    })