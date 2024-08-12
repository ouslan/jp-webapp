from django.shortcuts import render
from src.dao.data_db_dao import DAO
import csv
import os

def IP_540v(request):

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
        business_function = request.POST.get("business_function")
        branches = request.POST.get("branches")
        branches_yes = request.POST.get("branches_yes")
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        incomes_services_rendered_1 = request.POST.get("incomes_services_rendered_1")
        incomes_services_rendered_2 = request.POST.get("incomes_services_rendered_2")
        incomes_to_business_1 = request.POST.get("incomes_to_business_1")
        incomes_to_business_2 = request.POST.get("incomes_to_business_2")
        incomes_to_personal_pets_1 = request.POST.get("incomes_to_personal_pets_1")
        incomes_to_personal_pets_2 = request.POST.get("incomes_to_personal_pets_2")
        incomes_sale_merchandise_1 = request.POST.get("incomes_sale_merchandise_1")
        incomes_sale_merchandise_2 = request.POST.get("incomes_sale_merchandise_2")
        incomes_rent_of_land_and_building_1 = request.POST.get(
            "incomes_rent_of_land_and_building_1"
        )
        incomes_rent_of_land_and_building_2 = request.POST.get(
            "incomes_rent_of_land_and_building_2"
        )
        incomes_interests_1 = request.POST.get("incomes_interests_1")
        incomes_interests_2 = request.POST.get("incomes_interests_2")
        incomes_capital_gain_or_loss_1 = request.POST.get(
            "incomes_capital_gain_or_loss_1"
        )
        incomes_capital_gain_or_loss_2 = request.POST.get(
            "incomes_capital_gain_or_loss_2"
        )
        incomes_other_operating_income_1 = request.POST.get(
            "incomes_other_operating_income_1"
        )
        incomes_other_operating_income_2 = request.POST.get(
            "incomes_other_operating_income_2"
        )
        incomes_total_1 = request.POST.get("incomes_total_1")
        incomes_total_2 = request.POST.get("incomes_total_2")
        total_expenses_1 = request.POST.get("total_expenses_1")
        total_expenses_2 = request.POST.get("total_expenses_2")
        expenses_salaries_wages_bonus_1 = request.POST.get(
            "expenses_salaries_wages_bonus_1"
        )
        expenses_salaries_wages_bonus_2 = request.POST.get(
            "expenses_salaries_wages_bonus_2"
        )
        expenses_interests_1 = request.POST.get("expenses_interests_1")
        expenses_interests_2 = request.POST.get("expenses_interests_2")
        expenses_rent_1 = request.POST.get("expenses_rent_1")
        expenses_rent_2 = request.POST.get("expenses_rent_2")
        expenses_depreciation_1 = request.POST.get("expenses_depreciation_1")
        expenses_depreciation_2 = request.POST.get("expenses_depreciation_2")
        expenses_bad_debts_1 = request.POST.get("expenses_bad_debts_1")
        expenses_bad_debts_2 = request.POST.get("expenses_bad_debts_2")
        expenses_donations_1 = request.POST.get("expenses_donations_1")
        expenses_donations_2 = request.POST.get("expenses_donations_2")
        expenses_sales_taxes_1 = request.POST.get("expenses_sales_taxes_1")
        expenses_sales_taxes_2 = request.POST.get("expenses_sales_taxes_2")
        expenses_purchases_machinery_1 = request.POST.get(
            "expenses_purchases_machinery_1"
        )
        expenses_purchases_machinery_2 = request.POST.get(
            "expenses_purchases_machinery_2"
        )
        expenses_other_purchases_1 = request.POST.get("expenses_other_purchases_1")
        expenses_other_purchases_2 = request.POST.get("expenses_other_purchases_2")
        expenses_licenses_1 = request.POST.get("expenses_licenses_1")
        expenses_licenses_2 = request.POST.get("expenses_licenses_2")
        expenses_other_operating_1 = request.POST.get("expenses_other_operating_1")
        expenses_other_operating_2 = request.POST.get("expenses_other_operating_2")
        expenses_total_expenses_1 = request.POST.get("expenses_total_expenses_1")
        expenses_total_expenses_2 = request.POST.get("expenses_total_expenses_2")
        net_profit_1 = request.POST.get("net_profit_1")
        net_profit_2 = request.POST.get("net_profit_2")
        profit_income_tax_1 = request.POST.get("profit_income_tax_1")
        profit_income_tax_2 = request.POST.get("profit_income_tax_2")
        profit_after_income_tax_1 = request.POST.get("profit_after_income_tax_1")
        profit_after_income_tax_2 = request.POST.get("profit_after_income_tax_2")
        sales_tax_withheld_1 = request.POST.get("sales_tax_withheld_1")
        sales_tax_withheld_2 = request.POST.get("sales_tax_withheld_2")
        name = request.POST.get("name")
        rank = request.POST.get("name")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-540v.csv"
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
                        "business_function",
                        "branches",
                        "branches_yes",
                        "closing_date",
                        "start_year",
                        "end_year",
                        "incomes_services_rendered_1",
                        "incomes_services_rendered_2",
                        "incomes_to_business_1",
                        "incomes_to_business_2",
                        "incomes_to_personal_pets_1",
                        "incomes_to_personal_pets_2",
                        "incomes_sale_merchandise_1",
                        "incomes_sale_merchandise_2",
                        "incomes_rent_of_land_and_building_1",
                        "incomes_rent_of_land_and_building_2",
                        "incomes_interests_1",
                        "incomes_interests_2",
                        "incomes_capital_gain_or_loss_1",
                        "incomes_capital_gain_or_loss_2",
                        "incomes_other_operating_income_1",
                        "incomes_other_operating_income_2",
                        "incomes_total_1",
                        "incomes_total_2",
                        "total_expenses_1",
                        "total_expenses_2",
                        "expenses_salaries_wages_bonus_1",
                        "expenses_salaries_wages_bonus_2",
                        "expenses_interests_1",
                        "expenses_interests_2",
                        "expenses_rent_1",
                        "expenses_rent_2",
                        "expenses_depreciation_1",
                        "expenses_depreciation_2",
                        "expenses_bad_debts_1",
                        "expenses_bad_debts_2",
                        "expenses_donations_1",
                        "expenses_donations_2",
                        "expenses_sales_taxes_1",
                        "expenses_sales_taxes_2",
                        "expenses_purchases_machinery_1",
                        "expenses_purchases_machinery_2",
                        "expenses_other_purchases_1",
                        "expenses_other_purchases_2",
                        "expenses_licenses_1",
                        "expenses_licenses_2",
                        "expenses_other_operating_1",
                        "expenses_other_operating_2",
                        "expenses_total_expenses_1",
                        "expenses_total_expenses_2",
                        "net_profit_1",
                        "net_profit_2",
                        "profit_income_tax_1",
                        "profit_income_tax_2",
                        "profit_after_income_tax_1",
                        "profit_after_income_tax_2",
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
                    business_function,
                    branches,
                    branches_yes,
                    closing_date,
                    start_year,
                    end_year,
                    incomes_services_rendered_1,
                    incomes_services_rendered_2,
                    incomes_to_business_1,
                    incomes_to_business_2,
                    incomes_to_personal_pets_1,
                    incomes_to_personal_pets_2,
                    incomes_sale_merchandise_1,
                    incomes_sale_merchandise_2,
                    incomes_rent_of_land_and_building_1,
                    incomes_rent_of_land_and_building_2,
                    incomes_interests_1,
                    incomes_interests_2,
                    incomes_capital_gain_or_loss_1,
                    incomes_capital_gain_or_loss_2,
                    incomes_other_operating_income_1,
                    incomes_other_operating_income_2,
                    incomes_total_1,
                    incomes_total_2,
                    total_expenses_1,
                    total_expenses_2,
                    expenses_salaries_wages_bonus_1,
                    expenses_salaries_wages_bonus_2,
                    expenses_interests_1,
                    expenses_interests_2,
                    expenses_rent_1,
                    expenses_rent_2,
                    expenses_depreciation_1,
                    expenses_depreciation_2,
                    expenses_bad_debts_1,
                    expenses_bad_debts_2,
                    expenses_donations_1,
                    expenses_donations_2,
                    expenses_sales_taxes_1,
                    expenses_sales_taxes_2,
                    expenses_purchases_machinery_1,
                    expenses_purchases_machinery_2,
                    expenses_other_purchases_1,
                    expenses_other_purchases_2,
                    expenses_licenses_1,
                    expenses_licenses_2,
                    expenses_other_operating_1,
                    expenses_other_operating_2,
                    expenses_total_expenses_1,
                    expenses_total_expenses_2,
                    net_profit_1,
                    net_profit_2,
                    profit_income_tax_1,
                    profit_income_tax_2,
                    profit_after_income_tax_1,
                    profit_after_income_tax_2,
                    sales_tax_withheld_1,
                    sales_tax_withheld_2,
                    name,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-540v.csv",
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
                "business_function": str,
                "branches": str,
                "branches_yes": str,
                "closing_date": str,
                "start_year": int,
                "end_year": int,
                "incomes_services_rendered_1": float,
                "incomes_services_rendered_2": float,
                "incomes_to_business_1": float,
                "incomes_to_business_2": float,
                "incomes_to_personal_pets_1": float,
                "incomes_to_personal_pets_2": float,
                "incomes_sale_merchandise_1": float,
                "incomes_sale_merchandise_2": float,
                "incomes_rent_of_land_and_building_1": float,
                "incomes_rent_of_land_and_building_2": float,
                "incomes_interests_1": float,
                "incomes_interests_2": float,
                "incomes_capital_gain_or_loss_1": float,
                "incomes_capital_gain_or_loss_2": float,
                "incomes_other_operating_income_1": float,
                "incomes_other_operating_income_2": float,
                "incomes_total_1": float,
                "incomes_total_2": float,
                "total_expenses_1": float,
                "total_expenses_2": float,
                "expenses_salaries_wages_bonus_1": float,
                "expenses_salaries_wages_bonus_2": float,
                "expenses_interests_1": float,
                "expenses_interests_2": float,
                "expenses_rent_1": float,
                "expenses_rent_2": float,
                "expenses_depreciation_1": float,
                "expenses_depreciation_2": float,
                "expenses_bad_debts_1": float,
                "expenses_bad_debts_2": float,
                "expenses_donations_1": float,
                "expenses_donations_2": float,
                "expenses_sales_taxes_1": float,
                "expenses_sales_taxes_2": float,
                "expenses_purchases_machinery_1": float,
                "expenses_purchases_machinery_2": float,
                "expenses_other_purchases_1": float,
                "expenses_other_purchases_2": float,
                "expenses_licenses_1": float,
                "expenses_licenses_2": float,
                "expenses_other_operating_1": float,
                "expenses_other_operating_2": float,
                "expenses_total_expenses_1": float,
                "expenses_total_expenses_2": float,
                "net_profit_1": float,
                "net_profit_2": float,
                "profit_income_tax_1": float,
                "profit_income_tax_2": float,
                "profit_after_income_tax_1": float,
                "profit_after_income_tax_2": float,
                "sales_tax_withheld_1": float,
                "sales_tax_withheld_2": float,
                "name": str,
                "rank": str,
            },
            table_name="IP_540v",
            table_id=12,
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-540v.html")
