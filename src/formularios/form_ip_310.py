from django.shortcuts import render
from src.dao.data_db_dao import DAO
import csv
import os


def IP_310(request):
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
        end_month = request.POST.get("end_month")
        main_product_1 = request.POST.get("main_product_1")
        other_product_1 = request.POST.get("other_product_1")
        raw_material_used = request.POST.get("raw_material_used")
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        total_sales_1 = request.POST.get("total_sales_1")
        total_sales_2 = request.POST.get("total_sales_2")
        from_persons_1 = request.POST.get("from_persons_1")
        from_persons_2 = request.POST.get("from_persons_2")
        industries_businesses_1 = request.POST.get("industries_businesses_1")
        industries_businesses_2 = request.POST.get("industries_businesses_2")
        goods_manufactured_1 = request.POST.get("goods_manufactured_1")
        goods_manufactured_2 = request.POST.get("goods_manufactured_2")
        exports_val_1 = request.POST.get("exports_val_1")
        exports_val_2 = request.POST.get("exports_val_2")
        goods_manufactured_1_1 = request.POST.get("goods_manufactured_1_1")
        goods_manufactured_2_2 = request.POST.get("goods_manufactured_2_2")
        exports_val_1_1 = request.POST.get("exports_val_1_1")
        exports_val_2_2 = request.POST.get("exports_val_2_2")
        manufacturing_cost_1 = request.POST.get("manufacturing_cost_1")
        manufacturing_cost_2 = request.POST.get("manufacturing_cost_2")
        inventories_begginning_1 = request.POST.get("inventories_begginning_1")
        inventories_begginning_2 = request.POST.get("inventories_begginning_2")
        purchases_1 = request.POST.get("purchases_1")
        purchases_2 = request.POST.get("purchases_2")
        total_raw_1 = request.POST.get("total_raw_1")
        total_raw_2 = request.POST.get("total_raw_2")
        imported_1 = request.POST.get("imported_1")
        imported_2 = request.POST.get("imported_2")
        others_1 = request.POST.get("others_1")
        others_2 = request.POST.get("others_2")
        direct_wages_1 = request.POST.get("direct_wages_1")
        direct_wages_2 = request.POST.get("direct_wages_2")
        depreciation_1 = request.POST.get("depreciation_1")
        depreciation_2 = request.POST.get("depreciation_2")
        rent_land_1 = request.POST.get("rent_land_1")
        rent_land_2 = request.POST.get("rent_land_2")
        other_direct_1 = request.POST.get("other_direct_1")
        other_direct_2 = request.POST.get("other_direct_2")
        indirect_cost_1 = request.POST.get("indirect_cost_1")
        indirect_cost_2 = request.POST.get("indirect_cost_2")
        inventories_end_1 = request.POST.get("inventories_end_1")
        inventories_end_2 = request.POST.get("inventories_end_2")
        gross_profit_1 = request.POST.get("gross_profit_1")
        gross_profit_2 = request.POST.get("gross_profit_2")
        other_operating_1 = request.POST.get("other_operating_1")
        other_operating_2 = request.POST.get("other_operating_2")
        interest_1 = request.POST.get("interest_1")
        interest_2 = request.POST.get("interest_2")
        rent_land_3 = request.POST.get("rent_land_3")
        rent_land_4 = request.POST.get("rent_land_4")
        capital_gain_1 = request.POST.get("capital_gain_1")
        capital_gain_2 = request.POST.get("capital_gain_2")
        other_1 = request.POST.get("other_1")
        other_2 = request.POST.get("other_2")
        total_gross_1 = request.POST.get("total_gross_1")
        total_gross_2 = request.POST.get("total_gross_2")
        expenses_not_1 = request.POST.get("expenses_not_1")
        expenses_not_2 = request.POST.get("expenses_not_2")
        salaries_1 = request.POST.get("salaries_1")
        salaries_2 = request.POST.get("salaries_2")
        interest_3 = request.POST.get("interest_3")
        interest_4 = request.POST.get("interest_4")
        depreciation_3 = request.POST.get("depreciation_3")
        depreciation_4 = request.POST.get("depreciation_4")
        donations_1 = request.POST.get("donations_1")
        donations_2 = request.POST.get("donations_2")
        rent_land_5 = request.POST.get("rent_land_5")
        rent_land_6 = request.POST.get("rent_land_6")
        other_operating_3 = request.POST.get("other_operating_3")
        other_operating_4 = request.POST.get("other_operating_4")
        sales_tax_1 = request.POST.get("sales_tax_1")
        sales_tax_2 = request.POST.get("sales_tax_2")
        machinery_1 = request.POST.get("machinery_1")
        machinery_2 = request.POST.get("machinery_2")
        on_other_1 = request.POST.get("on_other_1")
        on_other_2 = request.POST.get("on_other_2")
        licenses_1 = request.POST.get("licenses_1")
        licenses_2 = request.POST.get("licenses_2")
        net_loss_1 = request.POST.get("net_loss_1")
        net_loss_2 = request.POST.get("net_loss_2")
        income_tax_1 = request.POST.get("income_tax_1")
        income_tax_2 = request.POST.get("income_tax_2")
        profit_after_tax_1 = request.POST.get("profit_after_tax_1")
        profit_after_tax_2 = request.POST.get("profit_after_tax_2")
        sales_and_use_withheld_1 = request.POST.get("sales_and_use_withheld_1")
        sales_and_use_withheld_2 = request.POST.get("sales_and_use_withheld_2")
        branches = request.POST.get("branches")
        branches_if_yes = request.POST.get("branches_if_yes")
        signature = request.POST.get("signature")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-310.csv"
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
                        "end_month",
                        "main_product_1",
                        "other_product_1",
                        "raw_material_used",
                        "closing_date",
                        "start_year",
                        "end_year",
                        "total_sales_1",
                        "total_sales_2",
                        "from_persons_1",
                        "from_persons_2",
                        "industries_businesses_1",
                        "industries_businesses_2",
                        "goods_manufactured_1",
                        "goods_manufactured_2",
                        "exports_val_1",
                        "exports_val_2",
                        "goods_manufactured_1_1",
                        "goods_manufactured_2_2",
                        "exports_val_1_1",
                        "exports_val_2_2",
                        "manufacturing_cost_1",
                        "manufacturing_cost_2",
                        "inventories_begginning_1",
                        "inventories_begginning_2",
                        "purchases_1",
                        "purchases_2",
                        "total_raw_1",
                        "total_raw_2",
                        "imported_1",
                        "imported_2",
                        "others_1",
                        "others_2",
                        "direct_wages_1",
                        "direct_wages_2",
                        "depreciation_1",
                        "depreciation_2",
                        "rent_land_1",
                        "rent_land_2",
                        "other_direct_1",
                        "other_direct_2",
                        "indirect_cost_1",
                        "indirect_cost_2",
                        "inventories_end_1",
                        "inventories_end_2",
                        "gross_profit_1",
                        "gross_profit_2",
                        "other_operating_1",
                        "other_operating_2",
                        "interest_1",
                        "interest_2",
                        "rent_land_3",
                        "rent_land_4",
                        "capital_gain_1",
                        "capital_gain_2",
                        "other_1",
                        "other_2",
                        "total_gross_1",
                        "total_gross_2",
                        "expenses_not_1",
                        "expenses_not_2",
                        "salaries_1",
                        "salaries_2",
                        "interest_3",
                        "interest_4",
                        "depreciation_3",
                        "depreciation_4",
                        "donations_1",
                        "donations_2",
                        "rent_land_5",
                        "rent_land_6",
                        "other_operating_3",
                        "other_operating_4",
                        "sales_tax_1",
                        "sales_tax_2",
                        "machinery_1",
                        "machinery_2",
                        "on_other_1",
                        "on_other_2",
                        "licenses_1",
                        "licenses_2",
                        "net_loss_1",
                        "net_loss_2",
                        "income_tax_1",
                        "income_tax_2",
                        "profit_after_tax_1",
                        "profit_after_tax_2",
                        "sales_and_use_withheld_1",
                        "sales_and_use_withheld_2",
                        "branches",
                        "branches_if_yes",
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
                    end_month,
                    main_product_1,
                    other_product_1,
                    raw_material_used,
                    closing_date,
                    start_year,
                    end_year,
                    total_sales_1,
                    total_sales_2,
                    from_persons_1,
                    from_persons_2,
                    industries_businesses_1,
                    industries_businesses_2,
                    goods_manufactured_1,
                    goods_manufactured_2,
                    exports_val_1,
                    exports_val_2,
                    goods_manufactured_1_1,
                    goods_manufactured_2_2,
                    exports_val_1_1,
                    exports_val_2_2,
                    manufacturing_cost_1,
                    manufacturing_cost_2,
                    inventories_begginning_1,
                    inventories_begginning_2,
                    purchases_1,
                    purchases_2,
                    total_raw_1,
                    total_raw_2,
                    imported_1,
                    imported_2,
                    others_1,
                    others_2,
                    direct_wages_1,
                    direct_wages_2,
                    depreciation_1,
                    depreciation_2,
                    rent_land_1,
                    rent_land_2,
                    other_direct_1,
                    other_direct_2,
                    indirect_cost_1,
                    indirect_cost_2,
                    inventories_end_1,
                    inventories_end_2,
                    gross_profit_1,
                    gross_profit_2,
                    other_operating_1,
                    other_operating_2,
                    interest_1,
                    interest_2,
                    rent_land_3,
                    rent_land_4,
                    capital_gain_1,
                    capital_gain_2,
                    other_1,
                    other_2,
                    total_gross_1,
                    total_gross_2,
                    expenses_not_1,
                    expenses_not_2,
                    salaries_1,
                    salaries_2,
                    interest_3,
                    interest_4,
                    depreciation_3,
                    depreciation_4,
                    donations_1,
                    donations_2,
                    rent_land_5,
                    rent_land_6,
                    other_operating_3,
                    other_operating_4,
                    sales_tax_1,
                    sales_tax_2,
                    machinery_1,
                    machinery_2,
                    on_other_1,
                    on_other_2,
                    licenses_1,
                    licenses_2,
                    net_loss_1,
                    net_loss_2,
                    income_tax_1,
                    income_tax_2,
                    profit_after_tax_1,
                    profit_after_tax_2,
                    sales_and_use_withheld_1,
                    sales_and_use_withheld_2,
                    branches,
                    branches_if_yes,
                    signature,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-310.csv",
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
                "end_month": str,
                "main_product_1": str,
                "other_product_1": str,
                "raw_material_used": str,
                "closing_date": str,
                "start_year": int,
                "end_year": int,
                "total_sales_1": float,
                "total_sales_2": float,
                "from_persons_1": float,
                "from_persons_2": float,
                "industries_businesses_1": float,
                "industries_businesses_2": float,
                "goods_manufactured_1": float,
                "goods_manufactured_2": float,
                "exports_val_1": float,
                "exports_val_2": float,
                "goods_manufactured_1_1": float,
                "goods_manufactured_2_2": float,
                "exports_val_1_1": float,
                "exports_val_2_2": float,
                "manufacturing_cost_1": float,
                "manufacturing_cost_2": float,
                "inventories_begginning_1": float,
                "inventories_begginning_2": float,
                "purchases_1": float,
                "purchases_2": float,
                "total_raw_1": float,
                "total_raw_2": float,
                "imported_1": float,
                "imported_2": float,
                "others_1": float,
                "others_2": float,
                "direct_wages_1": float,
                "direct_wages_2": float,
                "depreciation_1": float,
                "depreciation_2": float,
                "rent_land_1": float,
                "rent_land_2": float,
                "other_direct_1": float,
                "other_direct_2": float,
                "indirect_cost_1": float,
                "indirect_cost_2": float,
                "inventories_end_1": float,
                "inventories_end_2": float,
                "gross_profit_1": float,
                "gross_profit_2": float,
                "other_operating_1": float,
                "other_operating_2": float,
                "interest_1": float,
                "interest_2": float,
                "rent_land_3": float,
                "rent_land_4": float,
                "capital_gain_1": float,
                "capital_gain_2": float,
                "other_1": float,
                "other_2": float,
                "total_gross_1": float,
                "total_gross_2": float,
                "expenses_not_1": float,
                "expenses_not_2": float,
                "salaries_1": float,
                "salaries_2": float,
                "interest_3": float,
                "interest_4": float,
                "depreciation_3": float,
                "depreciation_4": float,
                "donations_1": float,
                "donations_2": float,
                "rent_land_5": float,
                "rent_land_6": float,
                "other_operating_3": float,
                "other_operating_4": float,
                "sales_tax_1": float,
                "sales_tax_2": float,
                "machinery_1": float,
                "machinery_2": float,
                "on_other_1": float,
                "on_other_2": float,
                "licenses_1": float,
                "licenses_2": float,
                "net_loss_1": float,
                "net_loss_2": float,
                "income_tax_1": float,
                "income_tax_2": float,
                "profit_after_tax_1": float,
                "profit_after_tax_2": float,
                "sales_and_use_withheld_1": float,
                "sales_and_use_withheld_2": float,
                "branches": str,
                "branches_if_yes": str,
                "signature": str,
                "rank": str,
            },
            table_name="IP_310",
            table_id="30",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-310.html")
