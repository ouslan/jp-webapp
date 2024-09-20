import polars as pl
import plotly.graph_objects as go

# Read the CSV file into a DataFrame
df = pl.read_csv("data/external/Trimestral_Historico.csv")

# Convert Polars DataFrame to a Pandas DataFrame for Plotly compatibility
df = df.to_pandas()

# Create figure
fig = go.Figure()

# Add traces using data from the CSV file
traces = []
y_columns = df.columns[1:]  # Assuming the first column is the x-axis and the rest are y-axes

for i, y_column in enumerate(y_columns):
    trace = go.Scatter(x=df['x_column'], y=df[y_column], name=y_column)
    traces.append(trace)
    fig.add_trace(trace)

# Create dropdown menu options to toggle traces on or off
update_menu = [
    dict(label=f"Show {y_column}",
         method="update",
         args=[{"visible": [i == idx or False for idx in range(len(y_columns))]},
               {"title": f"Showing {y_column}"}])
    for i, y_column in enumerate(y_columns)
]

# Add a "Show All" button to display all traces
update_menu.append(
    dict(label="Show All",
         method="update",
         args=[{"visible": [True] * len(y_columns)},
               {"title": "All Y-Axis Columns"}])
)

# Update layout with the updatemenus dropdown
fig.update_layout(
    updatemenus=[
        dict(
            buttons=update_menu,
            direction="down",
            showactive=True
        )
    ],
    xaxis=dict(
        rangeslider=dict(visible=True),
        type="date"
    ),
    title="Demographic Graph",
    xaxis_title="Time",
    yaxis_title="Value",
    width=800,
    height=800
)

# Convert the figure to HTML
t_graph_html = fig.to_html(full_html=False)

# Function to return the graph HTML
def trimestral_demographic_graph():
    return t_graph_html
