from django.shortcuts import render
from src.dao.data_db_dao import DAO
import polars as pl

def cuestionario_viajero_salida(request):
  return render(request, 'cuestionario_salida.html')