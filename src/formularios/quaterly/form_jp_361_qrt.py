from django.shortcuts import render
from src.dao.data_db_dao import DAO
import csv
import os

def JP_361_qrt(request):
    if request.method == "POST":
        # Retrieve form data
        income_expenses_year_1 = request.POST["income_expenses_year_1"]
        dropdown_fiscal_year_1 = request.POST["dropdown_fiscal_year_1"]
        income_life = request.POST["income_life"]
        income_disability = request.POST["income_disability"]
        income_auto = request.POST["income_auto"]
        income_other = request.POST["income_other"]
        income_interest = request.POST["income_interest"]
        income_rent = request.POST["income_rent"]
        income_other_2 = request.POST["income_other_2"]
        total_income_1 = request.POST["total_income_1"]
        expenses_life = request.POST["expenses_life"]
        expenses_disability = request.POST["expenses_disability"]
        expenses_auto = request.POST["expenses_auto"]
        expenses_other = request.POST["expenses_other"]
        expenses_salaries = request.POST["expenses_salaries"]
        expenses_interest = request.POST["expenses_interest"]
        expenses_rent = request.POST["expenses_rent"]
        expenses_depreciation = request.POST["expenses_depreciation"]
        expenses_donations = request.POST["expenses_donations"]
        expenses_commissions = request.POST["expenses_commissions"]
        expenses_employees = request.POST["expenses_employees"]
        expenses_brokers = request.POST["expenses_brokers"]
        expenses_other_operational = request.POST["expenses_other_operational"]
        total_expenses = request.POST["total_expenses"]
        net_profit = request.POST["net_profit"]
        income_expenses_year_2 = request.POST["income_expenses_year_2"]
        dropdown_fiscal_year_2 = request.POST["dropdown_fiscal_year_2"]
        guaranteed_1 = request.POST["guaranteed_1"]
        guaranteed_2 = request.POST["guaranteed_2"]
        veterans_1 = request.POST["veterans_1"]
        veterans_2 = request.POST["veterans_2"]
        conventional_1 = request.POST["conventional_1"]
        conventional_2 = request.POST["conventional_2"]
        other_1 = request.POST["other_1"]
        other_2 = request.POST["other_2"]
        policy_loans_1 = request.POST["policy_loans_1"]
        policy_loans_2 = request.POST["policy_loans_2"]
        other_specify_1 = request.POST["other_specify_1"]
        other_specify_2 = request.POST["other_specify_2"]
        policy_reserves_1 = request.POST["policy_reserves_1"]
        accrued_dividends_1 = request.POST["accrued_dividends_1"]
        signature = request.POST["signature"]
        position = request.POST["position"]
        date = request.POST["date"]
        phone = request.POST["phone"]

        csv_file_path = "data/cuestionarios/balanza_de_pagos/JP_361_qrt.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "income_expenses_year_1",
                        "dropdown_fiscal_year_1",
                        "income_life",
                        "income_disability",
                        "income_auto",
                        "income_other",
                        "income_interest",
                        "income_rent",
                        "income_other_2",
                        "total_income_1",
                        "expenses_life",
                        "expenses_disability",
                        "expenses_auto",
                        "expenses_other",
                        "expenses_salaries",
                        "expenses_interest",
                        "expenses_rent",
                        "expenses_depreciation",
                        "expenses_donations",
                        "expenses_commissions",
                        "expenses_employees",
                        "expenses_brokers",
                        "expenses_other_operational",
                        "total_expenses",
                        "net_profit",
                        "income_expenses_year_2",
                        "dropdown_fiscal_year_2",
                        "guaranteed_1",
                        "guaranteed_2",
                        "veterans_1",
                        "veterans_2",
                        "conventional_1",
                        "conventional_2",
                        "other_1",
                        "other_2",
                        "policy_loans_1",
                        "policy_loans_2",
                        "other_specify_1",
                        "other_specify_2",
                        "policy_reserves_1",
                        "accrued_dividends_1",
                        "signature",
                        "position",
                        "date",
                        "phone",
                    ]
                )

            writer.writerow(
                [
                    income_expenses_year_1,
                    dropdown_fiscal_year_1,
                    income_life,
                    income_disability,
                    income_auto,
                    income_other,
                    income_interest,
                    income_rent,
                    income_other_2,
                    total_income_1,
                    expenses_life,
                    expenses_disability,
                    expenses_auto,
                    expenses_other,
                    expenses_salaries,
                    expenses_interest,
                    expenses_rent,
                    expenses_depreciation,
                    expenses_donations,
                    expenses_commissions,
                    expenses_employees,
                    expenses_brokers,
                    expenses_other_operational,
                    total_expenses,
                    net_profit,
                    income_expenses_year_2,
                    dropdown_fiscal_year_2,
                    guaranteed_1,
                    guaranteed_2,
                    veterans_1,
                    veterans_2,
                    conventional_1,
                    conventional_2,
                    other_1,
                    other_2,
                    policy_loans_1,
                    policy_loans_2,
                    other_specify_1,
                    other_specify_2,
                    policy_reserves_1,
                    accrued_dividends_1,
                    signature,
                    position,
                    date,
                    phone,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/balanza_de_pagos/JP_361_qrt.csv",
            dtypes={
                    income_expenses_year_1: int,
                    dropdown_fiscal_year_1: str,
                    income_life: int,
                    income_disability:  int,
                    income_auto: int,
                    income_other: int,
                    income_interest: int,
                    income_rent: int,
                    income_other_2: int,
                    total_income_1: int,
                    expenses_life: int,
                    expenses_disability: int,
                    expenses_auto: int,
                    expenses_other: int,
                    expenses_salaries: int,
                    expenses_interest: int,
                    expenses_rent: int,
                    expenses_depreciation: int,
                    expenses_donations: int,
                    expenses_commissions: int,
                    expenses_employees: int,
                    expenses_brokers: int,
                    expenses_other_operational: int,
                    total_expenses: int,
                    net_profit: int,
                    income_expenses_year_2: int,
                    dropdown_fiscal_year_2: str,
                    guaranteed_1: int,
                    guaranteed_2: int,
                    veterans_1: int,
                    veterans_2: int,
                    conventional_1: int,
                    conventional_2: int,
                    other_1: int,
                    other_2: int,
                    policy_loans_1: int,
                    policy_loans_2: int,
                    other_specify_1: int,
                    other_specify_2: int,
                    policy_reserves_1: int,
                    accrued_dividends_1: int,
                    signature: str,
                    position: str,
                    date: str,
                    phone: str,
                
                    
            },
            table_name="JP_361_qrt",
            table_id="60",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/quaterly/balanza_de_pagos/JP-361-qrt.html")