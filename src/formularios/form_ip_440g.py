from django.shortcuts import render
from src.dao.data_db_dao import DAO
import polars as pl


def IP_440g(request):
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
        end_month = request.POST.get("end_month")

        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")

        sales_A_1 = request.POST.get("sales_A_1")
        sales_A_2 = request.POST.get("sales_A_2")

        fuel_A_1 = request.POST.get("fuel_A_1")
        fuel_A_2 = request.POST.get("fuel_A_2")

        other_products_A_1 = request.POST.get("other_products_A_1")
        other_products_A_2 = request.POST.get("other_products_A_2")

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

        others_A_1 = request.POST.get("others_A_1")
        others_A_2 = request.POST.get("others_A_2")

        total_gross_A_1 = request.POST.get("total_gross_A_1")
        total_gross_A_2 = request.POST.get("total_gross_A_2")

        cost_B_1 = request.POST.get("cost_B_1")
        cost_B_2 = request.POST.get("cost_B_2")

        salaries_B_1 = request.POST.get("salaries_B_1")
        salaries_B_2 = request.POST.get("salaries_B_2")

        interests_B_1 = request.POST.get("interests_B_1")
        interests_B_2 = request.POST.get("interests_B_2")

        depreciation_B_1 = request.POST.get("depreciation_B_1")
        depreciation_B_2 = request.POST.get("depreciation_B_2")

        rent_B_1 = request.POST.get("rent_B_1")
        rent_B_2 = request.POST.get("rent_B_2")

        bad_debts_B_1 = request.POST.get("bad_debts_B_1")
        bad_debts_B_2 = request.POST.get("bad_debts_B_2")

        donations_B_1 = request.POST.get("donations_B_1")
        donations_B_2 = request.POST.get("donations_B_2")

        sales_B_1 = request.POST.get("sales_B_1")
        sales_B_2 = request.POST.get("sales_B_2")

        purchases_B_1 = request.POST.get("purchases_B_1")
        purchases_B_2 = request.POST.get("purchases_B_2")

        other_purchases_B_1 = request.POST.get("other_purchases_B_1")
        other_purchases_B_2 = request.POST.get("other_purchases_B_2")

        licenses_B_1 = request.POST.get("licenses_B_1")
        licenses_B_2 = request.POST.get("licenses_B_2")

        other_operations_B_1 = request.POST.get("other_operations_B_1")
        other_operations_B_2 = request.POST.get("other_operations_B_2")

        total_operations_B_1 = request.POST.get("total_operations_B_1")
        total_operations_B_2 = request.POST.get("total_operations_B_2")

        net_profit_C_1 = request.POST.get("net_profit_C_1")
        net_profit_C_2 = request.POST.get("net_profit_C_2")

        income_C_1 = request.POST.get("income_C_1")
        income_C_2 = request.POST.get("income_C_2")

        profit_C_after_1 = request.POST.get("profit_C_after_1")
        profit_C_after_2 = request.POST.get("profit_C_after_2")

        sales_D_1 = request.POST.get("sales_D_1")
        sales_D_2 = request.POST.get("sales_D_2")

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
            pl.Series("end_month", [end_month], dtype=pl.String),
            pl.Series("start_year", [start_year], dtype=pl.String),
            pl.Series("end_year", [end_year], dtype=pl.String),
            pl.Series("sales_A_1", [float(sales_A_1)], dtype=pl.Float64), 
            pl.Series("sales_A_2", [float(sales_A_2)], dtype=pl.Float64),
            pl.Series("fuel_A_1", [float(fuel_A_1)], dtype=pl.Float64),
            pl.Series("fuel_A_2", [float(fuel_A_2)], dtype=pl.Float64),
            pl.Series("other_products_A_1", [float(other_products_A_1)], dtype=pl.Float64),
            pl.Series("other_products_A_2", [float(other_products_A_2)], dtype=pl.Float64),
            pl.Series("less_cost_A_1", [float(less_cost_A_1)], dtype=pl.Float64),
            pl.Series("less_cost_A_2", [float(less_cost_A_2)], dtype=pl.Float64),
            pl.Series("inventory_beginning_1", [float(inventory_beginning_1)], dtype=pl.Float64),
            pl.Series("inventory_beginning_2", [float(inventory_beginning_2)], dtype=pl.Float64),
            pl.Series("purchases_A_1", [float(purchases_A_1)], dtype=pl.Float64),
            pl.Series("purchases_A_2", [float(purchases_A_2)], dtype=pl.Float64),
            pl.Series("inventory_end_1", [float(inventory_end_1)], dtype=pl.Float64),
            pl.Series("inventory_end_2", [float(inventory_end_2)], dtype=pl.Float64),
            pl.Series("gross_profit_A_1", [float(gross_profit_A_1)], dtype=pl.Float64),
            pl.Series("gross_profit_A_2", [float(gross_profit_A_2)], dtype=pl.Float64),
            pl.Series("other_income_A_1", [float(other_income_A_1)], dtype=pl.Float64),
            pl.Series("other_income_A_2", [float(other_income_A_2)], dtype=pl.Float64),
            pl.Series("interests_A_1", [float(interests_A_1)], dtype=pl.Float64),
            pl.Series("interests_A_2", [float(interests_A_2)], dtype=pl.Float64),
            pl.Series("rent_A_1", [float(rent_A_1)], dtype=pl.Float64),
            pl.Series("rent_A_2", [float(rent_A_2)], dtype=pl.Float64),
            pl.Series("capital_gain_A_1", [float(capital_gain_A_1)], dtype=pl.Float64),
            pl.Series("capital_gain_A_2", [float(capital_gain_A_2)], dtype=pl.Float64),
            pl.Series("dividends_A_1", [float(dividends_A_1)], dtype=pl.Float64),
            pl.Series("dividends_A_2", [float(dividends_A_2)], dtype=pl.Float64),
            pl.Series("others_A_1", [float(others_A_1)], dtype=pl.Float64),
            pl.Series("others_A_2", [float(others_A_2)], dtype=pl.Float64),
            pl.Series("total_gross_A_1", [float(total_gross_A_1)], dtype=pl.Float64),
            pl.Series("total_gross_A_2", [float(total_gross_A_2)], dtype=pl.Float64),
            pl.Series("cost_B_1", [float(cost_B_1)], dtype=pl.Float64),
            pl.Series("cost_B_2", [float(cost_B_2)], dtype=pl.Float64),
            pl.Series("salaries_B_1", [float(salaries_B_1)], dtype=pl.Float64),
            pl.Series("salaries_B_2", [float(salaries_B_2)], dtype=pl.Float64),
            pl.Series("interests_B_1", [float(interests_B_1)], dtype=pl.Float64),
            pl.Series("interests_B_2", [float(interests_B_2)], dtype=pl.Float64),
            pl.Series("depreciation_B_1", [float(depreciation_B_1)], dtype=pl.Float64),
            pl.Series("depreciation_B_2", [float(depreciation_B_2)], dtype=pl.Float64),
            pl.Series("rent_B_1", [float(rent_B_1)], dtype=pl.Float64),
            pl.Series("rent_B_2", [float(rent_B_2)], dtype=pl.Float64),
            pl.Series("bad_debts_B_1", [float(bad_debts_B_1)], dtype=pl.Float64),
            pl.Series("bad_debts_B_2", [float(bad_debts_B_2)], dtype=pl.Float64),
            pl.Series("donations_B_1", [float(donations_B_1)], dtype=pl.Float64),
            pl.Series("donations_B_2", [float(donations_B_2)], dtype=pl.Float64),
            pl.Series("sales_B_1", [float(sales_B_1)], dtype=pl.Float64),
            pl.Series("sales_B_2", [float(sales_B_2)], dtype=pl.Float64),
            pl.Series("purchases_B_1", [float(purchases_B_1)], dtype=pl.Float64),
            pl.Series("purchases_B_2", [float(purchases_B_2)], dtype=pl.Float64),
            pl.Series("other_purchases_B_1", [float(other_purchases_B_1)], dtype=pl.Float64),
            pl.Series("other_purchases_B_2", [float(other_purchases_B_2)], dtype=pl.Float64),
            pl.Series("licenses_B_1", [float(licenses_B_1)], dtype=pl.Float64),
            pl.Series("licenses_B_2", [float(licenses_B_2)], dtype=pl.Float64),
            pl.Series("other_operations_B_1", [float(other_operations_B_1)], dtype=pl.Float64),
            pl.Series("other_operations_B_2", [float(other_operations_B_2)], dtype=pl.Float64),
            pl.Series("total_operations_B_1", [float(total_operations_B_1)], dtype=pl.Float64),
            pl.Series("total_operations_B_2", [float(total_operations_B_2)], dtype=pl.Float64),
            pl.Series("net_profit_C_1", [float(net_profit_C_1)], dtype=pl.Float64),
            pl.Series("net_profit_C_2", [float(net_profit_C_2)], dtype=pl.Float64),
            pl.Series("income_C_1", [float(income_C_1)], dtype=pl.Float64),
            pl.Series("income_C_2", [float(income_C_2)], dtype=pl.Float64),
            pl.Series("profit_C_after_1", [float(profit_C_after_1)], dtype=pl.Float64),
            pl.Series("profit_C_after_2", [float(profit_C_after_2)], dtype=pl.Float64),
            pl.Series("sales_D_1", [float(sales_D_1)], dtype=pl.Float64),
            pl.Series("sales_D_2", [float(sales_D_2)], dtype=pl.Float64),
            pl.Series("name", [name], dtype=pl.String),
            pl.Series("rank", [rank], dtype=pl.String)
        ]
        
        df = pl.DataFrame(data)
        DAO().insert_forms(df, "IP_440g", 33)

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-440g.html")
