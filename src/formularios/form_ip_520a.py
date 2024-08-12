from django.shortcuts import render
from src.dao.data_db_dao import DAO
import csv
import os


def IP_520a(request):
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
        start_month = request.POST.get("start_month")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        incomes_services_fee_1 = request.POST.get("incomes_services_fee_1")
        incomes_services_fee_2 = request.POST.get("incomes_services_fee_2")
        incomes_comissions_1 = request.POST.get("incomes_comissions_1")
        incomes_comissions_2 = request.POST.get("incomes_comissions_2")
        incomes_rent_1 = request.POST.get("incomes_rent_1")
        incomes_rent_2 = request.POST.get("incomes_rent_2")
        incomes_interest_1 = request.POST.get("incomes_interest_1")
        incomes_interest_2 = request.POST.get("incomes_interest_2")
        incomes_capital_gain_loss_1 = request.POST.get("incomes_capital_gain_loss_1")
        incomes_capital_gain_loss_2 = request.POST.get("incomes_capital_gain_loss_2")
        incomes_other_operating_1 = request.POST.get("incomes_other_operating_1")
        incomes_other_operating_2 = request.POST.get("incomes_other_operating_2")
        incomes_total_1 = request.POST.get("incomes_total_1")
        incomes_total_2 = request.POST.get("incomes_total_2")
        expenses_1 = request.POST.get("expenses_1")
        expenses_2 = request.POST.get("expenses_2")
        expenses_salaries_wages_bonus_1 = request.POST.get(
            "expenses_salaries_wages_bonus_1"
        )
        expenses_salaries_wages_bonus_2 = request.POST.get(
            "expenses_salaries_wages_bonus_2"
        )
        expenses_commissions_1 = request.POST.get("expenses_commissions_1")
        expenses_commissions_2 = request.POST.get("expenses_commissions_2")
        expenses_interests_1 = request.POST.get("expenses_interests_1")
        expenses_interests_2 = request.POST.get("expenses_interests_2")
        expenses_rent_1 = request.POST.get("expenses_rent_1")
        expenses_rent_2 = request.POST.get("expenses_rent_2")
        expenses_depreciation_1 = request.POST.get("expenses_depreciation_1")
        expenses_depreciation_2 = request.POST.get("expenses_depreciation_2")
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
        expenses_other_operation_1 = request.POST.get("expenses_other_operation_1")
        expenses_other_operation_2 = request.POST.get("expenses_other_operation_2")
        expenses_total_1 = request.POST.get("expenses_total_1")
        expenses_total_2 = request.POST.get("expenses_total_2")
        net_profit_loss_1 = request.POST.get("net_profit_loss_1")
        net_profit_loss_2 = request.POST.get("net_profit_loss_2")
        sales_tax_withheld_1 = request.POST.get("sales_tax_withheld_1")
        sales_tax_withheld_2 = request.POST.get("sales_tax_withheld_2")
        percent_local_enterprises = request.POST.get("percent_local_enterprises")
        percent_foreign_enterprises = request.POST.get("percent_foreign_enterprises")
        name = request.POST.get("name")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-520a.csv"
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
                        "start_month",
                        "start_year",
                        "end_year",
                        "incomes_services_fee_1",
                        "incomes_services_fee_2",
                        "incomes_comissions_1",
                        "incomes_comissions_2",
                        "incomes_rent_1",
                        "incomes_rent_2",
                        "incomes_interest_1",
                        "incomes_interest_2",
                        "incomes_capital_gain_loss_1",
                        "incomes_capital_gain_loss_2",
                        "incomes_other_operating_1",
                        "incomes_other_operating_2",
                        "incomes_total_1",
                        "incomes_total_2",
                        "expenses_1",
                        "expenses_2",
                        "expenses_salaries_wages_bonus_1",
                        "expenses_salaries_wages_bonus_2",
                        "expenses_commissions_1",
                        "expenses_commissions_2",
                        "expenses_interests_1",
                        "expenses_interests_2",
                        "expenses_rent_1",
                        "expenses_rent_2",
                        "expenses_depreciation_1",
                        "expenses_depreciation_2",
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
                        "expenses_other_operation_1",
                        "expenses_other_operation_2",
                        "expenses_total_1",
                        "expenses_total_2",
                        "net_profit_loss_1",
                        "net_profit_loss_2",
                        "sales_tax_withheld_1",
                        "sales_tax_withheld_2",
                        "percent_local_enterprises",
                        "percent_foreign_enterprises",
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
                    start_month,
                    start_year,
                    end_year,
                    incomes_services_fee_1,
                    incomes_services_fee_2,
                    incomes_comissions_1,
                    incomes_comissions_2,
                    incomes_rent_1,
                    incomes_rent_2,
                    incomes_interest_1,
                    incomes_interest_2,
                    incomes_capital_gain_loss_1,
                    incomes_capital_gain_loss_2,
                    incomes_other_operating_1,
                    incomes_other_operating_2,
                    incomes_total_1,
                    incomes_total_2,
                    expenses_1,
                    expenses_2,
                    expenses_salaries_wages_bonus_1,
                    expenses_salaries_wages_bonus_2,
                    expenses_commissions_1,
                    expenses_commissions_2,
                    expenses_interests_1,
                    expenses_interests_2,
                    expenses_rent_1,
                    expenses_rent_2,
                    expenses_depreciation_1,
                    expenses_depreciation_2,
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
                    expenses_other_operation_1,
                    expenses_other_operation_2,
                    expenses_total_1,
                    expenses_total_2,
                    net_profit_loss_1,
                    net_profit_loss_2,
                    sales_tax_withheld_1,
                    sales_tax_withheld_2,
                    percent_local_enterprises,
                    percent_foreign_enterprises,
                    name,
                    rank,
                ]
            )
            
        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-520a.csv",
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
                "start_month": str,
                "start_year": int,
                "end_year": int,
                "incomes_services_fee_1": float,
                "incomes_services_fee_2": float,
                "incomes_comissions_1": float,
                "incomes_comissions_2": float,
                "incomes_rent_1": float,
                "incomes_rent_2": float,
                "incomes_interest_1": float,
                "incomes_interest_2": float,
                "incomes_capital_gain_loss_1": float,
                "incomes_capital_gain_loss_2": float,
                "incomes_other_operating_1": float,
                "incomes_other_operating_2": float,
                "incomes_total_1": float,
                "incomes_total_2": float,
                "expenses_1": float,
                "expenses_2": float,
                "expenses_salaries_wages_bonus_1": float,
                "expenses_salaries_wages_bonus_2": float,
                "expenses_commissions_1": float,
                "expenses_commissions_2": float,
                "expenses_interests_1": float,
                "expenses_interests_2": float,
                "expenses_rent_1": float,
                "expenses_rent_2": float,
                "expenses_depreciation_1": float,
                "expenses_depreciation_2": float,
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
                "expenses_other_operation_1": float,
                "expenses_other_operation_2": float,
                "expenses_total_1": float,
                "expenses_total_2": float,
                "net_profit_loss_1": float,
                "net_profit_loss_2": float,
                "sales_tax_withheld_1": float,
                "sales_tax_withheld_2": float,
                "percent_local_enterprises": float,
                "percent_foreign_enterprises": float,
                "name": str,
                "rank": str,
            },
            table_name="IP_520a",
            table_id=38,
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-520a.html")
