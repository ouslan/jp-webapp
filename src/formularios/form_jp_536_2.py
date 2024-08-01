from django.shortcuts import render
from src.dao.data_db_dao import DAO
import csv
import os


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

        csv_file_path = "data/cuestionarios/balanza_de_pagos/JP-536-2.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "start_year",
                        "end_year",
                        "inventario1",
                        "inventario2",
                        "compras1",
                        "compras2",
                        "depre1",
                        "depre2",
                        "maquinaria1",
                        "maquinaria2",
                        "equipo1",
                        "equipo2",
                        "computadora1",
                        "computadora2",
                        "alquiler1",
                        "alquiler2",
                        "licencia1",
                        "licencia2",
                        "company_name",
                        "phone",
                        "name_title",
                        "date",
                    ]
                )

            writer.writerow(
                [
                    start_year,
                    end_year,
                    inventario1,
                    inventario2,
                    compras1,
                    compras2,
                    depre1,
                    depre2,
                    maquinaria1,
                    maquinaria2,
                    equipo1,
                    equipo2,
                    computadora1,
                    computadora2,
                    alquiler1,
                    alquiler2,
                    licencia1,
                    licencia2,
                    company_name,
                    phone,
                    name_title,
                    date,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/balanza_de_pagos/JP-536-2.csv",
            dtypes={
                "start_year": int,
                "end_year": int,
                "inventario1": float,
                "inventario2": float,
                "compras1": float,
                "compras2": float,
                "depre1": float,
                "depre2": float,
                "maquinaria1": float,
                "maquinaria2": float,
                "equipo1": float,
                "equipo2": float,
                "computadora1": float,
                "computadora2": float,
                "alquiler1": float,
                "alquiler2": float,
                "licencia1": float,
                "licencia2": float,
                "company_name": str,
                "phone": str,
                "name_title": str,
                "date": str,
            },
            table_name="JP_536_2",
            table_id="18",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/balanza_de_pagos/JP-536-2.html")

