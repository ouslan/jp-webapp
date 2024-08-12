from django.shortcuts import render
from src.dao.data_db_dao import DAO
import csv
import os


def IP_230(request):
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
        business_function = request.POST.get("business_function")
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        income_project_A_12 = request.POST.get("income_project_A_12")
        income_project_A_13 = request.POST.get("income_project_A_13")
        people_A_12 = request.POST.get("people_A_12")
        people_A_13 = request.POST.get("people_A_13")
        industries_businesses_A_12 = request.POST.get("industries_businesses_A_12")
        industries_businesses_A_13 = request.POST.get("industries_businesses_A_13")
        direct_indirect_B_12 = request.POST.get("direct_indirect_B_12")
        direct_indirect_B_13 = request.POST.get("direct_indirect_B_13")
        direct_christmas_vacation_B_12 = request.POST.get(
            "direct_christmas_vacation_B_12"
        )
        direct_christmas_vacation_B_13 = request.POST.get(
            "direct_christmas_vacation_B_13"
        )
        rent_land_building_B_12 = request.POST.get("rent_land_building_B_12")
        rent_land_building_B_13 = request.POST.get("rent_land_building_B_13")
        rent_equipment_B_12 = request.POST.get("rent_equipment_B_12")
        rent_equipment_B_13 = request.POST.get("rent_equipment_B_13")
        depreciation_B_12 = request.POST.get("depreciation_B_12")
        depreciation_B_13 = request.POST.get("depreciation_B_13")
        sales_tax_B_12 = request.POST.get("sales_tax_B_12")
        sales_tax_B_13 = request.POST.get("sales_tax_B_13")
        purchases_machinery_equipment_B_12 = request.POST.get(
            "purchases_machinery_equipment_B_12"
        )
        purchases_machinery_equipment_B_13 = request.POST.get(
            "purchases_machinery_equipment_B_13"
        )
        other_purchases_B_12 = request.POST.get("other_purchases_B_12")
        other_purchases_B_13 = request.POST.get("other_purchases_B_13")
        licenses_patent_B_12 = request.POST.get("licenses_patent_B_12")
        licenses_patent_B_13 = request.POST.get("licenses_patent_B_13")
        other_costs_direct_indirect_B_12 = request.POST.get(
            "other_costs_direct_indirect_B_12"
        )
        other_costs_direct_indirect_B_13 = request.POST.get(
            "other_costs_direct_indirect_B_13"
        )
        gross_profit_C_12 = request.POST.get("gross_profit_C_12")
        gross_profit_C_13 = request.POST.get("gross_profit_C_13")
        other_income_D_12 = request.POST.get("other_income_D_12")
        other_income_D_13 = request.POST.get("other_income_D_13")
        interest_D_12 = request.POST.get("interest_D_12")
        interest_D_13 = request.POST.get("interest_D_13")
        rent_land_building_D_12 = request.POST.get("rent_land_building_D_12")
        rent_land_building_D_13 = request.POST.get("rent_land_building_D_13")
        gain_loss_D_12 = request.POST.get("gain_loss_D_12")
        gain_loss_D_13 = request.POST.get("gain_loss_D_13")
        other_D_12 = request.POST.get("other_D_12")
        other_D_13 = request.POST.get("other_D_13")
        gross_profit_E_12 = request.POST.get("gross_profit_E_12")
        gross_profit_E_13 = request.POST.get("gross_profit_E_13")
        administrative_F_12 = request.POST.get("administrative_F_12")
        administrative_F_13 = request.POST.get("administrative_F_13")
        salaries_wages_bonus_commissions_F_12 = request.POST.get(
            "salaries_wages_bonus_commissions_F_12"
        )
        salaries_wages_bonus_commissions_F_13 = request.POST.get(
            "salaries_wages_bonus_commissions_F_13"
        )
        interest_F_12 = request.POST.get("interest_F_12")
        interest_F_13 = request.POST.get("interest_F_13")
        rent_land_building_F_12 = request.POST.get("rent_land_building_F_12")
        rent_land_building_F_13 = request.POST.get("rent_land_building_F_13")
        depreciation_F_12 = request.POST.get("depreciation_F_12")
        depreciation_F_13 = request.POST.get("depreciation_F_13")
        bad_debts_F_12 = request.POST.get("bad_debts_F_12")
        bad_debts_F_13 = request.POST.get("bad_debts_F_13")
        donation_F_12 = request.POST.get("donation_F_12")
        donation_F_13 = request.POST.get("donation_F_13")
        other_expenses_F_12 = request.POST.get("other_expenses_F_12")
        other_expenses_F_13 = request.POST.get("other_expenses_F_13")
        net_profit_G_12 = request.POST.get("net_profit_G_12")
        net_profit_G_13 = request.POST.get("net_profit_G_13")
        income_tax_G_12 = request.POST.get("income_tax_G_12")
        income_tax_G_13 = request.POST.get("income_tax_G_13")
        profit_after_tax_G_12 = request.POST.get("profit_after_tax_G_12")
        profit_after_tax_G_13 = request.POST.get("profit_after_tax_G_13")
        sales_tax_H_12 = request.POST.get("sales_tax_H_12")
        sales_tax_H_13 = request.POST.get("sales_tax_H_13")
        beginning_year_HA = request.POST.get("beginning_year_HA")
        end_year_HB = request.POST.get("end_year_HB")
        beginning_year_HC = request.POST.get("beginning_year_HC")
        end_year_HD = request.POST.get("end_year_HD")
        signature = request.POST.get("signature")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-230.csv"
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
                        "legal_form",
                        "cfc",
                        "business_function",
                        "closing_date",
                        "start_year",
                        "end_year",
                        "income_project_A_12",
                        "income_project_A_13",
                        "people_A_12",
                        "people_A_13",
                        "industries_businesses_A_12",
                        "industries_businesses_A_13",
                        "direct_indirect_B_12",
                        "direct_indirect_B_13",
                        "direct_christmas_vacation_B_12",
                        "direct_christmas_vacation_B_13",
                        "rent_land_building_B_12",
                        "rent_land_building_B_13",
                        "rent_equipment_B_12",
                        "rent_equipment_B_13",
                        "depreciation_B_12",
                        "depreciation_B_13",
                        "sales_tax_B_12",
                        "sales_tax_B_13",
                        "purchases_machinery_equipment_B_12",
                        "purchases_machinery_equipment_B_13",
                        "other_purchases_B_12",
                        "other_purchases_B_13",
                        "licenses_patent_B_12",
                        "licenses_patent_B_13",
                        "other_costs_direct_indirect_B_12",
                        "other_costs_direct_indirect_B_13",
                        "gross_profit_C_12",
                        "gross_profit_C_13",
                        "other_income_D_12",
                        "other_income_D_13",
                        "interest_D_12",
                        "interest_D_13",
                        "rent_land_building_D_12",
                        "rent_land_building_D_13",
                        "gain_loss_D_12",
                        "gain_loss_D_13",
                        "other_D_12",
                        "other_D_13",
                        "gross_profit_E_12",
                        "gross_profit_E_13",
                        "administrative_F_12",
                        "administrative_F_13",
                        "salaries_wages_bonus_commissions_F_12",
                        "salaries_wages_bonus_commissions_F_13",
                        "interest_F_12",
                        "interest_F_13",
                        "rent_land_building_F_12",
                        "rent_land_building_F_13",
                        "depreciation_F_12",
                        "depreciation_F_13",
                        "bad_debts_F_12",
                        "bad_debts_F_13",
                        "donation_F_12",
                        "donation_F_13",
                        "other_expenses_F_12",
                        "other_expenses_F_13",
                        "net_profit_G_12",
                        "net_profit_G_13",
                        "income_tax_G_12",
                        "income_tax_G_13",
                        "profit_after_tax_G_12",
                        "profit_after_tax_G_13",
                        "sales_tax_H_12",
                        "sales_tax_H_13",
                        "beginning_year_HA",
                        "end_year_HB",
                        "beginning_year_HC",
                        "end_year_HD",
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
                    legal_form,
                    cfc,
                    business_function,
                    closing_date,
                    start_year,
                    end_year,
                    income_project_A_12,
                    income_project_A_13,
                    people_A_12,
                    people_A_13,
                    industries_businesses_A_12,
                    industries_businesses_A_13,
                    direct_indirect_B_12,
                    direct_indirect_B_13,
                    direct_christmas_vacation_B_12,
                    direct_christmas_vacation_B_13,
                    rent_land_building_B_12,
                    rent_land_building_B_13,
                    rent_equipment_B_12,
                    rent_equipment_B_13,
                    depreciation_B_12,
                    depreciation_B_13,
                    sales_tax_B_12,
                    sales_tax_B_13,
                    purchases_machinery_equipment_B_12,
                    purchases_machinery_equipment_B_13,
                    other_purchases_B_12,
                    other_purchases_B_13,
                    licenses_patent_B_12,
                    licenses_patent_B_13,
                    other_costs_direct_indirect_B_12,
                    other_costs_direct_indirect_B_13,
                    gross_profit_C_12,
                    gross_profit_C_13,
                    other_income_D_12,
                    other_income_D_13,
                    interest_D_12,
                    interest_D_13,
                    rent_land_building_D_12,
                    rent_land_building_D_13,
                    gain_loss_D_12,
                    gain_loss_D_13,
                    other_D_12,
                    other_D_13,
                    gross_profit_E_12,
                    gross_profit_E_13,
                    administrative_F_12,
                    administrative_F_13,
                    salaries_wages_bonus_commissions_F_12,
                    salaries_wages_bonus_commissions_F_13,
                    interest_F_12,
                    interest_F_13,
                    rent_land_building_F_12,
                    rent_land_building_F_13,
                    depreciation_F_12,
                    depreciation_F_13,
                    bad_debts_F_12,
                    bad_debts_F_13,
                    donation_F_12,
                    donation_F_13,
                    other_expenses_F_12,
                    other_expenses_F_13,
                    net_profit_G_12,
                    net_profit_G_13,
                    income_tax_G_12,
                    income_tax_G_13,
                    profit_after_tax_G_12,
                    profit_after_tax_G_13,
                    sales_tax_H_12,
                    sales_tax_H_13,
                    beginning_year_HA,
                    end_year_HB,
                    beginning_year_HC,
                    end_year_HD,
                    signature,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-230.csv",
            dtypes={
                "company_name": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "ssn": str,
                "tel": str,
                "fax": str,
                "legal_form": str,
                "cfc": str,
                "business_function": str,
                "closing_date": str,
                "start_year": int,
                "end_year": int,
                "income_project_A_12": float,
                "income_project_A_13": float,
                "people_A_12": float,
                "people_A_13": float,
                "industries_businesses_A_12": float,
                "industries_businesses_A_13": float,
                "direct_indirect_B_12": float,
                "direct_indirect_B_13": float,
                "direct_christmas_vacation_B_12": float,
                "direct_christmas_vacation_B_13": float,
                "rent_land_building_B_12": float,
                "rent_land_building_B_13": float,
                "rent_equipment_B_12": float,
                "rent_equipment_B_13": float,
                "depreciation_B_12": float,
                "depreciation_B_13": float,
                "sales_tax_B_12": float,
                "sales_tax_B_13": float,
                "purchases_machinery_equipment_B_12": float,
                "purchases_machinery_equipment_B_13": float,
                "other_purchases_B_12": float,
                "other_purchases_B_13": float,
                "licenses_patent_B_12": float,
                "licenses_patent_B_13": float,
                "other_costs_direct_indirect_B_12": float,
                "other_costs_direct_indirect_B_13": float,
                "gross_profit_C_12": float,
                "gross_profit_C_13": float,
                "other_income_D_12": float,
                "other_income_D_13": float,
                "interest_D_12": float,
                "interest_D_13": float,
                "rent_land_building_D_12": float,
                "rent_land_building_D_13": float,
                "gain_loss_D_12": float,
                "gain_loss_D_13": float,
                "other_D_12": float,
                "other_D_13": float,
                "gross_profit_E_12": float,
                "gross_profit_E_13": float,
                "administrative_F_12": float,
                "administrative_F_13": float,
                "salaries_wages_bonus_commissions_F_12": float,
                "salaries_wages_bonus_commissions_F_13": float,
                "interest_F_12": float,
                "interest_F_13": float,
                "rent_land_building_F_12": float,
                "rent_land_building_F_13": float,
                "depreciation_F_12": float,
                "depreciation_F_13": float,
                "bad_debts_F_12": float,
                "bad_debts_F_13": float,
                "donation_F_12": float,
                "donation_F_13": float,
                "other_expenses_F_12": float,
                "other_expenses_F_13": float,
                "net_profit_G_12": float,
                "net_profit_G_13": float,
                "income_tax_G_12": float,
                "income_tax_G_13": float,
                "profit_after_tax_G_12": float,
                "profit_after_tax_G_13": float,
                "sales_tax_H_12": float,
                "sales_tax_H_13": float,
                "beginning_year_HA": int,
                "end_year_HB": int,
                "beginning_year_HC": int,
                "end_year_HD": int,
                "signature": str,
                "rank": str,
            },
            table_name="IP_230",
            table_id="21",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-230.html")
