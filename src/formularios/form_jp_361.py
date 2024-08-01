from django.shortcuts import render
from src.dao.data_db_dao import DAO
import csv
import os

def JP_361(request):
    if request.method == "POST":
        # Retrieve form data
        income_expenses_year_1 = request.POST.get("income_expenses_year_1")
        income_expenses_year_2 = request.POST.get("income_expenses_year_2")
        income_life_1 = request.POST.get("income_life_1")
        income_life_2 = request.POST.get("income_life_2")
        income_disability_1 = request.POST.get("income_disability_1")
        income_disability_2 = request.POST.get("income_disability_2")
        income_auto_1 = request.POST.get("income_auto_1")
        income_auto_2 = request.POST.get("income_auto_2")
        income_other_1 = request.POST.get("income_other_1")
        income_other_2 = request.POST.get("income_other_2")
        income_interest_1 = request.POST.get("income_interest_1")
        income_interest_2 = request.POST.get("income_interest_2")
        income_rent_1 = request.POST.get("income_rent_1")
        income_rent_2 = request.POST.get("income_rent_2")
        income_other_2_1 = request.POST.get("income_other_2_1")
        income_other_2_2 = request.POST.get("income_other_2_2")
        total_income_1 = request.POST.get("total_income_1")
        total_income_2 = request.POST.get("total_income_2")
        expenses_life_1 = request.POST.get("expenses_life_1")
        expenses_life_2 = request.POST.get("expenses_life_2")
        expenses_disability_1 = request.POST.get("expenses_disability_1")
        expenses_disability_2 = request.POST.get("expenses_disability_2")
        expenses_auto_1 = request.POST.get("expenses_auto_1")
        expenses_auto_2 = request.POST.get("expenses_auto_2")
        expenses_other_1 = request.POST.get("expenses_other_1")
        expenses_other_2 = request.POST.get("expenses_other_2")
        expenses_salaries_1 = request.POST.get("expenses_salaries_1")
        expenses_salaries_2 = request.POST.get("expenses_salaries_2")
        expenses_interes_1 = request.POST.get("expenses_interes_1")
        expenses_interes_2 = request.POST.get("expenses_interes_2")
        expenses_rent_1 = request.POST.get("expenses_rent_1")
        expenses_rent_2 = request.POST.get("expenses_rent_2")
        expenses_depreciation_1 = request.POST.get("expenses_depreciation_1")
        expenses_depreciation_2 = request.POST.get("expenses_depreciation_2")
        expenses_donations_1 = request.POST.get("expenses_donations_1")
        expenses_donations_2 = request.POST.get("expenses_donations_2")
        expenses_commissions_1 = request.POST.get("expenses_commissions_1")
        expenses_commissions_2 = request.POST.get("expenses_commissions_2")
        expenses_employees_1 = request.POST.get("expenses_employees_1")
        expenses_employees_2 = request.POST.get("expenses_employees_2")
        expenses_brokers_1 = request.POST.get("expenses_brokers_1")
        expenses_brokers_2 = request.POST.get("expenses_brokers_2")
        expenses_other_operational_1 = request.POST.get("expenses_other_operational_1")
        expenses_other_operational_2 = request.POST.get("expenses_other_operational_2")
        total_expenses_1 = request.POST.get("total_expenses_1")
        total_expenses_2 = request.POST.get("total_expenses_2")
        net_profit_1 = request.POST.get("net_profit_1")
        net_profit_2 = request.POST.get("net_profit_2")
        balance_year_1 = request.POST.get("balance_year_1")
        balance_year_2 = request.POST.get("balance_year_2")
        guaranteed_1 = request.POST.get("guaranteed_1")
        guaranteed_2 = request.POST.get("guaranteed_2")
        guaranteed_3 = request.POST.get("guaranteed_3")
        guaranteed_4 = request.POST.get("guaranteed_4")
        veterans_1 = request.POST.get("veterans_1")
        veterans_2 = request.POST.get("veterans_2")
        veterans_3 = request.POST.get("veterans_3")
        veterans_4 = request.POST.get("veterans_4")
        conventional_1 = request.POST.get("conventional_1")
        conventional_2 = request.POST.get("conventional_2")
        conventional_3 = request.POST.get("conventional_3")
        conventional_4 = request.POST.get("conventional_4")
        other_1 = request.POST.get("other_1")
        other_2 = request.POST.get("other_2")
        other_3 = request.POST.get("other_3")
        other_4 = request.POST.get("other_4")
        policy_loans_1 = request.POST.get("policy_loans_1")
        policy_loans_2 = request.POST.get("policy_loans_2")
        policy_loans_3 = request.POST.get("policy_loans_3")
        policy_loans_4 = request.POST.get("policy_loans_4")
        other_specify_1 = request.POST.get("other_specify_1")
        other_specify_2 = request.POST.get("other_specify_2")
        other_specify_3 = request.POST.get("other_specify_3")
        other_specify_4 = request.POST.get("other_specify_4")
        policy_reserves_1 = request.POST.get("policy_reserves_1")
        policy_reserves_2 = request.POST.get("policy_reserves_2")
        accrued_dividends_1 = request.POST.get("accrued_dividends_1")
        accrued_dividends_2 = request.POST.get("accrued_dividends_2")
        signature = request.POST.get("signature")
        date = request.POST.get("date")
        phone = request.POST.get("phone")
        position = request.POST.get("position")

        csv_file_path = "data/cuestionarios/balanza_de_pagos/JP-361.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "income_expenses_year_1",
                        "income_expenses_year_2",
                        "income_life_1",
                        "income_life_2",
                        "income_disability_1",
                        "income_disability_2",
                        "income_auto_1",
                        "income_auto_2",
                        "income_other_1",
                        "income_other_2",
                        "income_interest_1",
                        "income_interest_2",
                        "income_rent_1",
                        "income_rent_2",
                        "income_other_2_1",
                        "income_other_2_2",
                        "total_income_1",
                        "total_income_2",
                        "expenses_life_1",
                        "expenses_life_2",
                        "expenses_disability_1",
                        "expenses_disability_2",
                        "expenses_auto_1",
                        "expenses_auto_2",
                        "expenses_other_1",
                        "expenses_other_2",
                        "expenses_salaries_1",
                        "expenses_salaries_2",
                        "expenses_interes_1",
                        "expenses_interes_2",
                        "expenses_rent_1",
                        "expenses_rent_2",
                        "expenses_depreciation_1",
                        "expenses_depreciation_2",
                        "expenses_donations_1",
                        "expenses_donations_2",
                        "expenses_commissions_1",
                        "expenses_commissions_2",
                        "expenses_employees_1",
                        "expenses_employees_2",
                        "expenses_brokers_1",
                        "expenses_brokers_2",
                        "expenses_other_operational_1",
                        "expenses_other_operational_2",
                        "total_expenses_1",
                        "total_expenses_2",
                        "net_profit_1",
                        "net_profit_2",
                        "balance_year_1",
                        "balance_year_2",
                        "guaranteed_1",
                        "guaranteed_2",
                        "guaranteed_3",
                        "guaranteed_4",
                        "veterans_1",
                        "veterans_2",
                        "veterans_3",
                        "veterans_4",
                        "conventional_1",
                        "conventional_2",
                        "conventional_3",
                        "conventional_4",
                        "other_1",
                        "other_2",
                        "other_3",
                        "other_4",
                        "policy_loans_1",
                        "policy_loans_2",
                        "policy_loans_3",
                        "policy_loans_4",
                        "other_specify_1",
                        "other_specify_2",
                        "other_specify_3",
                        "other_specify_4",
                        "policy_reserves_1",
                        "policy_reserves_2",
                        "accrued_dividends_1",
                        "accrued_dividends_2",
                        "signature",
                        "date",
                        "phone",
                        "position",
                    ]
                )

            writer.writerow(
                [
                    income_expenses_year_1,
                    income_expenses_year_2,
                    income_life_1,
                    income_life_2,
                    income_disability_1,
                    income_disability_2,
                    income_auto_1,
                    income_auto_2,
                    income_other_1,
                    income_other_2,
                    income_interest_1,
                    income_interest_2,
                    income_rent_1,
                    income_rent_2,
                    income_other_2_1,
                    income_other_2_2,
                    total_income_1,
                    total_income_2,
                    expenses_life_1,
                    expenses_life_2,
                    expenses_disability_1,
                    expenses_disability_2,
                    expenses_auto_1,
                    expenses_auto_2,
                    expenses_other_1,
                    expenses_other_2,
                    expenses_salaries_1,
                    expenses_salaries_2,
                    expenses_interes_1,
                    expenses_interes_2,
                    expenses_rent_1,
                    expenses_rent_2,
                    expenses_depreciation_1,
                    expenses_depreciation_2,
                    expenses_donations_1,
                    expenses_donations_2,
                    expenses_commissions_1,
                    expenses_commissions_2,
                    expenses_employees_1,
                    expenses_employees_2,
                    expenses_brokers_1,
                    expenses_brokers_2,
                    expenses_other_operational_1,
                    expenses_other_operational_2,
                    total_expenses_1,
                    total_expenses_2,
                    net_profit_1,
                    net_profit_2,
                    balance_year_1,
                    balance_year_2,
                    guaranteed_1,
                    guaranteed_2,
                    guaranteed_3,
                    guaranteed_4,
                    veterans_1,
                    veterans_2,
                    veterans_3,
                    veterans_4,
                    conventional_1,
                    conventional_2,
                    conventional_3,
                    conventional_4,
                    other_1,
                    other_2,
                    other_3,
                    other_4,
                    policy_loans_1,
                    policy_loans_2,
                    policy_loans_3,
                    policy_loans_4,
                    other_specify_1,
                    other_specify_2,
                    other_specify_3,
                    other_specify_4,
                    policy_reserves_1,
                    policy_reserves_2,
                    accrued_dividends_1,
                    accrued_dividends_2,
                    signature,
                    date,
                    phone,
                    position,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/balanza_de_pagos/JP-361.csv",
            dtypes={
                "income_expenses_year_1": int,
                "income_expenses_year_2": int,
                "income_life_1": float,
                "income_life_2": float,
                "income_disability_1": float,
                "income_disability_2": float,
                "income_auto_1": float,
                "income_auto_2": float,
                "income_other_1": float,
                "income_other_2": float,
                "income_interest_1": float,
                "income_interest_2": float,
                "income_rent_1": float,
                "income_rent_2": float,
                "income_other_2_1": float,
                "income_other_2_2": float,
                "total_income_1": float,
                "total_income_2": float,
                "expenses_life_1": float,
                "expenses_life_2": float,
                "expenses_disability_1": float,
                "expenses_disability_2": float,
                "expenses_auto_1": float,
                "expenses_auto_2": float,
                "expenses_other_1": float,
                "expenses_other_2": float,
                "expenses_salaries_1": float,
                "expenses_salaries_2": float,
                "expenses_interes_1": float,
                "expenses_interes_2": float,
                "expenses_rent_1": float,
                "expenses_rent_2": float,
                "expenses_depreciation_1": float,
                "expenses_depreciation_2": float,
                "expenses_donations_1": float,
                "expenses_donations_2": float,
                "expenses_commissions_1": float,
                "expenses_commissions_2": float,
                "expenses_employees_1": float,
                "expenses_employees_2": float,
                "expenses_brokers_1": float,
                "expenses_brokers_2": float,
                "expenses_other_operational_1": float,
                "expenses_other_operational_2": float,
                "total_expenses_1": float,
                "total_expenses_2": float,
                "net_profit_1": float,
                "net_profit_2": float,
                "balance_year_1": int,
                "balance_year_2": int,
                "guaranteed_1": float,
                "guaranteed_2": float,
                "guaranteed_3": float,
                "guaranteed_4": float,
                "veterans_1": float,
                "veterans_2": float,
                "veterans_3": float,
                "veterans_4": float,
                "conventional_1": float,
                "conventional_2": float,
                "conventional_3": float,
                "conventional_4": float,
                "other_1": float,
                "other_2": float,
                "other_3": float,
                "other_4": float,
                "policy_loans_1": float,
                "policy_loans_2": float,
                "policy_loans_3": float,
                "policy_loans_4": float,
                "other_specify_1": float,
                "other_specify_2": float,
                "other_specify_3": float,
                "other_specify_4": float,
                "policy_reserves_1": float,
                "policy_reserves_2": float,
                "accrued_dividends_1": float,
                "accrued_dividends_2": float,
                "signature": str,
                "date": str,
                "phone": str,
                "position": str,
            },
            table_name="JP_361",
            table_id="2",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/balanza_de_pagos/JP-361.html")
