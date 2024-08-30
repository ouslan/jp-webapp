from django.shortcuts import render
from src.dao.data_db_dao import DAO
import polars as pl


def IP_520(request):
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
        closing_date = request.POST.get("closing_date")
        branches = request.POST.get("branches")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")

        incomes_interests_1 = request.POST.get("incomes_interests_1")
        incomes_interests_2 = request.POST.get("incomes_interests_2")
        incomes_personal_loans_1 = request.POST.get("incomes_personal_loans_1")
        incomes_personal_loans_2 = request.POST.get("incomes_personal_loans_2")
        incomes_mortage_loans_1 = request.POST.get("incomes_mortage_loans_1")
        incomes_mortage_loans_2 = request.POST.get("incomes_mortage_loans_2")
        incomes_other_1 = request.POST.get("incomes_other_1")
        incomes_other_2 = request.POST.get("incomes_other_2")
        incomes_rent_1 = request.POST.get("incomes_rent_1")
        incomes_rent_2 = request.POST.get("incomes_rent_2")
        incomes_dividends_1 = request.POST.get("incomes_dividends_1")
        incomes_dividends_2 = request.POST.get("incomes_dividends_2")
        incomes_financing_charges_1 = request.POST.get("incomes_financing_charges_1")
        incomes_financing_charges_2 = request.POST.get("incomes_financing_charges_2")
        incomes_service_charges_1 = request.POST.get("incomes_service_charges_1")
        incomes_service_charges_2 = request.POST.get("incomes_service_charges_2")
        incomes_commissions_1 = request.POST.get("incomes_commissions_1")
        incomes_commissions_2 = request.POST.get("incomes_commissions_2")
        incomes_finance_leasing_1 = request.POST.get("incomes_finance_leasing_1")
        incomes_finance_leasing_2 = request.POST.get("incomes_finance_leasing_2")
        incomes_capital_gain_loss_1 = request.POST.get("incomes_capital_gain_loss_1")
        incomes_capital_gain_loss_2 = request.POST.get("incomes_capital_gain_loss_2")
        incomes_other_operations_1 = request.POST.get("incomes_other_operations_1")
        incomes_other_operations_2 = request.POST.get("incomes_other_operations_2")
        incomes_total_1 = request.POST.get("incomes_total_1")
        incomes_total_2 = request.POST.get("incomes_total_2")
        expenses_salaries_wages_bonus_1 = request.POST.get(
            "expenses_salaries_wages_bonus_1"
        )
        expenses_salaries_wages_bonus_2 = request.POST.get(
            "expenses_salaries_wages_bonus_2"
        )
        expenses_interests_1 = request.POST.get("expenses_interests_1")
        expenses_interests_2 = request.POST.get("expenses_interests_2")
        interests_to_individuals_1 = request.POST.get("interests_to_individuals_1")
        interests_to_individuals_2 = request.POST.get("interests_to_individuals_2")
        interests_to_corporations_1 = request.POST.get("interests_to_corporations_1")
        interests_to_corporations_2 = request.POST.get("interests_to_corporations_2")
        corporation_936_1 = request.POST.get("corporation_936_1")
        corporation_936_2 = request.POST.get("corporation_936_2")
        other_corporation_1 = request.POST.get("other_corporation_1")
        other_corporation_2 = request.POST.get("other_corporation_2")
        interests_other_1 = request.POST.get("interests_other_1")
        interests_other_2 = request.POST.get("interests_other_2")
        expenses_rent_1 = request.POST.get("expenses_rent_1")
        expenses_rent_2 = request.POST.get("expenses_rent_2")
        expenses_depreciation_1 = request.POST.get("expenses_depreciation_1")
        expenses_depreciation_2 = request.POST.get("expenses_depreciation_2")
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
        expenses_total_1 = request.POST.get("expenses_total_1")
        expenses_total_2 = request.POST.get("expenses_total_2")
        gross_profit_1 = request.POST.get("gross_profit_1")
        gross_profit_2 = request.POST.get("gross_profit_2")
        profit_income_tax_1 = request.POST.get("profit_income_tax_1")
        profit_income_tax_2 = request.POST.get("profit_income_tax_2")
        profit_after_income_tax_1 = request.POST.get("profit_after_income_tax_1")
        profit_after_income_tax_2 = request.POST.get("profit_after_income_tax_2")
        dividends_paid_1 = request.POST.get("dividends_paid_1")
        dividends_paid_2 = request.POST.get("dividends_paid_2")
        sales_tax_1 = request.POST.get("sales_tax_1")
        sales_tax_2 = request.POST.get("sales_tax_2")

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
            pl.Series("closing_date", [closing_date], dtype=pl.String),
            pl.Series("branches", [branches], dtype=pl.String),
            pl.Series("start_year", [start_year], dtype=pl.String),
            pl.Series("end_year", [end_year], dtype=pl.String),
            pl.Series("incomes_interests_1", [float(incomes_interests_1)], dtype=pl.Float64),
            pl.Series("incomes_interests_2", [float(incomes_interests_2)], dtype=pl.Float64),
            pl.Series("incomes_personal_loans_1", [float(incomes_personal_loans_1)], dtype=pl.Float64),
            pl.Series("incomes_personal_loans_2", [float(incomes_personal_loans_2)], dtype=pl.Float64),
            pl.Series("incomes_mortage_loans_1", [float(incomes_mortage_loans_1)], dtype=pl.Float64),
            pl.Series("incomes_mortage_loans_2", [float(incomes_mortage_loans_2)], dtype=pl.Float64),
            pl.Series("incomes_other_1", [float(incomes_other_1)], dtype=pl.Float64),
            pl.Series("incomes_other_2", [float(incomes_other_2)], dtype=pl.Float64),
            pl.Series("incomes_rent_1", [float(incomes_rent_1)], dtype=pl.Float64),
            pl.Series("incomes_rent_2", [float(incomes_rent_2)], dtype=pl.Float64),
            pl.Series("incomes_dividends_1", [float(incomes_dividends_1)], dtype=pl.Float64),
            pl.Series("incomes_dividends_2", [float(incomes_dividends_2)], dtype=pl.Float64),
            pl.Series("incomes_financing_charges_1", [float(incomes_financing_charges_1)], dtype=pl.Float64),
            pl.Series("incomes_financing_charges_2", [float(incomes_financing_charges_2)], dtype=pl.Float64),
            pl.Series("incomes_service_charges_1", [float(incomes_service_charges_1)], dtype=pl.Float64),
            pl.Series("incomes_service_charges_2", [float(incomes_service_charges_2)], dtype=pl.Float64),
            pl.Series("incomes_commissions_1", [float(incomes_commissions_1)], dtype=pl.Float64),
            pl.Series("incomes_commissions_2", [float(incomes_commissions_2)], dtype=pl.Float64),
            pl.Series("incomes_finance_leasing_1", [float(incomes_finance_leasing_1)], dtype=pl.Float64),
            pl.Series("incomes_finance_leasing_2", [float(incomes_finance_leasing_2)], dtype=pl.Float64),
            pl.Series("incomes_capital_gain_loss_1", [float(incomes_capital_gain_loss_1)], dtype=pl.Float64),
            pl.Series("incomes_capital_gain_loss_2", [float(incomes_capital_gain_loss_2)], dtype=pl.Float64),
            pl.Series("incomes_other_operations_1", [float(incomes_other_operations_1)], dtype=pl.Float64),
            pl.Series("incomes_other_operations_2", [float(incomes_other_operations_2)], dtype=pl.Float64),
            pl.Series("incomes_total_1", [float(incomes_total_1)], dtype=pl.Float64),
            pl.Series("incomes_total_2", [float(incomes_total_2)], dtype=pl.Float64),
            pl.Series("expenses_salaries_wages_bonus_1", [float(expenses_salaries_wages_bonus_1)], dtype=pl.Float64),
            pl.Series("expenses_salaries_wages_bonus_2", [float(expenses_salaries_wages_bonus_2)], dtype=pl.Float64),
            pl.Series("expenses_interests_1", [float(expenses_interests_1)], dtype=pl.Float64),
            pl.Series("expenses_interests_2", [float(expenses_interests_2)], dtype=pl.Float64),
            pl.Series("interests_to_individuals_1", [float(interests_to_individuals_1)], dtype=pl.Float64),
            pl.Series("interests_to_individuals_2", [float(interests_to_individuals_2)], dtype=pl.Float64),
            pl.Series("interests_to_corporations_1", [float(interests_to_corporations_1)], dtype=pl.Float64),
            pl.Series("interests_to_corporations_2", [float(interests_to_corporations_2)], dtype=pl.Float64),
            pl.Series("corporation_936_1", [float(corporation_936_1)], dtype=pl.Float64),
            pl.Series("corporation_936_2", [float(corporation_936_2)], dtype=pl.Float64),
            pl.Series("other_corporation_1", [float(other_corporation_1)], dtype=pl.Float64),
            pl.Series("other_corporation_2", [float(other_corporation_2)], dtype=pl.Float64),
            pl.Series("interests_other_1", [float(interests_other_1)], dtype=pl.Float64),
            pl.Series("interests_other_2", [float(interests_other_2)], dtype=pl.Float64),
            pl.Series("expenses_rent_1", [float(expenses_rent_1)], dtype=pl.Float64),
            pl.Series("expenses_rent_2", [float(expenses_rent_2)], dtype=pl.Float64),
            pl.Series("expenses_depreciation_1", [float(expenses_depreciation_1)], dtype=pl.Float64),
            pl.Series("expenses_depreciation_2", [float(expenses_depreciation_2)], dtype=pl.Float64),
            pl.Series("expenses_bad_debts_1", [float(expenses_bad_debts_1)], dtype=pl.Float64),
            pl.Series("expenses_bad_debts_2", [float(expenses_bad_debts_2)], dtype=pl.Float64),
            pl.Series("expenses_donations_1", [float(expenses_donations_1)], dtype=pl.Float64),
            pl.Series("expenses_donations_2", [float(expenses_donations_2)], dtype=pl.Float64),
            pl.Series("expenses_sales_taxes_1", [float(expenses_sales_taxes_1)], dtype=pl.Float64),
            pl.Series("expenses_sales_taxes_2", [float(expenses_sales_taxes_2)], dtype=pl.Float64),
            pl.Series("expenses_machinary_1", [float(expenses_machinary_1)], dtype=pl.Float64),
            pl.Series("expenses_machinary_2", [float(expenses_machinary_2)], dtype=pl.Float64),
            pl.Series("expenses_other_purchases_1", [float(expenses_other_purchases_1)], dtype=pl.Float64),
            pl.Series("expenses_other_purchases_2", [float(expenses_other_purchases_2)], dtype=pl.Float64),
            pl.Series("expenses_licenses_1", [float(expenses_licenses_1)], dtype=pl.Float64),
            pl.Series("expenses_licenses_2", [float(expenses_licenses_2)], dtype=pl.Float64),
            pl.Series("expenses_other_operations_1", [float(expenses_other_operations_1)], dtype=pl.Float64),
            pl.Series("expenses_other_operations_2", [float(expenses_other_operations_2)], dtype=pl.Float64),
            pl.Series("expenses_total_1", [float(expenses_total_1)], dtype=pl.Float64),
            pl.Series("expenses_total_2", [float(expenses_total_2)], dtype=pl.Float64),
            pl.Series("gross_profit_1", [float(gross_profit_1)], dtype=pl.Float64),
            pl.Series("gross_profit_2", [float(gross_profit_2)], dtype=pl.Float64),
            pl.Series("profit_income_tax_1", [float(profit_income_tax_1)], dtype=pl.Float64),
            pl.Series("profit_income_tax_2", [float(profit_income_tax_2)], dtype=pl.Float64),
            pl.Series("profit_after_income_tax_1", [float(profit_after_income_tax_1)], dtype=pl.Float64),
            pl.Series("profit_after_income_tax_2", [float(profit_after_income_tax_2)], dtype=pl.Float64),
            pl.Series("dividends_paid_1", [float(dividends_paid_1)], dtype=pl.Float64),
            pl.Series("dividends_paid_2", [float(dividends_paid_2)], dtype=pl.Float64),
            pl.Series("sales_tax_1", [float(sales_tax_1)], dtype=pl.Float64),
            pl.Series("sales_tax_2", [float(sales_tax_2)], dtype=pl.Float64),
            pl.Series("name", [name], dtype=pl.String),
            pl.Series("rank", [rank], dtype=pl.String),
        ]
        
        df = pl.DataFrame(data)
        DAO().insert_forms(df, "IP_520", 37)

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-520.html")
