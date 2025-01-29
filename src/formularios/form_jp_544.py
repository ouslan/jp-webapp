from django.shortcuts import render
from src.dao.data_db_dao import DAO
import polars as pl


def JP_544(request):
    if request.method == "POST":
        # Retrieve form data
        agencia = request.POST.get("agencia")
        prep = request.POST.get("prep")
        titulo = request.POST.get("titulo")
        telefono = request.POST.get("telefono")
        fecha = request.POST.get("fecha")
        
        institucion1 = request.POST.get("institucion1")
        proposito1 = request.POST.get("proposito1")
        dolares1 = request.POST.get("dolares1")

        institucion2 = request.POST.get("institucion2")
        proposito2 = request.POST.get("proposito2")
        dolares2 = request.POST.get("dolares2")

        institucion3 = request.POST.get("institucion3")
        proposito3 = request.POST.get("proposito3")
        dolares3 = request.POST.get("dolares3")

        institucion4 = request.POST.get("institucion4")
        proposito4 = request.POST.get("proposito4")
        dolares4 = request.POST.get("dolares4")

        institucion5 = request.POST.get("institucion5")
        proposito5 = request.POST.get("proposito5")
        dolares5 = request.POST.get("dolares5")

        institucion6 = request.POST.get("institucion6")
        proposito6 = request.POST.get("proposito6")
        dolares6 = request.POST.get("dolares6")

        institucion7 = request.POST.get("institucion7")
        proposito7 = request.POST.get("proposito7")
        dolares7 = request.POST.get("dolares7")

        institucion8 = request.POST.get("institucion8")
        proposito8 = request.POST.get("proposito8")
        dolares8 = request.POST.get("dolares8")

        institucion9 = request.POST.get("institucion9")
        proposito9 = request.POST.get("proposito9")
        dolares9 = request.POST.get("dolares9")

        institucion10 = request.POST.get("institucion10")
        proposito10 = request.POST.get("proposito10")
        dolares10 = request.POST.get("dolares10")

        institucion11 = request.POST.get("institucion11")
        proposito11 = request.POST.get("proposito11")
        dolares11 = request.POST.get("dolares11")

        institucion12 = request.POST.get("institucion12")
        proposito12 = request.POST.get("proposito12")
        dolares12 = request.POST.get("dolares12")

        institucion13 = request.POST.get("institucion13")
        proposito13 = request.POST.get("proposito13")
        dolares13 = request.POST.get("dolares13")

        institucion14 = request.POST.get("institucion14")
        proposito14 = request.POST.get("proposito14")
        dolares14 = request.POST.get("dolares14")

        operation_expenses = request.POST.get("operation_expenses")
        salary = request.POST.get("salary")
        SS_SD_SR_beneficios_marginales = request.POST.get(
            "SS_SD_SR_beneficios_marginales"
        )
        servicios_profecionales_c = request.POST.get("servicios_profecionales_c")
        intereses = request.POST.get("intereses")
        other_gastos = request.POST.get("other_gastos")
        to_people = request.POST.get("to_people")
        servicios_profecionales_a = request.POST.get("servicios_profecionales_a")
        pension = request.POST.get("pension")
        name_other_1 = request.POST.get("name_other_1")
        quantity_other_1 = request.POST.get("quantity_other_1")
        name_other_2 = request.POST.get("name_other_2")
        quantity_other_2 = request.POST.get("quantity_other_2")
        name_other_3 = request.POST.get("name_other_3")
        quantity_other_3 = request.POST.get("quantity_other_3")
        name_other_4 = request.POST.get("name_other_4")
        quantity_other_4 = request.POST.get("quantity_other_4")

        data = [
            pl.Series("agencia", [agencia], dtype=pl.String),
            pl.Series("prep", [prep], dtype=pl.String),
            pl.Series("titulo", [titulo], dtype=pl.String),
            pl.Series("telefono", [telefono], dtype=pl.String),
            pl.Series("fecha", [fecha], dtype=pl.String),
            pl.Series("institucion1", [institucion1], dtype=pl.String),
            pl.Series("proposito1", [proposito1], dtype=pl.String),
            pl.Series("dolares1", [float(dolares1)], dtype=pl.Float64),
            pl.Series("institucion2", [institucion2], dtype=pl.String),
            pl.Series("proposito2", [proposito2], dtype=pl.String),
            pl.Series("dolares2", [float(dolares2)], dtype=pl.Float64),
            pl.Series("institucion3", [institucion3], dtype=pl.String),
            pl.Series("proposito3", [proposito3], dtype=pl.String),
            pl.Series("dolares3", [float(dolares3)], dtype=pl.Float64),
            pl.Series("institucion4", [institucion4], dtype=pl.String),
            pl.Series("proposito4", [proposito4], dtype=pl.String),
            pl.Series("dolares4", [float(dolares4)], dtype=pl.Float64),
            pl.Series("institucion5", [institucion5], dtype=pl.String),
            pl.Series("proposito5", [proposito5], dtype=pl.String),
            pl.Series("dolares5", [float(dolares5)], dtype=pl.Float64),
            pl.Series("institucion6", [institucion6], dtype=pl.String),
            pl.Series("proposito6", [proposito6], dtype=pl.String),
            pl.Series("dolares6", [float(dolares6)], dtype=pl.Float64),
            pl.Series("institucion7", [institucion7], dtype=pl.String),
            pl.Series("proposito7", [proposito7], dtype=pl.String),
            pl.Series("dolares7", [float(dolares7)], dtype=pl.Float64),
            pl.Series("institucion8", [institucion8], dtype=pl.String),
            pl.Series("proposito8", [proposito8], dtype=pl.String),
            pl.Series("dolares8", [float(dolares8)], dtype=pl.Float64),
            pl.Series("institucion9", [institucion9], dtype=pl.String),
            pl.Series("proposito9", [proposito9], dtype=pl.String),
            pl.Series("dolares9", [float(dolares9)], dtype=pl.Float64),
            pl.Series("institucion10", [institucion10], dtype=pl.String),
            pl.Series("proposito10", [proposito10], dtype=pl.String),
            pl.Series("dolares10", [float(dolares10)], dtype=pl.Float64),
            pl.Series("institucion11", [institucion11], dtype=pl.String),
            pl.Series("proposito11", [proposito11], dtype=pl.String),
            pl.Series("dolares11", [float(dolares11)], dtype=pl.Float64),
            pl.Series("institucion12", [institucion12], dtype=pl.String),
            pl.Series("proposito12", [proposito12], dtype=pl.String),
            pl.Series("dolares12", [float(dolares12)], dtype=pl.Float64),
            pl.Series("institucion13", [institucion13], dtype=pl.String),
            pl.Series("proposito13", [proposito13], dtype=pl.String),
            pl.Series("dolares13", [float(dolares13)], dtype=pl.Float64),
            pl.Series("institucion14", [institucion14], dtype=pl.String),
            pl.Series("proposito14", [proposito14], dtype=pl.String),
            pl.Series("dolares14", [float(dolares14)], dtype=pl.Float64),
            pl.Series("operation_expenses", [float(operation_expenses)], dtype=pl.Float64),
            pl.Series("salary", [float(salary)], dtype=pl.Float64),
            pl.Series("SS_SD_SR_beneficios_marginales",[float(SS_SD_SR_beneficios_marginales)],dtype=pl.Float64),
            pl.Series("servicios_profecionales_c", [float(servicios_profecionales_c)], dtype=pl.Float64),
            pl.Series("intereses", [float(intereses)], dtype=pl.Float64),
            pl.Series("other_gastos", [float(other_gastos)], dtype=pl.Float64),
            pl.Series("to_people", [float(to_people)], dtype=pl.Float64),
            pl.Series("servicios_profecionales_a", [float(servicios_profecionales_a)], dtype=pl.Float64),
            pl.Series("pension", [float(pension)], dtype=pl.Float64),
            pl.Series("name_other_1", [name_other_1], dtype=pl.String),
            pl.Series("quantity_other_1", [float(quantity_other_1)], dtype=pl.Float64),
            pl.Series("name_other_2", [name_other_2], dtype=pl.String),
            pl.Series("quantity_other_2", [float(quantity_other_2)], dtype=pl.Float64),
            pl.Series("name_other_3", [name_other_3], dtype=pl.String),
            pl.Series("quantity_other_3", [float(quantity_other_3)], dtype=pl.Float64),
            pl.Series("name_other_4", [name_other_4], dtype=pl.String),
            pl.Series("quantity_other_4", [float(quantity_other_4)], dtype=pl.Float64),
        ]
        
        df = pl.DataFrame(data)
        DAO().insert_forms(df, "JP_544", 46)

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/balanza_de_pagos/JP-544.html")
