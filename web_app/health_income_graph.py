import polars as pl
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Read the CSV file into a Polars DataFrame
df = pl.read_csv("data/processed/idh_index.csv")

# Fill missing values with 0
df_filled = df.fill_null(0)

# Convert Polars DataFrame to Pandas for Plotly compatibility
df_filled_pd = df_filled.to_pandas()

# Create figures

fig1 = go.Figure()
fig2 = go.Figure()

# Split the columns into normal and adjusted indexes
normal_columns = ['Year', 'health_index', 'income_index', 'edu_index', 'index', 'growth_rate']
adjusted_columns = ['Year', 'health_index_adjusted', 'income_index_ajusted', 'edu_index_ajusted', 'index_ajusted', 'growth_rate_ajusted']

# Add traces using data from the CSV file
traces = []

df_normal = df_filled_pd[normal_columns]
df_adjusted = df_filled_pd[adjusted_columns]

for y_column in normal_columns:
    trace = go.Scatter(x=df['Year'], y=normal_columns[1:], title='Indexes along the years')
    traces.append(trace)
    fig1.add_trace(trace)


for y_column in adjusted_columns:
    trace = go.Scatter(x=df['Year'], y=adjusted_columns[1:],  title='Adjusted Indexes along the years')
    traces.append(trace)
    fig2.add_trace(trace)

# Convert both figures to HTML
html_normal_indexes = fig1.to_html(full_html=False)
html_adjusted_indexes = fig2.to_html(full_html=False)

# Function to return the graph HTML (if needed for further web rendering)
def normal_indexes_graph():
    return html_normal_indexes

def adjusted_indexes_graph():
    return html_adjusted_indexes