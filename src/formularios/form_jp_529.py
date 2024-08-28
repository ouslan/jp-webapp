from django.shortcuts import render
from src.dao.data_db_dao import DAO
import polars as pl


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

        data = [
            pl.Series("year1", [year1], dtype=pl.String),
            pl.Series("year2", [year2], dtype=pl.String),
            pl.Series("company", [company], dtype=pl.String),
            pl.Series("address", [address], dtype=pl.String),
            pl.Series("email", [email], dtype=pl.String),
            pl.Series("liaison_officer", [liaison_officer], dtype=pl.String),
            pl.Series("tel", [tel], dtype=pl.String),
            pl.Series("choice", [choice], dtype=pl.String),
            pl.Series("agencia_a1", [agencia_a1], dtype=pl.String),
            pl.Series("federal_program_a1", [federal_program_a1], dtype=pl.String),
            pl.Series("quantity_a1", [float(quantity_a1)], dtype=pl.Float64),
            pl.Series("date_a1", [date_a1], dtype=pl.String),
            pl.Series("agencia_a2", [agencia_a2], dtype=pl.String),
            pl.Series("federal_program_a2", [federal_program_a2], dtype=pl.String),
            pl.Series("quantity_a2", [float(quantity_a2)], dtype=pl.Float64),
            pl.Series("date_a2", [date_a2], dtype=pl.String),
            pl.Series("agencia_a3", [agencia_a3], dtype=pl.String),
            pl.Series("federal_program_a3", [federal_program_a3], dtype=pl.String),
            pl.Series("quantity_a3", [float(quantity_a3)], dtype=pl.Float64),
            pl.Series("date_a3", [date_a3], dtype=pl.String),
            pl.Series("agencia_a4", [agencia_a4], dtype=pl.String),
            pl.Series("federal_program_a4", [federal_program_a4], dtype=pl.String),
            pl.Series("quantity_a4", [float(quantity_a4)], dtype=pl.Float64),
            pl.Series("date_a4", [date_a4], dtype=pl.String),
            pl.Series("agencia_a5", [agencia_a5], dtype=pl.String),
            pl.Series("federal_program_a5", [federal_program_a5], dtype=pl.String),
            pl.Series("quantity_a5", [float(quantity_a5)], dtype=pl.Float64),
            pl.Series("date_a5", [date_a5], dtype=pl.String),
            pl.Series("agencia_a6", [agencia_a6], dtype=pl.String),
            pl.Series("federal_program_a6", [federal_program_a6], dtype=pl.String),
            pl.Series("quantity_a6", [float(quantity_a6)], dtype=pl.Float64),
            pl.Series("date_a6", [date_a6], dtype=pl.String),
            pl.Series("agencia_a7", [agencia_a7], dtype=pl.String),
            pl.Series("federal_program_a7", [federal_program_a7], dtype=pl.String),
            pl.Series("quantity_a7", [float(quantity_a7)], dtype=pl.Float64),
            pl.Series("date_a7", [date_a7], dtype=pl.String),
            pl.Series("agencia_a8", [agencia_a8], dtype=pl.String),
            pl.Series("federal_program_a8", [federal_program_a8], dtype=pl.String),
            pl.Series("quantity_a8", [float(quantity_a8)], dtype=pl.Float64),
            pl.Series("date_a8", [date_a8], dtype=pl.String),
            pl.Series("agencia_b1", [agencia_b1], dtype=pl.String),
            pl.Series("federal_program_b1", [federal_program_b1], dtype=pl.String),
            pl.Series("quantity_b1", [float(quantity_b1)], dtype=pl.Float64),
            pl.Series("date_b1", [date_b1], dtype=pl.String),
            pl.Series("agencia_b2", [agencia_b2], dtype=pl.String),
            pl.Series("federal_program_b2", [federal_program_b2], dtype=pl.String),
            pl.Series("quantity_b2", [float(quantity_b2)], dtype=pl.Float64),
            pl.Series("date_b2", [date_b2], dtype=pl.String),
            pl.Series("agencia_b3", [agencia_b3], dtype=pl.String),
            pl.Series("federal_program_b3", [federal_program_b3], dtype=pl.String),
            pl.Series("quantity_b3", [float(quantity_b3)], dtype=pl.Float64),
            pl.Series("date_b3", [date_b3], dtype=pl.String),
            pl.Series("agencia_b4", [agencia_b4], dtype=pl.String),
            pl.Series("federal_program_b4", [federal_program_b4], dtype=pl.String),
            pl.Series("quantity_b4", [float(quantity_b4)], dtype=pl.Float64),
            pl.Series("date_b4", [date_b4], dtype=pl.String),
            pl.Series("agencia_b5", [agencia_b5], dtype=pl.String),
            pl.Series("federal_program_b5", [federal_program_b5], dtype=pl.String),
            pl.Series("quantity_b5", [float(quantity_b5)], dtype=pl.Float64),
            pl.Series("date_b5", [date_b5], dtype=pl.String),
            pl.Series("agencia_b6", [agencia_b6], dtype=pl.String),
            pl.Series("federal_program_b6", [federal_program_b6], dtype=pl.String),
            pl.Series("quantity_b6", [float(quantity_b6)], dtype=pl.Float64),
            pl.Series("date_b6", [date_b6], dtype=pl.String),
            pl.Series("agencia_b7", [agencia_b7], dtype=pl.String),
            pl.Series("federal_program_b7", [federal_program_b7], dtype=pl.String),
            pl.Series("quantity_b7", [float(quantity_b7)], dtype=pl.Float64),
            pl.Series("date_b7", [date_b7], dtype=pl.String),
            pl.Series("agencia_b8", [agencia_b8], dtype=pl.String),
            pl.Series("federal_program_b8", [federal_program_b8], dtype=pl.String),
            pl.Series("quantity_b8", [float(quantity_b8)], dtype=pl.Float64),
            pl.Series("date_b8", [date_b8], dtype=pl.String),
            pl.Series("instuition1", [instuition1], dtype=pl.String),
            pl.Series("money1", [float(money1)], dtype=pl.Float64),
            pl.Series("date1", [date1], dtype=pl.String),
            pl.Series("instuition2", [instuition2], dtype=pl.String),
            pl.Series("money2", [float(money2)], dtype=pl.Float64),
            pl.Series("date2", [date2], dtype=pl.String),
            pl.Series("instuition3", [instuition3], dtype=pl.String),
            pl.Series("money3", [float(money3)], dtype=pl.Float64),
            pl.Series("date3", [date3], dtype=pl.String),
            pl.Series("instuition4", [instuition4], dtype=pl.String),
            pl.Series("money4", [float(money4)], dtype=pl.Float64),
            pl.Series("date4", [date4], dtype=pl.String),
            pl.Series("instuition5", [instuition5], dtype=pl.String),
            pl.Series("money5", [float(money5)], dtype=pl.Float64),
            pl.Series("date5", [date5], dtype=pl.String),
            pl.Series("instuition6", [instuition6], dtype=pl.String),
            pl.Series("money6", [float(money6)], dtype=pl.Float64),
            pl.Series("date6", [date6], dtype=pl.String),
            pl.Series("instuition7", [instuition7], dtype=pl.String),
            pl.Series("money7", [float(money7)], dtype=pl.Float64),
            pl.Series("date7", [date7], dtype=pl.String),
            pl.Series("instuition8", [instuition8], dtype=pl.String),
            pl.Series("money8", [float(money8)], dtype=pl.Float64),
            pl.Series("date8", [date8], dtype=pl.String),
            pl.Series("instuition9", [instuition9], dtype=pl.String),
            pl.Series("money9", [float(money9)], dtype=pl.Float64),
            pl.Series("date9", [date9], dtype=pl.String),
            pl.Series("instuition10", [instuition10], dtype=pl.String),
            pl.Series("money10", [float(money10)], dtype=pl.Float64),
            pl.Series("date10", [date10], dtype=pl.String),
            pl.Series("name", [name], dtype=pl.String),
            pl.Series("puesto", [puesto], dtype=pl.String),
            pl.Series("date", [date], dtype=pl.String),
        ]
        
        df = pl.DataFrame(data)
        DAO().insert_forms(df, "JP_529", 5)

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/balanza_de_pagos/JP-529.html")
