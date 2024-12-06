import plotly.graph_objects as go
import pandas as pd
import requests
from django.shortcuts import render

def productos_ranking(request):
    # URLs for each frequency
    response = requests.get("https://api.econlabs.net/data/trade/moving?agr=true").json()

    # Convert session data into DataFrames
    df = pd.DataFrame(response)
    # print(df.columns)

    # Find the last month in the DataFrame
    last_month = df['date'].max()

    # Filter the data for the last month
    df_last_month = df[df['date'] == last_month]
    # Sort the DataFrame by export and import rank, then select the top 5 items
    df_imports = df_last_month.sort_values(by="moving_import_rank")
    df_exports = df_last_month.sort_values(by="moving_export_rank")
    
    top5_imports = df_imports.head(5)
    top5_exports = df_exports.head(5)
    last5_imports = df_imports.tail(5)
    last5_exports = df_exports.tail(5)
    # print(top5_exports)
    # print(last5_exports)
    # print(top5_imports)
    # print(last5_imports)
    # Prepare data for diverging bar chart
    # For imports (negative values for bottom 5 to move them to the left)
    # last5_imports['moving_price_imports'] *= -1
    # print(last5_imports["moving_price_imports"])
    imports_data = pd.concat([last5_imports, top5_imports])

    # For exports (negative values for bottom 5 to move them to the left)
    # last5_exports['moving_price_exports'] *= -1
    # print(top5_exports["moving_price_exports"])
    exports_data = pd.concat([last5_exports, top5_exports])
    # Group by the new column and sum the qty_imports
    fig_export = go.Figure()
    fig_export.add_trace(go.Bar(
        x=exports_data['moving_price_exports'],
        y=exports_data['hs4'],
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
        x=imports_data['moving_price_imports'],
        y=imports_data['hs4'],
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