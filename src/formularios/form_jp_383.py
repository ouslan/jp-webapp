from django.shortcuts import render
from src.dao.data_db_dao import DAO
import csv
import os


def JP_383(request):
    if request.method == "POST":
        # Retrieve form data
        other_section = request.POST.get("other_section")
        año = request.POST.get("año")
        julio_1 = request.POST.get("julio_1")
        julio_2 = request.POST.get("julio_2")
        julio_3 = request.POST.get("julio_3")
        julio_4 = request.POST.get("julio_4")
        julio_5 = request.POST.get("julio_5")
        julio_6 = request.POST.get("julio_6")
        agosto_1 = request.POST.get("agosto_1")
        agosto_2 = request.POST.get("agosto_2")
        agosto_3 = request.POST.get("agosto_3")
        agosto_4 = request.POST.get("agosto_4")
        agosto_5 = request.POST.get("agosto_5")
        agosto_6 = request.POST.get("agosto_6")
        septiembre_1 = request.POST.get("septiembre_1")
        septiembre_2 = request.POST.get("septiembre_2")
        septiembre_3 = request.POST.get("septiembre_3")
        septiembre_4 = request.POST.get("septiembre_4")
        septiembre_5 = request.POST.get("septiembre_5")
        septiembre_6 = request.POST.get("septiembre_6")
        subtotal_1 = request.POST.get("subtotal_1")
        subtotal_2 = request.POST.get("subtotal_2")
        subtotal_3 = request.POST.get("subtotal_3")
        subtotal_4 = request.POST.get("subtotal_4")
        subtotal_5 = request.POST.get("subtotal_5")
        subtotal_6 = request.POST.get("subtotal_6")
        octubre_1 = request.POST.get("octubre_1")
        octubre_2 = request.POST.get("octubre_2")
        octubre_3 = request.POST.get("octubre_3")
        octubre_4 = request.POST.get("octubre_4")
        octubre_5 = request.POST.get("octubre_5")
        octubre_6 = request.POST.get("octubre_6")
        noviembre_1 = request.POST.get("noviembre_1")
        noviembre_2 = request.POST.get("noviembre_2")
        noviembre_3 = request.POST.get("noviembre_3")
        noviembre_4 = request.POST.get("noviembre_4")
        noviembre_5 = request.POST.get("noviembre_5")
        noviembre_6 = request.POST.get("noviembre_6")
        diciembre_1 = request.POST.get("diciembre_1")
        diciembre_2 = request.POST.get("diciembre_2")
        diciembre_3 = request.POST.get("diciembre_3")
        diciembre_4 = request.POST.get("diciembre_4")
        diciembre_5 = request.POST.get("diciembre_5")
        diciembre_6 = request.POST.get("diciembre_6")
        subtotal_11 = request.POST.get("subtotal_11")
        subtotal_12 = request.POST.get("subtotal_12")
        subtotal_13 = request.POST.get("subtotal_13")
        subtotal_14 = request.POST.get("subtotal_14")
        subtotal_15 = request.POST.get("subtotal_15")
        subtotal_16 = request.POST.get("subtotal_16")
        año_1 = request.POST.get("año_1")
        enero_1 = request.POST.get("enero_1")
        enero_2 = request.POST.get("enero_2")
        enero_3 = request.POST.get("enero_3")
        enero_4 = request.POST.get("enero_4")
        enero_5 = request.POST.get("enero_5")
        enero_6 = request.POST.get("enero_6")
        febrero_1 = request.POST.get("febrero_1")
        febrero_2 = request.POST.get("febrero_2")
        febrero_3 = request.POST.get("febrero_3")
        febrero_4 = request.POST.get("febrero_4")
        febrero_5 = request.POST.get("febrero_5")
        febrero_6 = request.POST.get("febrero_6")
        marzo_1 = request.POST.get("marzo_1")
        marzo_2 = request.POST.get("marzo_2")
        marzo_3 = request.POST.get("marzo_3")
        marzo_4 = request.POST.get("marzo_4")
        marzo_5 = request.POST.get("marzo_5")
        marzo_6 = request.POST.get("marzo_6")
        subtotal_21 = request.POST.get("subtotal_21")
        subtotal_22 = request.POST.get("subtotal_22")
        subtotal_23 = request.POST.get("subtotal_23")
        subtotal_24 = request.POST.get("subtotal_24")
        subtotal_25 = request.POST.get("subtotal_25")
        subtotal_26 = request.POST.get("subtotal_26")
        abril_1 = request.POST.get("abril_1")
        abril_2 = request.POST.get("abril_2")
        abril_3 = request.POST.get("abril_3")
        abril_4 = request.POST.get("abril_4")
        abril_5 = request.POST.get("abril_5")
        abril_6 = request.POST.get("abril_6")
        mayo_1 = request.POST.get("mayo_1")
        mayo_2 = request.POST.get("mayo_2")
        mayo_3 = request.POST.get("mayo_3")
        mayo_4 = request.POST.get("mayo_4")
        mayo_5 = request.POST.get("mayo_5")
        mayo_6 = request.POST.get("mayo_6")
        junio_1 = request.POST.get("junio_1")
        junio_2 = request.POST.get("junio_2")
        junio_3 = request.POST.get("junio_3")
        junio_4 = request.POST.get("junio_4")
        junio_5 = request.POST.get("junio_5")
        junio_6 = request.POST.get("junio_6")
        subtotal_31 = request.POST.get("subtotal_31")
        subtotal_32 = request.POST.get("subtotal_32")
        subtotal_33 = request.POST.get("subtotal_33")
        subtotal_34 = request.POST.get("subtotal_34")
        subtotal_35 = request.POST.get("subtotal_35")
        subtotal_36 = request.POST.get("subtotal_36")
        total_1 = request.POST.get("total_1")
        total_2 = request.POST.get("total_2")
        total_3 = request.POST.get("total_3")
        total_4 = request.POST.get("total_4")
        total_5 = request.POST.get("total_5")
        total_6 = request.POST.get("total_6")
        signature = request.POST.get("signature")
        name = request.POST.get("name")
        title = request.POST.get("title")
        phone = request.POST.get("phone")

        csv_file_path = "data/cuestionarios/balanza_de_pagos/JP-383.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "other_section",
                        "año",
                        "julio_1",
                        "julio_2",
                        "julio_3",
                        "julio_4",
                        "julio_5",
                        "julio_6",
                        "agosto_1",
                        "agosto_2",
                        "agosto_3",
                        "agosto_4",
                        "agosto_5",
                        "agosto_6",
                        "septiembre_1",
                        "septiembre_2",
                        "septiembre_3",
                        "septiembre_4",
                        "septiembre_5",
                        "septiembre_6",
                        "subtotal_1",
                        "subtotal_2",
                        "subtotal_3",
                        "subtotal_4",
                        "subtotal_5",
                        "subtotal_6",
                        "octubre_1",
                        "octubre_2",
                        "octubre_3",
                        "octubre_4",
                        "octubre_5",
                        "octubre_6",
                        "noviembre_1",
                        "noviembre_2",
                        "noviembre_3",
                        "noviembre_4",
                        "noviembre_5",
                        "noviembre_6",
                        "diciembre_1",
                        "diciembre_2",
                        "diciembre_3",
                        "diciembre_4",
                        "diciembre_5",
                        "diciembre_6",
                        "subtotal_11",
                        "subtotal_12",
                        "subtotal_13",
                        "subtotal_14",
                        "subtotal_15",
                        "subtotal_16",
                        "año_1",
                        "enero_1",
                        "enero_2",
                        "enero_3",
                        "enero_4",
                        "enero_5",
                        "enero_6",
                        "febrero_1",
                        "febrero_2",
                        "febrero_3",
                        "febrero_4",
                        "febrero_5",
                        "febrero_6",
                        "marzo_1",
                        "marzo_2",
                        "marzo_3",
                        "marzo_4",
                        "marzo_5",
                        "marzo_6",
                        "subtotal_21",
                        "subtotal_22",
                        "subtotal_23",
                        "subtotal_24",
                        "subtotal_25",
                        "subtotal_26",
                        "abril_1",
                        "abril_2",
                        "abril_3",
                        "abril_4",
                        "abril_5",
                        "abril_6",
                        "mayo_1",
                        "mayo_2",
                        "mayo_3",
                        "mayo_4",
                        "mayo_5",
                        "mayo_6",
                        "junio_1",
                        "junio_2",
                        "junio_3",
                        "junio_4",
                        "junio_5",
                        "junio_6",
                        "subtotal_31",
                        "subtotal_32",
                        "subtotal_33",
                        "subtotal_34",
                        "subtotal_35",
                        "subtotal_36",
                        "total_1",
                        "total_2",
                        "total_3",
                        "total_4",
                        "total_5",
                        "total_6",
                        "signature",
                        "name",
                        "title",
                        "phone",
                    ]
                )

            writer.writerow(
                [
                    other_section,
                    año,
                    julio_1,
                    julio_2,
                    julio_3,
                    julio_4,
                    julio_5,
                    julio_6,
                    agosto_1,
                    agosto_2,
                    agosto_3,
                    agosto_4,
                    agosto_5,
                    agosto_6,
                    septiembre_1,
                    septiembre_2,
                    septiembre_3,
                    septiembre_4,
                    septiembre_5,
                    septiembre_6,
                    subtotal_1,
                    subtotal_2,
                    subtotal_3,
                    subtotal_4,
                    subtotal_5,
                    subtotal_6,
                    octubre_1,
                    octubre_2,
                    octubre_3,
                    octubre_4,
                    octubre_5,
                    octubre_6,
                    noviembre_1,
                    noviembre_2,
                    noviembre_3,
                    noviembre_4,
                    noviembre_5,
                    noviembre_6,
                    diciembre_1,
                    diciembre_2,
                    diciembre_3,
                    diciembre_4,
                    diciembre_5,
                    diciembre_6,
                    subtotal_11,
                    subtotal_12,
                    subtotal_13,
                    subtotal_14,
                    subtotal_15,
                    subtotal_16,
                    año_1,
                    enero_1,
                    enero_2,
                    enero_3,
                    enero_4,
                    enero_5,
                    enero_6,
                    febrero_1,
                    febrero_2,
                    febrero_3,
                    febrero_4,
                    febrero_5,
                    febrero_6,
                    marzo_1,
                    marzo_2,
                    marzo_3,
                    marzo_4,
                    marzo_5,
                    marzo_6,
                    subtotal_21,
                    subtotal_22,
                    subtotal_23,
                    subtotal_24,
                    subtotal_25,
                    subtotal_26,
                    abril_1,
                    abril_2,
                    abril_3,
                    abril_4,
                    abril_5,
                    abril_6,
                    mayo_1,
                    mayo_2,
                    mayo_3,
                    mayo_4,
                    mayo_5,
                    mayo_6,
                    junio_1,
                    junio_2,
                    junio_3,
                    junio_4,
                    junio_5,
                    junio_6,
                    subtotal_31,
                    subtotal_32,
                    subtotal_33,
                    subtotal_34,
                    subtotal_35,
                    subtotal_36,
                    total_1,
                    total_2,
                    total_3,
                    total_4,
                    total_5,
                    total_6,
                    signature,
                    name,
                    title,
                    phone,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/balanza_de_pagos/JP-383.csv",
            dtypes={
                "other_section": str,
                "año": int,
                "julio_1": float,
                "julio_2": float,
                "julio_3": float,
                "julio_4": float,
                "julio_5": float,
                "julio_6": float,
                "agosto_1": float,
                "agosto_2": float,
                "agosto_3": float,
                "agosto_4": float,
                "agosto_5": float,
                "agosto_6": float,
                "septiembre_1": float,
                "septiembre_2": float,
                "septiembre_3": float,
                "septiembre_4": float,
                "septiembre_5": float,
                "septiembre_6": float,
                "subtotal_1": float,
                "subtotal_2": float,
                "subtotal_3": float,
                "subtotal_4": float,
                "subtotal_5": float,
                "subtotal_6": float,
                "octubre_1": float,
                "octubre_2": float,
                "octubre_3": float,
                "octubre_4": float,
                "octubre_5": float,
                "octubre_6": float,
                "noviembre_1": float,
                "noviembre_2": float,
                "noviembre_3": float,
                "noviembre_4": float,
                "noviembre_5": float,
                "noviembre_6": float,
                "diciembre_1": float,
                "diciembre_2": float,
                "diciembre_3": float,
                "diciembre_4": float,
                "diciembre_5": float,
                "diciembre_6": float,
                "subtotal_11": float,
                "subtotal_12": float,
                "subtotal_13": float,
                "subtotal_14": float,
                "subtotal_15": float,
                "subtotal_16": float,
                "año_1": int,
                "enero_1": float,
                "enero_2": float,
                "enero_3": float,
                "enero_4": float,
                "enero_5": float,
                "enero_6": float,
                "febrero_1": float,
                "febrero_2": float,
                "febrero_3": float,
                "febrero_4": float,
                "febrero_5": float,
                "febrero_6": float,
                "marzo_1": float,
                "marzo_2": float,
                "marzo_3": float,
                "marzo_4": float,
                "marzo_5": float,
                "marzo_6": float,
                "subtotal_21": float,
                "subtotal_22": float,
                "subtotal_23": float,
                "subtotal_24": float,
                "subtotal_25": float,
                "subtotal_26": float,
                "abril_1": float,
                "abril_2": float,
                "abril_3": float,
                "abril_4": float,
                "abril_5": float,
                "abril_6": float,
                "mayo_1": float,
                "mayo_2": float,
                "mayo_3": float,
                "mayo_4": float,
                "mayo_5": float,
                "mayo_6": float,
                "junio_1": float,
                "junio_2": float,
                "junio_3": float,
                "junio_4": float,
                "junio_5": float,
                "junio_6": float,
                "subtotal_31": float,
                "subtotal_32": float,
                "subtotal_33": float,
                "subtotal_34": float,
                "subtotal_35": float,
                "subtotal_36": float,
                "total_1": float,
                "total_2": float,
                "total_3": float,
                "total_4": float,
                "total_5": float,
                "total_6": float,
                "signature": str,
                "name": str,
                "title": str,
                "phone": str,
            },
            table_name="JP_383",
            table_id="45",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/balanza_de_pagos/JP-383.html")
