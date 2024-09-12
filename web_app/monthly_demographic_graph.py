import polars as pl
import plotly.graph_objects as go


# Read the CSV file into a DataFrame
df = pl.read_csv("data/external/Mensual_Historico.csv")

# Print the first few rows of the DataFrame to verify
print(df.head())
print('selected_y_column' in df.columns)

# Create figure Added now
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
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        ),
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
m_graph_html = fig.to_html(full_html=False)

# Function to return the graph HTML
def monthly_demographic_graph():
    return m_graph_html
