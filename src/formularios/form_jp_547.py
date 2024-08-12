from django.shortcuts import render
from src.dao.data_db_dao import DAO
import csv
import os

def JP_547(request):
    if request.method == "POST":
        # Retrieve form data
        agency_form = request.POST.get("agency_form")
        agency_to = request.POST.get("agency_to")

        salaries_wages = request.POST.get("salaries_wages")
        civil_service = request.POST.get("civil_service")
        federal_employee_retirement = request.POST.get("federal_employee_retirement")
        thrift_savings_disbursements = request.POST.get("thrift_savings_disbursements")
        social_security = request.POST.get("social_security")
        life_insurance_health_disbursements = request.POST.get(
            "life_insurance_health_disbursements"
        )
        other_disbursements = request.POST.get("other_disbursements")
        construction_contracts = request.POST.get("construction_contracts")
        rent_disbursements = request.POST.get("rent_disbursements")
        other_purchases = request.POST.get("other_purchases")
        equipment_supplies = request.POST.get("equipment_supplies")
        rent_sales = request.POST.get("rent_sales")
        other_sales = request.POST.get("other_sales")
        income_tax = request.POST.get("income_tax")
        other_taxes_licenses = request.POST.get("other_taxes_licenses")
        fines_penalties = request.POST.get("fines_penalties")
        interest = request.POST.get("interest")
        other_collections_1 = request.POST.get("other_collections_1")
        other_collections_amount_1 = request.POST.get("other_collections_amount_1")
        other_collections_2 = request.POST.get("other_collections_2")
        other_collections_amount_2 = request.POST.get("other_collections_amount_2")
        other_collections_3 = request.POST.get("other_collections_3")
        other_collections_amount_3 = request.POST.get("other_collections_amount_3")
        civil_service_2 = request.POST.get("civil_service_2")
        federal_employee = request.POST.get("federal_employee")
        thrift_saving_deductions = request.POST.get("thrift_saving_deductions")
        social_security_deductions = request.POST.get("social_security_deductions")
        life_insurance_health_deductions = request.POST.get(
            "life_insurance_health_deductions"
        )
        income_tax_deductions = request.POST.get("income_tax_deductions")
        saving_bonds = request.POST.get("saving_bonds")
        other_deductions = request.POST.get("other_deductions")
        other_deductions_amount = request.POST.get("other_deductions_amount")
        commonwealth = request.POST.get("commonwealth")
        municipal = request.POST.get("municipal")
        individuals_private_institutions = request.POST.get(
            "individuals_private_institutions"
        )
        death_disability = request.POST.get("death_disability")
        other_payments_1 = request.POST.get("other_payments_1")
        other_payments_amount_1 = request.POST.get("other_payments_amount_1")
        other_payments_2 = request.POST.get("other_payments_2")
        other_payments_amount_2 = request.POST.get("other_payments_amount_2")
        loans_advances = request.POST.get("loans_advances")
        repayments_loans = request.POST.get("repayments_loans")
        total_loans_amount = request.POST.get("total_loans_amount")
        loans_cancelled = request.POST.get("loans_cancelled")
        other_credits = request.POST.get("other_credits")
        loans_and_advances = request.POST.get("loans_and_advances")
        loans_and_advances_amount = request.POST.get("loans_and_advances_amount")
        interest_collected = request.POST.get("interest_collected")
        forgiveness_credit = request.POST.get("forgiveness_credit")

        reporting_agency = request.POST.get("reporting_agency")

        csv_file_path = "data/cuestionarios/balanza_de_pagos/JP-547.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "agency_form",
                        "agency_to",
                        "salaries_wages",
                        "civil_service",
                        "federal_employee_retirement",
                        "thrift_savings_disbursements",
                        "social_security",
                        "life_insurance_health_disbursements",
                        "other_disbursements",
                        "construction_contracts",
                        "rent_disbursements",
                        "other_purchases",
                        "equipment_supplies",
                        "rent_sales",
                        "other_sales",
                        "income_tax",
                        "other_taxes_licenses",
                        "fines_penalties",
                        "interest",
                        "other_collections_1",
                        "other_collections_amount_1",
                        "other_collections_2",
                        "other_collections_amount_2",
                        "other_collections_3",
                        "other_collections_amount_3",
                        "civil_service_2",
                        "federal_employee",
                        "thrift_saving_deductions",
                        "social_security_deductions",
                        "life_insurance_health_deductions",
                        "income_tax_deductions",
                        "saving_bonds",
                        "other_deductions",
                        "other_deductions_amount",
                        "commonwealth",
                        "municipal",
                        "individuals_private_institutions",
                        "death_disability",
                        "other_payments_1",
                        "other_payments_amount_1",
                        "other_payments_2",
                        "other_payments_amount_2",
                        "loans_advances",
                        "repayments_loans",
                        "total_loans_amount",
                        "loans_cancelled",
                        "other_credits",
                        "loans_and_advances",
                        "loans_and_advances_amount",
                        "interest_collected",
                        "forgiveness_credit",
                        "reporting_agency",
                    ]
                )

            writer.writerow(
                [
                    agency_form,
                    agency_to,
                    salaries_wages,
                    civil_service,
                    federal_employee_retirement,
                    thrift_savings_disbursements,
                    social_security,
                    life_insurance_health_disbursements,
                    other_disbursements,
                    construction_contracts,
                    rent_disbursements,
                    other_purchases,
                    equipment_supplies,
                    rent_sales,
                    other_sales,
                    income_tax,
                    other_taxes_licenses,
                    fines_penalties,
                    interest,
                    other_collections_1,
                    other_collections_amount_1,
                    other_collections_2,
                    other_collections_amount_2,
                    other_collections_3,
                    other_collections_amount_3,
                    civil_service_2,
                    federal_employee,
                    thrift_saving_deductions,
                    social_security_deductions,
                    life_insurance_health_deductions,
                    income_tax_deductions,
                    saving_bonds,
                    other_deductions,
                    other_deductions_amount,
                    commonwealth,
                    municipal,
                    individuals_private_institutions,
                    death_disability,
                    other_payments_1,
                    other_payments_amount_1,
                    other_payments_2,
                    other_payments_amount_2,
                    loans_advances,
                    repayments_loans,
                    total_loans_amount,
                    loans_cancelled,
                    other_credits,
                    loans_and_advances,
                    loans_and_advances_amount,
                    interest_collected,
                    forgiveness_credit,
                    reporting_agency,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/balanza_de_pagos/JP-547.csv",
            dtypes={
                "agency_form": str,
                "agency_to": str,
                "salaries_wages": float,
                "civil_service": float,
                "federal_employee_retirement": float,
                "thrift_savings_disbursements": float,
                "social_security": float,
                "life_insurance_health_disbursements": float,
                "other_disbursements": float,
                "construction_contracts": float,
                "rent_disbursements": float,
                "other_purchases": float,
                "equipment_supplies": float,
                "rent_sales": float,
                "other_sales": float,
                "income_tax": float,
                "other_taxes_licenses": float,
                "fines_penalties": float,
                "interest": float,
                "other_collections_1": str,
                "other_collections_amount_1": float,
                "other_collections_2": str,
                "other_collections_amount_2": float,
                "other_collections_3": str,
                "other_collections_amount_3": float,
                "civil_service_2": float,
                "federal_employee": float,
                "thrift_saving_deductions": float,
                "social_security_deductions": float,
                "life_insurance_health_deductions": float,
                "income_tax_deductions": float,
                "saving_bonds": float,
                "other_deductions": str,
                "other_deductions_amount": float,
                "commonwealth": float,
                "municipal": float,
                "individuals_private_institutions": float,
                "death_disability": float,
                "other_payments_1": str,
                "other_payments_amount_1": float,
                "other_payments_2": str,
                "other_payments_amount_2": float,
                "loans_advances": float,
                "repayments_loans": float,
                "total_loans_amount": float,
                "loans_cancelled": float,
                "other_credits": float,
                "loans_and_advances": float,
                "loans_and_advances_amount": float,
                "interest_collected": float,
                "forgiveness_credit": float,
                "reporting_agency": str,
            },
            table_name="JP_547",
            table_id=6,
            debug=False,
        )
        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/balanza_de_pagos/JP-547.html")
