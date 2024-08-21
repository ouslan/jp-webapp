import plotly.graph_objects as go
import pandas as pd

# Read the CSV file
df = pd.read_csv('data/external/fiscal_year_idb.csv')

# Create the Plotly table
fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='',
                align='left'),
    cells=dict(values=[df.fyear, df.population, df.births, df.deaths, df.net_migration, df.pop_change, df.pop_diff, df.error, df.percentage_error],
               fill_color='',
               align='left'))
])

table_html = fig.to_html()

def Forecast_Table():
    return table_html