from django.shortcuts import render
from src.dao.data_db_dao import DAO
import polars as pl


def IP_490(request):

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
        income_operations_1 = request.POST.get("income_operations_1")
        income_operations_2 = request.POST.get("income_operations_2")
        people_A_1 = request.POST.get("people_A_1")
        people_A_2 = request.POST.get("people_A_2")
        industries_businesses_A_1 = request.POST.get("industries_businesses_A_1")
        industries_businesses_A_2 = request.POST.get("industries_businesses_A_2")
        interest_A_1 = request.POST.get("interest_A_1")
        interest_A_2 = request.POST.get("interest_A_2")
        rent_land_1 = request.POST.get("rent_land_1")
        rent_land_2 = request.POST.get("rent_land_2")
        capital_gain_1 = request.POST.get("capital_gain_1")
        capital_gain_2 = request.POST.get("capital_gain_2")
        other_income_A_1 = request.POST.get("other_income_A_1")
        other_income_A_2 = request.POST.get("other_income_A_2")
        total_income_A_1 = request.POST.get("total_income_A_1")
        total_income_A_2 = request.POST.get("total_income_A_2")
        salaries_wages_bonus_B_1 = request.POST.get("salaries_wages_bonus_B_1")
        salaries_wages_bonus_B_2 = request.POST.get("salaries_wages_bonus_B_2")
        interests_B_1 = request.POST.get("interests_B_1")
        interests_B_2 = request.POST.get("interests_B_2")
        rent_B_1 = request.POST.get("rent_B_1")
        rent_B_2 = request.POST.get("rent_B_2")
        depreciation_B_1 = request.POST.get("depreciation_B_1")
        depreciation_B_2 = request.POST.get("depreciation_B_2")
        donation_B_1 = request.POST.get("donation_B_1")
        donation_B_2 = request.POST.get("donation_B_2")
        sales_taxes_B_1 = request.POST.get("sales_taxes_B_1")
        sales_taxes_B_2 = request.POST.get("sales_taxes_B_2")
        purchases_B_1 = request.POST.get("purchases_B_1")
        purchases_B_2 = request.POST.get("purchases_B_2")
        other_purchases_B_1 = request.POST.get("other_purchases_B_1")
        other_purchases_B_2 = request.POST.get("other_purchases_B_2")
        other_operations_B_1 = request.POST.get("other_operations_B_1")
        other_operations_B_2 = request.POST.get("other_operations_B_2")
        total_expenses_B_1 = request.POST.get("total_expenses_B_1")
        total_expenses_B_2 = request.POST.get("total_expenses_B_2")
        net_profit_1 = request.POST.get("net_profit_1")
        net_profit_2 = request.POST.get("net_profit_2")
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
            pl.Series("business_type", [business_type], dtype=pl.String),
            pl.Series("business_function", [business_function], dtype=pl.String),
            pl.Series("closing_date", [closing_date], dtype=pl.String),
            pl.Series("start_year", [start_year], dtype=pl.String),
            pl.Series("end_year", [end_year], dtype=pl.String),
            pl.Series("income_operations_1", [float(income_operations_1)], dtype=pl.Float64),
            pl.Series("income_operations_2", [float(income_operations_2)], dtype=pl.Float64),
            pl.Series("people_A_1", [float(people_A_1)], dtype=pl.Float64),
            pl.Series("people_A_2", [float(people_A_2)], dtype=pl.Float64),
            pl.Series("industries_businesses_A_1", [float(industries_businesses_A_1)], dtype=pl.Float64),
            pl.Series("industries_businesses_A_2", [float(industries_businesses_A_2)], dtype=pl.Float64),
            pl.Series("interest_A_1", [float(interest_A_1)], dtype=pl.Float64),
            pl.Series("interest_A_2", [float(interest_A_2)], dtype=pl.Float64),
            pl.Series("rent_land_1", [float(rent_land_1)], dtype=pl.Float64),
            pl.Series("rent_land_2", [float(rent_land_2)], dtype=pl.Float64),
            pl.Series("capital_gain_1", [float(capital_gain_1)], dtype=pl.Float64),
            pl.Series("capital_gain_2", [float(capital_gain_2)], dtype=pl.Float64),
            pl.Series("other_income_A_1", [float(other_income_A_1)], dtype=pl.Float64),
            pl.Series("other_income_A_2", [float(other_income_A_2)], dtype=pl.Float64),
            pl.Series("total_income_A_1", [float(total_income_A_1)], dtype=pl.Float64),
            pl.Series("total_income_A_2", [float(total_income_A_2)], dtype=pl.Float64),
            pl.Series("salaries_wages_bonus_B_1", [float(salaries_wages_bonus_B_1)], dtype=pl.Float64),
            pl.Series("salaries_wages_bonus_B_2", [float(salaries_wages_bonus_B_2)], dtype=pl.Float64),
            pl.Series("interests_B_1", [float(interests_B_1)], dtype=pl.Float64),
            pl.Series("interests_B_2", [float(interests_B_2)], dtype=pl.Float64),
            pl.Series("rent_B_1", [float(rent_B_1)], dtype=pl.Float64),
            pl.Series("rent_B_2", [float(rent_B_2)], dtype=pl.Float64),
            pl.Series("depreciation_B_1", [float(depreciation_B_1)], dtype=pl.Float64),
            pl.Series("depreciation_B_2", [float(depreciation_B_2)], dtype=pl.Float64),
            pl.Series("donation_B_1", [float(donation_B_1)], dtype=pl.Float64),
            pl.Series("donation_B_2", [float(donation_B_2)], dtype=pl.Float64),
            pl.Series("sales_taxes_B_1", [float(sales_taxes_B_1)], dtype=pl.Float64),
            pl.Series("sales_taxes_B_2", [float(sales_taxes_B_2)], dtype=pl.Float64),
            pl.Series("purchases_B_1", [float(purchases_B_1)], dtype=pl.Float64),
            pl.Series("purchases_B_2", [float(purchases_B_2)], dtype=pl.Float64),
            pl.Series("other_purchases_B_1", [float(other_purchases_B_1)], dtype=pl.Float64),
            pl.Series("other_purchases_B_2", [float(other_purchases_B_2)], dtype=pl.Float64),
            pl.Series("other_operations_B_1", [float(other_operations_B_1)], dtype=pl.Float64),
            pl.Series("other_operations_B_2", [float(other_operations_B_2)], dtype=pl.Float64),
            pl.Series("total_expenses_B_1", [float(total_expenses_B_1)], dtype=pl.Float64),
            pl.Series("total_expenses_B_2", [float(total_expenses_B_2)], dtype=pl.Float64),
            pl.Series("net_profit_1", [float(net_profit_1)], dtype=pl.Float64),
            pl.Series("net_profit_2", [float(net_profit_2)], dtype=pl.Float64),
            pl.Series("income_C_1", [float(income_C_1)], dtype=pl.Float64),
            pl.Series("income_C_2", [float(income_C_2)], dtype=pl.Float64),
            pl.Series("profit_C_after_1", [float(profit_C_after_1)], dtype=pl.Float64),
            pl.Series("profit_C_after_2", [float(profit_C_after_2)], dtype=pl.Float64),
            pl.Series("sales_D_1", [float(sales_D_1)], dtype=pl.Float64),
            pl.Series("sales_D_2", [float(sales_D_2)], dtype=pl.Float64),
            pl.Series("name", [name], dtype=pl.String),
            pl.Series("rank", [rank], dtype=pl.String),
        ]
        
        df = pl.DataFrame(data)
        DAO().insert_forms(df, "IP_490", 35)

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-490.html")
