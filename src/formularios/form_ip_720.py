from django.shortcuts import render
from src.dao.data_db_dao import DAO
import polars as pl

def IP_720(request):
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
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")

        total_incomes_1 = request.POST.get("total_incomes_1")
        total_incomes_2 = request.POST.get("total_incomes_2")
        incomes_from_persons_1 = request.POST.get("incomes_from_persons_1")
        incomes_from_persons_2 = request.POST.get("incomes_from_persons_2")
        incomes_from_industries_1 = request.POST.get("incomes_from_industries_1")
        incomes_from_industries_2 = request.POST.get("incomes_from_industries_2")
        incomes_room_rental_1 = request.POST.get("incomes_room_rental_1")
        incomes_room_rental_2 = request.POST.get("incomes_room_rental_2")
        incomes_casino_1 = request.POST.get("incomes_casino_1")
        incomes_casino_2 = request.POST.get("incomes_casino_2")
        incomes_less_prizes_1 = request.POST.get("incomes_less_prizes_1")
        incomes_less_prizes_2 = request.POST.get("incomes_less_prizes_2")
        incomes_food_beverages_1 = request.POST.get("incomes_food_beverages_1")
        incomes_food_beverages_2 = request.POST.get("incomes_food_beverages_2")
        incomes_interests_1 = request.POST.get("incomes_interests_1")
        incomes_interests_2 = request.POST.get("incomes_interests_2")
        incomes_rent_1 = request.POST.get("incomes_rent_1")
        incomes_rent_2 = request.POST.get("incomes_rent_2")
        incomes_capital_gain_loss_1 = request.POST.get("incomes_capital_gain_loss_1")
        incomes_capital_gain_loss_2 = request.POST.get("incomes_capital_gain_loss_2")
        other_incomes_1 = request.POST.get("other_incomes_1")
        other_incomes_2 = request.POST.get("other_incomes_2")
        total_expenses_1 = request.POST.get("total_expenses_1")
        total_expenses_2 = request.POST.get("total_expenses_2")
        expenses_food_beverages_1 = request.POST.get("expenses_food_beverages_1")
        expenses_food_beverages_2 = request.POST.get("expenses_food_beverages_2")
        expenses_food_1 = request.POST.get("expenses_food_1")
        expenses_food_2 = request.POST.get("expenses_food_2")
        expenses_beverages_1 = request.POST.get("expenses_beverages_1")
        expenses_beverages_2 = request.POST.get("expenses_beverages_2")
        expenses_music_entertainment_1 = request.POST.get(
            "expenses_music_entertainment_1"
        )
        expenses_music_entertainment_2 = request.POST.get(
            "expenses_music_entertainment_2"
        )
        expenses_salaries_wages_bonus_1 = request.POST.get(
            "expenses_salaries_wages_bonus_1"
        )
        expenses_salaries_wages_bonus_2 = request.POST.get(
            "expenses_salaries_wages_bonus_2"
        )
        expenses_uniform_1 = request.POST.get("expenses_uniform_1")
        expenses_uniform_2 = request.POST.get("expenses_uniform_2")
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
        expenses_free_food_employees_1 = request.POST.get(
            "expenses_free_food_employees_1"
        )
        expenses_free_food_employees_2 = request.POST.get(
            "expenses_free_food_employees_2"
        )
        expenses_sales_tax_1 = request.POST.get("expenses_sales_tax_1")
        expenses_sales_tax_2 = request.POST.get("expenses_sales_tax_2")
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
        other_expenses_1 = request.POST.get("other_expenses_1")
        other_expenses_2 = request.POST.get("other_expenses_2")
        net_profit_loss_1 = request.POST.get("net_profit_loss_1")
        net_profit_loss_2 = request.POST.get("net_profit_loss_2")
        profit_incomes_tax_1 = request.POST.get("profit_incomes_tax_1")
        profit_incomes_tax_2 = request.POST.get("profit_incomes_tax_2")
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
            pl.Series("closing_date", [closing_date], dtype=pl.String),
            pl.Series("start_year", [start_year], dtype=pl.String),
            pl.Series("end_year", [end_year], dtype=pl.String),
            pl.Series("total_incomes_1", [float(total_incomes_1)], dtype=pl.Float64),
            pl.Series("total_incomes_2", [float(total_incomes_2)], dtype=pl.Float64),
            pl.Series("incomes_from_persons_1", [float(incomes_from_persons_1)], dtype=pl.Float64),
            pl.Series("incomes_from_persons_2", [float(incomes_from_persons_2)], dtype=pl.Float64),
            pl.Series("incomes_from_industries_1", [float(incomes_from_industries_1)], dtype=pl.Float64),
            pl.Series("incomes_from_industries_2", [float(incomes_from_industries_2)], dtype=pl.Float64),
            pl.Series("incomes_room_rental_1", [float(incomes_room_rental_1)], dtype=pl.Float64),
            pl.Series("incomes_room_rental_2", [float(incomes_room_rental_2)], dtype=pl.Float64),
            pl.Series("incomes_casino_1", [float(incomes_casino_1)], dtype=pl.Float64),
            pl.Series("incomes_casino_2", [float(incomes_casino_2)], dtype=pl.Float64),
            pl.Series("incomes_less_prizes_1", [float(incomes_less_prizes_1)], dtype=pl.Float64),
            pl.Series("incomes_less_prizes_2", [float(incomes_less_prizes_2)], dtype=pl.Float64),
            pl.Series("incomes_food_beverages_1", [float(incomes_food_beverages_1)], dtype=pl.Float64),
            pl.Series("incomes_food_beverages_2", [float(incomes_food_beverages_2)], dtype=pl.Float64),
            pl.Series("incomes_interests_1", [float(incomes_interests_1)], dtype=pl.Float64),
            pl.Series("incomes_interests_2", [float(incomes_interests_2)], dtype=pl.Float64),
            pl.Series("incomes_rent_1", [float(incomes_rent_1)], dtype=pl.Float64),
            pl.Series("incomes_rent_2", [float(incomes_rent_2)], dtype=pl.Float64),
            pl.Series("incomes_capital_gain_loss_1", [float(incomes_capital_gain_loss_1)], dtype=pl.Float64),
            pl.Series("incomes_capital_gain_loss_2", [float(incomes_capital_gain_loss_2)], dtype=pl.Float64),
            pl.Series("other_incomes_1", [float(other_incomes_1)], dtype=pl.Float64),
            pl.Series("other_incomes_2", [float(other_incomes_2)], dtype=pl.Float64),
            pl.Series("total_expenses_1", [float(total_expenses_1)], dtype=pl.Float64),
            pl.Series("total_expenses_2", [float(total_expenses_2)], dtype=pl.Float64),
            pl.Series("expenses_food_beverages_1", [float(expenses_food_beverages_1)], dtype=pl.Float64),
            pl.Series("expenses_food_beverages_2", [float(expenses_food_beverages_2)], dtype=pl.Float64),
            pl.Series("expenses_food_1", [float(expenses_food_1)], dtype=pl.Float64),
            pl.Series("expenses_food_2", [float(expenses_food_2)], dtype=pl.Float64),
            pl.Series("expenses_beverages_1", [float(expenses_beverages_1)], dtype=pl.Float64),
            pl.Series("expenses_beverages_2", [float(expenses_beverages_2)], dtype=pl.Float64),
            pl.Series("expenses_music_entertainment_1", [float(expenses_music_entertainment_1)], dtype=pl.Float64),
            pl.Series("expenses_music_entertainment_2", [float(expenses_music_entertainment_2)], dtype=pl.Float64),
            pl.Series("expenses_salaries_wages_bonus_1", [float(expenses_salaries_wages_bonus_1)], dtype=pl.Float64),
            pl.Series("expenses_salaries_wages_bonus_2", [float(expenses_salaries_wages_bonus_2)], dtype=pl.Float64),
            pl.Series("expenses_uniform_1", [float(expenses_uniform_1)], dtype=pl.Float64),
            pl.Series("expenses_uniform_2", [float(expenses_uniform_2)], dtype=pl.Float64),
            pl.Series("expenses_interests_1", [float(expenses_interests_1)], dtype=pl.Float64),
            pl.Series("expenses_interests_2", [float(expenses_interests_2)], dtype=pl.Float64),
            pl.Series("expenses_rent_1", [float(expenses_rent_1)], dtype=pl.Float64),
            pl.Series("expenses_rent_2", [float(expenses_rent_2)], dtype=pl.Float64),
            pl.Series("expenses_depreciation_1", [float(expenses_depreciation_1)], dtype=pl.Float64),
            pl.Series("expenses_depreciation_2", [float(expenses_depreciation_2)], dtype=pl.Float64),
            pl.Series("expenses_bad_debts_1", [float(expenses_bad_debts_1)], dtype=pl.Float64),
            pl.Series("expenses_bad_debts_2", [float(expenses_bad_debts_2)], dtype=pl.Float64),
            pl.Series("expenses_donations_1", [float(expenses_donations_1)], dtype=pl.Float64),
            pl.Series("expenses_donations_2", [float(expenses_donations_2)], dtype=pl.Float64),
            pl.Series("expenses_free_food_employees_1", [float(expenses_free_food_employees_1)], dtype=pl.Float64),
            pl.Series("expenses_free_food_employees_2", [float(expenses_free_food_employees_2)], dtype=pl.Float64),
            pl.Series("expenses_sales_tax_1", [float(expenses_sales_tax_1)], dtype=pl.Float64),
            pl.Series("expenses_sales_tax_2", [float(expenses_sales_tax_2)], dtype=pl.Float64),
            pl.Series("expenses_purchases_machinery_1", [float(expenses_purchases_machinery_1)], dtype=pl.Float64),
            pl.Series("expenses_purchases_machinery_2", [float(expenses_purchases_machinery_2)], dtype=pl.Float64),
            pl.Series("expenses_other_purchases_1", [float(expenses_other_purchases_1)], dtype=pl.Float64),
            pl.Series("expenses_other_purchases_2", [float(expenses_other_purchases_2)], dtype=pl.Float64),
            pl.Series("expenses_licenses_1", [float(expenses_licenses_1)], dtype=pl.Float64),
            pl.Series("expenses_licenses_2", [float(expenses_licenses_2)], dtype=pl.Float64),
            pl.Series("other_expenses_1", [float(other_expenses_1)], dtype=pl.Float64),
            pl.Series("other_expenses_2", [float(other_expenses_2)], dtype=pl.Float64),
            pl.Series("net_profit_loss_1", [float(net_profit_loss_1)], dtype=pl.Float64),
            pl.Series("net_profit_loss_2", [float(net_profit_loss_2)], dtype=pl.Float64),
            pl.Series("profit_incomes_tax_1", [float(profit_incomes_tax_1)], dtype=pl.Float64),
            pl.Series("profit_incomes_tax_2", [float(profit_incomes_tax_2)], dtype=pl.Float64),
            pl.Series("profit_after_income_tax_1", [float(profit_after_income_tax_1)], dtype=pl.Float64),
            pl.Series("profit_after_income_tax_2", [float(profit_after_income_tax_2)], dtype=pl.Float64),
            pl.Series("sales_tax_withheld_1", [float(sales_tax_withheld_1)], dtype=pl.Float64),
            pl.Series("sales_tax_withheld_2", [float(sales_tax_withheld_2)], dtype=pl.Float64),
            pl.Series("name", [name], dtype=pl.String),
            pl.Series("rank", [rank], dtype=pl.String),
        ]
        
        df = pl.DataFrame(data)
        DAO().insert_forms(df, "IP_720", 10)

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-720.html")
