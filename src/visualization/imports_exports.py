import polars as pl
import plotly.graph_objects as go
import plotly.express as px
from django.shortcuts import render

def web_app_imports_exports(request):
  data = dict(
    character=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parent=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    value=[10, 14, 12, 10, 2, 6, 6, 4, 4])

  fig = px.sunburst(
      data,
      names='character',
      parents='parent',
      values='value',
  )
  imports_and_exports = fig.to_html(full_html=False, default_height=500, default_width=700)
  
  context = {
    "imports_and_exports": imports_and_exports
  }
  return render(request, "imports_exports.html", context)