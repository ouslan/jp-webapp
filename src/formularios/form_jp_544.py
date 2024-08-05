from django.shortcuts import render
from src.dao.data_db_dao import DAO
import csv
import os


def JP_544(request):
    if request.method == "POST":
        # Retrieve form data
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
        agencia = request.POST.get("agencia")
        prep = request.POST.get("prep")
        titulo = request.POST.get("titulo")
        telefono = request.POST.get("telefono")
        fecha = request.POST.get("fecha")

        csv_file_path = "data/cuestionarios/balanza_de_pagos/JP-544.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "institucion1",
                        "proposito1",
                        "dolares1",
                        "institucion2",
                        "proposito2",
                        "dolares2",
                        "institucion3",
                        "proposito3",
                        "dolares3",
                        "institucion4",
                        "proposito4",
                        "dolares4",
                        "institucion5",
                        "proposito5",
                        "dolares5",
                        "institucion6",
                        "proposito6",
                        "dolares6",
                        "institucion7",
                        "proposito7",
                        "dolares7",
                        "institucion8",
                        "proposito8",
                        "dolares8",
                        "institucion9",
                        "proposito9",
                        "dolares9",
                        "institucion10",
                        "proposito10",
                        "dolares10",
                        "institucion11",
                        "proposito11",
                        "dolares11",
                        "institucion12",
                        "proposito12",
                        "dolares12",
                        "institucion13",
                        "proposito13",
                        "dolares13",
                        "institucion14",
                        "proposito14",
                        "dolares14",
                        "operation_expenses",
                        "salary",
                        "SS_SD_SR_beneficios_marginales",
                        "servicios_profecionales_c",
                        "intereses",
                        "other_gastos",
                        "to_people",
                        "servicios_profecionales_a",
                        "pension",
                        "name_other_1",
                        "quantity_other_1",
                        "name_other_2",
                        "quantity_other_2",
                        "name_other_3",
                        "quantity_other_3",
                        "name_other_4",
                        "quantity_other_4",
                        "agencia",
                        "prep",
                        "titulo",
                        "telefono",
                        "fecha",
                    ]
                )

            writer.writerow(
                [
                    institucion1,
                    proposito1,
                    dolares1,
                    institucion2,
                    proposito2,
                    dolares2,
                    institucion3,
                    proposito3,
                    dolares3,
                    institucion4,
                    proposito4,
                    dolares4,
                    institucion5,
                    proposito5,
                    dolares5,
                    institucion6,
                    proposito6,
                    dolares6,
                    institucion7,
                    proposito7,
                    dolares7,
                    institucion8,
                    proposito8,
                    dolares8,
                    institucion9,
                    proposito9,
                    dolares9,
                    institucion10,
                    proposito10,
                    dolares10,
                    institucion11,
                    proposito11,
                    dolares11,
                    institucion12,
                    proposito12,
                    dolares12,
                    institucion13,
                    proposito13,
                    dolares13,
                    institucion14,
                    proposito14,
                    dolares14,
                    operation_expenses,
                    salary,
                    SS_SD_SR_beneficios_marginales,
                    servicios_profecionales_c,
                    intereses,
                    other_gastos,
                    to_people,
                    servicios_profecionales_a,
                    pension,
                    name_other_1,
                    quantity_other_1,
                    name_other_2,
                    quantity_other_2,
                    name_other_3,
                    quantity_other_3,
                    name_other_4,
                    quantity_other_4,
                    agencia,
                    prep,
                    titulo,
                    telefono,
                    fecha,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/balanza_de_pagos/JP-544.csv",
            dtypes={
                "institucion1": str,
                "proposito1": str,
                "dolares1": float,
                "institucion2": str,
                "proposito2": str,
                "dolares2": float,
                "institucion3": str,
                "proposito3": str,
                "dolares3": float,
                "institucion4": str,
                "proposito4": str,
                "dolares4": float,
                "institucion5": str,
                "proposito5": str,
                "dolares5": float,
                "institucion6": str,
                "proposito6": str,
                "dolares6": float,
                "institucion7": str,
                "proposito7": str,
                "dolares7": float,
                "institucion8": str,
                "proposito8": str,
                "dolares8": float,
                "institucion9": str,
                "proposito9": str,
                "dolares9": float,
                "institucion10": str,
                "proposito10": str,
                "dolares10": float,
                "institucion11": str,
                "proposito11": str,
                "dolares11": float,
                "institucion12": str,
                "proposito12": str,
                "dolares12": float,
                "institucion13": str,
                "proposito13": str,
                "dolares13": float,
                "institucion14": str,
                "proposito14": str,
                "dolares14": float,
                "operation_expenses": float,
                "salary": float,
                "SS_SD_SR_beneficios_marginales": float,
                "servicios_profecionales_c": float,
                "intereses": float,
                "other_gastos": float,
                "to_people": float,
                "servicios_profecionales_a": float,
                "pension": float,
                "name_other_1": str,
                "quantity_other_1": float,
                "name_other_2": str,
                "quantity_other_2": float,
                "name_other_3": str,
                "quantity_other_3": float,
                "name_other_4": str,
                "quantity_other_4": float,
                "agencia": str,
                "prep": str,
                "titulo": str,
                "telefono": str,
                "fecha": str,
            },
            table_name="JP_544",
            table_id="46",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/balanza_de_pagos/JP-544.html")
