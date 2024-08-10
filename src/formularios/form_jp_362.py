from django.shortcuts import render
from src.dao.data_db_dao import DAO
import csv
import os


def JP_362(request):
    if request.method == "POST":
        # Retrieve form data
        year_1 = request.POST.get("year_1")
        year_2 = request.POST.get("year_2")

        company_name = request.POST.get("company_name")

        debts_balance = request.POST.get("debts_balance")
        debts_emision = request.POST.get("debts_emision")
        debts_amortizacion = request.POST.get("debts_amortizacion")
        debts_final = request.POST.get("debts_final")
        debts_interes = request.POST.get("debts_interes")
        debts_acreedor = request.POST.get("debts_acreedor")

        debts_bond_balance = request.POST.get("debts_bond_balance")
        debts_bond_emision = request.POST.get("debts_bond_emision")
        debts_bond_amortizacion = request.POST.get("debts_bond_amortizacion")
        debts_bond_final = request.POST.get("debts_bond_final")
        debts_bond_interes = request.POST.get("debts_bond_interes")
        debts_bond_acreedor = request.POST.get("debts_bond_acreedor")

        debts_promossory_notes_balance = request.POST.get(
            "debts_promossory_notes_balance"
        )
        debts_promossory_notes_emision = request.POST.get(
            "debts_promossory_notes_emision"
        )
        debts_promossory_notes_amortizacion = request.POST.get(
            "debts_promossory_notes_amortizacion"
        )
        debts_promossory_notes_final = request.POST.get("debts_promossory_notes_final")
        debts_promossory_notes_interes = request.POST.get(
            "debts_promossory_notes_interes"
        )
        debts_promossory_notes_acreedor = request.POST.get(
            "debts_promossory_notes_acreedor"
        )

        debts_others_balance = request.POST.get("debts_others_balance")
        debts_others_emision = request.POST.get("debts_others_emision")
        debts_others_amortizacion = request.POST.get("debts_others_amortizacion")
        debts_others_final = request.POST.get("debts_others_final")
        debts_others_interes = request.POST.get("debts_others_interes")
        debts_others_acreedor = request.POST.get("debts_others_acreedor")

        short_promossory_balance = request.POST.get("short_promossory_balance")
        short_promossory_emision = request.POST.get("short_promossory_emision")
        short_promossory_amortizacion = request.POST.get(
            "short_promossory_amortizacion"
        )
        short_promossory_final = request.POST.get("short_promossory_final")
        short_promossory_interes = request.POST.get("short_promossory_interes")
        short_promossory_acreedor = request.POST.get("short_promossory_acreedor")

        short_account_balance = request.POST.get("short_account_balance")
        short_account_emision = request.POST.get("short_account_emision")
        short_account_amortizacion = request.POST.get("short_account_amortizacion")
        short_account_final = request.POST.get("short_account_final")
        short_account_interes = request.POST.get("short_account_interes")
        short_account_acreedor = request.POST.get("short_account_acreedor")

        short_others_balance = request.POST.get("short_others_balance")
        short_others_emision = request.POST.get("short_others_emision")
        short_others_amortizacion = request.POST.get("short_others_amortizacion")
        short_others_final = request.POST.get("short_others_final")
        short_others_interes = request.POST.get("short_others_interes")
        short_others_acreedor = request.POST.get("short_others_acreedor")

        short_term_balance = request.POST.get("short_term_balance")
        short_term_emision = request.POST.get("short_term_emision")
        short_term_amortizacion = request.POST.get("short_term_amortizacion")
        short_term_final = request.POST.get("short_term_final")
        short_term_interes = request.POST.get("short_term_interes")
        short_term_acreedor = request.POST.get("short_term_acreedor")

        assets_balance = request.POST.get("assets_balance")
        assets_emision = request.POST.get("assets_emision")
        assets_amortizacion = request.POST.get("assets_amortizacion")
        assets_final = request.POST.get("assets_final")
        assets_interes = request.POST.get("assets_interes")

        assets_values_balance = request.POST.get("assets_values_balance")
        assets_values_emision = request.POST.get("assets_values_emision")
        assets_values_amortizacion = request.POST.get("assets_values_amortizacion")
        assets_values_final = request.POST.get("assets_values_final")
        assets_values_interes = request.POST.get("assets_values_interes")

        assets_others_balance = request.POST.get("assets_others_balance")
        assets_others_emision = request.POST.get("assets_others_emision")
        assets_others_amortizacion = request.POST.get("assets_others_amortizacion")
        assets_others_final = request.POST.get("assets_others_final")
        assets_others_interes = request.POST.get("assets_others_interes")

        short_balance = request.POST.get("short_balance")
        short_emision = request.POST.get("short_emision")
        short_amortizacion = request.POST.get("short_amortizacion")
        short_final = request.POST.get("short_final")
        short_interes = request.POST.get("short_interes")

        short_balance_balance = request.POST.get("short_balance_balance")
        short_balance_emision = request.POST.get("short_balance_emision")
        short_balance_amortizacion = request.POST.get("short_balance_amortizacion")
        short_balance_final = request.POST.get("short_balance_final")
        short_balance_interes = request.POST.get("short_balance_interes")

        short_accouts_balance = request.POST.get("short_accouts_balance")
        short_accouts_emision = request.POST.get("short_accouts_emision")
        short_accouts_amortizacion = request.POST.get("short_accouts_amortizacion")
        short_accouts_final = request.POST.get("short_accouts_final")
        short_accouts_interes = request.POST.get("short_accouts_interes")

        short_others_balance_2 = request.POST.get("short_others_balance_2")
        short_others_emision_2 = request.POST.get("short_others_emision_2")
        short_others_amortizacion_2 = request.POST.get("short_others_amortizacion_2")
        short_others_final_2 = request.POST.get("short_others_final_2")
        short_others_interes_2 = request.POST.get("short_others_interes_2")

        signature = request.POST.get("signature")
        position = request.POST.get("position")
        date = request.POST.get("date")
        phone = request.POST.get("phone")

        csv_file_path = "data/cuestionarios/balanza_de_pagos/JP-362.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "year_1",
                        "year_2",
                        "company_name",
                        "debts_balance",
                        "debts_emision",
                        "debts_amortizacion",
                        "debts_final",
                        "debts_interes",
                        "debts_acreedor",
                        "debts_bond_balance",
                        "debts_bond_emision",
                        "debts_bond_amortizacion",
                        "debts_bond_final",
                        "debts_bond_interes",
                        "debts_bond_acreedor",
                        "debts_promossory_notes_balance",
                        "debts_promossory_notes_emision",
                        "debts_promossory_notes_amortizacion",
                        "debts_promossory_notes_final",
                        "debts_promossory_notes_interes",
                        "debts_promossory_notes_acreedor",
                        "debts_others_balance",
                        "debts_others_emision",
                        "debts_others_amortizacion",
                        "debts_others_final",
                        "debts_others_interes",
                        "debts_others_acreedor",
                        "short_term_balance",
                        "short_term_emision",
                        "short_term_amortizacion",
                        "short_term_final",
                        "short_term_interes",
                        "short_term_acreedor",
                        "short_promossory_balance",
                        "short_promossory_emision",
                        "short_promossory_amortizacion",
                        "short_promossory_final",
                        "short_promossory_interes",
                        "short_promossory_acreedor",
                        "short_account_balance",
                        "short_account_emision",
                        "short_account_amortizacion",
                        "short_account_final",
                        "short_account_interes",
                        "short_account_acreedor",
                        "short_others_balance",
                        "short_others_emision",
                        "short_others_amortizacion",
                        "short_others_final",
                        "short_others_interes",
                        "short_others_acreedor",
                        "assets_balance",
                        "assets_emision",
                        "assets_amortizacion",
                        "assets_final",
                        "assets_interes",
                        "assets_values_balance",
                        "assets_values_emision",
                        "assets_values_amortizacion",
                        "assets_values_final",
                        "assets_values_interes",
                        "assets_others_balance",
                        "assets_others_emision",
                        "assets_others_amortizacion",
                        "assets_others_final",
                        "assets_others_interes",
                        "short_balance",
                        "short_emision",
                        "short_amortizacion",
                        "short_final",
                        "short_interes",
                        "short_balance_balance",
                        "short_balance_emision",
                        "short_balance_amortizacion",
                        "short_balance_final",
                        "short_balance_interes",
                        "short_accouts_balance",
                        "short_accouts_emision",
                        "short_accouts_amortizacion",
                        "short_accouts_final",
                        "short_accouts_interes",
                        "short_others_balance_2",
                        "short_others_emision_2",
                        "short_others_amortizacion_2",
                        "short_others_final_2",
                        "short_others_interes_2",
                        "signature",
                        "position",
                        "date",
                        "phone",
                    ]
                )

            writer.writerow(
                [
                    year_1,
                    year_2,
                    company_name,
                    debts_balance,
                    debts_emision,
                    debts_amortizacion,
                    debts_final,
                    debts_interes,
                    debts_acreedor,
                    debts_bond_balance,
                    debts_bond_emision,
                    debts_bond_amortizacion,
                    debts_bond_final,
                    debts_bond_interes,
                    debts_bond_acreedor,
                    debts_promossory_notes_balance,
                    debts_promossory_notes_emision,
                    debts_promossory_notes_amortizacion,
                    debts_promossory_notes_final,
                    debts_promossory_notes_interes,
                    debts_promossory_notes_acreedor,
                    debts_others_balance,
                    debts_others_emision,
                    debts_others_amortizacion,
                    debts_others_final,
                    debts_others_interes,
                    debts_others_acreedor,
                    short_term_balance,
                    short_term_emision,
                    short_term_amortizacion,
                    short_term_final,
                    short_term_interes,
                    short_term_acreedor,
                    short_promossory_balance,
                    short_promossory_emision,
                    short_promossory_amortizacion,
                    short_promossory_final,
                    short_promossory_interes,
                    short_promossory_acreedor,
                    short_account_balance,
                    short_account_emision,
                    short_account_amortizacion,
                    short_account_final,
                    short_account_interes,
                    short_account_acreedor,
                    short_others_balance,
                    short_others_emision,
                    short_others_amortizacion,
                    short_others_final,
                    short_others_interes,
                    short_others_acreedor,
                    assets_balance,
                    assets_emision,
                    assets_amortizacion,
                    assets_final,
                    assets_interes,
                    assets_values_balance,
                    assets_values_emision,
                    assets_values_amortizacion,
                    assets_values_final,
                    assets_values_interes,
                    assets_others_balance,
                    assets_others_emision,
                    assets_others_amortizacion,
                    assets_others_final,
                    assets_others_interes,
                    short_balance,
                    short_emision,
                    short_amortizacion,
                    short_final,
                    short_interes,
                    short_balance_balance,
                    short_balance_emision,
                    short_balance_amortizacion,
                    short_balance_final,
                    short_balance_interes,
                    short_accouts_balance,
                    short_accouts_emision,
                    short_accouts_amortizacion,
                    short_accouts_final,
                    short_accouts_interes,
                    short_others_balance_2,
                    short_others_emision_2,
                    short_others_amortizacion_2,
                    short_others_final_2,
                    short_others_interes_2,
                    signature,
                    position,
                    date,
                    phone,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/balanza_de_pagos/JP-362.csv",
            dtypes={
                "year_1": int,
                "year_2": int,
                "company_name": str,
                "debts_balance": float,
                "debts_emision": float,
                "debts_amortizacion": float,
                "debts_final": float,
                "debts_interes": float,
                "debts_acreedor": str,
                "debts_bond_balance": float,
                "debts_bond_emision": float,
                "debts_bond_amortizacion": float,
                "debts_bond_final": float,
                "debts_bond_interes": float,
                "debts_bond_acreedor": str,
                "debts_promossory_notes_balance": float,
                "debts_promossory_notes_emision": float,
                "debts_promossory_notes_amortizacion": float,
                "debts_promossory_notes_final": float,
                "debts_promossory_notes_interes": float,
                "debts_promossory_notes_acreedor": str,
                "debts_others_balance": float,
                "debts_others_emision": float,
                "debts_others_amortizacion": float,
                "debts_others_final": float,
                "debts_others_interes": float,
                "debts_others_acreedor": str,
                "short_term_balance": float,
                "short_term_emision": float,
                "short_term_amortizacion": float,
                "short_term_final": float,
                "short_term_interes": float,
                "short_term_acreedor": str,
                "short_promossory_balance": float,
                "short_promossory_emision": float,
                "short_promossory_amortizacion": float,
                "short_promossory_final": float,
                "short_promossory_interes": float,
                "short_promossory_acreedor": str,
                "short_account_balance": float,
                "short_account_emision": float,
                "short_account_amortizacion": float,
                "short_account_final": float,
                "short_account_interes": float,
                "short_account_acreedor": str,
                "short_others_balance": float,
                "short_others_emision": float,
                "short_others_amortizacion": float,
                "short_others_final": float,
                "short_others_interes": float,
                "short_others_acreedor": str,
                "assets_balance": float,
                "assets_emision": float,
                "assets_amortizacion": float,
                "assets_final": float,
                "assets_interes": float,
                "assets_values_balance": float,
                "assets_values_emision": float,
                "assets_values_amortizacion": float,
                "assets_values_final": float,
                "assets_values_interes": float,
                "assets_others_balance": float,
                "assets_others_emision": float,
                "assets_others_amortizacion": float,
                "assets_others_final": float,
                "assets_others_interes": float,
                "short_balance": float,
                "short_emision": float,
                "short_amortizacion": float,
                "short_final": float,
                "short_interes": float,
                "short_balance_balance": float,
                "short_balance_emision": float,
                "short_balance_amortizacion": float,
                "short_balance_final": float,
                "short_balance_interes": float,
                "short_accouts_balance": float,
                "short_accouts_emision": float,
                "short_accouts_amortizacion": float,
                "short_accouts_final": float,
                "short_accouts_interes": float,
                "short_others_balance_2": float,
                "short_others_emision_2": float,
                "short_others_amortizacion_2": float,
                "short_others_final_2": float,
                "short_others_interes_2": float,
                "signature": str,
                "position": str,
                "date": str,
                "phone": str,
            },
            table_name="JP_362",
            table_id="3",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/balanza_de_pagos/JP-362.html")
