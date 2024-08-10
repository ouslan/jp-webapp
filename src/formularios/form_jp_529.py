from django.shortcuts import render
from src.dao.data_db_dao import DAO
import csv
import os


def JP_529(request):
    if request.method == "POST":
        # Retrieve form data
        # header
        year1 = request.POST.get("year1")
        year2 = request.POST.get("year2")
        company = request.POST.get("company")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")
        tel = request.POST.get("tel")

        choice = request.POST.get("choice")

        # tabla 1
        agencia_a1 = request.POST.get("agencia_a1")
        federal_program_a1 = request.POST.get("federal_program_a1")
        quantity_a1 = request.POST.get("quantity_a1")
        date_a1 = request.POST.get("date_a1")

        agencia_a2 = request.POST.get("agencia_a2")
        federal_program_a2 = request.POST.get("federal_program_a2")
        quantity_a2 = request.POST.get("quantity_a2")
        date_a2 = request.POST.get("date_a2")

        agencia_a3 = request.POST.get("agencia_a3")
        federal_program_a3 = request.POST.get("federal_program_a3")
        quantity_a3 = request.POST.get("quantity_a3")
        date_a3 = request.POST.get("date_a3")

        agencia_a4 = request.POST.get("agencia_a4")
        federal_program_a4 = request.POST.get("federal_program_a4")
        quantity_a4 = request.POST.get("quantity_a4")
        date_a4 = request.POST.get("date_a4")

        agencia_a5 = request.POST.get("agencia_a5")
        federal_program_a5 = request.POST.get("federal_program_a5")
        quantity_a5 = request.POST.get("quantity_a5")
        date_a5 = request.POST.get("date_a5")

        agencia_a6 = request.POST.get("agencia_a6")
        federal_program_a6 = request.POST.get("federal_program_a6")
        quantity_a6 = request.POST.get("quantity_a6")
        date_a6 = request.POST.get("date_a6")

        agencia_a7 = request.POST.get("agencia_a7")
        federal_program_a7 = request.POST.get("federal_program_a7")
        quantity_a7 = request.POST.get("quantity_a7")
        date_a7 = request.POST.get("date_a7")

        agencia_a8 = request.POST.get("agencia_a8")
        federal_program_a8 = request.POST.get("federal_program_a8")
        quantity_a8 = request.POST.get("quantity_a8")
        date_a8 = request.POST.get("date_a8")

        # tabla 2
        agencia_b1 = request.POST.get("agencia_b1")
        federal_program_b1 = request.POST.get("federal_program_b1")
        quantity_b1 = request.POST.get("quantity_b1")
        date_b1 = request.POST.get("date_b1")

        agencia_b2 = request.POST.get("agencia_b2")
        federal_program_b2 = request.POST.get("federal_program_b2")
        quantity_b2 = request.POST.get("quantity_b2")
        date_b2 = request.POST.get("date_b2")

        agencia_b3 = request.POST.get("agencia_b3")
        federal_program_b3 = request.POST.get("federal_program_b3")
        quantity_b3 = request.POST.get("quantity_b3")
        date_b3 = request.POST.get("date_b3")

        agencia_b4 = request.POST.get("agencia_b4")
        federal_program_b4 = request.POST.get("federal_program_b4")
        quantity_b4 = request.POST.get("quantity_b4")
        date_b4 = request.POST.get("date_b4")

        agencia_b5 = request.POST.get("agencia_b5")
        federal_program_b5 = request.POST.get("federal_program_b5")
        quantity_b5 = request.POST.get("quantity_b5")
        date_b5 = request.POST.get("date_b5")

        agencia_b6 = request.POST.get("agencia_b6")
        federal_program_b6 = request.POST.get("federal_program_b6")
        quantity_b6 = request.POST.get("quantity_b6")
        date_b6 = request.POST.get("date_b6")

        agencia_b7 = request.POST.get("agencia_b7")
        federal_program_b7 = request.POST.get("federal_program_b7")
        quantity_b7 = request.POST.get("quantity_b7")
        date_b7 = request.POST.get("date_b7")

        agencia_b8 = request.POST.get("agencia_b8")
        federal_program_b8 = request.POST.get("federal_program_b8")
        quantity_b8 = request.POST.get("quantity_b8")
        date_b8 = request.POST.get("date_b8")

        # section2
        # tabla 1
        instuition1 = request.POST.get("instuition1")
        money1 = request.POST.get("money1")
        date1 = request.POST.get("date1")

        # tabla 2
        instuition2 = request.POST.get("instuition2")
        money2 = request.POST.get("money2")
        date2 = request.POST.get("date2")

        # tabla 3
        instuition3 = request.POST.get("instuition3")
        money3 = request.POST.get("money3")
        date3 = request.POST.get("date3")

        # tabla 4
        instuition4 = request.POST.get("instuition4")
        money4 = request.POST.get("money4")
        date4 = request.POST.get("date4")

        # tabla 5
        instuition5 = request.POST.get("instuition5")
        money5 = request.POST.get("money5")
        date5 = request.POST.get("date5")

        # tabla 6
        instuition6 = request.POST.get("instuition6")
        money6 = request.POST.get("money6")
        date6 = request.POST.get("date6")

        # tabla 7
        instuition7 = request.POST.get("instuition7")
        money7 = request.POST.get("money7")
        date7 = request.POST.get("date7")

        # tabla 8
        instuition8 = request.POST.get("instuition8")
        money8 = request.POST.get("money8")
        date8 = request.POST.get("date8")

        # tabla 9
        instuition9 = request.POST.get("instuition9")
        money9 = request.POST.get("money9")
        date9 = request.POST.get("date9")

        # tabla 10
        instuition10 = request.POST.get("instuition10")
        money10 = request.POST.get("money10")
        date10 = request.POST.get("date10")

        # footer
        name = request.POST.get("name")
        puesto = request.POST.get("puesto")
        date = request.POST.get("date")

        csv_file_path = "data/cuestionarios/balanza_de_pagos/JP-529.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "year1",
                        "year2",
                        "company",
                        "address",
                        "email",
                        "liaison_officer",
                        "tel",
                        "choice",
                        "agencia_a1",
                        "federal_program_a1",
                        "quantity_a1",
                        "date_a1",
                        "agencia_a2",
                        "federal_program_a2",
                        "quantity_a2",
                        "date_a2",
                        "agencia_a3",
                        "federal_program_a3",
                        "quantity_a3",
                        "date_a3",
                        "agencia_a4",
                        "federal_program_a4",
                        "quantity_a4",
                        "date_a4",
                        "agencia_a5",
                        "federal_program_a5",
                        "quantity_a5",
                        "date_a5",
                        "agencia_a6",
                        "federal_program_a6",
                        "quantity_a6",
                        "date_a6",
                        "agencia_a7",
                        "federal_program_a7",
                        "quantity_a7",
                        "date_a7",
                        "agencia_a8",
                        "federal_program_a8",
                        "quantity_a8",
                        "date_a8",
                        "agencia_b1",
                        "federal_program_b1",
                        "quantity_b1",
                        "date_b1",
                        "agencia_b2",
                        "federal_program_b2",
                        "quantity_b2",
                        "date_b2",
                        "agencia_b3",
                        "federal_program_b3",
                        "quantity_b3",
                        "date_b3",
                        "agencia_b4",
                        "federal_program_b4",
                        "quantity_b4",
                        "date_b4",
                        "agencia_b5",
                        "federal_program_b5",
                        "quantity_b5",
                        "date_b5",
                        "agencia_b6",
                        "federal_program_b6",
                        "quantity_b6",
                        "date_b6",
                        "agencia_b7",
                        "federal_program_b7",
                        "quantity_b7",
                        "date_b7",
                        "agencia_b8",
                        "federal_program_b8",
                        "quantity_b8",
                        "date_b8",
                        "instuition1",
                        "money1",
                        "date1",
                        "instuition2",
                        "money2",
                        "date2",
                        "instuition3",
                        "money3",
                        "date3",
                        "instuition4",
                        "money4",
                        "date4",
                        "instuition5",
                        "money5",
                        "date5",
                        "instuition6",
                        "money6",
                        "date6",
                        "instuition7",
                        "money7",
                        "date7",
                        "instuition8",
                        "money8",
                        "date8",
                        "instuition9",
                        "money9",
                        "date9",
                        "instuition10",
                        "money10",
                        "date10",
                        "name",
                        "puesto",
                        "date",
                    ]
                )

            writer.writerow(
                [
                    year1,
                    year2,
                    company,
                    address,
                    email,
                    liaison_officer,
                    tel,
                    choice,
                    agencia_a1,
                    federal_program_a1,
                    quantity_a1,
                    date_a1,
                    agencia_a2,
                    federal_program_a2,
                    quantity_a2,
                    date_a2,
                    agencia_a3,
                    federal_program_a3,
                    quantity_a3,
                    date_a3,
                    agencia_a4,
                    federal_program_a4,
                    quantity_a4,
                    date_a4,
                    agencia_a5,
                    federal_program_a5,
                    quantity_a5,
                    date_a5,
                    agencia_a6,
                    federal_program_a6,
                    quantity_a6,
                    date_a6,
                    agencia_a7,
                    federal_program_a7,
                    quantity_a7,
                    date_a7,
                    agencia_a8,
                    federal_program_a8,
                    quantity_a8,
                    date_a8,
                    agencia_b1,
                    federal_program_b1,
                    quantity_b1,
                    date_b1,
                    agencia_b2,
                    federal_program_b2,
                    quantity_b2,
                    date_b2,
                    agencia_b3,
                    federal_program_b3,
                    quantity_b3,
                    date_b3,
                    agencia_b4,
                    federal_program_b4,
                    quantity_b4,
                    date_b4,
                    agencia_b5,
                    federal_program_b5,
                    quantity_b5,
                    date_b5,
                    agencia_b6,
                    federal_program_b6,
                    quantity_b6,
                    date_b6,
                    agencia_b7,
                    federal_program_b7,
                    quantity_b7,
                    date_b7,
                    agencia_b8,
                    federal_program_b8,
                    quantity_b8,
                    date_b8,
                    instuition1,
                    money1,
                    date1,
                    instuition2,
                    money2,
                    date2,
                    instuition3,
                    money3,
                    date3,
                    instuition4,
                    money4,
                    date4,
                    instuition5,
                    money5,
                    date5,
                    instuition6,
                    money6,
                    date6,
                    instuition7,
                    money7,
                    date7,
                    instuition8,
                    money8,
                    date8,
                    instuition9,
                    money9,
                    date9,
                    instuition10,
                    money10,
                    date10,
                    name,
                    puesto,
                    date,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/balanza_de_pagos/JP-529.csv",
            dtypes={
                "year1": int,
                "year2": int,
                "company": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "tel": str,
                "choice": str,
                "agencia_a1": str,
                "federal_program_a1": str,
                "quantity_a1": float,
                "date_a1": str,
                "agencia_a2": str,
                "federal_program_a2": str,
                "quantity_a2": float,
                "date_a2": str,
                "agencia_a3": str,
                "federal_program_a3": str,
                "quantity_a3": float,
                "date_a3": str,
                "agencia_a4": str,
                "federal_program_a4": str,
                "quantity_a4": float,
                "date_a4": str,
                "agencia_a5": str,
                "federal_program_a5": str,
                "quantity_a5": float,
                "date_a5": str,
                "agencia_a6": str,
                "federal_program_a6": str,
                "quantity_a6": float,
                "date_a6": str,
                "agencia_a7": str,
                "federal_program_a7": str,
                "quantity_a7": float,
                "date_a7": str,
                "agencia_a8": str,
                "federal_program_a8": str,
                "quantity_a8": float,
                "date_a8": str,
                "agencia_b1": str,
                "federal_program_b1": str,
                "quantity_b1": float,
                "date_b1": str,
                "agencia_b2": str,
                "federal_program_b2": str,
                "quantity_b2": float,
                "date_b2": str,
                "agencia_b3": str,
                "federal_program_b3": str,
                "quantity_b3": float,
                "date_b3": str,
                "agencia_b4": str,
                "federal_program_b4": str,
                "quantity_b4": float,
                "date_b4": str,
                "agencia_b5": str,
                "federal_program_b5": str,
                "quantity_b5": float,
                "date_b5": str,
                "agencia_b6": str,
                "federal_program_b6": str,
                "quantity_b6": float,
                "date_b6": str,
                "agencia_b7": str,
                "federal_program_b7": str,
                "quantity_b7": float,
                "date_b7": str,
                "agencia_b8": str,
                "federal_program_b8": str,
                "quantity_b8": float,
                "date_b8": str,
                "instuition1": str,
                "money1": float,
                "date1": str,
                "instuition2": str,
                "money2": float,
                "date2": str,
                "instuition3": str,
                "money3": float,
                "date3": str,
                "instuition4": str,
                "money4": float,
                "date4": str,
                "instuition5": str,
                "money5": float,
                "date5": str,
                "instuition6": str,
                "money6": float,
                "date6": str,
                "instuition7": str,
                "money7": float,
                "date7": str,
                "instuition8": str,
                "money8": float,
                "date8": str,
                "instuition9": str,
                "money9": float,
                "date9": str,
                "instuition10": str,
                "money10": float,
                "date10": str,
                "name": str,
                "puesto": str,
                "date": str,
            },
            table_name="JP_529",
            table_id="5",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/balanza_de_pagos/JP-529.html")
