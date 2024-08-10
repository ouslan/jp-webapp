from django.shortcuts import render
from src.dao.data_db_dao import DAO
import csv
import os


def IP_440(request):
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
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        sales_A_1 = request.POST.get("sales_A_1")
        sales_A_2 = request.POST.get("sales_A_2")
        people_A_1 = request.POST.get("people_A_1")
        people_A_2 = request.POST.get("people_A_2")
        industries_businesses_A_1 = request.POST.get("industries_businesses_A_1")
        industries_businesses_A_2 = request.POST.get("industries_businesses_A_2")
        less_cost_A_1 = request.POST.get("less_cost_A_1")
        less_cost_A_2 = request.POST.get("less_cost_A_2")
        inventory_beginning_1 = request.POST.get("inventory_beginning_1")
        inventory_beginning_2 = request.POST.get("inventory_beginning_2")
        purchases_A_1 = request.POST.get("purchases_A_1")
        purchases_A_2 = request.POST.get("purchases_A_2")
        inventory_end_1 = request.POST.get("inventory_end_1")
        inventory_end_2 = request.POST.get("inventory_end_2")
        gross_profit_A_1 = request.POST.get("gross_profit_A_1")
        gross_profit_A_2 = request.POST.get("gross_profit_A_2")
        other_income_A_1 = request.POST.get("other_income_A_1")
        other_income_A_2 = request.POST.get("other_income_A_2")
        interests_A_1 = request.POST.get("interests_A_1")
        interests_A_2 = request.POST.get("interests_A_2")
        rent_A_1 = request.POST.get("rent_A_1")
        rent_A_2 = request.POST.get("rent_A_2")
        capital_gain_A_1 = request.POST.get("capital_gain_A_1")
        capital_gain_A_2 = request.POST.get("capital_gain_A_2")
        dividends_A_1 = request.POST.get("dividends_A_1")
        dividends_A_2 = request.POST.get("dividends_A_2")
        other_A_1 = request.POST.get("other_A_1")
        other_A_2 = request.POST.get("other_A_2")
        total_gross_A_1 = request.POST.get("total_gross_A_1")
        total_gross_A_2 = request.POST.get("total_gross_A_2")
        expenses_1 = request.POST.get("expenses_1")
        expenses_2 = request.POST.get("expenses_2")
        salaries_1 = request.POST.get("salaries_1")
        salaries_2 = request.POST.get("salaries_2")
        expenses_interests_1 = request.POST.get("expenses_interests_1")
        expenses_interests_2 = request.POST.get("expenses_interests_2")
        expenses_rents_1 = request.POST.get("expenses_rents_1")
        expenses_rents_2 = request.POST.get("expenses_rents_2")
        depreciation_1 = request.POST.get("depreciation_1")
        depreciation_2 = request.POST.get("depreciation_2")
        bad_debts_1 = request.POST.get("bad_debts_1")
        bad_debts_2 = request.POST.get("bad_debts_2")
        donations_1 = request.POST.get("donations_1")
        donations_2 = request.POST.get("donations_2")
        sales_tax_1 = request.POST.get("sales_tax_1")
        sales_tax_2 = request.POST.get("sales_tax_2")
        machinery_1 = request.POST.get("machinery_1")
        machinery_2 = request.POST.get("machinery_2")
        other_purchases_1 = request.POST.get("other_purchases_1")
        other_purchases_2 = request.POST.get("other_purchases_2")
        licenses_1 = request.POST.get("licenses_1")
        licenses_2 = request.POST.get("licenses_2")
        other_expenses_1 = request.POST.get("other_expenses_1")
        other_expenses_2 = request.POST.get("other_expenses_2")
        total_expenses_1 = request.POST.get("total_expenses_1")
        total_expenses_2 = request.POST.get("total_expenses_2")
        net_profit_1 = request.POST.get("net_profit_1")
        net_profit_2 = request.POST.get("net_profit_2")
        income_tax_1 = request.POST.get("income_tax_1")
        income_tax_2 = request.POST.get("income_tax_2")
        profit_after_tax_1 = request.POST.get("profit_after_tax_1")
        profit_after_tax_2 = request.POST.get("profit_after_tax_2")
        sales_D_1 = request.POST.get("sales_D_1")
        sales_D_2 = request.POST.get("sales_D_2")
        name = request.POST.get("name")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-440.csv"
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
                        "closing_date",
                        "start_year",
                        "end_year",
                        "sales_A_1",
                        "sales_A_2",
                        "people_A_1",
                        "people_A_2",
                        "industries_businesses_A_1",
                        "industries_businesses_A_2",
                        "less_cost_A_1",
                        "less_cost_A_2",
                        "inventory_beginning_1",
                        "inventory_beginning_2",
                        "purchases_A_1",
                        "purchases_A_2",
                        "inventory_end_1",
                        "inventory_end_2",
                        "gross_profit_A_1",
                        "gross_profit_A_2",
                        "other_income_A_1",
                        "other_income_A_2",
                        "interests_A_1",
                        "interests_A_2",
                        "rent_A_1",
                        "rent_A_2",
                        "capital_gain_A_1",
                        "capital_gain_A_2",
                        "dividends_A_1",
                        "dividends_A_2",
                        "other_A_1",
                        "other_A_2",
                        "total_gross_A_1",
                        "total_gross_A_2",
                        "expenses_1",
                        "expenses_2",
                        "salaries_1",
                        "salaries_2",
                        "expenses_interests_1",
                        "expenses_interests_2",
                        "expenses_rents_1",
                        "expenses_rents_2",
                        "depreciation_1",
                        "depreciation_2",
                        "bad_debts_1",
                        "bad_debts_2",
                        "donations_1",
                        "donations_2",
                        "sales_tax_1",
                        "sales_tax_2",
                        "machinery_1",
                        "machinery_2",
                        "other_purchases_1",
                        "other_purchases_2",
                        "licenses_1",
                        "licenses_2",
                        "other_expenses_1",
                        "other_expenses_2",
                        "total_expenses_1",
                        "total_expenses_2",
                        "net_profit_1",
                        "net_profit_2",
                        "income_tax_1",
                        "income_tax_2",
                        "profit_after_tax_1",
                        "profit_after_tax_2",
                        "sales_D_1",
                        "sales_D_2",
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
                    closing_date,
                    start_year,
                    end_year,
                    sales_A_1,
                    sales_A_2,
                    people_A_1,
                    people_A_2,
                    industries_businesses_A_1,
                    industries_businesses_A_2,
                    less_cost_A_1,
                    less_cost_A_2,
                    inventory_beginning_1,
                    inventory_beginning_2,
                    purchases_A_1,
                    purchases_A_2,
                    inventory_end_1,
                    inventory_end_2,
                    gross_profit_A_1,
                    gross_profit_A_2,
                    other_income_A_1,
                    other_income_A_2,
                    interests_A_1,
                    interests_A_2,
                    rent_A_1,
                    rent_A_2,
                    capital_gain_A_1,
                    capital_gain_A_2,
                    dividends_A_1,
                    dividends_A_2,
                    other_A_1,
                    other_A_2,
                    total_gross_A_1,
                    total_gross_A_2,
                    expenses_1,
                    expenses_2,
                    salaries_1,
                    salaries_2,
                    expenses_interests_1,
                    expenses_interests_2,
                    expenses_rents_1,
                    expenses_rents_2,
                    depreciation_1,
                    depreciation_2,
                    bad_debts_1,
                    bad_debts_2,
                    donations_1,
                    donations_2,
                    sales_tax_1,
                    sales_tax_2,
                    machinery_1,
                    machinery_2,
                    other_purchases_1,
                    other_purchases_2,
                    licenses_1,
                    licenses_2,
                    other_expenses_1,
                    other_expenses_2,
                    total_expenses_1,
                    total_expenses_2,
                    net_profit_1,
                    net_profit_2,
                    income_tax_1,
                    income_tax_2,
                    profit_after_tax_1,
                    profit_after_tax_2,
                    sales_D_1,
                    sales_D_2,
                    name,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-440.csv",
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
                "closing_date": str,
                "start_year": int,
                "end_year": int,
                "sales_A_1": float,
                "sales_A_2": float,
                "people_A_1": float,
                "people_A_2": float,
                "industries_businesses_A_1": float,
                "industries_businesses_A_2": float,
                "less_cost_A_1": float,
                "less_cost_A_2": float,
                "inventory_beginning_1": float,
                "inventory_beginning_2": float,
                "purchases_A_1": float,
                "purchases_A_2": float,
                "inventory_end_1": float,
                "inventory_end_2": float,
                "gross_profit_A_1": float,
                "gross_profit_A_2": float,
                "other_income_A_1": float,
                "other_income_A_2": float,
                "interests_A_1": float,
                "interests_A_2": float,
                "rent_A_1": float,
                "rent_A_2": float,
                "capital_gain_A_1": float,
                "capital_gain_A_2": float,
                "dividends_A_1": float,
                "dividends_A_2": float,
                "other_A_1": float,
                "other_A_2": float,
                "total_gross_A_1": float,
                "total_gross_A_2": float,
                "expenses_1": float,
                "expenses_2": float,
                "salaries_1": float,
                "salaries_2": float,
                "expenses_interests_1": float,
                "expenses_interests_2": float,
                "expenses_rents_1": float,
                "expenses_rents_2": float,
                "depreciation_1": float,
                "depreciation_2": float,
                "bad_debts_1": float,
                "bad_debts_2": float,
                "donations_1": float,
                "donations_2": float,
                "sales_tax_1": float,
                "sales_tax_2": float,
                "machinery_1": float,
                "machinery_2": float,
                "other_purchases_1": float,
                "other_purchases_2": float,
                "licenses_1": float,
                "licenses_2": float,
                "other_expenses_1": float,
                "other_expenses_2": float,
                "total_expenses_1": float,
                "total_expenses_2": float,
                "net_profit_1": float,
                "net_profit_2": float,
                "income_tax_1": float,
                "income_tax_2": float,
                "profit_after_tax_1": float,
                "profit_after_tax_2": float,
                "sales_D_1": float,
                "sales_D_2": float,
                "name": str,
                "rank": str,
            },
            table_name="IP_440",
            table_id="31",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-440.html")
