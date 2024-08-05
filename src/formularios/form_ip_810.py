from django.shortcuts import render
from src.dao.data_db_dao import DAO
import csv
import os

def IP_810(request):
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

        total_income_1 = request.POST.get("total_income_1")
        total_income_2 = request.POST.get("total_income_2")
        services_rendered_1 = request.POST.get("services_rendered_1")
        services_rendered_2 = request.POST.get("services_rendered_2")
        from_persons_1 = request.POST.get("from_persons_1")
        from_persons_2 = request.POST.get("from_persons_2")
        industries_businesses_1 = request.POST.get("industries_businesses_1")
        industries_businesses_2 = request.POST.get("industries_businesses_2")
        sales_1 = request.POST.get("sales_1")
        sales_2 = request.POST.get("sales_2")
        rent_machinery_1 = request.POST.get("rent_machinery_1")
        rent_machinery_2 = request.POST.get("rent_machinery_2")
        rent_land_1 = request.POST.get("rent_land_1")
        rent_land_2 = request.POST.get("rent_land_2")
        interest_1 = request.POST.get("interest_1")
        interest_2 = request.POST.get("interest_2")
        capitan_gain_loss_1 = request.POST.get("capitan_gain_loss_1")
        capitan_gain_loss_2 = request.POST.get("capitan_gain_loss_2")

        total_expenses_1 = request.POST.get("total_expenses_1")
        total_expenses_2 = request.POST.get("total_expenses_2")
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
        other_operating_expenses_1 = request.POST.get("other_operating_expenses_1")
        other_operating_expenses_2 = request.POST.get("other_operating_expenses_2")
        sales_tax_1 = request.POST.get("sales_tax_1")
        sales_tax_2 = request.POST.get("sales_tax_2")
        purchases_1 = request.POST.get("purchases_1")
        purchases_2 = request.POST.get("purchases_2")
        other_purchases_1 = request.POST.get("other_purchases_1")
        other_purchases_2 = request.POST.get("other_purchases_2")
        licenses_patents_1 = request.POST.get("licenses_patents_1")
        licenses_patents_2 = request.POST.get("licenses_patents_2")

        net_profit_loss_1 = request.POST.get("net_profit_loss_1")
        net_profit_loss_2 = request.POST.get("net_profit_loss_2")
        income_tax_1 = request.POST.get("income_tax_1")
        income_tax_2 = request.POST.get("income_tax_2")
        profit_after_tax_1 = request.POST.get("profit_after_tax_1")
        profit_after_tax_2 = request.POST.get("profit_after_tax_2")

        withheld_tax_1 = request.POST.get("withheld_tax_1")
        withheld_tax_2 = request.POST.get("withheld_tax_2")

        name = request.POST.get("name")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-810.csv"
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
                        "total_income_1",
                        "total_income_2",
                        "services_rendered_1",
                        "services_rendered_2",
                        "from_persons_1",
                        "from_persons_2",
                        "industries_businesses_1",
                        "industries_businesses_2",
                        "sales_1",
                        "sales_2",
                        "rent_machinery_1",
                        "rent_machinery_2",
                        "rent_land_1",
                        "rent_land_2",
                        "interest_1",
                        "interest_2",
                        "capitan_gain_loss_1",
                        "capitan_gain_loss_2",
                        "total_expenses_1",
                        "total_expenses_2",
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
                        "other_operating_expenses_1",
                        "other_operating_expenses_2",
                        "sales_tax_1",
                        "sales_tax_2",
                        "purchases_1",
                        "purchases_2",
                        "other_purchases_1",
                        "other_purchases_2",
                        "licenses_patents_1",
                        "licenses_patents_2",
                        "net_profit_loss_1",
                        "net_profit_loss_2",
                        "income_tax_1",
                        "income_tax_2",
                        "profit_after_tax_1",
                        "profit_after_tax_2",
                        "withheld_tax_1",
                        "withheld_tax_2",
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
                    total_income_1,
                    total_income_2,
                    services_rendered_1,
                    services_rendered_2,
                    from_persons_1,
                    from_persons_2,
                    industries_businesses_1,
                    industries_businesses_2,
                    sales_1,
                    sales_2,
                    rent_machinery_1,
                    rent_machinery_2,
                    rent_land_1,
                    rent_land_2,
                    interest_1,
                    interest_2,
                    capitan_gain_loss_1,
                    capitan_gain_loss_2,
                    total_expenses_1,
                    total_expenses_2,
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
                    other_operating_expenses_1,
                    other_operating_expenses_2,
                    sales_tax_1,
                    sales_tax_2,
                    purchases_1,
                    purchases_2,
                    other_purchases_1,
                    other_purchases_2,
                    licenses_patents_1,
                    licenses_patents_2,
                    net_profit_loss_1,
                    net_profit_loss_2,
                    income_tax_1,
                    income_tax_2,
                    profit_after_tax_1,
                    profit_after_tax_2,
                    withheld_tax_1,
                    withheld_tax_2,
                    name,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-810.csv",
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
                "total_income_1": float,
                "total_income_2": float,
                "services_rendered_1": float,
                "services_rendered_2": float,
                "from_persons_1": float,
                "from_persons_2": float,
                "industries_businesses_1": float,
                "industries_businesses_2": float,
                "sales_1": float,
                "sales_2": float,
                "rent_machinery_1": float,
                "rent_machinery_2": float,
                "rent_land_1": float,
                "rent_land_2": float,
                "interest_1": float,
                "interest_2": float,
                "capitan_gain_loss_1": float,
                "capitan_gain_loss_2": float,
                "total_expenses_1": float,
                "total_expenses_2": float,
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
                "other_operating_expenses_1": float,
                "other_operating_expenses_2": float,
                "sales_tax_1": float,
                "sales_tax_2": float,
                "purchases_1": float,
                "purchases_2": float,
                "other_purchases_1": float,
                "other_purchases_2": float,
                "licenses_patents_1": float,
                "licenses_patents_2": float,
                "net_profit_loss_1": float,
                "net_profit_loss_2": float,
                "income_tax_1": float,
                "income_tax_2": float,
                "profit_after_tax_1": float,
                "profit_after_tax_2": float,
                "withheld_tax_1": float,
                "withheld_tax_2": float,
                "name": str,
                "rank": str,
            },
            table_name="IP_810",
            table_id=8,
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-810.html")
