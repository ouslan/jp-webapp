from django.shortcuts import render
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import requests

def web_app_income_employment(request):
  df = pd.read_parquet("data/external/naics4_df.parquet")
  df = pd.DataFrame(df)
  
  df_sorted = df.sort_values(by=["year", "qtr"], ascending=True)
  df_sorted = df_sorted[df_sorted["year"] < 2024]
  
  
  df_filtered = df_sorted[df_sorted["first_4_naics_code"] == "9999"]
  df_filtered = df_filtered.sort_values(by=["year", "qtr"], ascending=True)
  
  x_axis = df_filtered.apply(lambda row: f"Q{row['qtr']} {row['year']}", axis=1)
  
  y_axis = df_filtered["total_employment_sum"]
  
  title = "Employment in the US by Year"
  
  naics = df_sorted.sort_values(by="first_4_naics_code")
  naics = naics[naics["first_4_naics_code"] != "0"]["first_4_naics_code"].unique()

  context = {
    'naics_code': naics,
  }
  
  fig = go.Figure()
  fig.add_trace(go.Scatter(x=x_axis, y=y_axis, mode='lines+markers'))

  fig.update_layout(title=title)
  return render(request, "income_employment.html", {'graph': fig.to_html(), **context})