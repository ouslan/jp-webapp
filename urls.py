#This file was temporarily created to generate the Altair viz graph

from django.urls import path
from .views import get_static_chart

urlpatterns = [
    path("chart/", get_static_chart, name="static_chart"),
]
