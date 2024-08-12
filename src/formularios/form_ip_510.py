from django.shortcuts import render
from src.dao.data_db_dao import DAO
import csv
import os

def IP_510(request):
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
        accounting_period = request.POST.get("accounting_period")
        main_product_1 = request.POST.get("main_product_1")
        main_product_2 = request.POST.get("main_product_2")
        raw_material_used = request.POST.get("raw_material_used")
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        sales_from_persons_1 = request.POST.get("sales_from_persons_1")
        sales_from_persons_2 = request.POST.get("sales_from_persons_2")
        sales_industries_businesses_1 = request.POST.get(
            "sales_industries_businesses_1"
        )
        sales_industries_businesses_2 = request.POST.get(
            "sales_industries_businesses_2"
        )
        sales_goods_1 = request.POST.get("sales_goods_1")
        sales_goods_2 = request.POST.get("sales_goods_2")
        sales_exports_goods_1 = request.POST.get("sales_exports_goods_1")
        sales_exports_goods_2 = request.POST.get("sales_exports_goods_2")
        sales_goods_from_others_firms_1 = request.POST.get(
            "sales_goods_from_others_firms_1"
        )
        sales_goods_from_others_firms_2 = request.POST.get(
            "sales_goods_from_others_firms_2"
        )
        sales_exports_goods_other_firms_1 = request.POST.get(
            "sales_exports_goods_other_firms_1"
        )
        sales_exports_goods_other_firms_2 = request.POST.get(
            "sales_exports_goods_other_firms_2"
        )
        total_cost_1 = request.POST.get("total_cost_1")
        total_cost_2 = request.POST.get("total_cost_2")
        total_cost_inventories_begginning_1 = request.POST.get(
            "total_cost_inventories_begginning_1"
        )
        total_cost_inventories_begginning_2 = request.POST.get(
            "total_cost_inventories_begginning_2"
        )
        total_cost_purchases_1 = request.POST.get("total_cost_purchases_1")
        total_cost_purchases_2 = request.POST.get("total_cost_purchases_2")
        total_cost_total_raw_1 = request.POST.get("total_cost_total_raw_1")
        total_cost_total_raw_2 = request.POST.get("total_cost_total_raw_2")
        total_cost_imported_1 = request.POST.get("total_cost_imported_1")
        total_cost_imported_2 = request.POST.get("total_cost_imported_2")
        total_cost_others_1 = request.POST.get("total_cost_others_1")
        total_cost_others_2 = request.POST.get("total_cost_others_2")
        total_cost_direct_wages_1 = request.POST.get("total_cost_direct_wages_1")
        total_cost_direct_wages_2 = request.POST.get("total_cost_direct_wages_2")
        total_cost_depreciation_1 = request.POST.get("total_cost_depreciation_1")
        total_cost_depreciation_2 = request.POST.get("total_cost_depreciation_2")
        total_cost_rent_land_1 = request.POST.get("total_cost_rent_land_1")
        total_cost_rent_land_2 = request.POST.get("total_cost_rent_land_2")
        total_cost_other_direct_1 = request.POST.get("total_cost_other_direct_1")
        total_cost_other_direct_2 = request.POST.get("total_cost_other_direct_2")
        total_cost_indirect_cost_1 = request.POST.get("total_cost_indirect_cost_1")
        total_cost_indirect_cost_2 = request.POST.get("total_cost_indirect_cost_2")
        total_cost_inventories_end_1 = request.POST.get("total_cost_inventories_end_1")
        total_cost_inventories_end_2 = request.POST.get("total_cost_inventories_end_2")
        gross_profit_1 = request.POST.get("gross_profit_1")
        gross_profit_2 = request.POST.get("gross_profit_2")
        other_operating_1 = request.POST.get("other_operating_1")
        other_operating_2 = request.POST.get("other_operating_2")
        other_operating_interest_1 = request.POST.get("other_operating_interest_1")
        other_operating_interest_2 = request.POST.get("other_operating_interest_2")
        other_operating_rent_land_1 = request.POST.get("other_operating_rent_land_1")
        other_operating_rent_land_2 = request.POST.get("other_operating_rent_land_2")
        other_operating_capital_gain_1 = request.POST.get(
            "other_operating_capital_gain_1"
        )
        other_operating_capital_gain_2 = request.POST.get(
            "other_operating_capital_gain_2"
        )
        other_operating_other_1 = request.POST.get("other_operating_other_1")
        other_operating_other_2 = request.POST.get("other_operating_other_2")
        total_gross_1 = request.POST.get("total_gross_1")
        total_gross_2 = request.POST.get("total_gross_2")
        expenses_not_included_1 = request.POST.get("expenses_not_included_1")
        expenses_not_included_2 = request.POST.get("expenses_not_included_2")
        expenses_not_included_salaries_1 = request.POST.get(
            "expenses_not_included_salaries_1"
        )
        expenses_not_included_salaries_2 = request.POST.get(
            "expenses_not_included_salaries_2"
        )
        expenses_not_included_interest_1 = request.POST.get(
            "expenses_not_included_interest_1"
        )
        expenses_not_included_interest_2 = request.POST.get(
            "expenses_not_included_interest_2"
        )
        expenses_not_included_depreciation_1 = request.POST.get(
            "expenses_not_included_depreciation_1"
        )
        expenses_not_included_depreciation_2 = request.POST.get(
            "expenses_not_included_depreciation_2"
        )
        expenses_not_included_donations_1 = request.POST.get(
            "expenses_not_included_donations_1"
        )
        expenses_not_included_donations_2 = request.POST.get(
            "expenses_not_included_donations_2"
        )
        expenses_not_included_rent_land_1 = request.POST.get(
            "expenses_not_included_rent_land_1"
        )
        expenses_not_included_rent_land_2 = request.POST.get(
            "expenses_not_included_rent_land_2"
        )
        expenses_not_included_other_operating_1 = request.POST.get(
            "expenses_not_included_other_operating_1"
        )
        expenses_not_included_other_operating_2 = request.POST.get(
            "expenses_not_included_other_operating_2"
        )
        expenses_not_included_sales_tax_1 = request.POST.get(
            "expenses_not_included_sales_tax_1"
        )
        expenses_not_included_sales_tax_2 = request.POST.get(
            "expenses_not_included_sales_tax_2"
        )
        expenses_not_included_machinery_1 = request.POST.get(
            "expenses_not_included_machinery_1"
        )
        expenses_not_included_machinery_2 = request.POST.get(
            "expenses_not_included_machinery_2"
        )
        expenses_not_included_on_other_1 = request.POST.get(
            "expenses_not_included_on_other_1"
        )
        expenses_not_included_on_other_2 = request.POST.get(
            "expenses_not_included_on_other_2"
        )
        expenses_not_included_licenses_1 = request.POST.get(
            "expenses_not_included_licenses_1"
        )
        expenses_not_included_licenses_2 = request.POST.get(
            "expenses_not_included_licenses_2"
        )
        net_profit_loss_1 = request.POST.get("net_profit_loss_1")
        net_profit_loss_2 = request.POST.get("net_profit_loss_2")
        net_profit_loss_income_tax_1 = request.POST.get("net_profit_loss_income_tax_1")
        net_profit_loss_income_tax_2 = request.POST.get("net_profit_loss_income_tax_2")
        profit_after_tax_1 = request.POST.get("profit_after_tax_1")
        profit_after_tax_2 = request.POST.get("profit_after_tax_2")
        sales_and_use_withheld_1 = request.POST.get("sales_and_use_withheld_1")
        sales_and_use_withheld_2 = request.POST.get("sales_and_use_withheld_2")
        branches = request.POST.get("branches")
        branches_if_yes = request.POST.get("branches_if_yes")
        name = request.POST.get("name")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-510.csv"
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
                        "accounting_period",
                        "main_product_1",
                        "main_product_2",
                        "raw_material_used",
                        "closing_date",
                        "start_year",
                        "end_year",
                        "sales_from_persons_1",
                        "sales_from_persons_2",
                        "sales_industries_businesses_1",
                        "sales_industries_businesses_2",
                        "sales_goods_1",
                        "sales_goods_2",
                        "sales_exports_goods_1",
                        "sales_exports_goods_2",
                        "sales_goods_from_others_firms_1",
                        "sales_goods_from_others_firms_2",
                        "sales_exports_goods_other_firms_1",
                        "sales_exports_goods_other_firms_2",
                        "total_cost_1",
                        "total_cost_2",
                        "total_cost_inventories_begginning_1",
                        "total_cost_inventories_begginning_2",
                        "total_cost_purchases_1",
                        "total_cost_purchases_2",
                        "total_cost_total_raw_1",
                        "total_cost_total_raw_2",
                        "total_cost_imported_1",
                        "total_cost_imported_2",
                        "total_cost_others_1",
                        "total_cost_others_2",
                        "total_cost_direct_wages_1",
                        "total_cost_direct_wages_2",
                        "total_cost_depreciation_1",
                        "total_cost_depreciation_2",
                        "total_cost_rent_land_1",
                        "total_cost_rent_land_2",
                        "total_cost_other_direct_1",
                        "total_cost_other_direct_2",
                        "total_cost_indirect_cost_1",
                        "total_cost_indirect_cost_2",
                        "total_cost_inventories_end_1",
                        "total_cost_inventories_end_2",
                        "gross_profit_1",
                        "gross_profit_2",
                        "other_operating_1",
                        "other_operating_2",
                        "other_operating_interest_1",
                        "other_operating_interest_2",
                        "other_operating_rent_land_1",
                        "other_operating_rent_land_2",
                        "other_operating_capital_gain_1",
                        "other_operating_capital_gain_2",
                        "other_operating_other_1",
                        "other_operating_other_2",
                        "total_gross_1",
                        "total_gross_2",
                        "expenses_not_included_1",
                        "expenses_not_included_2",
                        "expenses_not_included_salaries_1",
                        "expenses_not_included_salaries_2",
                        "expenses_not_included_interest_1",
                        "expenses_not_included_interest_2",
                        "expenses_not_included_depreciation_1",
                        "expenses_not_included_depreciation_2",
                        "expenses_not_included_donations_1",
                        "expenses_not_included_donations_2",
                        "expenses_not_included_rent_land_1",
                        "expenses_not_included_rent_land_2",
                        "expenses_not_included_other_operating_1",
                        "expenses_not_included_other_operating_2",
                        "expenses_not_included_sales_tax_1",
                        "expenses_not_included_sales_tax_2",
                        "expenses_not_included_machinery_1",
                        "expenses_not_included_machinery_2",
                        "expenses_not_included_on_other_1",
                        "expenses_not_included_on_other_2",
                        "expenses_not_included_licenses_1",
                        "expenses_not_included_licenses_2",
                        "net_profit_loss_1",
                        "net_profit_loss_2",
                        "net_profit_loss_income_tax_1",
                        "net_profit_loss_income_tax_2",
                        "profit_after_tax_1",
                        "profit_after_tax_2",
                        "sales_and_use_withheld_1",
                        "sales_and_use_withheld_2",
                        "branches",
                        "branches_if_yes",
                        "name",
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
                    accounting_period,
                    main_product_1,
                    main_product_2,
                    raw_material_used,
                    closing_date,
                    start_year,
                    end_year,
                    sales_from_persons_1,
                    sales_from_persons_2,
                    sales_industries_businesses_1,
                    sales_industries_businesses_2,
                    sales_goods_1,
                    sales_goods_2,
                    sales_exports_goods_1,
                    sales_exports_goods_2,
                    sales_goods_from_others_firms_1,
                    sales_goods_from_others_firms_2,
                    sales_exports_goods_other_firms_1,
                    sales_exports_goods_other_firms_2,
                    total_cost_1,
                    total_cost_2,
                    total_cost_inventories_begginning_1,
                    total_cost_inventories_begginning_2,
                    total_cost_purchases_1,
                    total_cost_purchases_2,
                    total_cost_total_raw_1,
                    total_cost_total_raw_2,
                    total_cost_imported_1,
                    total_cost_imported_2,
                    total_cost_others_1,
                    total_cost_others_2,
                    total_cost_direct_wages_1,
                    total_cost_direct_wages_2,
                    total_cost_depreciation_1,
                    total_cost_depreciation_2,
                    total_cost_rent_land_1,
                    total_cost_rent_land_2,
                    total_cost_other_direct_1,
                    total_cost_other_direct_2,
                    total_cost_indirect_cost_1,
                    total_cost_indirect_cost_2,
                    total_cost_inventories_end_1,
                    total_cost_inventories_end_2,
                    gross_profit_1,
                    gross_profit_2,
                    other_operating_1,
                    other_operating_2,
                    other_operating_interest_1,
                    other_operating_interest_2,
                    other_operating_rent_land_1,
                    other_operating_rent_land_2,
                    other_operating_capital_gain_1,
                    other_operating_capital_gain_2,
                    other_operating_other_1,
                    other_operating_other_2,
                    total_gross_1,
                    total_gross_2,
                    expenses_not_included_1,
                    expenses_not_included_2,
                    expenses_not_included_salaries_1,
                    expenses_not_included_salaries_2,
                    expenses_not_included_interest_1,
                    expenses_not_included_interest_2,
                    expenses_not_included_depreciation_1,
                    expenses_not_included_depreciation_2,
                    expenses_not_included_donations_1,
                    expenses_not_included_donations_2,
                    expenses_not_included_rent_land_1,
                    expenses_not_included_rent_land_2,
                    expenses_not_included_other_operating_1,
                    expenses_not_included_other_operating_2,
                    expenses_not_included_sales_tax_1,
                    expenses_not_included_sales_tax_2,
                    expenses_not_included_machinery_1,
                    expenses_not_included_machinery_2,
                    expenses_not_included_on_other_1,
                    expenses_not_included_on_other_2,
                    expenses_not_included_licenses_1,
                    expenses_not_included_licenses_2,
                    net_profit_loss_1,
                    net_profit_loss_2,
                    net_profit_loss_income_tax_1,
                    net_profit_loss_income_tax_2,
                    profit_after_tax_1,
                    profit_after_tax_2,
                    sales_and_use_withheld_1,
                    sales_and_use_withheld_2,
                    branches,
                    branches_if_yes,
                    name,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-510.csv",
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
                "accounting_period": str,
                "main_product_1": str,
                "main_product_2": str,
                "raw_material_used": str,
                "closing_date": str,
                "start_year": int,
                "end_year": int,
                "sales_from_persons_1": float,
                "sales_from_persons_2": float,
                "sales_industries_businesses_1": float,
                "sales_industries_businesses_2": float,
                "sales_goods_1": float,
                "sales_goods_2": float,
                "sales_exports_goods_1": float,
                "sales_exports_goods_2": float,
                "sales_goods_from_others_firms_1": float,
                "sales_goods_from_others_firms_2": float,
                "sales_exports_goods_other_firms_1": float,
                "sales_exports_goods_other_firms_2": float,
                "total_cost_1": float,
                "total_cost_2": float,
                "total_cost_inventories_begginning_1": float,
                "total_cost_inventories_begginning_2": float,
                "total_cost_purchases_1": float,
                "total_cost_purchases_2": float,
                "total_cost_total_raw_1": float,
                "total_cost_total_raw_2": float,
                "total_cost_imported_1": float,
                "total_cost_imported_2": float,
                "total_cost_others_1": float,
                "total_cost_others_2": float,
                "total_cost_direct_wages_1": float,
                "total_cost_direct_wages_2": float,
                "total_cost_depreciation_1": float,
                "total_cost_depreciation_2": float,
                "total_cost_rent_land_1": float,
                "total_cost_rent_land_2": float,
                "total_cost_other_direct_1": float,
                "total_cost_other_direct_2": float,
                "total_cost_indirect_cost_1": float,
                "total_cost_indirect_cost_2": float,
                "total_cost_inventories_end_1": float,
                "total_cost_inventories_end_2": float,
                "gross_profit_1": float,
                "gross_profit_2": float,
                "other_operating_1": float,
                "other_operating_2": float,
                "other_operating_interest_1": float,
                "other_operating_interest_2": float,
                "other_operating_rent_land_1": float,
                "other_operating_rent_land_2": float,
                "other_operating_capital_gain_1": float,
                "other_operating_capital_gain_2": float,
                "other_operating_other_1": float,
                "other_operating_other_2": float,
                "total_gross_1": float,
                "total_gross_2": float,
                "expenses_not_included_1": float,
                "expenses_not_included_2": float,
                "expenses_not_included_salaries_1": float,
                "expenses_not_included_salaries_2": float,
                "expenses_not_included_interest_1": float,
                "expenses_not_included_interest_2": float,
                "expenses_not_included_depreciation_1": float,
                "expenses_not_included_depreciation_2": float,
                "expenses_not_included_donations_1": float,
                "expenses_not_included_donations_2": float,
                "expenses_not_included_rent_land_1": float,
                "expenses_not_included_rent_land_2": float,
                "expenses_not_included_other_operating_1": float,
                "expenses_not_included_other_operating_2": float,
                "expenses_not_included_sales_tax_1": float,
                "expenses_not_included_sales_tax_2": float,
                "expenses_not_included_machinery_1": float,
                "expenses_not_included_machinery_2": float,
                "expenses_not_included_on_other_1": float,
                "expenses_not_included_on_other_2": float,
                "expenses_not_included_licenses_1": float,
                "expenses_not_included_licenses_2": float,
                "net_profit_loss_1": float,
                "net_profit_loss_2": float,
                "net_profit_loss_income_tax_1": float,
                "net_profit_loss_income_tax_2": float,
                "profit_after_tax_1": float,
                "profit_after_tax_2": float,
                "sales_and_use_withheld_1": float,
                "sales_and_use_withheld_2": float,
                "branches": str,
                "branches_if_yes": str,
                "name": str,
                "rank": str,
            },
            table_name="IP_510",
            table_id="36",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-510.html")