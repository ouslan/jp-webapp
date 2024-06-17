from django.contrib import admin
from django.urls import path, re_path
from web_app import views

urlpatterns = [
    re_path(r"^$", views.home, name="home"),
    re_path(r"^centro-de-datos-macroeconomicos/$", views.macro, name="macro"),
    re_path(r"^ciclos-economicos/$", views.ciclos_economicos, name="ciclos_economicos"),
    re_path(r"^indicadores-mensuales/$", views.indicadores, name="indicadores"),
    re_path(r"^datos-demograficos/$", views.datos_demograficos, name="datos_demograficos"),
    re_path(r"^cuestionario-relacion-de-aportaciones-federales/$", views.JP_304, name="JP-304"),
    re_path(r"^cuestionario-agricultura/$", views.IP_110, name="IP-110"),
    re_path(r"^cuestionario-construccion/$", views.JP_541, name="JP-541"),
    re_path(r"^cuestionario-servicios/$", views.JP_361, name="JP-361"),
]
