from django.shortcuts import render
from src.dao.data_db_dao import DAO
import polars as pl

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

        data = [
            pl.Series("agency_form", [agency_form], dtype=pl.String),
            pl.Series("agency_to", [agency_to], dtype=pl.String),
            pl.Series("salaries_wages", [float(salaries_wages)], dtype=pl.Float64),
            pl.Series("civil_service", [float(civil_service)], dtype=pl.Float64),
            pl.Series("federal_employee_retirement",[float(federal_employee_retirement)],dtype=pl.Float64),
            pl.Series("thrift_savings_disbursements",[float(thrift_savings_disbursements)],dtype=pl.Float64),
            pl.Series("social_security",[float(social_security)],dtype=pl.Float64),
            pl.Series("life_insurance_health_disbursements",[float(life_insurance_health_disbursements)],dtype=pl.Float64),
            pl.Series("other_disbursements",[float(other_disbursements)],dtype=pl.Float64),
            pl.Series("construction_contracts",[float(construction_contracts)],dtype=pl.Float64),
            pl.Series("rent_disbursements",[float(rent_disbursements)],dtype=pl.Float64),
            pl.Series("other_purchases",[float(other_purchases)],dtype=pl.Float64),
            pl.Series("equipment_supplies",[float(equipment_supplies)],dtype=pl.Float64),
            pl.Series("rent_sales",[float(rent_sales)],dtype=pl.Float64),
            pl.Series("other_sales",[float(other_sales)],dtype=pl.Float64),
            pl.Series("income_tax",[float(income_tax)],dtype=pl.Float64),
            pl.Series("other_taxes_licenses",[float(other_taxes_licenses)],dtype=pl.Float64),
            pl.Series("fines_penalties",[float(fines_penalties)],dtype=pl.Float64),
            pl.Series("interest",[float(interest)],dtype=pl.Float64),
            pl.Series("other_collections_1",[other_collections_1],dtype=pl.String),
            pl.Series("other_collections_amount_1",[float(other_collections_amount_1)],dtype=pl.Float64),
            pl.Series("other_collections_2",[other_collections_2],dtype=pl.String),
            pl.Series("other_collections_amount_2",[float(other_collections_amount_2)],dtype=pl.Float64),
            pl.Series("other_collections_3",[other_collections_3],dtype=pl.String),
            pl.Series("other_collections_amount_3",[float(other_collections_amount_3)],dtype=pl.Float64),
            pl.Series("civil_service_2",[float(civil_service_2)],dtype=pl.Float64),
            pl.Series("federal_employee",[float(federal_employee)],dtype=pl.Float64),
            pl.Series("thrift_saving_deductions",[float(thrift_saving_deductions)],dtype=pl.Float64),
            pl.Series("social_security_deductions",[float(social_security_deductions)],dtype=pl.Float64),
            pl.Series("life_insurance_health_deductions",[float(life_insurance_health_deductions)],dtype=pl.Float64),
            pl.Series("income_tax_deductions",[float(income_tax_deductions)],dtype=pl.Float64),
            pl.Series("saving_bonds",[float(saving_bonds)],dtype=pl.Float64),
            pl.Series("other_deductions",[other_deductions],dtype=pl.String),
            pl.Series("other_deductions_amount",[float(other_deductions_amount)],dtype=pl.Float64),
            pl.Series("commonwealth",[float(commonwealth)],dtype=pl.Float64),
            pl.Series("municipal",[float(municipal)],dtype=pl.Float64),
            pl.Series("individuals_private_institutions",[float(individuals_private_institutions)],dtype=pl.Float64),
            pl.Series("death_disability",[float(death_disability)],dtype=pl.Float64),
            pl.Series("other_payments_1",[other_payments_1],dtype=pl.String),
            pl.Series("other_payments_amount_1",[float(other_payments_amount_1)],dtype=pl.Float64),
            pl.Series("other_payments_2",[other_payments_2],dtype=pl.String),
            pl.Series("other_payments_amount_2",[float(other_payments_amount_2)],dtype=pl.Float64),
            pl.Series("loans_advances",[float(loans_advances)],dtype=pl.Float64),
            pl.Series("repayments_loans",[float(repayments_loans)],dtype=pl.Float64),
            pl.Series("total_loans_amount",[float(total_loans_amount)],dtype=pl.Float64),
            pl.Series("loans_cancelled",[float(loans_cancelled)],dtype=pl.Float64),
            pl.Series("other_credits",[float(other_credits)],dtype=pl.Float64),
            pl.Series("loans_and_advances",[loans_and_advances],dtype=pl.String),
            pl.Series("loans_and_advances_amount",[float(loans_and_advances_amount)],dtype=pl.Float64),
            pl.Series("interest_collected",[float(interest_collected)],dtype=pl.Float64),
            pl.Series("forgiveness_credit",[float(forgiveness_credit)],dtype=pl.Float64),
            pl.Series("reporting_agency",[reporting_agency],dtype=pl.String),
        ]
        
        df = pl.DataFrame(data)
        DAO().insert_forms(df, "JP_547", 6)
        
        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/balanza_de_pagos/JP-547.html")
