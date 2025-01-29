from django.shortcuts import render
from src.dao.data_db_dao import DAO
import polars as pl

def JP_383(request):
    if request.method == "POST":
        # Define field names
        field_names = [
            "other_section", "año", "julio_1", "julio_2", "julio_3", "julio_4", "julio_5", "julio_6",
            "agosto_1", "agosto_2", "agosto_3", "agosto_4", "agosto_5", "agosto_6",
            "septiembre_1", "septiembre_2", "septiembre_3", "septiembre_4", "septiembre_5", "septiembre_6",
            "subtotal_1", "subtotal_2", "subtotal_3", "subtotal_4", "subtotal_5", "subtotal_6",
            "octubre_1", "octubre_2", "octubre_3", "octubre_4", "octubre_5", "octubre_6",
            "noviembre_1", "noviembre_2", "noviembre_3", "noviembre_4", "noviembre_5", "noviembre_6",
            "diciembre_1", "diciembre_2", "diciembre_3", "diciembre_4", "diciembre_5", "diciembre_6",
            "subtotal_11", "subtotal_12", "subtotal_13", "subtotal_14", "subtotal_15", "subtotal_16",
            "año_1", "enero_1", "enero_2", "enero_3", "enero_4", "enero_5", "enero_6",
            "febrero_1", "febrero_2", "febrero_3", "febrero_4", "febrero_5", "febrero_6",
            "marzo_1", "marzo_2", "marzo_3", "marzo_4", "marzo_5", "marzo_6",
            "subtotal_21", "subtotal_22", "subtotal_23", "subtotal_24", "subtotal_25", "subtotal_26",
            "abril_1", "abril_2", "abril_3", "abril_4", "abril_5", "abril_6",
            "mayo_1", "mayo_2", "mayo_3", "mayo_4", "mayo_5", "mayo_6",
            "junio_1", "junio_2", "junio_3", "junio_4", "junio_5", "junio_6",
            "subtotal_31", "subtotal_32", "subtotal_33", "subtotal_34", "subtotal_35", "subtotal_36",
            "total_1", "total_2", "total_3", "total_4", "total_5", "total_6",
            "signature", "name", "title", "phone"
        ]

        # Create data dynamically
        data = []
        for field in field_names:
            value = request.POST.get(field)
            # Attempt to convert to float, fallback to str
            if value is not None and value.strip():
                try:
                    value = float(value)
                except ValueError:
                    value = str(value)
            else:
                value = None  # Handle None values explicitly

            # Determine the correct dtype based on the field name
            dtype = pl.Float64 if "subtotal" in field or "total" in field or "enero" in field else pl.String
            data.append(pl.Series(field, [value], dtype=dtype))

        # Create DataFrame
        df = pl.DataFrame(data)

        # Insert into database
        DAO().insert_forms(df, "JP_383", 45)

        return render(request, "forms/successful.html")

    return render(request, "forms/yearly/balanza_de_pagos/JP-383.html")
