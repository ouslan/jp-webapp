from django.shortcuts import render
from src.dao.data_db_dao import DAO
import polars as pl

def IP_540J(request):
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
        incomes_industries_business_1 = request.POST.get(
            "incomes_industries_business_1"
        )
        incomes_industries_business_2 = request.POST.get(
            "incomes_industries_business_2"
        )
        expenses_newspapers_1 = request.POST.get("expenses_newspapers_1")
        expenses_newspapers_2 = request.POST.get("expenses_newspapers_2")
        expenses_radio_television_1 = request.POST.get("expenses_radio_television_1")
        expenses_radio_television_2 = request.POST.get("expenses_radio_television_2")
        expenses_other_1 = request.POST.get("expenses_other_1")
        expenses_other_2 = request.POST.get("expenses_other_2")
        gross_profit_1 = request.POST.get("gross_profit_1")
        gross_profit_2 = request.POST.get("gross_profit_2")
        dividends_paid_1 = request.POST.get("dividends_paid_1")
        dividends_paid_2 = request.POST.get("dividends_paid_2")
        expenses_interests_1 = request.POST.get("expenses_interests_1")
        expenses_interests_2 = request.POST.get("expenses_interests_2")
        expenses_rent_1 = request.POST.get("expenses_rent_1")
        expenses_rent_2 = request.POST.get("expenses_rent_2")
        expenses_gain_loss_1 = request.POST.get("expenses_gain_loss_1")
        expenses_gain_loss_2 = request.POST.get("expenses_gain_loss_2")
        dividends_paid_other_1 = request.POST.get("dividends_paid_other_1")
        dividends_paid_other_2 = request.POST.get("dividends_paid_other_2")
        incomes_total_1 = request.POST.get("incomes_total_1")
        incomes_total_2 = request.POST.get("incomes_total_2")
        expenses_total_1 = request.POST.get("expenses_total_1")
        expenses_total_2 = request.POST.get("expenses_total_2")
        salaries_wages_bonus_1 = request.POST.get("salaries_wages_bonus_1")
        salaries_wages_bonus_2 = request.POST.get("salaries_wages_bonus_2")
        interests_1 = request.POST.get("interests_1")
        interests_2 = request.POST.get("interests_2")
        rents_1 = request.POST.get("rents_1")
        rents_2 = request.POST.get("rents_2")
        depreciation_1 = request.POST.get("depreciation_1")
        depreciation_2 = request.POST.get("depreciation_2")
        other_taxes_1 = request.POST.get("other_taxes_1")
        other_taxes_2 = request.POST.get("other_taxes_2")
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
        other_operating_expenses_1 = request.POST.get("other_operating_expenses_1")
        other_operating_expenses_2 = request.POST.get("other_operating_expenses_2")
        profit_incomes_tax_1 = request.POST.get("profit_incomes_tax_1")
        profit_incomes_tax_2 = request.POST.get("profit_incomes_tax_2")
        profit_incomes_mortage_loans_1 = request.POST.get(
            "profit_incomes_mortage_loans_1"
        )
        profit_incomes_mortage_loans_2 = request.POST.get(
            "profit_incomes_mortage_loans_2"
        )
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
            pl.Series("incomes_industries_business_1", [float(incomes_industries_business_1)], dtype=pl.Float64),
            pl.Series("incomes_industries_business_2", [float(incomes_industries_business_2)], dtype=pl.Float64),
            pl.Series("expenses_newspapers_1", [float(expenses_newspapers_1)], dtype=pl.Float64),
            pl.Series("expenses_newspapers_2", [float(expenses_newspapers_2)], dtype=pl.Float64),
            pl.Series("expenses_radio_television_1", [float(expenses_radio_television_1)], dtype=pl.Float64),
            pl.Series("expenses_radio_television_2", [float(expenses_radio_television_2)], dtype=pl.Float64),
            pl.Series("expenses_other_1", [float(expenses_other_1)], dtype=pl.Float64),
            pl.Series("expenses_other_2", [float(expenses_other_2)], dtype=pl.Float64),
            pl.Series("gross_profit_1", [float(gross_profit_1)], dtype=pl.Float64),
            pl.Series("gross_profit_2", [float(gross_profit_2)], dtype=pl.Float64),
            pl.Series("dividends_paid_1", [float(dividends_paid_1)], dtype=pl.Float64),
            pl.Series("dividends_paid_2", [float(dividends_paid_2)], dtype=pl.Float64),
            pl.Series("expenses_interests_1", [float(expenses_interests_1)], dtype=pl.Float64),
            pl.Series("expenses_interests_2", [float(expenses_interests_2)], dtype=pl.Float64),
            pl.Series("expenses_rent_1", [float(expenses_rent_1)], dtype=pl.Float64),
            pl.Series("expenses_rent_2", [float(expenses_rent_2)], dtype=pl.Float64),
            pl.Series("expenses_gain_loss_1", [float(expenses_gain_loss_1)], dtype=pl.Float64),
            pl.Series("expenses_gain_loss_2", [float(expenses_gain_loss_2)], dtype=pl.Float64),
            pl.Series("dividends_paid_other_1", [float(dividends_paid_other_1)], dtype=pl.Float64),
            pl.Series("dividends_paid_other_2", [float(dividends_paid_other_2)], dtype=pl.Float64),
            pl.Series("incomes_total_1", [float(incomes_total_1)], dtype=pl.Float64),
            pl.Series("incomes_total_2", [float(incomes_total_2)], dtype=pl.Float64),
            pl.Series("expenses_total_1", [float(expenses_total_1)], dtype=pl.Float64),
            pl.Series("expenses_total_2", [float(expenses_total_2)], dtype=pl.Float64),
            pl.Series("salaries_wages_bonus_1", [float(salaries_wages_bonus_1)], dtype=pl.Float64),
            pl.Series("salaries_wages_bonus_2", [float(salaries_wages_bonus_2)], dtype=pl.Float64),
            pl.Series("interests_1", [float(interests_1)], dtype=pl.Float64),
            pl.Series("interests_2", [float(interests_2)], dtype=pl.Float64),
            pl.Series("rents_1", [float(rents_1)], dtype=pl.Float64),
            pl.Series("rents_2", [float(rents_2)], dtype=pl.Float64),
            pl.Series("depreciation_1", [float(depreciation_1)], dtype=pl.Float64),
            pl.Series("depreciation_2", [float(depreciation_2)], dtype=pl.Float64),
            pl.Series("other_taxes_1", [float(other_taxes_1)], dtype=pl.Float64),
            pl.Series("other_taxes_2", [float(other_taxes_2)], dtype=pl.Float64),
            pl.Series("donations_1", [float(donations_1)], dtype=pl.Float64),
            pl.Series("donations_2", [float(donations_2)], dtype=pl.Float64),
            pl.Series("sales_tax_1", [float(sales_tax_1)], dtype=pl.Float64),
            pl.Series("sales_tax_2", [float(sales_tax_2)], dtype=pl.Float64),
            pl.Series("machinery_1", [float(machinery_1)], dtype=pl.Float64),
            pl.Series("machinery_2", [float(machinery_2)], dtype=pl.Float64),
            pl.Series("other_purchases_1", [float(other_purchases_1)], dtype=pl.Float64),
            pl.Series("other_purchases_2", [float(other_purchases_2)], dtype=pl.Float64),
            pl.Series("licenses_1", [float(licenses_1)], dtype=pl.Float64),
            pl.Series("licenses_2", [float(licenses_2)], dtype=pl.Float64),
            pl.Series("other_operating_expenses_1", [float(other_operating_expenses_1)], dtype=pl.Float64),
            pl.Series("other_operating_expenses_2", [float(other_operating_expenses_2)], dtype=pl.Float64),
            pl.Series("profit_incomes_tax_1", [float(profit_incomes_tax_1)], dtype=pl.Float64),
            pl.Series("profit_incomes_tax_2", [float(profit_incomes_tax_2)], dtype=pl.Float64),
            pl.Series("profit_incomes_mortage_loans_1", [float(profit_incomes_mortage_loans_1)], dtype=pl.Float64),
            pl.Series("profit_incomes_mortage_loans_2", [float(profit_incomes_mortage_loans_2)], dtype=pl.Float64),
            pl.Series("sales_tax_withheld_1", [float(sales_tax_withheld_1)], dtype=pl.Float64),
            pl.Series("sales_tax_withheld_2", [float(sales_tax_withheld_2)], dtype=pl.Float64),
            pl.Series("name", [name], dtype=pl.String),
            pl.Series("rank", [rank], dtype=pl.String),
        ]
        
        df = pl.DataFrame(data)
        DAO().insert_forms(df, "IP_540J", 42)

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-540J.html")
