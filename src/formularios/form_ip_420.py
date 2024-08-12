from django.shortcuts import render
from src.dao.data_db_dao import DAO
import csv
import os

def IP_420(request):
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
        main_line = request.POST.get("main_line")
        business_type = request.POST.get("business_type")
        other_business_type = request.POST.get("other_business_type")
        accounting_period = request.POST.get("accounting_period")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        incomes_sales_1 = request.POST.get("incomes_sales_1")
        incomes_sales_2 = request.POST.get("incomes_sales_2")
        incomes_from_people_1 = request.POST.get("incomes_from_people_1")
        incomes_from_people_2 = request.POST.get("incomes_from_people_2")
        incomes_industries_businesses_1 = request.POST.get(
            "incomes_industries_businesses_1"
        )
        incomes_industries_businesses_2 = request.POST.get(
            "incomes_industries_businesses_2"
        )
        incomes_less_cost_1 = request.POST.get("incomes_less_cost_1")
        incomes_less_cost_2 = request.POST.get("incomes_less_cost_2")
        incomes_inventory_beginning_1 = request.POST.get(
            "incomes_inventory_beginning_1"
        )
        incomes_inventory_beginning_2 = request.POST.get(
            "incomes_inventory_beginning_2"
        )
        incomes_purchases_1 = request.POST.get("incomes_purchases_1")
        incomes_purchases_2 = request.POST.get("incomes_purchases_2")
        incomes_inventory_end_1 = request.POST.get("incomes_inventory_end_1")
        incomes_inventory_end_2 = request.POST.get("incomes_inventory_end_2")
        incomes_gross_profit_1 = request.POST.get("incomes_gross_profit_1")
        incomes_gross_profit_2 = request.POST.get("incomes_gross_profit_2")
        other_operation_incomes_1 = request.POST.get("other_operation_incomes_1")
        other_operation_incomes_2 = request.POST.get("other_operation_incomes_2")
        incomes_interests_1 = request.POST.get("incomes_interests_1")
        incomes_interests_2 = request.POST.get("incomes_interests_2")
        incomes_rent_1 = request.POST.get("incomes_rent_1")
        incomes_rent_2 = request.POST.get("incomes_rent_2")
        incomes_gain_loss_1 = request.POST.get("incomes_gain_loss_1")
        incomes_gain_loss_2 = request.POST.get("incomes_gain_loss_2")
        incomes_dividends_1 = request.POST.get("incomes_dividends_1")
        incomes_dividends_2 = request.POST.get("incomes_dividends_2")
        other_incomes_1 = request.POST.get("other_incomes_1")
        other_incomes_2 = request.POST.get("other_incomes_2")
        incomes_total_gross_1 = request.POST.get("incomes_total_gross_1")
        incomes_total_gross_2 = request.POST.get("incomes_total_gross_2")
        expenses_1 = request.POST.get("expenses_1")
        expenses_2 = request.POST.get("expenses_2")
        expenses_salaries_wages_bonus_1 = request.POST.get(
            "expenses_salaries_wages_bonus_1"
        )
        expenses_salaries_wages_bonus_2 = request.POST.get(
            "expenses_salaries_wages_bonus_2"
        )
        expenses_interests_1 = request.POST.get("expenses_interests_1")
        expenses_interests_2 = request.POST.get("expenses_interests_2")
        expenses_depreciation_1 = request.POST.get("expenses_depreciation_1")
        expenses_depreciation_2 = request.POST.get("expenses_depreciation_2")
        expenses_rent_1 = request.POST.get("expenses_rent_1")
        expenses_rent_2 = request.POST.get("expenses_rent_2")
        expenses_bad_debts_1 = request.POST.get("expenses_bad_debts_1")
        expenses_bad_debts_2 = request.POST.get("expenses_bad_debts_2")
        expenses_donations_1 = request.POST.get("expenses_donations_1")
        expenses_donations_2 = request.POST.get("expenses_donations_2")
        expenses_sales_taxes_1 = request.POST.get("expenses_sales_taxes_1")
        expenses_sales_taxes_2 = request.POST.get("expenses_sales_taxes_2")
        expenses_machinary_1 = request.POST.get("expenses_machinary_1")
        expenses_machinary_2 = request.POST.get("expenses_machinary_2")
        expenses_other_purchases_1 = request.POST.get("expenses_other_purchases_1")
        expenses_other_purchases_2 = request.POST.get("expenses_other_purchases_2")
        expenses_licenses_1 = request.POST.get("expenses_licenses_1")
        expenses_licenses_2 = request.POST.get("expenses_licenses_2")
        expenses_other_operations_1 = request.POST.get("expenses_other_operations_1")
        expenses_other_operations_2 = request.POST.get("expenses_other_operations_2")
        expenses_total_operations_1 = request.POST.get("expenses_total_operations_1")
        expenses_total_operations_2 = request.POST.get("expenses_total_operations_2")
        gross_profit_1 = request.POST.get("gross_profit_1")
        gross_profit_2 = request.POST.get("gross_profit_2")
        profit_income_tax_1 = request.POST.get("profit_income_tax_1")
        profit_income_tax_2 = request.POST.get("profit_income_tax_2")
        profit_after_income_tax_1 = request.POST.get("profit_after_income_tax_1")
        profit_after_income_tax_2 = request.POST.get("profit_after_income_tax_2")
        sales_tax_1 = request.POST.get("sales_tax_1")
        sales_tax_2 = request.POST.get("sales_tax_2")
        name = request.POST.get("name")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-420.csv"
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
                        "main_line",
                        "business_type",
                        "other_business_type",
                        "accounting_period",
                        "start_year",
                        "end_year",
                        "incomes_sales_1",
                        "incomes_sales_2",
                        "incomes_from_people_1",
                        "incomes_from_people_2",
                        "incomes_industries_businesses_1",
                        "incomes_industries_businesses_2",
                        "incomes_less_cost_1",
                        "incomes_less_cost_2",
                        "incomes_inventory_beginning_1",
                        "incomes_inventory_beginning_2",
                        "incomes_purchases_1",
                        "incomes_purchases_2",
                        "incomes_inventory_end_1",
                        "incomes_inventory_end_2",
                        "incomes_gross_profit_1",
                        "incomes_gross_profit_2",
                        "other_operation_incomes_1",
                        "other_operation_incomes_2",
                        "incomes_interests_1",
                        "incomes_interests_2",
                        "incomes_rent_1",
                        "incomes_rent_2",
                        "incomes_gain_loss_1",
                        "incomes_gain_loss_2",
                        "incomes_dividends_1",
                        "incomes_dividends_2",
                        "other_incomes_1",
                        "other_incomes_2",
                        "incomes_total_gross_1",
                        "incomes_total_gross_2",
                        "expenses_1",
                        "expenses_2",
                        "expenses_salaries_wages_bonus_1",
                        "expenses_salaries_wages_bonus_2",
                        "expenses_interests_1",
                        "expenses_interests_2",
                        "expenses_depreciation_1",
                        "expenses_depreciation_2",
                        "expenses_rent_1",
                        "expenses_rent_2",
                        "expenses_bad_debts_1",
                        "expenses_bad_debts_2",
                        "expenses_donations_1",
                        "expenses_donations_2",
                        "expenses_sales_taxes_1",
                        "expenses_sales_taxes_2",
                        "expenses_machinary_1",
                        "expenses_machinary_2",
                        "expenses_other_purchases_1",
                        "expenses_other_purchases_2",
                        "expenses_licenses_1",
                        "expenses_licenses_2",
                        "expenses_other_operations_1",
                        "expenses_other_operations_2",
                        "expenses_total_operations_1",
                        "expenses_total_operations_2",
                        "gross_profit_1",
                        "gross_profit_2",
                        "profit_income_tax_1",
                        "profit_income_tax_2",
                        "profit_after_income_tax_1",
                        "profit_after_income_tax_2",
                        "sales_tax_1",
                        "sales_tax_2",
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
                    main_line,
                    business_type,
                    other_business_type,
                    accounting_period,
                    start_year,
                    end_year,
                    incomes_sales_1,
                    incomes_sales_2,
                    incomes_from_people_1,
                    incomes_from_people_2,
                    incomes_industries_businesses_1,
                    incomes_industries_businesses_2,
                    incomes_less_cost_1,
                    incomes_less_cost_2,
                    incomes_inventory_beginning_1,
                    incomes_inventory_beginning_2,
                    incomes_purchases_1,
                    incomes_purchases_2,
                    incomes_inventory_end_1,
                    incomes_inventory_end_2,
                    incomes_gross_profit_1,
                    incomes_gross_profit_2,
                    other_operation_incomes_1,
                    other_operation_incomes_2,
                    incomes_interests_1,
                    incomes_interests_2,
                    incomes_rent_1,
                    incomes_rent_2,
                    incomes_gain_loss_1,
                    incomes_gain_loss_2,
                    incomes_dividends_1,
                    incomes_dividends_2,
                    other_incomes_1,
                    other_incomes_2,
                    incomes_total_gross_1,
                    incomes_total_gross_2,
                    expenses_1,
                    expenses_2,
                    expenses_salaries_wages_bonus_1,
                    expenses_salaries_wages_bonus_2,
                    expenses_interests_1,
                    expenses_interests_2,
                    expenses_depreciation_1,
                    expenses_depreciation_2,
                    expenses_rent_1,
                    expenses_rent_2,
                    expenses_bad_debts_1,
                    expenses_bad_debts_2,
                    expenses_donations_1,
                    expenses_donations_2,
                    expenses_sales_taxes_1,
                    expenses_sales_taxes_2,
                    expenses_machinary_1,
                    expenses_machinary_2,
                    expenses_other_purchases_1,
                    expenses_other_purchases_2,
                    expenses_licenses_1,
                    expenses_licenses_2,
                    expenses_other_operations_1,
                    expenses_other_operations_2,
                    expenses_total_operations_1,
                    expenses_total_operations_2,
                    gross_profit_1,
                    gross_profit_2,
                    profit_income_tax_1,
                    profit_income_tax_2,
                    profit_after_income_tax_1,
                    profit_after_income_tax_2,
                    sales_tax_1,
                    sales_tax_2,
                    name,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-420.csv",
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
                "main_line": str,
                "business_type": str,
                "other_business_type": str,
                "accounting_period": str,
                "start_year": int,
                "end_year": int,
                "incomes_sales_1": float,
                "incomes_sales_2": float,
                "incomes_from_people_1": float,
                "incomes_from_people_2": float,
                "incomes_industries_businesses_1": float,
                "incomes_industries_businesses_2": float,
                "incomes_less_cost_1": float,
                "incomes_less_cost_2": float,
                "incomes_inventory_beginning_1": float,
                "incomes_inventory_beginning_2": float,
                "incomes_purchases_1": float,
                "incomes_purchases_2": float,
                "incomes_inventory_end_1": float,
                "incomes_inventory_end_2": float,
                "incomes_gross_profit_1": float,
                "incomes_gross_profit_2": float,
                "other_operation_incomes_1": float,
                "other_operation_incomes_2": float,
                "incomes_interests_1": float,
                "incomes_interests_2": float,
                "incomes_rent_1": float,
                "incomes_rent_2": float,
                "incomes_gain_loss_1": float,
                "incomes_gain_loss_2": float,
                "incomes_dividends_1": float,
                "incomes_dividends_2": float,
                "other_incomes_1": float,
                "other_incomes_2": float,
                "incomes_total_gross_1": float,
                "incomes_total_gross_2": float,
                "expenses_1": float,
                "expenses_2": float,
                "expenses_salaries_wages_bonus_1": float,
                "expenses_salaries_wages_bonus_2": float,
                "expenses_interests_1": float,
                "expenses_interests_2": float,
                "expenses_depreciation_1": float,
                "expenses_depreciation_2": float,
                "expenses_rent_1": float,
                "expenses_rent_2": float,
                "expenses_bad_debts_1": float,
                "expenses_bad_debts_2": float,
                "expenses_donations_1": float,
                "expenses_donations_2": float,
                "expenses_sales_taxes_1": float,
                "expenses_sales_taxes_2": float,
                "expenses_machinary_1": float,
                "expenses_machinary_2": float,
                "expenses_other_purchases_1": float,
                "expenses_other_purchases_2": float,
                "expenses_licenses_1": float,
                "expenses_licenses_2": float,
                "expenses_other_operations_1": float,
                "expenses_other_operations_2": float,
                "expenses_total_operations_1": float,
                "expenses_total_operations_2": float,
                "gross_profit_1": float,
                "gross_profit_2": float,
                "profit_income_tax_1": float,
                "profit_income_tax_2": float,
                "profit_after_income_tax_1": float,
                "profit_after_income_tax_2": float,
                "sales_tax_1": float,
                "sales_tax_2": float,
                "name": str,
                "rank": str,
            },
            table_name="IP_420",
            table_id="29",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-420.html")
