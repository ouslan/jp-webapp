import re
import pandas as pd
from django.shortcuts import render

import plotly.graph_objects as go
import plotly.express as px

def web_app_imports_exports(request):
  return render(request, "imports_exports.html")