import pandas as pd
from django.shortcuts import render

import plotly.graph_objects as go
import plotly.express as px

def salary_and_employee(request):

    context = {
      
    }
    return render(request, "salario_y_empleo.html", context)
