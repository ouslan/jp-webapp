from django.shortcuts import render
from numpy import dtype
from src.dao.data_db_dao import DAO
import polars as pl


def IP_610(request):
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
        incomes_unrestricted_A_1 = request.POST.get("incomes_unrestricted_A_1")
        incomes_unrestricted_A_2 = request.POST.get("incomes_unrestricted_A_2")
        incomes_restricted_A_1 = request.POST.get("incomes_restricted_A_1")
        incomes_restricted_A_2 = request.POST.get("incomes_restricted_A_2")
        incomes_sales_1 = request.POST.get("incomes_sales_1")
        incomes_sales_2 = request.POST.get("incomes_sales_2")
        incomes_rents_1 = request.POST.get("incomes_rents_1")
        incomes_rents_2 = request.POST.get("incomes_rents_2")
        incomes_interests_1 = request.POST.get("incomes_interests_1")
        incomes_interests_2 = request.POST.get("incomes_interests_2")
        incomes_capital_1 = request.POST.get("incomes_capital_1")
        incomes_capital_2 = request.POST.get("incomes_capital_2")
        incomes_total_1 = request.POST.get("incomes_total_1")
        incomes_total_2 = request.POST.get("incomes_total_2")

        expenses_1 = request.POST.get("expenses_1")
        expenses_2 = request.POST.get("expenses_2")
        expenses_salaries_1 = request.POST.get("expenses_salaries_1")
        expenses_salaries_2 = request.POST.get("expenses_salaries_2")
        expenses_interests_1 = request.POST.get("expenses_interests_1")
        expenses_interests_2 = request.POST.get("expenses_interests_2")
        expenses_rents_1 = request.POST.get("expenses_rents_1")
        expenses_rents_2 = request.POST.get("expenses_rents_2")
        expenses_depreciation_1 = request.POST.get("expenses_depreciation_1")
        expenses_depreciation_2 = request.POST.get("expenses_depreciation_2")
        expenses_debts_1 = request.POST.get("expenses_debts_1")
        expenses_debts_2 = request.POST.get("expenses_debts_2")
        expenses_donations_1 = request.POST.get("expenses_donations_1")
        expenses_donations_2 = request.POST.get("expenses_donations_2")
        expenses_tax_1 = request.POST.get("expenses_tax_1")
        expenses_tax_2 = request.POST.get("expenses_tax_2")
        expenses_machinery_1 = request.POST.get("expenses_machinery_1")
        expenses_machinery_2 = request.POST.get("expenses_machinery_2")
        other_purchases_1 = request.POST.get("other_purchases_1")
        other_purchases_2 = request.POST.get("other_purchases_2")
        expenses_licenses_1 = request.POST.get("expenses_licenses_1")
        expenses_licenses_2 = request.POST.get("expenses_licenses_2")
        expenses_other_1 = request.POST.get("expenses_other_1")
        expenses_other_2 = request.POST.get("expenses_other_2")
        net_profit_1 = request.POST.get("net_profit_1")
        net_profit_2 = request.POST.get("net_profit_2")
        income_tax_1 = request.POST.get("income_tax_1")
        income_tax_2 = request.POST.get("income_tax_2")
        profit_after_tax_1 = request.POST.get("profit_after_tax_1")
        profit_after_tax_2 = request.POST.get("profit_after_tax_2")
        withheld_tax_1 = request.POST.get("withheld_tax_1")
        withheld_tax_2 = request.POST.get("withheld_tax_2")

        signature = request.POST.get("signature")
        rank = request.POST.get("rank")

        data = [
            pl.Series("company_name", [company_name], dtype=pl.String),
            pl.Series("address", [address], dtype=pl.String),
            pl.Series("email", [email], dtype=pl.String),
            pl.Series("liaison_officer", [liaison_officer], dtype=pl.String),
            pl.Series("ssn", [ssn], dtype=pl.String),
            pl.Series("tel", [tel], dtype=pl.String),
            pl.Series("fax", [fax], dtype=pl.String),
            pl.Series("legal_form", [legal_form], dtype=pl.String),
            pl.Series("cfc", [cfc], dtype=pl.String),
            pl.Series("business_type", [business_type], dtype=pl.String),
            pl.Series("business_function", [business_function], dtype=pl.String),
            pl.Series("branches", [branches], dtype=pl.String),
            pl.Series("branches_yes", [branches_yes], dtype=pl.String),
            pl.Series("closing_date", [closing_date], dtype=pl.String),
            pl.Series("start_year", [start_year], dtype=pl.String),
            pl.Series("end_year", [end_year], dtype=pl.String),
            pl.Series("incomes_services_rendered_1", [float(incomes_services_rendered_1)], dtype=pl.Float64),
            pl.Series("incomes_services_rendered_2", [float(incomes_services_rendered_2)], dtype=pl.Float64),
            pl.Series("incomes_unrestricted_A_1", [float(incomes_unrestricted_A_1)], dtype=pl.Float64),
            pl.Series("incomes_unrestricted_A_2", [float(incomes_unrestricted_A_2)], dtype=pl.Float64),
            pl.Series("incomes_restricted_A_1", [float(incomes_restricted_A_1)], dtype=pl.Float64),
            pl.Series("incomes_restricted_A_2", [float(incomes_restricted_A_2)], dtype=pl.Float64),
            pl.Series("incomes_sales_1", [float(incomes_sales_1)], dtype=pl.Float64),
            pl.Series("incomes_sales_2", [float(incomes_sales_2)], dtype=pl.Float64),
            pl.Series("incomes_rents_1", [float(incomes_rents_1)], dtype=pl.Float64),
            pl.Series("incomes_rents_2", [float(incomes_rents_2)], dtype=pl.Float64),
            pl.Series("incomes_interests_1", [float(incomes_interests_1)], dtype=pl.Float64),
            pl.Series("incomes_interests_2", [float(incomes_interests_2)], dtype=pl.Float64),
            pl.Series("incomes_capital_1", [float(incomes_capital_1)], dtype=pl.Float64),
            pl.Series("incomes_capital_2", [float(incomes_capital_2)], dtype=pl.Float64),
            pl.Series("incomes_total_1", [float(incomes_total_1)], dtype=pl.Float64),
            pl.Series("incomes_total_2", [float(incomes_total_2)], dtype=pl.Float64),
            pl.Series("expenses_1", [float(expenses_1)], dtype=pl.Float64),
            pl.Series("expenses_2", [float(expenses_2)], dtype=pl.Float64),
            pl.Series("expenses_salaries_1", [float(expenses_salaries_1)], dtype=pl.Float64),
            pl.Series("expenses_salaries_2", [float(expenses_salaries_2)], dtype=pl.Float64),
            pl.Series("expenses_interests_1", [float(expenses_interests_1)], dtype=pl.Float64),
            pl.Series("expenses_interests_2", [float(expenses_interests_2)], dtype=pl.Float64),
            pl.Series("expenses_rents_1", [float(expenses_rents_1)], dtype=pl.Float64),
            pl.Series("expenses_rents_2", [float(expenses_rents_2)], dtype=pl.Float64),
            pl.Series("expenses_depreciation_1", [float(expenses_depreciation_1)], dtype=pl.Float64),
            pl.Series("expenses_depreciation_2", [float(expenses_depreciation_2)], dtype=pl.Float64),
            pl.Series("expenses_debts_1", [float(expenses_debts_1)], dtype=pl.Float64),
            pl.Series("expenses_debts_2", [float(expenses_debts_2)], dtype=pl.Float64),
            pl.Series("expenses_donations_1", [float(expenses_donations_1)], dtype=pl.Float64),
            pl.Series("expenses_donations_2", [float(expenses_donations_2)], dtype=pl.Float64),
            pl.Series("expenses_tax_1", [float(expenses_tax_1)], dtype=pl.Float64),
            pl.Series("expenses_tax_2", [float(expenses_tax_2)], dtype=pl.Float64),
            pl.Series("expenses_machinery_1", [float(expenses_machinery_1)], dtype=pl.Float64),
            pl.Series("expenses_machinery_2", [float(expenses_machinery_2)], dtype=pl.Float64),
            pl.Series("other_purchases_1", [float(other_purchases_1)], dtype=pl.Float64),
            pl.Series("other_purchases_2", [float(other_purchases_2)], dtype=pl.Float64),
            pl.Series("expenses_licenses_1", [float(expenses_licenses_1)], dtype=pl.Float64),
            pl.Series("expenses_licenses_2", [float(expenses_licenses_2)], dtype=pl.Float64),
            pl.Series("expenses_other_1", [float(expenses_other_1)], dtype=pl.Float64),
            pl.Series("expenses_other_2", [float(expenses_other_2)], dtype=pl.Float64),
            pl.Series("net_profit_1", [float(net_profit_1)], dtype=pl.Float64),
            pl.Series("net_profit_2", [float(net_profit_2)], dtype=pl.Float64),
            pl.Series("income_tax_1", [float(income_tax_1)], dtype=pl.Float64),
            pl.Series("income_tax_2", [float(income_tax_2)], dtype=pl.Float64),
            pl.Series("profit_after_tax_1", [float(profit_after_tax_1)], dtype=pl.Float64),
            pl.Series("profit_after_tax_2", [float(profit_after_tax_2)], dtype=pl.Float64),
            pl.Series("withheld_tax_1", [float(withheld_tax_1)], dtype=pl.Float64),
            pl.Series("withheld_tax_2", [float(withheld_tax_2)], dtype=pl.Float64),
            pl.Series("signature", [signature], dtype=pl.String),
            pl.Series("rank", [rank], dtype=pl.String),
        ]
        
        df = pl.DataFrame(data)
        DAO().insert_forms(df, "IP_610", 26)

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-610.html")
