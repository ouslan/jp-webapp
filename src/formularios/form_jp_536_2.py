from django.shortcuts import render
from src.dao.data_db_dao import DAO
import polars as pl


def JP_536_2(request):
    if request.method == "POST":
        # Retrieve form data
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        inventario1 = request.POST.get("inventario1")
        inventario2 = request.POST.get("inventario2")
        compras1 = request.POST.get("compras1")
        compras2 = request.POST.get("compras2")
        depre1 = request.POST.get("depre1")
        depre2 = request.POST.get("depre2")
        maquinaria1 = request.POST.get("maquinaria1")
        maquinaria2 = request.POST.get("maquinaria2")
        equipo1 = request.POST.get("equipo1")
        equipo2 = request.POST.get("equipo2")
        computadora1 = request.POST.get("computadora1")
        computadora2 = request.POST.get("computadora2")
        alquiler1 = request.POST.get("alquiler1")
        alquiler2 = request.POST.get("alquiler2")
        licencia1 = request.POST.get("licencia1")
        licencia2 = request.POST.get("licencia2")
        company_name = request.POST.get("company_name")
        phone = request.POST.get("phone")
        name_title = request.POST.get("name_title")
        date = request.POST.get("date")

        data = [
            pl.Series("start_year", [start_year], dtype=pl.String),
            pl.Series("end_year", [end_year], dtype=pl.String),
            pl.Series("inventario1", [float(inventario1)], dtype=pl.Float64),
            pl.Series("inventario2", [float(inventario2)], dtype=pl.Float64),
            pl.Series("compras1", [float(compras1)], dtype=pl.Float64),
            pl.Series("compras2", [float(compras2)], dtype=pl.Float64),
            pl.Series("depre1", [float(depre1)], dtype=pl.Float64),
            pl.Series("depre2", [float(depre2)], dtype=pl.Float64),
            pl.Series("maquinaria1", [float(maquinaria1)], dtype=pl.Float64),
            pl.Series("maquinaria2", [float(maquinaria2)], dtype=pl.Float64),
            pl.Series("equipo1", [float(equipo1)], dtype=pl.Float64),
            pl.Series("equipo2", [float(equipo2)], dtype=pl.Float64),
            pl.Series("computadora1", [float(computadora1)], dtype=pl.Float64),
            pl.Series("computadora2", [float(computadora2)], dtype=pl.Float64),
            pl.Series("alquiler1", [float(alquiler1)], dtype=pl.Float64),
            pl.Series("alquiler2", [float(alquiler2)], dtype=pl.Float64),
            pl.Series("licencia1", [float(licencia1)], dtype=pl.Float64),
            pl.Series("licencia2", [float(licencia2)], dtype=pl.Float64),
            pl.Series("company_name", [company_name], dtype=pl.String),
            pl.Series("phone", [phone], dtype=pl.String),
            pl.Series("name_title", [name_title], dtype=pl.String),
            pl.Series("date", [date], dtype=pl.String),
        ]
        
        df = pl.DataFrame(data)
        DAO().insert_forms(df, "JP_536_2", 18)

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/balanza_de_pagos/JP-536-2.html")

