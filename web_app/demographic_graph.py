import polars as pl
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# Read the CSV file into a DataFrame
df = pl.read_csv("data/external/Anual_Historico.csv")

# Print the first few rows of the DataFrame to verify
print(df.head())
print('selected_y_column' in df.columns)

# Create subplots with secondary y-axes
fig = make_subplots(rows=2, cols=2, specs=[[{"secondary_y": True}, {"secondary_y": True}], [{"secondary_y": True}, {"secondary_y": True}]])

# Add traces using data from the CSV file
# Top left
fig.add_trace(
    go.Scatter(x=df['x_column'], y=df['y_column1'], name="yaxis data"),
    row=1, col=1, secondary_y=False)
fig.add_trace(
    go.Scatter(x=df['x_column'], y=df['y_column2'], name="yaxis2 data"),
    row=1, col=1, secondary_y=True)

# Top right
fig.add_trace(
    go.Scatter(x=df['x_column'], y=df['y_column3'], name="yaxis3 data"),
    row=1, col=2, secondary_y=False)
fig.add_trace(
    go.Scatter(x=df['x_column'], y=df['y_column4'], name="yaxis4 data"),
    row=1, col=2, secondary_y=True)

# Bottom left
fig.add_trace(
    go.Scatter(x=df['x_column'], y=df['y_column5'], name="yaxis5 data"),
    row=2, col=1, secondary_y=False)
fig.add_trace(
    go.Scatter(x=df['x_column'], y=df['y_column6'], name="yaxis6 data"),
    row=2, col=1, secondary_y=True)

# Bottom right
fig.add_trace(
    go.Scatter(x=df['x_column'], y=df['y_column7'], name="yaxis7 data"),
    row=2, col=2, secondary_y=False)
fig.add_trace(
    go.Scatter(x=df['x_column'], y=df['y_column8'], name="yaxis8 data"),
    row=2, col=2, secondary_y=True)

# Update the y-axis based on user selection
def update_y_axis(selected_y_column):
    y_data = df[selected_y_column]
    fig.data[0].y = y_data
    fig.data[0].name = selected_y_column

# Call the update_y_axis function with the user's selected y column
update_y_axis('selected_y_column')

# Customize layout to make the graph less wide
fig.update_layout(
    title='Demographic Graph',
    xaxis_title='Time',
    yaxis_title='Value',
    width = 800,
    height = 800
)

# Convert the figure to HTML
graph_html = fig.to_html(full_html=False)

# Function to return the graph HTML
def demographic_graph():
    return graph_html
