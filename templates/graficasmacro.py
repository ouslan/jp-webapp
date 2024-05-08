import plotly.express as px
import pandas as pd

 
 
df = pd.read_pickle("data/processed/fiscal.pkl")
df_us = df[df["country"] == "United States"]
    
fig = px.line( x= df_us['Fiscal Year'], 
        y= df_us['exports'], 
        title='US Exports Over Time', 
        labels={'x':'Fiscal Year', 'y':'Exports (USD)'}
      )
fig.update_layout(title = {'font_size' : 22, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'})
home = fig.to_html()