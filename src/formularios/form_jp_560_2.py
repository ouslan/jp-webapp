from django.shortcuts import render
from src.dao.data_db_dao import DAO
import csv
import os


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

        csv_file_path = "data/cuestionarios/ingreso_neto/JP-560-2.csv"
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
                        "sales_1",
                        "sales_2",
                        "interest_received_1",
                        "interest_received_2",
                        "other_income_1",
                        "other_income_2",
                        "total_income_1",
                        "total_income_2",
                        "interest_paid_1",
                        "interest_paid_2",
                        "other_expenditures_1_1",
                        "other_expenditures_2_1",
                        "other_expenditures_1_2",
                        "other_expenditures_2_2",
                        "net_profit_loss_1",
                        "net_profit_loss_2",
                        "initial_inventory_1",
                        "initial_inventory_2",
                        "final_inventory_1",
                        "final_inventory_2",
                        "signature",
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
                    sales_1,
                    sales_2,
                    interest_received_1,
                    interest_received_2,
                    other_income_1,
                    other_income_2,
                    total_income_1,
                    total_income_2,
                    interest_paid_1,
                    interest_paid_2,
                    other_expenditures_1_1,
                    other_expenditures_2_1,
                    other_expenditures_1_2,
                    other_expenditures_2_2,
                    net_profit_loss_1,
                    net_profit_loss_2,
                    initial_inventory_1,
                    initial_inventory_2,
                    final_inventory_1,
                    final_inventory_2,
                    signature,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/JP-560-2.csv",
            dtypes={
                "company_name": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "ssn": str,
                "tel": str,
                "fax": str,
                "sales_1": float,
                "sales_2": float,
                "interest_received_1": float,
                "interest_received_2": float,
                "other_income_1": float,
                "other_income_2": float,
                "total_income_1": float,
                "total_income_2": float,
                "interest_paid_1": float,
                "interest_paid_2": float,
                "other_expenditures_1_1": float,
                "other_expenditures_2_1": float,
                "other_expenditures_1_2": float,
                "other_expenditures_2_2": float,
                "net_profit_loss_1": float,
                "net_profit_loss_2": float,
                "initial_inventory_1": float,
                "initial_inventory_2": float,
                "final_inventory_1": float,
                "final_inventory_2": float,
                "signature": str,
                "rank": str,
            },
            table_name="JP_560_2",
            table_id="43",
            debug=False,
        )

        return render(request, "forms/succesfull.html")

    return render(request, "forms/yearly/ingreso_neto/JP-560-2.html")
