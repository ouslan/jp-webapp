from django.contrib import admin
from django.urls import path, re_path
from web_app import views

urlpatterns = [
    re_path(r"^$", views.home, name="home"),
    re_path(r"^centro-de-datos-macroeconomicos/$", views.macro, name="macro"),
    re_path(r"^ciclos-economicos/$", views.ciclos_economicos, name="ciclos_economicos"),
    re_path(r"^indicadores-mensuales/$", views.indicadores, name="indicadores"),
    re_path(r"^datos-demograficos/$", views.datos_demograficos, name="datos_demograficos"),
    re_path(r"^succesfull_page/$", views.succesfull_page, name="succesfull_page"),
    re_path(r"^JP-304-relacion-de-aportaciones-federales/$", views.JP_304, name="JP-304"),
    re_path(r"^IP-110-agricultura/$", views.IP_110, name="IP-110"),
    re_path(r"^JP-541-valor-de-la-inversion-en-obras-de-construccion/$", views.JP_541, name="JP-541"),
    re_path(r"^JP-361-transactions-in-pr-of-external-insurance-companies/$", views.JP_361, name="JP-361"),
    re_path(r"^JP-362-transacciones-con-el-exterior/$", views.JP_362, name="JP-362"),
    re_path(r"^JP-363-investment-in-securities-of-the-central-goverment/$", views.JP_363, name="JP-363"),
    re_path(r"^JP-560-63110-seguros-domesticos-de-vida/$", views.JP_560_63110, name="JP-560-63110"),
    re_path(r"^IP-210-mineria/$", views.IP_210, name="IP-210"),    
    re_path(r"^IP-220-utilidades/$", views.IP_220, name="IP-220"),
    re_path(r"^JP-560-63111/$", views.JP_560_63111, name="JP-560-63111"),
    re_path(r"^JP-364-informacion-sobre-compañias de seguros/$", views.JP_364, name="JP-364"),
    re_path(r"^JP-560-forms/$", views.JP_560, name="JP-560"),

    re_path(r"^Forms/$", views.Forms, name="Forms"),
]

