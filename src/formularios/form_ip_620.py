from django.shortcuts import render
from src.dao.data_db_dao import DAO
import csv
import os


def IP_620(request):
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

        patients_service_revenue_from_persons_1 = request.POST.get(
            "patients_service_revenue_from_persons_1"
        )
        patients_service_revenue_from_persons_2 = request.POST.get(
            "patients_service_revenue_from_persons_2"
        )
        patients_service_revenue_from_industries_business_1 = request.POST.get(
            "patients_service_revenue_from_industries_business_1"
        )
        patients_service_revenue_from_industries_business_2 = request.POST.get(
            "patients_service_revenue_from_industries_business_2"
        )
        contractual_adjustments_1 = request.POST.get("contractual_adjustments_1")
        contractual_adjustments_2 = request.POST.get("contractual_adjustments_2")
        net_patient_service_revenue_1 = request.POST.get(
            "net_patient_service_revenue_1"
        )
        net_patient_service_revenue_2 = request.POST.get(
            "net_patient_service_revenue_2"
        )
        other_incomes_1 = request.POST.get("other_incomes_1")
        other_incomes_2 = request.POST.get("other_incomes_2")
        other_incomes_rent_1 = request.POST.get("other_incomes_rent_1")
        other_incomes_rent_2 = request.POST.get("other_incomes_rent_2")
        other_incomes_interest_1 = request.POST.get("other_incomes_interest_1")
        other_incomes_interest_2 = request.POST.get("other_incomes_interest_2")
        other_incomes_capital_gain_loss_1 = request.POST.get(
            "other_incomes_capital_gain_loss_1"
        )
        other_incomes_capital_gain_loss_2 = request.POST.get(
            "other_incomes_capital_gain_loss_2"
        )
        other_incomes_operating_1 = request.POST.get("other_incomes_operating_1")
        other_incomes_operating_2 = request.POST.get("other_incomes_operating_2")
        total_incomes_1 = request.POST.get("total_incomes_1")
        total_incomes_2 = request.POST.get("total_incomes_2")
        total_expenses_1 = request.POST.get("total_expenses_1")
        total_expenses_2 = request.POST.get("total_expenses_2")
        expenses_salaries_wages_bonus_1 = request.POST.get(
            "expenses_salaries_wages_bonus_1"
        )
        expenses_salaries_wages_bonus_2 = request.POST.get(
            "expenses_salaries_wages_bonus_2"
        )
        expenses_interest_1 = request.POST.get("expenses_interest_1")
        expenses_interest_2 = request.POST.get("expenses_interest_2")
        expenses_rent_1 = request.POST.get("expenses_rent_1")
        expenses_rent_2 = request.POST.get("expenses_rent_2")
        expenses_food_patients_1 = request.POST.get("expenses_food_patients_1")
        expenses_food_patients_2 = request.POST.get("expenses_food_patients_2")
        expenses_free_food_to_employees_1 = request.POST.get(
            "expenses_free_food_to_employees_1"
        )
        expenses_free_food_to_employees_2 = request.POST.get(
            "expenses_free_food_to_employees_2"
        )
        expenses_uniforms_1 = request.POST.get("expenses_uniforms_1")
        expenses_uniforms_2 = request.POST.get("expenses_uniforms_2")
        expenses_depreciation_1 = request.POST.get("expenses_depreciation_1")
        expenses_depreciation_2 = request.POST.get("expenses_depreciation_2")
        expenses_bad_debts_1 = request.POST.get("expenses_bad_debts_1")
        expenses_bad_debts_2 = request.POST.get("expenses_bad_debts_2")
        expenses_donations_1 = request.POST.get("expenses_donations_1")
        expenses_donations_2 = request.POST.get("expenses_donations_2")
        expenses_sales_tax_1 = request.POST.get("expenses_sales_tax_1")
        expenses_sales_tax_2 = request.POST.get("expenses_sales_tax_2")
        expenses_machinery_1 = request.POST.get("expenses_machinery_1")
        expenses_machinery_2 = request.POST.get("expenses_machinery_2")
        expenses_on_other_purchases_1 = request.POST.get(
            "expenses_on_other_purchases_1"
        )
        expenses_on_other_purchases_2 = request.POST.get(
            "expenses_on_other_purchases_2"
        )
        expenses_licenses_1 = request.POST.get("expenses_licenses_1")
        expenses_licenses_2 = request.POST.get("expenses_licenses_2")
        expenses_other_operating_1 = request.POST.get("expenses_other_operating_1")
        expenses_other_operating_2 = request.POST.get("expenses_other_operating_2")
        net_profit_loss_1 = request.POST.get("net_profit_loss_1")
        net_profit_loss_2 = request.POST.get("net_profit_loss_2")
        net_profit_loss_income_tax_1 = request.POST.get("net_profit_loss_income_tax_1")
        net_profit_loss_income_tax_2 = request.POST.get("net_profit_loss_income_tax_2")
        net_profit_after_tax_1 = request.POST.get("net_profit_after_tax_1")
        net_profit_after_tax_2 = request.POST.get("net_profit_after_tax_2")
        sales_and_use_withheld_1 = request.POST.get("sales_and_use_withheld_1")
        sales_and_use_withheld_2 = request.POST.get("sales_and_use_withheld_2")
        name = request.POST.get("name")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-620.csv"
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
                        "patients_service_revenue_from_persons_1",
                        "patients_service_revenue_from_persons_2",
                        "patients_service_revenue_from_industries_business_1",
                        "patients_service_revenue_from_industries_business_2",
                        "contractual_adjustments_1",
                        "contractual_adjustments_2",
                        "net_patient_service_revenue_1",
                        "net_patient_service_revenue_2",
                        "other_incomes_1",
                        "other_incomes_2",
                        "other_incomes_rent_1",
                        "other_incomes_rent_2",
                        "other_incomes_interest_1",
                        "other_incomes_interest_2",
                        "other_incomes_capital_gain_loss_1",
                        "other_incomes_capital_gain_loss_2",
                        "other_incomes_operating_1",
                        "other_incomes_operating_2",
                        "total_incomes_1",
                        "total_incomes_2",
                        "total_expenses_1",
                        "total_expenses_2",
                        "expenses_salaries_wages_bonus_1",
                        "expenses_salaries_wages_bonus_2",
                        "expenses_interest_1",
                        "expenses_interest_2",
                        "expenses_rent_1",
                        "expenses_rent_2",
                        "expenses_food_patients_1",
                        "expenses_food_patients_2",
                        "expenses_free_food_to_employees_1",
                        "expenses_free_food_to_employees_2",
                        "expenses_uniforms_1",
                        "expenses_uniforms_2",
                        "expenses_depreciation_1",
                        "expenses_depreciation_2",
                        "expenses_bad_debts_1",
                        "expenses_bad_debts_2",
                        "expenses_donations_1",
                        "expenses_donations_2",
                        "expenses_sales_tax_1",
                        "expenses_sales_tax_2",
                        "expenses_machinery_1",
                        "expenses_machinery_2",
                        "expenses_on_other_purchases_1",
                        "expenses_on_other_purchases_2",
                        "expenses_licenses_1",
                        "expenses_licenses_2",
                        "expenses_other_operating_1",
                        "expenses_other_operating_2",
                        "net_profit_loss_1",
                        "net_profit_loss_2",
                        "net_profit_loss_income_tax_1",
                        "net_profit_loss_income_tax_2",
                        "net_profit_after_tax_1",
                        "net_profit_after_tax_2",
                        "sales_and_use_withheld_1",
                        "sales_and_use_withheld_2",
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
                    patients_service_revenue_from_persons_1,
                    patients_service_revenue_from_persons_2,
                    patients_service_revenue_from_industries_business_1,
                    patients_service_revenue_from_industries_business_2,
                    contractual_adjustments_1,
                    contractual_adjustments_2,
                    net_patient_service_revenue_1,
                    net_patient_service_revenue_2,
                    other_incomes_1,
                    other_incomes_2,
                    other_incomes_rent_1,
                    other_incomes_rent_2,
                    other_incomes_interest_1,
                    other_incomes_interest_2,
                    other_incomes_capital_gain_loss_1,
                    other_incomes_capital_gain_loss_2,
                    other_incomes_operating_1,
                    other_incomes_operating_2,
                    total_incomes_1,
                    total_incomes_2,
                    total_expenses_1,
                    total_expenses_2,
                    expenses_salaries_wages_bonus_1,
                    expenses_salaries_wages_bonus_2,
                    expenses_interest_1,
                    expenses_interest_2,
                    expenses_rent_1,
                    expenses_rent_2,
                    expenses_food_patients_1,
                    expenses_food_patients_2,
                    expenses_free_food_to_employees_1,
                    expenses_free_food_to_employees_2,
                    expenses_uniforms_1,
                    expenses_uniforms_2,
                    expenses_depreciation_1,
                    expenses_depreciation_2,
                    expenses_bad_debts_1,
                    expenses_bad_debts_2,
                    expenses_donations_1,
                    expenses_donations_2,
                    expenses_sales_tax_1,
                    expenses_sales_tax_2,
                    expenses_machinery_1,
                    expenses_machinery_2,
                    expenses_on_other_purchases_1,
                    expenses_on_other_purchases_2,
                    expenses_licenses_1,
                    expenses_licenses_2,
                    expenses_other_operating_1,
                    expenses_other_operating_2,
                    net_profit_loss_1,
                    net_profit_loss_2,
                    net_profit_loss_income_tax_1,
                    net_profit_loss_income_tax_2,
                    net_profit_after_tax_1,
                    net_profit_after_tax_2,
                    sales_and_use_withheld_1,
                    sales_and_use_withheld_2,
                    name,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-620.csv",
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
                "patients_service_revenue_from_persons_1": float,
                "patients_service_revenue_from_persons_2": float,
                "patients_service_revenue_from_industries_business_1": float,
                "patients_service_revenue_from_industries_business_2": float,
                "contractual_adjustments_1": float,
                "contractual_adjustments_2": float,
                "net_patient_service_revenue_1": float,
                "net_patient_service_revenue_2": float,
                "other_incomes_1": float,
                "other_incomes_2": float,
                "other_incomes_rent_1": float,
                "other_incomes_rent_2": float,
                "other_incomes_interest_1": float,
                "other_incomes_interest_2": float,
                "other_incomes_capital_gain_loss_1": float,
                "other_incomes_capital_gain_loss_2": float,
                "other_incomes_operating_1": float,
                "other_incomes_operating_2": float,
                "total_incomes_1": float,
                "total_incomes_2": float,
                "total_expenses_1": float,
                "total_expenses_2": float,
                "expenses_salaries_wages_bonus_1": float,
                "expenses_salaries_wages_bonus_2": float,
                "expenses_interest_1": float,
                "expenses_interest_2": float,
                "expenses_rent_1": float,
                "expenses_rent_2": float,
                "expenses_food_patients_1": float,
                "expenses_food_patients_2": float,
                "expenses_free_food_to_employees_1": float,
                "expenses_free_food_to_employees_2": float,
                "expenses_uniforms_1": float,
                "expenses_uniforms_2": float,
                "expenses_depreciation_1": float,
                "expenses_depreciation_2": float,
                "expenses_bad_debts_1": float,
                "expenses_bad_debts_2": float,
                "expenses_donations_1": float,
                "expenses_donations_2": float,
                "expenses_sales_tax_1": float,
                "expenses_sales_tax_2": float,
                "expenses_machinery_1": float,
                "expenses_machinery_2": float,
                "expenses_on_other_purchases_1": float,
                "expenses_on_other_purchases_2": float,
                "expenses_licenses_1": float,
                "expenses_licenses_2": float,
                "expenses_other_operating_1": float,
                "expenses_other_operating_2": float,
                "net_profit_loss_1": float,
                "net_profit_loss_2": float,
                "net_profit_loss_income_tax_1": float,
                "net_profit_loss_income_tax_2": float,
                "net_profit_after_tax_1": float,
                "net_profit_after_tax_2": float,
                "sales_and_use_withheld_1": float,
                "sales_and_use_withheld_2": float,
                "name": str,
                "rank": str,
            },
            table_name="IP_620",
            table_id=22,
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-620.html")
