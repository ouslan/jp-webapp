from django.shortcuts import render
from src.dao.data_db_dao import DAO
import polars as pl


def JP_375(request):
    if request.method == "POST":
        # Retrieve form data
        year_1 = request.POST.get("year_1")
        year_2 = request.POST.get("year_2")
        year_3 = request.POST.get("year_3")

        FHA_1 = request.POST.get("FHA_1")
        FHA_2 = request.POST.get("FHA_2")
        FHA_3 = request.POST.get("FHA_3")

        veteran_1 = request.POST.get("veteran_1")
        veteran_2 = request.POST.get("veteran_2")
        veteran_3 = request.POST.get("veteran_3")

        bank_1 = request.POST.get("bank_1")
        bank_2 = request.POST.get("bank_2")
        bank_3 = request.POST.get("bank_3")

        conventional_1 = request.POST.get("conventional_1")
        conventional_2 = request.POST.get("conventional_2")
        conventional_3 = request.POST.get("conventional_3")

        other_1 = request.POST.get("other_1")
        other_2 = request.POST.get("other_2")
        other_3 = request.POST.get("other_3")

        FHA_2_1 = request.POST.get("FHA_2_1")
        FHA_2_2 = request.POST.get("FHA_2_2")
        FHA_2_3 = request.POST.get("FHA_2_3")

        veteran_2_1 = request.POST.get("veteran_2_1")
        veteran_2_2 = request.POST.get("veteran_2_2")
        veteran_2_3 = request.POST.get("veteran_2_3")

        conventional_2_1 = request.POST.get("conventional_2_1")
        conventional_2_2 = request.POST.get("conventional_2_2")
        conventional_2_3 = request.POST.get("conventional_2_3")

        others_2_1 = request.POST.get("others_2_1")
        others_2_2 = request.POST.get("others_2_2")
        others_2_3 = request.POST.get("others_2_3")

        FHA_3_1 = request.POST.get("FHA_3_1")
        FHA_3_2 = request.POST.get("FHA_3_2")
        FHA_3_3 = request.POST.get("FHA_3_3")

        veteran_3_1 = request.POST.get("veteran_3_1")
        veteran_3_2 = request.POST.get("veteran_3_2")
        veteran_3_3 = request.POST.get("veteran_3_3")

        bank_2_1 = request.POST.get("bank_2_1")
        bank_2_2 = request.POST.get("bank_2_2")
        bank_2_3 = request.POST.get("bank_2_3")

        conventional_3_1 = request.POST.get("conventional_3_1")
        conventional_3_2 = request.POST.get("conventional_3_2")
        conventional_3_3 = request.POST.get("conventional_3_3")

        others_3_1 = request.POST.get("others_3_1")
        others_3_2 = request.POST.get("others_3_2")
        others_3_3 = request.POST.get("others_3_3")

        FHA_4_1 = request.POST.get("FHA_4_1")
        FHA_4_2 = request.POST.get("FHA_4_2")
        FHA_4_3 = request.POST.get("FHA_4_3")

        veteran_4_1 = request.POST.get("veteran_4_1")
        veteran_4_2 = request.POST.get("veteran_4_2")
        veteran_4_3 = request.POST.get("veteran_4_3")

        conventional_4_1 = request.POST.get("conventional_4_1")
        conventional_4_2 = request.POST.get("conventional_4_2")
        conventional_4_3 = request.POST.get("conventional_4_3")

        others_4_1 = request.POST.get("others_4_1")
        others_4_2 = request.POST.get("others_4_2")
        others_4_3 = request.POST.get("others_4_3")

        commissions_1 = request.POST.get("commissions_1")
        commissions_2 = request.POST.get("commissions_2")
        commissions_3 = request.POST.get("commissions_3")

        phone = request.POST.get("phone")
        signature = request.POST.get("signature")
        position = request.POST.get("position")

        data = [
            pl.Series("year_1", [year_1], dtype=pl.String),
            pl.Series("year_2", [year_2], dtype=pl.String),
            pl.Series("year_3", [year_3], dtype=pl.String),
            pl.Series("FHA_1", [float(FHA_1)], dtype=pl.Float64),
            pl.Series("FHA_2", [float(FHA_2)], dtype=pl.Float64),
            pl.Series("FHA_3", [float(FHA_3)], dtype=pl.Float64),
            pl.Series("veteran_1", [float(veteran_1)], dtype=pl.Float64),
            pl.Series("veteran_2", [float(veteran_2)], dtype=pl.Float64),
            pl.Series("veteran_3", [float(veteran_3)], dtype=pl.Float64),
            pl.Series("bank_1", [float(bank_1)], dtype=pl.Float64),
            pl.Series("bank_2", [float(bank_2)], dtype=pl.Float64),
            pl.Series("bank_3", [float(bank_3)], dtype=pl.Float64),
            pl.Series("conventional_1", [float(conventional_1)], dtype=pl.Float64),
            pl.Series("conventional_2", [float(conventional_2)], dtype=pl.Float64),
            pl.Series("conventional_3", [float(conventional_3)], dtype=pl.Float64),
            pl.Series("other_1", [float(other_1)], dtype=pl.Float64),
            pl.Series("other_2", [float(other_2)], dtype=pl.Float64),
            pl.Series("other_3", [float(other_3)], dtype=pl.Float64),
            pl.Series("FHA_2_1", [float(FHA_2_1)], dtype=pl.Float64),
            pl.Series("FHA_2_2", [float(FHA_2_2)], dtype=pl.Float64),
            pl.Series("FHA_2_3", [float(FHA_2_3)], dtype=pl.Float64),
            pl.Series("veteran_2_1", [float(veteran_2_1)], dtype=pl.Float64),
            pl.Series("veteran_2_2", [float(veteran_2_2)], dtype=pl.Float64),
            pl.Series("veteran_2_3", [float(veteran_2_3)], dtype=pl.Float64),
            pl.Series("conventional_2_1", [float(conventional_2_1)], dtype=pl.Float64),
            pl.Series("conventional_2_2", [float(conventional_2_2)], dtype=pl.Float64),
            pl.Series("conventional_2_3", [float(conventional_2_3)], dtype=pl.Float64),
            pl.Series("others_2_1", [float(others_2_1)], dtype=pl.Float64),
            pl.Series("others_2_2", [float(others_2_2)], dtype=pl.Float64),
            pl.Series("others_2_3", [float(others_2_3)], dtype=pl.Float64),
            pl.Series("FHA_3_1", [float(FHA_3_1)], dtype=pl.Float64),
            pl.Series("FHA_3_2", [float(FHA_3_2)], dtype=pl.Float64),
            pl.Series("FHA_3_3", [float(FHA_3_3)], dtype=pl.Float64),
            pl.Series("veteran_3_1", [float(veteran_3_1)], dtype=pl.Float64),
            pl.Series("veteran_3_2", [float(veteran_3_2)], dtype=pl.Float64),
            pl.Series("veteran_3_3", [float(veteran_3_3)], dtype=pl.Float64),
            pl.Series("bank_2_1", [float(bank_2_1)], dtype=pl.Float64),
            pl.Series("bank_2_2", [float(bank_2_2)], dtype=pl.Float64),
            pl.Series("bank_2_3", [float(bank_2_3)], dtype=pl.Float64),
            pl.Series("conventional_3_1", [float(conventional_3_1)], dtype=pl.Float64),
            pl.Series("conventional_3_2", [float(conventional_3_2)], dtype=pl.Float64),
            pl.Series("conventional_3_3", [float(conventional_3_3)], dtype=pl.Float64),
            pl.Series("others_3_1", [float(others_3_1)], dtype=pl.Float64),
            pl.Series("others_3_2", [float(others_3_2)], dtype=pl.Float64),
            pl.Series("others_3_3", [float(others_3_3)], dtype=pl.Float64),
            pl.Series("FHA_4_1", [float(FHA_4_1)], dtype=pl.Float64),
            pl.Series("FHA_4_2", [float(FHA_4_2)], dtype=pl.Float64),
            pl.Series("FHA_4_3", [float(FHA_4_3)], dtype=pl.Float64),
            pl.Series("veteran_4_1", [float(veteran_4_1)], dtype=pl.Float64),
            pl.Series("veteran_4_2", [float(veteran_4_2)], dtype=pl.Float64),
            pl.Series("veteran_4_3", [float(veteran_4_3)], dtype=pl.Float64),
            pl.Series("conventional_4_1", [float(conventional_4_1)], dtype=pl.Float64),
            pl.Series("conventional_4_2", [float(conventional_4_2)], dtype=pl.Float64),
            pl.Series("conventional_4_3", [float(conventional_4_3)], dtype=pl.Float64),
            pl.Series("others_4_1", [float(others_4_1)], dtype=pl.Float64),
            pl.Series("others_4_2", [float(others_4_2)], dtype=pl.Float64),
            pl.Series("others_4_3", [float(others_4_3)], dtype=pl.Float64),
            pl.Series("commissions_1", [float(commissions_1)], dtype=pl.Float64),
            pl.Series("commissions_2", [float(commissions_2)], dtype=pl.Float64),
            pl.Series("commissions_3", [float(commissions_3)], dtype=pl.Float64),
            pl.Series("phone", [phone], dtype=pl.String),
            pl.Series("signature", [signature], dtype=pl.String),
            pl.Series("position", [position], dtype=pl.String),
        ]
        
        df = pl.DataFrame(data)
        DAO().insert_forms(df, "JP_375", 25)

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/balanza_de_pagos/JP-375.html")
