from django.shortcuts import render
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import requests

def web_app_income_employment(request):
  return render(request, "income_employment.html")