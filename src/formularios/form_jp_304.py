from django.shortcuts import render
from src.dao.data_db_dao import DAO
import csv
import os


def JP_304(request):
    if request.method == "POST":
        # Retrieve form data
        start_month = request.POST.get("start_month")
        end_month = request.POST.get("end_month")
        year = request.POST.get("year")
        name = request.POST.get("name")
        direction = request.POST.get("direction")
        liaison_officer = request.POST.get("liaison_officer")
        title = request.POST.get("title")
        tel = request.POST.get("tel")

        nombre_agencia_federal_1 = request.POST.get("nombre_agencia_federal_1")
        catalogo_federal_1 = request.POST.get("catalogo_federal_1")
        sai_federal_1 = request.POST.get("sai_federal_1")
        titulo_federal_1 = request.POST.get("titulo_federal_1")
        aportacion_aprobada_federal_1 = request.POST.get(
            "aportacion_aprobada_federal_1"
        )
        fecha_aprobacion_federal_1 = request.POST.get("fecha_aprobacion_federal_1")
        aportacion_recibida_federal_1 = request.POST.get(
            "aportacion_recibida_federal_1"
        )
        fecha_recibo_federal_1 = request.POST.get("fecha_recibo_federal_1")
        aportacion_gastada_federal_1 = request.POST.get("aportacion_gastada_federal_1")
        fecha_gasto_federal_1 = request.POST.get("fecha_gasto_federal_1")

        nombre_agencia_federal_2 = request.POST.get("nombre_agencia_federal_2")
        catalogo_federal_2 = request.POST.get("catalogo_federal_2")
        sai_federal_2 = request.POST.get("sai_federal_2")
        titulo_federal_2 = request.POST.get("titulo_federal_2")
        aportacion_aprobada_federal_2 = request.POST.get(
            "aportacion_aprobada_federal_2"
        )
        fecha_aprobacion_federal_2 = request.POST.get("fecha_aprobacion_federal_2")
        aportacion_recibida_federal_2 = request.POST.get(
            "aportacion_recibida_federal_2"
        )
        fecha_recibo_federal_2 = request.POST.get("fecha_recibo_federal_2")
        aportacion_gastada_federal_2 = request.POST.get("aportacion_gastada_federal_2")
        fecha_gasto_federal_2 = request.POST.get("fecha_gasto_federal_2")

        nombre_agencia_federal_3 = request.POST.get("nombre_agencia_federal_3")
        catalogo_federal_3 = request.POST.get("catalogo_federal_3")
        sai_federal_3 = request.POST.get("sai_federal_3")
        titulo_federal_3 = request.POST.get("titulo_federal_3")
        aportacion_aprobada_federal_3 = request.POST.get(
            "aportacion_aprobada_federal_3"
        )
        fecha_aprobacion_federal_3 = request.POST.get("fecha_aprobacion_federal_3")
        aportacion_recibida_federal_3 = request.POST.get(
            "aportacion_recibida_federal_3"
        )
        fecha_recibo_federal_3 = request.POST.get("fecha_recibo_federal_3")
        aportacion_gastada_federal_3 = request.POST.get("aportacion_gastada_federal_3")
        fecha_gasto_federal_3 = request.POST.get("fecha_gasto_federal_3")

        nombre_agencia_federal_4 = request.POST.get("nombre_agencia_federal_4")
        catalogo_federal_4 = request.POST.get("catalogo_federal_4")
        sai_federal_4 = request.POST.get("sai_federal_4")
        titulo_federal_4 = request.POST.get("titulo_federal_4")
        aportacion_aprobada_federal_4 = request.POST.get(
            "aportacion_aprobada_federal_4"
        )
        fecha_aprobacion_federal_4 = request.POST.get("fecha_aprobacion_federal_4")
        aportacion_recibida_federal_4 = request.POST.get(
            "aportacion_recibida_federal_4"
        )
        fecha_recibo_federal_4 = request.POST.get("fecha_recibo_federal_4")
        aportacion_gastada_federal_4 = request.POST.get("aportacion_gastada_federal_4")
        fecha_gasto_federal_4 = request.POST.get("fecha_gasto_federal_4")

        nombre_agencia_federal_5 = request.POST.get("nombre_agencia_federal_5")
        catalogo_federal_5 = request.POST.get("catalogo_federal_5")
        sai_federal_5 = request.POST.get("sai_federal_5")
        titulo_federal_5 = request.POST.get("titulo_federal_5")
        aportacion_aprobada_federal_5 = request.POST.get(
            "aportacion_aprobada_federal_5"
        )
        fecha_aprobacion_federal_5 = request.POST.get("fecha_aprobacion_federal_5")
        aportacion_recibida_federal_5 = request.POST.get(
            "aportacion_recibida_federal_5"
        )
        fecha_recibo_federal_5 = request.POST.get("fecha_recibo_federal_5")
        aportacion_gastada_federal_5 = request.POST.get("aportacion_gastada_federal_5")
        fecha_gasto_federal_5 = request.POST.get("fecha_gasto_federal_5")

        agencia_local_table_box_1 = request.POST.get("agencia_local_table_box_1")
        catalogo_local_1 = request.POST.get("catalogo_local_1")
        programa_local_1 = request.POST.get("programa_local_1")
        aportacion_federal_aprobada_local_1 = request.POST.get(
            "aportacion_federal_aprobada_local_1"
        )
        fecha_aprobacion_local_1 = request.POST.get("fecha_aprobacion_local_1")
        aportacion_federal_recibida_local_1 = request.POST.get(
            "aportacion_federal_recibida_local_1"
        )
        fecha_recibo_local_1 = request.POST.get("fecha_recibo_local_1")
        aportacion_federal_gastada_local_1 = request.POST.get(
            "aportacion_federal_gastada_local_1"
        )
        fecha_gasto_local_1 = request.POST.get("fecha_gasto_local_1")
        numero_cuenta_local_1 = request.POST.get("numero_cuenta_local_1")

        agencia_local_table_box_2 = request.POST.get("agencia_local_table_box_2")
        catalogo_local_2 = request.POST.get("catalogo_local_2")
        programa_local_2 = request.POST.get("programa_local_2")
        aportacion_federal_aprobada_local_2 = request.POST.get(
            "aportacion_federal_aprobada_local_2"
        )
        fecha_aprobacion_local_2 = request.POST.get("fecha_aprobacion_local_2")
        aportacion_federal_recibida_local_2 = request.POST.get(
            "aportacion_federal_recibida_local_2"
        )
        fecha_recibo_local_2 = request.POST.get("fecha_recibo_local_2")
        aportacion_federal_gastada_local_2 = request.POST.get(
            "aportacion_federal_gastada_local_2"
        )
        fecha_gasto_local_2 = request.POST.get("fecha_gasto_local_2")
        numero_cuenta_local_2 = request.POST.get("numero_cuenta_local_2")

        agencia_local_table_box_3 = request.POST.get("agencia_local_table_box_3")
        catalogo_local_3 = request.POST.get("catalogo_local_3")
        programa_local_3 = request.POST.get("programa_local_3")
        aportacion_federal_aprobada_local_3 = request.POST.get(
            "aportacion_federal_aprobada_local_3"
        )
        fecha_aprobacion_local_3 = request.POST.get("fecha_aprobacion_local_3")
        aportacion_federal_recibida_local_3 = request.POST.get(
            "aportacion_federal_recibida_local_3"
        )
        fecha_recibo_local_3 = request.POST.get("fecha_recibo_local_3")
        aportacion_federal_gastada_local_3 = request.POST.get(
            "aportacion_federal_gastada_local_3"
        )
        fecha_gasto_local_3 = request.POST.get("fecha_gasto_local_3")
        numero_cuenta_local_3 = request.POST.get("numero_cuenta_local_3")

        agencia_local_table_box_4 = request.POST.get("agencia_local_table_box_4")
        catalogo_local_4 = request.POST.get("catalogo_local_4")
        programa_local_4 = request.POST.get("programa_local_4")
        aportacion_federal_aprobada_local_4 = request.POST.get(
            "aportacion_federal_aprobada_local_4"
        )
        fecha_aprobacion_local_4 = request.POST.get("fecha_aprobacion_local_4")
        aportacion_federal_recibida_local_4 = request.POST.get(
            "aportacion_federal_recibida_local_4"
        )
        fecha_recibo_local_4 = request.POST.get("fecha_recibo_local_4")
        aportacion_federal_gastada_local_4 = request.POST.get(
            "aportacion_federal_gastada_local_4"
        )
        fecha_gasto_local_4 = request.POST.get("fecha_gasto_local_4")
        numero_cuenta_local_4 = request.POST.get("numero_cuenta_local_4")

        agencia_local_table_box_5 = request.POST.get("agencia_local_table_box_5")
        catalogo_local_5 = request.POST.get("catalogo_local_5")
        programa_local_5 = request.POST.get("programa_local_5")
        aportacion_federal_aprobada_local_5 = request.POST.get(
            "aportacion_federal_aprobada_local_5"
        )
        fecha_aprobacion_local_5 = request.POST.get("fecha_aprobacion_local_5")
        aportacion_federal_recibida_local_5 = request.POST.get(
            "aportacion_federal_recibida_local_5"
        )
        fecha_recibo_local_5 = request.POST.get("fecha_recibo_local_5")
        aportacion_federal_gastada_local_5 = request.POST.get(
            "aportacion_federal_gastada_local_5"
        )
        fecha_gasto_local_5 = request.POST.get("fecha_gasto_local_5")
        numero_cuenta_local_5 = request.POST.get("numero_cuenta_local_5")

        csv_file_path = "data/cuestionarios/balanza_de_pagos/JP-304.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "start_month",
                        "end_month",
                        "year",
                        "name",
                        "direction",
                        "liaison_officer",
                        "title",
                        "tel",
                        "nombre_agencia_federal_1",
                        "catalogo_federal_1",
                        "sai_federal_1",
                        "titulo_federal_1",
                        "aportacion_aprobada_federal_1",
                        "fecha_aprobacion_federal_1",
                        "aportacion_recibida_federal_1",
                        "fecha_recibo_federal_1",
                        "aportacion_gastada_federal_1",
                        "fecha_gasto_federal_1",
                        "nombre_agencia_federal_2",
                        "catalogo_federal_2",
                        "sai_federal_2",
                        "titulo_federal_2",
                        "aportacion_aprobada_federal_2",
                        "fecha_aprobacion_federal_2",
                        "aportacion_recibida_federal_2",
                        "fecha_recibo_federal_2",
                        "aportacion_gastada_federal_2",
                        "fecha_gasto_federal_2",
                        "nombre_agencia_federal_3",
                        "catalogo_federal_3",
                        "sai_federal_3",
                        "titulo_federal_3",
                        "aportacion_aprobada_federal_3",
                        "fecha_aprobacion_federal_3",
                        "aportacion_recibida_federal_3",
                        "fecha_recibo_federal_3",
                        "aportacion_gastada_federal_3",
                        "fecha_gasto_federal_3",
                        "nombre_agencia_federal_4",
                        "catalogo_federal_4",
                        "sai_federal_4",
                        "titulo_federal_4",
                        "aportacion_aprobada_federal_4",
                        "fecha_aprobacion_federal_4",
                        "aportacion_recibida_federal_4",
                        "fecha_recibo_federal_4",
                        "aportacion_gastada_federal_4",
                        "fecha_gasto_federal_4",
                        "nombre_agencia_federal_5",
                        "catalogo_federal_5",
                        "sai_federal_5",
                        "titulo_federal_5",
                        "aportacion_aprobada_federal_5",
                        "fecha_aprobacion_federal_5",
                        "aportacion_recibida_federal_5",
                        "fecha_recibo_federal_5",
                        "aportacion_gastada_federal_5",
                        "fecha_gasto_federal_5",
                        "agencia_local_table_box_1",
                        "catalogo_local_1",
                        "programa_local_1",
                        "aportacion_federal_aprobada_local_1",
                        "fecha_aprobacion_local_1",
                        "aportacion_federal_recibida_local_1",
                        "fecha_recibo_local_1",
                        "aportacion_federal_gastada_local_1",
                        "fecha_gasto_local_1",
                        "numero_cuenta_local_1",
                        "agencia_local_table_box_2",
                        "catalogo_local_2",
                        "programa_local_2",
                        "aportacion_federal_aprobada_local_2",
                        "fecha_aprobacion_local_2",
                        "aportacion_federal_recibida_local_2",
                        "fecha_recibo_local_2",
                        "aportacion_federal_gastada_local_2",
                        "fecha_gasto_local_2",
                        "numero_cuenta_local_2",
                        "agencia_local_table_box_3",
                        "catalogo_local_3",
                        "programa_local_3",
                        "aportacion_federal_aprobada_local_3",
                        "fecha_aprobacion_local_3",
                        "aportacion_federal_recibida_local_3",
                        "fecha_recibo_local_3",
                        "aportacion_federal_gastada_local_3",
                        "fecha_gasto_local_3",
                        "numero_cuenta_local_3",
                        "agencia_local_table_box_4",
                        "catalogo_local_4",
                        "programa_local_4",
                        "aportacion_federal_aprobada_local_4",
                        "fecha_aprobacion_local_4",
                        "aportacion_federal_recibida_local_4",
                        "fecha_recibo_local_4",
                        "aportacion_federal_gastada_local_4",
                        "fecha_gasto_local_4",
                        "numero_cuenta_local_4",
                        "agencia_local_table_box_5",
                        "catalogo_local_5",
                        "programa_local_5",
                        "aportacion_federal_aprobada_local_5",
                        "fecha_aprobacion_local_5",
                        "aportacion_federal_recibida_local_5",
                        "fecha_recibo_local_5",
                        "aportacion_federal_gastada_local_5",
                        "fecha_gasto_local_5",
                        "numero_cuenta_local_5",
                    ]
                )

            writer.writerow(
                [
                    start_month,
                    end_month,
                    year,
                    name,
                    direction,
                    liaison_officer,
                    title,
                    tel,
                    nombre_agencia_federal_1,
                    catalogo_federal_1,
                    sai_federal_1,
                    titulo_federal_1,
                    aportacion_aprobada_federal_1,
                    fecha_aprobacion_federal_1,
                    aportacion_recibida_federal_1,
                    fecha_recibo_federal_1,
                    aportacion_gastada_federal_1,
                    fecha_gasto_federal_1,
                    nombre_agencia_federal_2,
                    catalogo_federal_2,
                    sai_federal_2,
                    titulo_federal_2,
                    aportacion_aprobada_federal_2,
                    fecha_aprobacion_federal_2,
                    aportacion_recibida_federal_2,
                    fecha_recibo_federal_2,
                    aportacion_gastada_federal_2,
                    fecha_gasto_federal_2,
                    nombre_agencia_federal_3,
                    catalogo_federal_3,
                    sai_federal_3,
                    titulo_federal_3,
                    aportacion_aprobada_federal_3,
                    fecha_aprobacion_federal_3,
                    aportacion_recibida_federal_3,
                    fecha_recibo_federal_3,
                    aportacion_gastada_federal_3,
                    fecha_gasto_federal_3,
                    nombre_agencia_federal_4,
                    catalogo_federal_4,
                    sai_federal_4,
                    titulo_federal_4,
                    aportacion_aprobada_federal_4,
                    fecha_aprobacion_federal_4,
                    aportacion_recibida_federal_4,
                    fecha_recibo_federal_4,
                    aportacion_gastada_federal_4,
                    fecha_gasto_federal_4,
                    nombre_agencia_federal_5,
                    catalogo_federal_5,
                    sai_federal_5,
                    titulo_federal_5,
                    aportacion_aprobada_federal_5,
                    fecha_aprobacion_federal_5,
                    aportacion_recibida_federal_5,
                    fecha_recibo_federal_5,
                    aportacion_gastada_federal_5,
                    fecha_gasto_federal_5,
                    agencia_local_table_box_1,
                    catalogo_local_1,
                    programa_local_1,
                    aportacion_federal_aprobada_local_1,
                    fecha_aprobacion_local_1,
                    aportacion_federal_recibida_local_1,
                    fecha_recibo_local_1,
                    aportacion_federal_gastada_local_1,
                    fecha_gasto_local_1,
                    numero_cuenta_local_1,
                    agencia_local_table_box_2,
                    catalogo_local_2,
                    programa_local_2,
                    aportacion_federal_aprobada_local_2,
                    fecha_aprobacion_local_2,
                    aportacion_federal_recibida_local_2,
                    fecha_recibo_local_2,
                    aportacion_federal_gastada_local_2,
                    fecha_gasto_local_2,
                    numero_cuenta_local_2,
                    agencia_local_table_box_3,
                    catalogo_local_3,
                    programa_local_3,
                    aportacion_federal_aprobada_local_3,
                    fecha_aprobacion_local_3,
                    aportacion_federal_recibida_local_3,
                    fecha_recibo_local_3,
                    aportacion_federal_gastada_local_3,
                    fecha_gasto_local_3,
                    numero_cuenta_local_3,
                    agencia_local_table_box_4,
                    catalogo_local_4,
                    programa_local_4,
                    aportacion_federal_aprobada_local_4,
                    fecha_aprobacion_local_4,
                    aportacion_federal_recibida_local_4,
                    fecha_recibo_local_4,
                    aportacion_federal_gastada_local_4,
                    fecha_gasto_local_4,
                    numero_cuenta_local_4,
                    agencia_local_table_box_5,
                    catalogo_local_5,
                    programa_local_5,
                    aportacion_federal_aprobada_local_5,
                    fecha_aprobacion_local_5,
                    aportacion_federal_recibida_local_5,
                    fecha_recibo_local_5,
                    aportacion_federal_gastada_local_5,
                    fecha_gasto_local_5,
                    numero_cuenta_local_5,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/balanza_de_pagos/JP-304.csv",
            dtypes={
                "start_month": str,
                "end_month": str,
                "year": int,
                "name": str,
                "direction": str,
                "liaison_officer": str,
                "title": str,
                "tel": str,
                "nombre_agencia_federal_1": str,
                "catalogo_federal_1": str,
                "sai_federal_1": str,
                "titulo_federal_1": str,
                "aportacion_aprobada_federal_1": float,
                "fecha_aprobacion_federal_1": str,
                "aportacion_recibida_federal_1": float,
                "fecha_recibo_federal_1": str,
                "aportacion_gastada_federal_1": float,
                "fecha_gasto_federal_1": str,
                "nombre_agencia_federal_2": str,
                "catalogo_federal_2": str,
                "sai_federal_2": str,
                "titulo_federal_2": str,
                "aportacion_aprobada_federal_2": float,
                "fecha_aprobacion_federal_2": str,
                "aportacion_recibida_federal_2": float,
                "fecha_recibo_federal_2": str,
                "aportacion_gastada_federal_2": float,
                "fecha_gasto_federal_2": str,
                "nombre_agencia_federal_3": str,
                "catalogo_federal_3": str,
                "sai_federal_3": str,
                "titulo_federal_3": str,
                "aportacion_aprobada_federal_3": float,
                "fecha_aprobacion_federal_3": str,
                "aportacion_recibida_federal_3": float,
                "fecha_recibo_federal_3": str,
                "aportacion_gastada_federal_3": float,
                "fecha_gasto_federal_3": str,
                "nombre_agencia_federal_4": str,
                "catalogo_federal_4": str,
                "sai_federal_4": str,
                "titulo_federal_4": str,
                "aportacion_aprobada_federal_4": float,
                "fecha_aprobacion_federal_4": str,
                "aportacion_recibida_federal_4": float,
                "fecha_recibo_federal_4": str,
                "aportacion_gastada_federal_4": float,
                "fecha_gasto_federal_4": str,
                "nombre_agencia_federal_5": str,
                "catalogo_federal_5": str,
                "sai_federal_5": str,
                "titulo_federal_5": str,
                "aportacion_aprobada_federal_5": float,
                "fecha_aprobacion_federal_5": str,
                "aportacion_recibida_federal_5": str,
                "fecha_recibo_federal_5": str,
                "aportacion_gastada_federal_5": float,
                "fecha_gasto_federal_5": str,
                "agencia_local_table_box_1": str,
                "catalogo_local_1": str,
                "programa_local_1": str,
                "aportacion_federal_aprobada_local_1": float,
                "fecha_aprobacion_local_1": str,
                "aportacion_federal_recibida_local_1": float,
                "fecha_recibo_local_1": str,
                "aportacion_federal_gastada_local_1": float,
                "fecha_gasto_local_1": str,
                "numero_cuenta_local_1": str,
                "agencia_local_table_box_2": str,
                "catalogo_local_2": str,
                "programa_local_2": str,
                "aportacion_federal_aprobada_local_2": float,
                "fecha_aprobacion_local_2": str,
                "aportacion_federal_recibida_local_2": float,
                "fecha_recibo_local_2": str,
                "aportacion_federal_gastada_local_2": float,
                "fecha_gasto_local_2": str,
                "numero_cuenta_local_2": str,
                "agencia_local_table_box_3": str,
                "catalogo_local_3": str,
                "programa_local_3": str,
                "aportacion_federal_aprobada_local_3": float,
                "fecha_aprobacion_local_3": str,
                "aportacion_federal_recibida_local_3": float,
                "fecha_recibo_local_3": str,
                "aportacion_federal_gastada_local_3": float,
                "fecha_gasto_local_3": str,
                "numero_cuenta_local_3": str,
                "agencia_local_table_box_4": str,
                "catalogo_local_4": str,
                "programa_local_4": str,
                "aportacion_federal_aprobada_local_4": float,
                "fecha_aprobacion_local_4": str,
                "aportacion_federal_recibida_local_4": float,
                "fecha_recibo_local_4": str,
                "aportacion_federal_gastada_local_4": float,
                "fecha_gasto_local_4": str,
                "numero_cuenta_local_4": str,
                "agencia_local_table_box_5": str,
                "catalogo_local_5": str,
                "programa_local_5": str,
                "aportacion_federal_aprobada_local_5": float,
                "fecha_aprobacion_local_5": str,
                "aportacion_federal_recibida_local_5": float,
                "fecha_recibo_local_5": str,
                "aportacion_federal_gastada_local_5": float,
                "fecha_gasto_local_5": str,
                "numero_cuenta_local_5": str,
            },
            table_name="JP_304",
            table_id=44,
            debug=False,
        )
        
        return render(request, "forms/succesfull.html")
    return render(request, "forms/quaterly/balanza_de_pagos/JP-304.html")