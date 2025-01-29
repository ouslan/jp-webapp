from django.shortcuts import render
from src.dao.data_db_dao import DAO
import polars as pl


def JP_560_2(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get("company_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")
        sales_1 = request.POST.get("sales_1")
        sales_2 = request.POST.get("sales_2")
        interest_received_1 = request.POST.get("interest_received_1")
        interest_received_2 = request.POST.get("interest_received_2")
        other_income_1 = request.POST.get("other_income_1")
        other_income_2 = request.POST.get("other_income_2")
        total_income_1 = request.POST.get("total_income_1")
        total_income_2 = request.POST.get("total_income_2")
        interest_paid_1 = request.POST.get("interest_paid_1")
        interest_paid_2 = request.POST.get("interest_paid_2")
        other_expenditures_1_1 = request.POST.get("other_expenditures_1_1")
        other_expenditures_2_1 = request.POST.get("other_expenditures_1_2")
        other_expenditures_1_2 = request.POST.get("other_expenditures_2_1")
        other_expenditures_2_2 = request.POST.get("other_expenditures_2_2")
        net_profit_loss_1 = request.POST.get("net_profit_loss_1")
        net_profit_loss_2 = request.POST.get("net_profit_loss_2")
        initial_inventory_1 = request.POST.get("initial_inventory_1")
        initial_inventory_2 = request.POST.get("initial_inventory_2")
        final_inventory_1 = request.POST.get("final_inventory_1")
        final_inventory_2 = request.POST.get("final_inventory_2")
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
            pl.Series("sales_1", [float(sales_1)], dtype=pl.Float64),
            pl.Series("sales_2", [float(sales_2)], dtype=pl.Float64),
            pl.Series("interest_received_1", [float(interest_received_1)], dtype=pl.Float64),
            pl.Series("interest_received_2", [float(interest_received_2)], dtype=pl.Float64),
            pl.Series("other_income_1", [float(other_income_1)], dtype=pl.Float64),
            pl.Series("other_income_2", [float(other_income_2)], dtype=pl.Float64),
            pl.Series("total_income_1", [float(total_income_1)], dtype=pl.Float64),
            pl.Series("total_income_2", [float(total_income_2)], dtype=pl.Float64),
            pl.Series("interest_paid_1", [float(interest_paid_1)], dtype=pl.Float64),
            pl.Series("interest_paid_2", [float(interest_paid_2)], dtype=pl.Float64),
            pl.Series("other_expenditures_1_1", [float(other_expenditures_1_1)], dtype=pl.Float64),
            pl.Series("other_expenditures_2_1", [float(other_expenditures_2_1)], dtype=pl.Float64),
            pl.Series("other_expenditures_1_2", [float(other_expenditures_1_2)], dtype=pl.Float64),
            pl.Series("other_expenditures_2_2", [float(other_expenditures_2_2)], dtype=pl.Float64),
            pl.Series("net_profit_loss_1", [float(net_profit_loss_1)], dtype=pl.Float64),
            pl.Series("net_profit_loss_2", [float(net_profit_loss_2)], dtype=pl.Float64),
            pl.Series("initial_inventory_1", [float(initial_inventory_1)], dtype=pl.Float64),
            pl.Series("initial_inventory_2", [float(initial_inventory_2)], dtype=pl.Float64),
            pl.Series("final_inventory_1", [float(final_inventory_1)], dtype=pl.Float64),
            pl.Series("final_inventory_2", [float(final_inventory_2)], dtype=pl.Float64),
            pl.Series("signature", [signature], dtype=pl.String),
            pl.Series("rank", [rank], dtype=pl.String),
        ]
        
        df = pl.DataFrame(data)
        DAO().insert_forms(df, "JP_560_2", 43)

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/JP-560-2.html")
