import plotly.graph_objects as go
import plotly.express as px

def graph(x_axis, y_axis, x_title, y_title):
    fig = px.scatter(
        x= x_axis,
        y= y_axis,
        labels={'x': 'Time', 'y': 'Values'},
    )

    fig.add_trace(go.Scatter(
        x= x_axis,
        y= y_axis,
        mode='lines+markers',
        name='test',
        line=dict(color='#FF2525', width=3),
        marker=dict(size=10, color='#00CDFF'),
        hoverinfo='text',
    ))

    fig.update_layout(
        margin=dict(l=0, r=1, t=25, b=0),
        plot_bgcolor='#F7F7F7',
        titlefont=dict(size=16, color='rgb(20, 24, 54)', family='Arial'),
        hovermode='x',
        
        xaxis = dict(
            title = x_title,
            color = 'black',
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
        yaxis = dict(
            title=y_title,
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
    )
    
    return fig