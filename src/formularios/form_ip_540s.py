from django.shortcuts import render
from src.dao.data_db_dao import DAO
import polars as pl

def IP_540S(request):
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
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        incomes_from_persons_1 = request.POST.get("incomes_from_persons_1")
        incomes_from_persons_2 = request.POST.get("incomes_from_persons_2")
        incomes_from_industries_and_businesses_1 = request.POST.get(
            "incomes_from_industries_and_businesses_1"
        )
        incomes_from_industries_and_businesses_2 = request.POST.get(
            "incomes_from_industries_and_businesses_2"
        )
        expenses_newspapers_1 = request.POST.get("expenses_newspapers_1")
        expenses_newspapers_2 = request.POST.get("expenses_newspapers_2")
        expenses_radio_1 = request.POST.get("expenses_radio_1")
        expenses_radio_2 = request.POST.get("expenses_radio_2")
        expenses_other_1 = request.POST.get("expenses_other_1")
        expenses_other_2 = request.POST.get("expenses_other_2")
        gross_profit_1 = request.POST.get("gross_profit_1")
        gross_profit_2 = request.POST.get("gross_profit_2")
        gross_other_income_1 = request.POST.get("gross_other_income_1")
        gross_other_income_2 = request.POST.get("gross_other_income_2")
        gross_interests_1 = request.POST.get("gross_interests_1")
        gross_interests_2 = request.POST.get("gross_interests_2")
        gross_rent_land_1 = request.POST.get("gross_rent_land_1")
        gross_rent_land_2 = request.POST.get("gross_rent_land_2")
        gross_capital_gain_1 = request.POST.get("gross_capital_gain_1")
        gross_capital_gain_2 = request.POST.get("gross_capital_gain_2")
        gross_other_1 = request.POST.get("gross_other_1")
        gross_other_2 = request.POST.get("gross_other_2")
        income_total_income_1 = request.POST.get("income_total_income_1")
        income_total_income_2 = request.POST.get("income_total_income_2")
        income_total_expenses_1 = request.POST.get("income_total_expenses_1")
        income_total_expenses_2 = request.POST.get("income_total_expenses_2")
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
        expenses_other_taxes_1 = request.POST.get("expenses_other_taxes_1")
        expenses_other_taxes_2 = request.POST.get("expenses_other_taxes_2")
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
        expenses_other_operation_1 = request.POST.get("expenses_other_operation_1")
        expenses_other_operation_2 = request.POST.get("expenses_other_operation_2")
        net_profit_1 = request.POST.get("net_profit_1")
        net_profit_2 = request.POST.get("net_profit_2")
        profit_income_tax_1 = request.POST.get("profit_income_tax_1")
        profit_income_tax_2 = request.POST.get("profit_income_tax_2")
        profit_after_income_tax_1 = request.POST.get("profit_after_income_tax_1")
        profit_after_income_tax_2 = request.POST.get("profit_after_income_tax_2")
        sales_tax_withheld_1 = request.POST.get("sales_tax_withheld_1")
        sales_tax_withheld_2 = request.POST.get("sales_tax_withheld_2")
        name = request.POST.get("name")
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
            pl.Series("closing_date", [closing_date], dtype=pl.String),
            pl.Series("start_year", [start_year], dtype=pl.String),
            pl.Series("end_year", [end_year], dtype=pl.String),
            pl.Series("incomes_from_persons_1", [float(incomes_from_persons_1)], dtype=pl.Float64),
            pl.Series("incomes_from_persons_2", [float(incomes_from_persons_2)], dtype=pl.Float64),
            pl.Series("incomes_from_industries_and_businesses_1", [float(incomes_from_industries_and_businesses_1)], dtype=pl.Float64),
            pl.Series("incomes_from_industries_and_businesses_2", [float(incomes_from_industries_and_businesses_2)], dtype=pl.Float64),
            pl.Series("expenses_newspapers_1", [float(expenses_newspapers_1)], dtype=pl.Float64),
            pl.Series("expenses_newspapers_2", [float(expenses_newspapers_2)], dtype=pl.Float64),
            pl.Series("expenses_radio_1", [float(expenses_radio_1)], dtype=pl.Float64),
            pl.Series("expenses_radio_2", [float(expenses_radio_2)], dtype=pl.Float64),
            pl.Series("expenses_other_1", [float(expenses_other_1)], dtype=pl.Float64),
            pl.Series("expenses_other_2", [float(expenses_other_2)], dtype=pl.Float64),
            pl.Series("gross_profit_1", [float(gross_profit_1)], dtype=pl.Float64),
            pl.Series("gross_profit_2", [float(gross_profit_2)], dtype=pl.Float64),
            pl.Series("gross_other_income_1", [float(gross_other_income_1)], dtype=pl.Float64),
            pl.Series("gross_other_income_2", [float(gross_other_income_2)], dtype=pl.Float64),
            pl.Series("gross_interests_1", [float(gross_interests_1)], dtype=pl.Float64),
            pl.Series("gross_interests_2", [float(gross_interests_2)], dtype=pl.Float64),
            pl.Series("gross_rent_land_1", [float(gross_rent_land_1)], dtype=pl.Float64),
            pl.Series("gross_rent_land_2", [float(gross_rent_land_2)], dtype=pl.Float64),
            pl.Series("gross_capital_gain_1", [float(gross_capital_gain_1)], dtype=pl.Float64),
            pl.Series("gross_capital_gain_2", [float(gross_capital_gain_2)], dtype=pl.Float64),
            pl.Series("gross_other_1", [float(gross_other_1)], dtype=pl.Float64),
            pl.Series("gross_other_2", [float(gross_other_2)], dtype=pl.Float64),
            pl.Series("income_total_income_1", [float(income_total_income_1)], dtype=pl.Float64),
            pl.Series("income_total_income_2", [float(income_total_income_2)], dtype=pl.Float64),
            pl.Series("income_total_expenses_1", [float(income_total_expenses_1)], dtype=pl.Float64),
            pl.Series("income_total_expenses_2", [float(income_total_expenses_2)], dtype=pl.Float64),
            pl.Series("expenses_salaries_wages_bonus_1", [float(expenses_salaries_wages_bonus_1)], dtype=pl.Float64),
            pl.Series("expenses_salaries_wages_bonus_2", [float(expenses_salaries_wages_bonus_2)], dtype=pl.Float64),
            pl.Series("expenses_interests_1", [float(expenses_interests_1)], dtype=pl.Float64),
            pl.Series("expenses_interests_2", [float(expenses_interests_2)], dtype=pl.Float64),
            pl.Series("expenses_rent_1", [float(expenses_rent_1)], dtype=pl.Float64),
            pl.Series("expenses_rent_2", [float(expenses_rent_2)], dtype=pl.Float64),
            pl.Series("expenses_depreciation_1", [float(expenses_depreciation_1)], dtype=pl.Float64),
            pl.Series("expenses_depreciation_2", [float(expenses_depreciation_2)], dtype=pl.Float64),
            pl.Series("expenses_other_taxes_1", [float(expenses_other_taxes_1)], dtype=pl.Float64),
            pl.Series("expenses_other_taxes_2", [float(expenses_other_taxes_2)], dtype=pl.Float64),
            pl.Series("expenses_donations_1", [float(expenses_donations_1)], dtype=pl.Float64),
            pl.Series("expenses_donations_2", [float(expenses_donations_2)], dtype=pl.Float64),
            pl.Series("expenses_sales_taxes_1", [float(expenses_sales_taxes_1)], dtype=pl.Float64),
            pl.Series("expenses_sales_taxes_2", [float(expenses_sales_taxes_2)], dtype=pl.Float64),
            pl.Series("expenses_purchases_machinery_1", [float(expenses_purchases_machinery_1)], dtype=pl.Float64),
            pl.Series("expenses_purchases_machinery_2", [float(expenses_purchases_machinery_2)], dtype=pl.Float64),
            pl.Series("expenses_other_purchases_1", [float(expenses_other_purchases_1)], dtype=pl.Float64),
            pl.Series("expenses_other_purchases_2", [float(expenses_other_purchases_2)], dtype=pl.Float64),
            pl.Series("expenses_licenses_1", [float(expenses_licenses_1)], dtype=pl.Float64),
            pl.Series("expenses_licenses_2", [float(expenses_licenses_2)], dtype=pl.Float64),
            pl.Series("expenses_other_operation_1", [float(expenses_other_operation_1)], dtype=pl.Float64),
            pl.Series("expenses_other_operation_2", [float(expenses_other_operation_2)], dtype=pl.Float64),
            pl.Series("net_profit_1", [float(net_profit_1)], dtype=pl.Float64),
            pl.Series("net_profit_2", [float(net_profit_2)], dtype=pl.Float64),
            pl.Series("profit_income_tax_1", [float(profit_income_tax_1)], dtype=pl.Float64),
            pl.Series("profit_income_tax_2", [float(profit_income_tax_2)], dtype=pl.Float64),
            pl.Series("profit_after_income_tax_1", [float(profit_after_income_tax_1)], dtype=pl.Float64),
            pl.Series("profit_after_income_tax_2", [float(profit_after_income_tax_2)], dtype=pl.Float64),
            pl.Series("sales_tax_withheld_1", [float(sales_tax_withheld_1)], dtype=pl.Float64),
            pl.Series("sales_tax_withheld_2", [float(sales_tax_withheld_2)], dtype=pl.Float64),
            pl.Series("name", [name], dtype=pl.String),
            pl.Series("rank", [rank], dtype=pl.String),
        ]
        
        df = pl.DataFrame(data)
        DAO().insert_forms(df, "IP_540S", 16)

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-540S.html")
