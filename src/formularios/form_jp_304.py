from django.shortcuts import render
from src.dao.data_db_dao import DAO
import polars as pl


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

        data = [
            pl.Series("start_month", [start_month], dtype=pl.String),
            pl.Series("end_month", [end_month], dtype=pl.String),
            pl.Series("year", [year], dtype=pl.String),
            pl.Series("name", [name], dtype=pl.String),
            pl.Series("direction", [direction], dtype=pl.String),
            pl.Series("liaison_officer", [liaison_officer], dtype=pl.String),
            pl.Series("title", [title], dtype=pl.String),
            pl.Series("tel", [tel], dtype=pl.String),
            pl.Series("nombre_agencia_federal_1", [nombre_agencia_federal_1], dtype=pl.String),
            pl.Series("catalogo_federal_1", [catalogo_federal_1], dtype=pl.String),
            pl.Series("sai_federal_1", [sai_federal_1], dtype=pl.String),
            pl.Series("titulo_federal_1", [titulo_federal_1], dtype=pl.String),
            pl.Series("aportacion_aprobada_federal_1", [aportacion_aprobada_federal_1], dtype=pl.String),
            pl.Series("fecha_aprobacion_federal_1", [fecha_aprobacion_federal_1], dtype=pl.String),
            pl.Series("aportacion_recibida_federal_1", [aportacion_recibida_federal_1], dtype=pl.String),
            pl.Series("fecha_recibo_federal_1", [fecha_recibo_federal_1], dtype=pl.String),
            pl.Series("aportacion_gastada_federal_1", [aportacion_gastada_federal_1], dtype=pl.String),
            pl.Series("fecha_gasto_federal_1", [fecha_gasto_federal_1], dtype=pl.String),
            pl.Series("nombre_agencia_federal_2", [nombre_agencia_federal_2], dtype=pl.String),
            pl.Series("catalogo_federal_2", [catalogo_federal_2], dtype=pl.String),
            pl.Series("sai_federal_2", [sai_federal_2], dtype=pl.String),
            pl.Series("titulo_federal_2", [titulo_federal_2], dtype=pl.String),
            pl.Series("aportacion_aprobada_federal_2", [aportacion_aprobada_federal_2], dtype=pl.String),
            pl.Series("fecha_aprobacion_federal_2", [fecha_aprobacion_federal_2], dtype=pl.String),
            pl.Series("aportacion_recibida_federal_2", [aportacion_recibida_federal_2], dtype=pl.String),
            pl.Series("fecha_recibo_federal_2", [fecha_recibo_federal_2], dtype=pl.String),
            pl.Series("aportacion_gastada_federal_2", [aportacion_gastada_federal_2], dtype=pl.String),
            pl.Series("fecha_gasto_federal_2", [fecha_gasto_federal_2], dtype=pl.String),
            pl.Series("nombre_agencia_federal_3", [nombre_agencia_federal_3], dtype=pl.String),
            pl.Series("catalogo_federal_3", [catalogo_federal_3], dtype=pl.String),
            pl.Series("sai_federal_3", [sai_federal_3], dtype=pl.String),
            pl.Series("titulo_federal_3", [titulo_federal_3], dtype=pl.String),
            pl.Series("aportacion_aprobada_federal_3", [aportacion_aprobada_federal_3], dtype=pl.String),
            pl.Series("fecha_aprobacion_federal_3", [fecha_aprobacion_federal_3], dtype=pl.String),
            pl.Series("aportacion_recibida_federal_3", [aportacion_recibida_federal_3], dtype=pl.String),
            pl.Series("fecha_recibo_federal_3", [fecha_recibo_federal_3], dtype=pl.String),
            pl.Series("aportacion_gastada_federal_3", [aportacion_gastada_federal_3], dtype=pl.String),
            pl.Series("fecha_gasto_federal_3", [fecha_gasto_federal_3], dtype=pl.String),
            pl.Series("nombre_agencia_federal_4", [nombre_agencia_federal_4], dtype=pl.String),
            pl.Series("catalogo_federal_4", [catalogo_federal_4], dtype=pl.String),
            pl.Series("sai_federal_4", [sai_federal_4], dtype=pl.String),
            pl.Series("titulo_federal_4", [titulo_federal_4], dtype=pl.String),
            pl.Series("aportacion_aprobada_federal_4", [aportacion_aprobada_federal_4], dtype=pl.String),
            pl.Series("fecha_aprobacion_federal_4", [fecha_aprobacion_federal_4], dtype=pl.String),
            pl.Series("aportacion_recibida_federal_4", [aportacion_recibida_federal_4], dtype=pl.String),
            pl.Series("fecha_recibo_federal_4", [fecha_recibo_federal_4], dtype=pl.String),
            pl.Series("aportacion_gastada_federal_4", [aportacion_gastada_federal_4], dtype=pl.String),
            pl.Series("fecha_gasto_federal_4", [fecha_gasto_federal_4], dtype=pl.String),
            pl.Series("nombre_agencia_federal_5", [nombre_agencia_federal_5], dtype=pl.String),
            pl.Series("catalogo_federal_5", [catalogo_federal_5], dtype=pl.String),
            pl.Series("sai_federal_5", [sai_federal_5], dtype=pl.String),
            pl.Series("titulo_federal_5", [titulo_federal_5], dtype=pl.String),
            pl.Series("aportacion_aprobada_federal_5", [aportacion_aprobada_federal_5], dtype=pl.String),
            pl.Series("fecha_aprobacion_federal_5", [fecha_aprobacion_federal_5], dtype=pl.String),
            pl.Series("aportacion_recibida_federal_5", [aportacion_recibida_federal_5], dtype=pl.String),
            pl.Series("fecha_recibo_federal_5", [fecha_recibo_federal_5], dtype=pl.String),
            pl.Series("aportacion_gastada_federal_5", [aportacion_gastada_federal_5], dtype=pl.String),
            pl.Series("fecha_gasto_federal_5", [fecha_gasto_federal_5], dtype=pl.String),
            pl.Series("agencia_local_table_box_1", [agencia_local_table_box_1], dtype=pl.String),
            pl.Series("catalogo_local_1", [catalogo_local_1], dtype=pl.String),
            pl.Series("programa_local_1", [programa_local_1], dtype=pl.String),
            pl.Series("aportacion_federal_aprobada_local_1", [aportacion_federal_aprobada_local_1], dtype=pl.String),
            pl.Series("fecha_aprobacion_local_1", [fecha_aprobacion_local_1], dtype=pl.String),
            pl.Series("aportacion_federal_recibida_local_1", [aportacion_federal_recibida_local_1], dtype=pl.String),
            pl.Series("fecha_recibo_local_1", [fecha_recibo_local_1], dtype=pl.String),
            pl.Series("aportacion_federal_gastada_local_1", [aportacion_federal_gastada_local_1], dtype=pl.String),
            pl.Series("fecha_gasto_local_1", [fecha_gasto_local_1], dtype=pl.String),
            pl.Series("numero_cuenta_local_1", [numero_cuenta_local_1], dtype=pl.String),
            pl.Series("agencia_local_table_box_2", [agencia_local_table_box_2], dtype=pl.String),
            pl.Series("catalogo_local_2", [catalogo_local_2], dtype=pl.String),
            pl.Series("programa_local_2", [programa_local_2], dtype=pl.String),
            pl.Series("aportacion_federal_aprobada_local_2", [aportacion_federal_aprobada_local_2], dtype=pl.String),
            pl.Series("fecha_aprobacion_local_2", [fecha_aprobacion_local_2], dtype=pl.String),
            pl.Series("aportacion_federal_recibida_local_2", [aportacion_federal_recibida_local_2], dtype=pl.String),
            pl.Series("fecha_recibo_local_2", [fecha_recibo_local_2], dtype=pl.String),
            pl.Series("aportacion_federal_gastada_local_2", [aportacion_federal_gastada_local_2], dtype=pl.String),
            pl.Series("fecha_gasto_local_2", [fecha_gasto_local_2], dtype=pl.String),
            pl.Series("numero_cuenta_local_2", [numero_cuenta_local_2], dtype=pl.String),
            pl.Series("agencia_local_table_box_3", [agencia_local_table_box_3], dtype=pl.String),
            pl.Series("catalogo_local_3", [catalogo_local_3], dtype=pl.String),
            pl.Series("programa_local_3", [programa_local_3], dtype=pl.String),
            pl.Series("aportacion_federal_aprobada_local_3", [aportacion_federal_aprobada_local_3], dtype=pl.String),
            pl.Series("fecha_aprobacion_local_3", [fecha_aprobacion_local_3], dtype=pl.String),
            pl.Series("aportacion_federal_recibida_local_3", [aportacion_federal_recibida_local_3], dtype=pl.String),
            pl.Series("fecha_recibo_local_3", [fecha_recibo_local_3], dtype=pl.String),
            pl.Series("aportacion_federal_gastada_local_3", [aportacion_federal_gastada_local_3], dtype=pl.String),
            pl.Series("fecha_gasto_local_3", [fecha_gasto_local_3], dtype=pl.String),
            pl.Series("numero_cuenta_local_3", [numero_cuenta_local_3], dtype=pl.String),
            pl.Series("agencia_local_table_box_4", [agencia_local_table_box_4], dtype=pl.String),
            pl.Series("catalogo_local_4", [catalogo_local_4], dtype=pl.String),
            pl.Series("programa_local_4", [programa_local_4], dtype=pl.String),
            pl.Series("aportacion_federal_aprobada_local_4", [aportacion_federal_aprobada_local_4], dtype=pl.String),
            pl.Series("fecha_aprobacion_local_4", [fecha_aprobacion_local_4], dtype=pl.String),
            pl.Series("aportacion_federal_recibida_local_4", [aportacion_federal_recibida_local_4], dtype=pl.String),
            pl.Series("fecha_recibo_local_4", [fecha_recibo_local_4], dtype=pl.String),
            pl.Series("aportacion_federal_gastada_local_4", [aportacion_federal_gastada_local_4], dtype=pl.String),
            pl.Series("fecha_gasto_local_4", [fecha_gasto_local_4], dtype=pl.String),
            pl.Series("numero_cuenta_local_4", [numero_cuenta_local_4], dtype=pl.String),
            pl.Series("agencia_local_table_box_5", [agencia_local_table_box_5], dtype=pl.String),
            pl.Series("catalogo_local_5", [catalogo_local_5], dtype=pl.String),
            pl.Series("programa_local_5", [programa_local_5], dtype=pl.String),
            pl.Series("aportacion_federal_aprobada_local_5", [aportacion_federal_aprobada_local_5], dtype=pl.String),
            pl.Series("fecha_aprobacion_local_5", [fecha_aprobacion_local_5], dtype=pl.String),
            pl.Series("aportacion_federal_recibida_local_5", [aportacion_federal_recibida_local_5], dtype=pl.String),
            pl.Series("fecha_recibo_local_5", [fecha_recibo_local_5], dtype=pl.String),
            pl.Series("aportacion_federal_gastada_local_5", [aportacion_federal_gastada_local_5], dtype=pl.String),
            pl.Series("fecha_gasto_local_5", [fecha_gasto_local_5], dtype=pl.String),
            pl.Series("numero_cuenta_local_5", [numero_cuenta_local_5], dtype=pl.String),
        ]
        
        df = pl.DataFrame(data)
        DAO().insert_forms(df, "JP_304", 44)
        
        return render(request, "forms/succesfull.html")
    return render(request, "forms/quaterly/balanza_de_pagos/JP-304.html")