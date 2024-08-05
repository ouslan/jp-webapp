from django.shortcuts import render
from src.dao.data_db_dao import DAO
import csv
import os


def JP_560_63111(request):

    if request.method == "POST":
        # Retrieve form data
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")
        sales_1 = request.POST.get("sales_1")
        sales_2 = request.POST.get("sales_2")
        premiums_1 = request.POST.get("premiums_1")
        premiums_2 = request.POST.get("premiums_2")
        interest_received_1 = request.POST.get("interest_received_1")
        interest_received_2 = request.POST.get("interest_received_2")
        other_income_1 = request.POST.get("other_income_1")
        other_income_2 = request.POST.get("other_income_2")
        total_income_1 = request.POST.get("total_income_1")
        total_income_2 = request.POST.get("total_income_2")
        interest_paid_1 = request.POST.get("interest_paid_1")
        interest_paid_2 = request.POST.get("interest_paid_2")
        claims_paid_1 = request.POST.get("claims_paid_1")
        claims_paid_2 = request.POST.get("claims_paid_2")
        other_expenditures_1 = request.POST.get("other_expenditures_1")
        other_expenditures_2 = request.POST.get("other_expenditures_2")
        total_expenditures_1 = request.POST.get("total_expenditures_1")
        total_expenditures_2 = request.POST.get("total_expenditures_2")
        net_profit_loss_1 = request.POST.get("net_profit_loss_1")
        net_profit_loss_2 = request.POST.get("net_profit_loss_2")
        initial_inventory_1 = request.POST.get("initial_inventory_1")
        initial_inventory_2 = request.POST.get("initial_inventory_2")
        final_inventory_1 = request.POST.get("final_inventory_1")
        final_inventory_2 = request.POST.get("final_inventory_2")
        signature = request.POST.get("signature")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/JP-560-63111.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "ssn",
                        "tel",
                        "fax",
                        "sales_1",
                        "sales_2",
                        "premiums_1",
                        "premiums_2",
                        "interest_received_1",
                        "interest_received_2",
                        "other_income_1",
                        "other_income_2",
                        "total_income_1",
                        "total_income_2",
                        "interest_paid_1",
                        "interest_paid_2",
                        "claims_paid_1",
                        "claims_paid_2",
                        "other_expenditures_1",
                        "other_expenditures_2",
                        "total_expenditures_1",
                        "total_expenditures_2",
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
                    ssn,
                    tel,
                    fax,
                    sales_1,
                    sales_2,
                    premiums_1,
                    premiums_2,
                    interest_received_1,
                    interest_received_2,
                    other_income_1,
                    other_income_2,
                    total_income_1,
                    total_income_2,
                    interest_paid_1,
                    interest_paid_2,
                    claims_paid_1,
                    claims_paid_2,
                    other_expenditures_1,
                    other_expenditures_2,
                    total_expenditures_1,
                    total_expenditures_2,
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
            data_path="data/cuestionarios/ingreso_neto/JP-560-63111.csv",
            dtypes={
                "ssn": str,
                "tel": str,
                "fax": str,
                "sales_1": float,
                "sales_2": float,
                "premiums_1": float,
                "premiums_2": float,
                "interest_received_1": float,
                "interest_received_2": float,
                "other_income_1": float,
                "other_income_2": float,
                "total_income_1": float,
                "total_income_2": float,
                "interest_paid_1": float,
                "interest_paid_2": float,
                "claims_paid_1": float,
                "claims_paid_2": float,
                "other_expenditures_1": float,
                "other_expenditures_2": float,
                "total_expenditures_1": float,
                "total_expenditures_2": float,
                "net_profit_loss_1": float,
                "net_profit_loss_2": float,
                "initial_inventory_1": float,
                "initial_inventory_2": float,
                "final_inventory_1": float,
                "final_inventory_2": float,
                "signature": str,
                "rank": str,
            },
            table_name="JP_560_63111",
            table_id="19",
            debug=False,
        )

        return render(request, "forms/succesfull.html")

    return render(request, "forms/yearly/ingreso_neto/JP-560-63111.html")
