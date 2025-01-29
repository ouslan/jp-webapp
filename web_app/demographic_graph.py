import polars as pl
import plotly.graph_objects as go

# Read the CSV file into a DataFrame
df = pl.read_csv("data/external/Anual_Historico.csv")

# Create figure
fig = go.Figure()

# Add traces using data from the CSV file
# Top left
fig.add_trace(
    go.Scatter(x=df['x_column'], y=df['y_column1'], name="yaxis data"),
)
fig.add_trace(
    go.Scatter(x=df['x_column'], y=df['y_column2'], name="yaxis2 data"),
)

# Top right
fig.add_trace(
    go.Scatter(x=df['x_column'], y=df['y_column3'], name="yaxis3 data"),
)
fig.add_trace(
    go.Scatter(x=df['x_column'], y=df['y_column4'], name="yaxis4 data"),
)

# Bottom left
fig.add_trace(
    go.Scatter(x=df['x_column'], y=df['y_column5'], name="yaxis5 data"),
)
fig.add_trace(
    go.Scatter(x=df['x_column'], y=df['y_column6'], name="yaxis6 data"),
)

# Bottom right
fig.add_trace(
    go.Scatter(x=df['x_column'], y=df['y_column7'], name="yaxis7 data"),
)
fig.add_trace(
    go.Scatter(x=df['x_column'], y=df['y_column8'], name="yaxis8 data"),
)

# Update layout with range slider and selectors
fig.update_layout(
    xaxis=dict(
        rangeslider=dict(visible=True),
        type="date"
    ),
    title="Gráfica Anual",
    xaxis_title="Time",
    yaxis_title="Value",
    width=1400,
    height=750
)

# Add Annotations (if needed, for now static)
annotations = [
    dict(x="2022-01-01", y=100, xref="x", yref="y",
         text="Annotation Text", showarrow=True, arrowhead=1, ax=0, ay=-40)
]

# Create the button options to toggle y-columns on or off
update_menu = [
    dict(label=f"Show {y_column}",
         method="update",
         args=[{"visible": [i == idx or vis for idx, vis in enumerate([False] * len(y_columns))]},  # Make the selected trace visible
               {"title": f"Showing {y_column}"}])
    for i, y_column in enumerate(y_columns)
]

# Add a "Show All" button to display all traces
update_menu.append(
    dict(label="Show All",
         method="update",
         args=[{"visible": [True] * len(y_columns)},  # Show all traces
               {"title": "All Y-Axis Columns"}])
)

# Update layout with the updatemenus dropdown
fig.update_layout(
    updatemenus=[
        dict(
            active=0,
            buttons=update_menu,
            direction="down",
            showactive=True
        )
    ]
)

# Convert the figure to HTML
graph_html = fig.to_html(full_html=False)

# Function to return the graph HTML
def demographic_graph():
    return graph_html
