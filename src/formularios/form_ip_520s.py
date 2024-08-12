from django.shortcuts import render
from src.dao.data_db_dao import DAO
import csv
import os


def IP_520s(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get("company_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")
        legal_form = request.POST.get("legal_form")
        cfc = request.POST.get("cfc")
        business_type = request.POST.get("business_type")
        other_business_type = request.POST.get("other_business_type")
        risk_type = request.POST.get("risk_type")
        branches = request.POST.get("branches")
        branches_if_yes = request.POST.get("branches_if_yes")
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        incomes_premium_earned_1 = request.POST.get("incomes_premium_earned_1")
        incomes_premium_earned_2 = request.POST.get("incomes_premium_earned_2")
        incomes_disability_1 = request.POST.get("incomes_disability_1")
        incomes_disability_2 = request.POST.get("incomes_disability_2")
        incomes_life_1 = request.POST.get("incomes_life_1")
        incomes_life_2 = request.POST.get("incomes_life_2")
        incomes_auto_1 = request.POST.get("incomes_auto_1")
        incomes_auto_2 = request.POST.get("incomes_auto_2")
        incomes_other_1 = request.POST.get("incomes_other_1")
        incomes_other_2 = request.POST.get("incomes_other_2")
        incomes_dividend_1 = request.POST.get("incomes_dividend_1")
        incomes_dividend_2 = request.POST.get("incomes_dividend_2")
        incomes_rent_1 = request.POST.get("incomes_rent_1")
        incomes_rent_2 = request.POST.get("incomes_rent_2")
        incomes_commissions_1 = request.POST.get("incomes_commissions_1")
        incomes_commissions_2 = request.POST.get("incomes_commissions_2")
        incomes_interests_1 = request.POST.get("incomes_interests_1")
        incomes_interests_2 = request.POST.get("incomes_interests_2")
        incomes_capital_gain_loss_1 = request.POST.get("incomes_capital_gain_loss_1")
        incomes_capital_gain_loss_2 = request.POST.get("incomes_capital_gain_loss_2")
        incomes_other_operation_1 = request.POST.get("incomes_other_operation_1")
        incomes_other_operation_2 = request.POST.get("incomes_other_operation_2")
        incomes_total_1 = request.POST.get("incomes_total_1")
        incomes_total_2 = request.POST.get("incomes_total_2")
        expenses_1 = request.POST.get("expenses_1")
        expenses_2 = request.POST.get("expenses_2")
        expenses_premium_earned_1 = request.POST.get("expenses_premium_earned_1")
        expenses_premium_earned_2 = request.POST.get("expenses_premium_earned_2")
        expenses_disability_1 = request.POST.get("expenses_disability_1")
        expenses_disability_2 = request.POST.get("expenses_disability_2")
        expenses_life_1 = request.POST.get("expenses_life_1")
        expenses_life_2 = request.POST.get("expenses_life_2")
        expenses_auto_1 = request.POST.get("expenses_auto_1")
        expenses_auto_2 = request.POST.get("expenses_auto_2")
        expenses_other_1 = request.POST.get("expenses_other_1")
        expenses_other_2 = request.POST.get("expenses_other_2")
        expenses_increase_reserves_1 = request.POST.get("expenses_increase_reserves_1")
        expenses_increase_reserves_2 = request.POST.get("expenses_increase_reserves_2")
        expenses_salaries_wages_bonus_1 = request.POST.get(
            "expenses_salaries_wages_bonus_1"
        )
        expenses_salaries_wages_bonus_2 = request.POST.get(
            "expenses_salaries_wages_bonus_2"
        )
        expenses_commissions_1 = request.POST.get("expenses_commissions_1")
        expenses_commissions_2 = request.POST.get("expenses_commissions_2")
        expenses_to_employees_1 = request.POST.get("expenses_to_employees_1")
        expenses_to_employees_2 = request.POST.get("expenses_to_employees_2")
        expenses_independent_agents_1 = request.POST.get(
            "expenses_independent_agents_1"
        )
        expenses_independent_agents_2 = request.POST.get(
            "expenses_independent_agents_2"
        )
        expenses_interest_1 = request.POST.get("expenses_interest_1")
        expenses_interest_2 = request.POST.get("expenses_interest_2")
        expenses_rent_1 = request.POST.get("expenses_rent_1")
        expenses_rent_2 = request.POST.get("expenses_rent_2")
        expenses_depreciation_1 = request.POST.get("expenses_depreciation_1")
        expenses_depreciation_2 = request.POST.get("expenses_depreciation_2")
        expenses_dividend_policy_holder_1 = request.POST.get(
            "expenses_dividend_policy_holder_1"
        )
        expenses_dividend_policy_holder_2 = request.POST.get(
            "expenses_dividend_policy_holder_2"
        )
        expenses_donation_1 = request.POST.get("expenses_donation_1")
        expenses_donation_2 = request.POST.get("expenses_donation_2")
        expenses_sales_tax_1 = request.POST.get("expenses_sales_tax_1")
        expenses_sales_tax_2 = request.POST.get("expenses_sales_tax_2")
        expenses_machinary_1 = request.POST.get("expenses_machinary_1")
        expenses_machinary_2 = request.POST.get("expenses_machinary_2")
        expenses_other_purchases_1 = request.POST.get("expenses_other_purchases_1")
        expenses_other_purchases_2 = request.POST.get("expenses_other_purchases_2")
        expenses_licenses_1 = request.POST.get("expenses_licenses_1")
        expenses_licenses_2 = request.POST.get("expenses_licenses_2")
        expenses_other_operating_1 = request.POST.get("expenses_other_operating_1")
        expenses_other_operating_2 = request.POST.get("expenses_other_operating_2")
        expenses_total_1 = request.POST.get("expenses_total_1")
        expenses_total_2 = request.POST.get("expenses_total_2")
        gross_profit_1 = request.POST.get("gross_profit_1")
        gross_profit_2 = request.POST.get("gross_profit_2")
        sales_tax_withheld_1 = request.POST.get("sales_tax_withheld_1")
        sales_tax_withheld_2 = request.POST.get("sales_tax_withheld_2")
        name = request.POST.get("name")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-520s.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "company_name",
                        "address",
                        "email",
                        "liaison_officer",
                        "ssn",
                        "tel",
                        "fax",
                        "legal_form",
                        "cfc",
                        "business_type",
                        "other_business_type",
                        "risk_type",
                        "branches",
                        "branches_if_yes",
                        "closing_date",
                        "start_year",
                        "end_year",
                        "incomes_premium_earned_1",
                        "incomes_premium_earned_2",
                        "incomes_disability_1",
                        "incomes_disability_2",
                        "incomes_life_1",
                        "incomes_life_2",
                        "incomes_auto_1",
                        "incomes_auto_2",
                        "incomes_other_1",
                        "incomes_other_2",
                        "incomes_dividend_1",
                        "incomes_dividend_2",
                        "incomes_rent_1",
                        "incomes_rent_2",
                        "incomes_commissions_1",
                        "incomes_commissions_2",
                        "incomes_interests_1",
                        "incomes_interests_2",
                        "incomes_capital_gain_loss_1",
                        "incomes_capital_gain_loss_2",
                        "incomes_other_operation_1",
                        "incomes_other_operation_2",
                        "incomes_total_1",
                        "incomes_total_2",
                        "expenses_1",
                        "expenses_2",
                        "expenses_premium_earned_1",
                        "expenses_premium_earned_2",
                        "expenses_disability_1",
                        "expenses_disability_2",
                        "expenses_life_1",
                        "expenses_life_2",
                        "expenses_auto_1",
                        "expenses_auto_2",
                        "expenses_other_1",
                        "expenses_other_2",
                        "expenses_increase_reserves_1",
                        "expenses_increase_reserves_2",
                        "expenses_salaries_wages_bonus_1",
                        "expenses_salaries_wages_bonus_2",
                        "expenses_commissions_1",
                        "expenses_commissions_2",
                        "expenses_to_employees_1",
                        "expenses_to_employees_2",
                        "expenses_independent_agents_1",
                        "expenses_independent_agents_2",
                        "expenses_interest_1",
                        "expenses_interest_2",
                        "expenses_rent_1",
                        "expenses_rent_2",
                        "expenses_depreciation_1",
                        "expenses_depreciation_2",
                        "expenses_dividend_policy_holder_1",
                        "expenses_dividend_policy_holder_2",
                        "expenses_donation_1",
                        "expenses_donation_2",
                        "expenses_sales_tax_1",
                        "expenses_sales_tax_2",
                        "expenses_machinary_1",
                        "expenses_machinary_2",
                        "expenses_other_purchases_1",
                        "expenses_other_purchases_2",
                        "expenses_licenses_1",
                        "expenses_licenses_2",
                        "expenses_other_operating_1",
                        "expenses_other_operating_2",
                        "expenses_total_1",
                        "expenses_total_2",
                        "gross_profit_1",
                        "gross_profit_2",
                        "sales_tax_withheld_1",
                        "sales_tax_withheld_2",
                        "name",
                        "rank",
                    ]
                )

            writer.writerow(
                [
                    company_name,
                    address,
                    email,
                    liaison_officer,
                    ssn,
                    tel,
                    fax,
                    legal_form,
                    cfc,
                    business_type,
                    other_business_type,
                    risk_type,
                    branches,
                    branches_if_yes,
                    closing_date,
                    start_year,
                    end_year,
                    incomes_premium_earned_1,
                    incomes_premium_earned_2,
                    incomes_disability_1,
                    incomes_disability_2,
                    incomes_life_1,
                    incomes_life_2,
                    incomes_auto_1,
                    incomes_auto_2,
                    incomes_other_1,
                    incomes_other_2,
                    incomes_dividend_1,
                    incomes_dividend_2,
                    incomes_rent_1,
                    incomes_rent_2,
                    incomes_commissions_1,
                    incomes_commissions_2,
                    incomes_interests_1,
                    incomes_interests_2,
                    incomes_capital_gain_loss_1,
                    incomes_capital_gain_loss_2,
                    incomes_other_operation_1,
                    incomes_other_operation_2,
                    incomes_total_1,
                    incomes_total_2,
                    expenses_1,
                    expenses_2,
                    expenses_premium_earned_1,
                    expenses_premium_earned_2,
                    expenses_disability_1,
                    expenses_disability_2,
                    expenses_life_1,
                    expenses_life_2,
                    expenses_auto_1,
                    expenses_auto_2,
                    expenses_other_1,
                    expenses_other_2,
                    expenses_increase_reserves_1,
                    expenses_increase_reserves_2,
                    expenses_salaries_wages_bonus_1,
                    expenses_salaries_wages_bonus_2,
                    expenses_commissions_1,
                    expenses_commissions_2,
                    expenses_to_employees_1,
                    expenses_to_employees_2,
                    expenses_independent_agents_1,
                    expenses_independent_agents_2,
                    expenses_interest_1,
                    expenses_interest_2,
                    expenses_rent_1,
                    expenses_rent_2,
                    expenses_depreciation_1,
                    expenses_depreciation_2,
                    expenses_dividend_policy_holder_1,
                    expenses_dividend_policy_holder_2,
                    expenses_donation_1,
                    expenses_donation_2,
                    expenses_sales_tax_1,
                    expenses_sales_tax_2,
                    expenses_machinary_1,
                    expenses_machinary_2,
                    expenses_other_purchases_1,
                    expenses_other_purchases_2,
                    expenses_licenses_1,
                    expenses_licenses_2,
                    expenses_other_operating_1,
                    expenses_other_operating_2,
                    expenses_total_1,
                    expenses_total_2,
                    gross_profit_1,
                    gross_profit_2,
                    sales_tax_withheld_1,
                    sales_tax_withheld_2,
                    name,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-520s.csv",
            dtypes={
                "company_name": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "ssn": str,
                "tel": str,
                "fax": str,
                "legal_form": str,
                "cfc": str,
                "business_type": str,
                "other_business_type": str,
                "risk_type": str,
                "branches": str,
                "branches_if_yes": str,
                "closing_date": str,
                "start_year": int,
                "end_year": int,
                "incomes_premium_earned_1": float,
                "incomes_premium_earned_2": float,
                "incomes_disability_1": float,
                "incomes_disability_2": float,
                "incomes_life_1": float,
                "incomes_life_2": float,
                "incomes_auto_1": float,
                "incomes_auto_2": float,
                "incomes_other_1": float,
                "incomes_other_2": float,
                "incomes_dividend_1": float,
                "incomes_dividend_2": float,
                "incomes_rent_1": float,
                "incomes_rent_2": float,
                "incomes_commissions_1": float,
                "incomes_commissions_2": float,
                "incomes_interests_1": float,
                "incomes_interests_2": float,
                "incomes_capital_gain_loss_1": float,
                "incomes_capital_gain_loss_2": float,
                "incomes_other_operation_1": float,
                "incomes_other_operation_2": float,
                "incomes_total_1": float,
                "incomes_total_2": float,
                "expenses_1": float,
                "expenses_2": float,
                "expenses_premium_earned_1": float,
                "expenses_premium_earned_2": float,
                "expenses_disability_1": float,
                "expenses_disability_2": float,
                "expenses_life_1": float,
                "expenses_life_2": float,
                "expenses_auto_1": float,
                "expenses_auto_2": float,
                "expenses_other_1": float,
                "expenses_other_2": float,
                "expenses_increase_reserves_1": float,
                "expenses_increase_reserves_2": float,
                "expenses_salaries_wages_bonus_1": float,
                "expenses_salaries_wages_bonus_2": float,
                "expenses_commissions_1": float,
                "expenses_commissions_2": float,
                "expenses_to_employees_1": float,
                "expenses_to_employees_2": float,
                "expenses_independent_agents_1": float,
                "expenses_independent_agents_2": float,
                "expenses_interest_1": float,
                "expenses_interest_2": float,
                "expenses_rent_1": float,
                "expenses_rent_2": float,
                "expenses_depreciation_1": float,
                "expenses_depreciation_2": float,
                "expenses_dividend_policy_holder_1": float,
                "expenses_dividend_policy_holder_2": float,
                "expenses_donation_1": float,
                "expenses_donation_2": float,
                "expenses_sales_tax_1": float,
                "expenses_sales_tax_2": float,
                "expenses_machinary_1": float,
                "expenses_machinary_2": float,
                "expenses_other_purchases_1": float,
                "expenses_other_purchases_2": float,
                "expenses_licenses_1": float,
                "expenses_licenses_2": float,
                "expenses_other_operating_1": float,
                "expenses_other_operating_2": float,
                "expenses_total_1": float,
                "expenses_total_2": float,
                "gross_profit_1": float,
                "gross_profit_2": float,
                "sales_tax_withheld_1": float,
                "sales_tax_withheld_2": float,
                "name": str,
                "rank": str,
            },
            table_name="IP_520s",
            table_id="39",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-520s.html")
