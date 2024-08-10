from django.shortcuts import render
from src.dao.data_db_dao import DAO
import csv
import os


def JP_363(request):
    if request.method == "POST":
        # Retrieve form data
        bonds_year_left = request.POST.get("bonds_year_left")
        bonds_year_right = request.POST.get("bonds_year_right")
        notes_year_left = request.POST.get("notes_year_left")
        notes_year_right = request.POST.get("notes_year_right")
        CG_bonds_left = request.POST.get("CG_bonds_left")
        CG_bonds_right = request.POST.get("CG_bonds_right")
        CG_notes_left = request.POST.get("CG_notes_left")
        CG_notes_right = request.POST.get("CG_notes_right")
        CG_name_service = request.POST.get("CG_name_service")
        town_bonds_left = request.POST.get("town_bonds_left")
        town_bonds_right = request.POST.get("town_bonds_right")
        town_notes_left = request.POST.get("town_notes_left")
        town_notes_right = request.POST.get("town_notes_right")
        town_name_service = request.POST.get("town_name_service")
        PC_bonds_left = request.POST.get("PC_bonds_left")
        PC_bonds_right = request.POST.get("PC_bonds_right")
        PC_notes_left = request.POST.get("PC_notes_left")
        PC_notes_right = request.POST.get("PC_notes_right")
        PC_name_service = request.POST.get("PC_name_service")
        EPA_bonds_left = request.POST.get("EPA_bonds_left")
        EPA_bonds_right = request.POST.get("EPA_bonds_right")
        EPA_notes_left = request.POST.get("EPA_notes_left")
        EPA_notes_right = request.POST.get("EPA_notes_right")
        EPA_name_service = request.POST.get("EPA_name_service")
        HA_bonds_left = request.POST.get("HA_bonds_left")
        HA_bonds_right = request.POST.get("HA_bonds_right")
        HA_notes_left = request.POST.get("HA_notes_left")
        HA_notes_right = request.POST.get("HA_notes_right")
        HA_name_service = request.POST.get("HA_name_service")
        ASA_bonds_left = request.POST.get("ASA_bonds_left")
        ASA_bonds_right = request.POST.get("ASA_bonds_right")
        ASA_notes_left = request.POST.get("ASA_notes_left")
        ASA_notes_right = request.POST.get("ASA_notes_right")
        ASA_name_service = request.POST.get("ASA_name_service")
        PBA_bonds_left = request.POST.get("PBA_bonds_left")
        PBA_bonds_right = request.POST.get("PBA_bonds_right")
        PBA_notes_left = request.POST.get("PBA_notes_left")
        PBA_notes_right = request.POST.get("PBA_notes_right")
        PBA_name_service = request.POST.get("PBA_name_service")
        PA_bonds_left = request.POST.get("PA_bonds_left")
        PA_bonds_right = request.POST.get("PA_bonds_right")
        PA_notes_left = request.POST.get("PA_notes_left")
        PA_notes_right = request.POST.get("PA_notes_right")
        PA_name_service = request.POST.get("PA_name_service")
        TA_bonds_left = request.POST.get("TA_bonds_left")
        TA_bonds_right = request.POST.get("TA_bonds_right")
        TA_notes_left = request.POST.get("TA_notes_left")
        TA_notes_right = request.POST.get("TA_notes_right")
        TA_name_service = request.POST.get("TA_name_service")
        IDC_bonds_left = request.POST.get("IDC_bonds_left")
        IDC_bonds_right = request.POST.get("IDC_bonds_right")
        IDC_notes_left = request.POST.get("IDC_notes_left")
        IDC_notes_right = request.POST.get("IDC_notes_right")
        IDC_name_service = request.POST.get("IDC_name_service")
        GDB_bonds_left = request.POST.get("GDB_bonds_left")
        GDB_bonds_right = request.POST.get("GDB_bonds_right")
        GDB_notes_left = request.POST.get("GDB_notes_left")
        GDB_notes_right = request.POST.get("GDB_notes_right")
        GDB_name_service = request.POST.get("GDB_name_service")
        HFC_bonds_left = request.POST.get("HFC_bonds_left")
        HFC_bonds_right = request.POST.get("HFC_bonds_right")
        HFC_notes_left = request.POST.get("HFC_notes_left")
        HFC_notes_right = request.POST.get("HFC_notes_right")
        HFC_name_service = request.POST.get("HFC_name_service")
        other = request.POST.get("other")
        other_bonds_left = request.POST.get("other_bonds_left")
        other_bonds_right = request.POST.get("other_bonds_right")
        other_notes_left = request.POST.get("other_notes_left")
        other_notes_right = request.POST.get("other_notes_right")
        other_name_service = request.POST.get("other_name_service")
        other_PC_1 = request.POST.get("other_PC_1")
        other_PC_1_bonds_left = request.POST.get("other_PC_1_bonds_left")
        other_PC_1_bonds_right = request.POST.get("other_PC_1_bonds_right")
        other_PC_1_notes_left = request.POST.get("other_PC_1_notes_left")
        other_PC_1_notes_right = request.POST.get("other_PC_1_notes_right")
        other_PC_1_name_service = request.POST.get("other_PC_1_name_service")
        other_PC_2 = request.POST.get("other_PC_2")
        other_PC_2_bonds_left = request.POST.get("other_PC_2_bonds_left")
        other_PC_2_bonds_right = request.POST.get("other_PC_2_bonds_right")
        other_PC_2_notes_left = request.POST.get("other_PC_2_notes_left")
        other_PC_2_notes_right = request.POST.get("other_PC_2_notes_right")
        other_PC_2_name_service = request.POST.get("other_PC_2_name_service")
        GNMA_bonds_left = request.POST.get("GNMA_bonds_left")
        GNMA_bonds_right = request.POST.get("GNMA_bonds_right")
        GNMA_notes_left = request.POST.get("GNMA_notes_left")
        GNMA_notes_right = request.POST.get("GNMA_notes_right")
        GNMA_name_service = request.POST.get("GNMA_name_service")
        other5 = request.POST.get("other5")
        other5_bonds_left = request.POST.get("other5_bonds_left")
        other5_bonds_right = request.POST.get("other5_bonds_right")
        other5_notes_left = request.POST.get("other5_notes_left")
        other5_notes_right = request.POST.get("other5_notes_right")
        other5_name_service = request.POST.get("other5_name_service")
        signature = request.POST.get("signature")
        position = request.POST.get("position")
        date = request.POST.get("date")
        phone = request.POST.get("phone")

        csv_file_path = "data/cuestionarios/balanza_de_pagos/JP-363.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "bonds_year_left",
                        "bonds_year_right",
                        "notes_year_left",
                        "notes_year_right",
                        "CG_bonds_left",
                        "CG_bonds_right",
                        "CG_notes_left",
                        "CG_notes_right",
                        "CG_name_service",
                        "town_bonds_left",
                        "town_bonds_right",
                        "town_notes_left",
                        "town_notes_right",
                        "town_name_service",
                        "PC_bonds_left",
                        "PC_bonds_right",
                        "PC_notes_left",
                        "PC_notes_right",
                        "PC_name_service",
                        "EPA_bonds_left",
                        "EPA_bonds_right",
                        "EPA_notes_left",
                        "EPA_notes_right",
                        "EPA_name_service",
                        "HA_bonds_left",
                        "HA_bonds_right",
                        "HA_notes_left",
                        "HA_notes_right",
                        "HA_name_service",
                        "ASA_bonds_left",
                        "ASA_bonds_right",
                        "ASA_notes_left",
                        "ASA_notes_right",
                        "ASA_name_service",
                        "PBA_bonds_left",
                        "PBA_bonds_right",
                        "PBA_notes_left",
                        "PBA_notes_right",
                        "PBA_name_service",
                        "PA_bonds_left",
                        "PA_bonds_right",
                        "PA_notes_left",
                        "PA_notes_right",
                        "PA_name_service",
                        "TA_bonds_left",
                        "TA_bonds_right",
                        "TA_notes_left",
                        "TA_notes_right",
                        "TA_name_service",
                        "IDC_bonds_left",
                        "IDC_bonds_right",
                        "IDC_notes_left",
                        "IDC_notes_right",
                        "IDC_name_service",
                        "GDB_bonds_left",
                        "GDB_bonds_right",
                        "GDB_notes_left",
                        "GDB_notes_right",
                        "GDB_name_service",
                        "HFC_bonds_left",
                        "HFC_bonds_right",
                        "HFC_notes_left",
                        "HFC_notes_right",
                        "HFC_name_service",
                        "other",
                        "other_bonds_left",
                        "other_bonds_right",
                        "other_notes_left",
                        "other_notes_right",
                        "other_name_service",
                        "other_PC_1",
                        "other_PC_1_bonds_left",
                        "other_PC_1_bonds_right",
                        "other_PC_1_notes_left",
                        "other_PC_1_notes_right",
                        "other_PC_1_name_service",
                        "other_PC_2",
                        "other_PC_2_bonds_left",
                        "other_PC_2_bonds_right",
                        "other_PC_2_notes_left",
                        "other_PC_2_notes_right",
                        "other_PC_2_name_service",
                        "GNMA_bonds_left",
                        "GNMA_bonds_right",
                        "GNMA_notes_left",
                        "GNMA_notes_right",
                        "GNMA_name_service",
                        "other5",
                        "other5_bonds_left",
                        "other5_bonds_right",
                        "other5_notes_left",
                        "other5_notes_right",
                        "other5_name_service",
                        "signature",
                        "position",
                        "date",
                        "phone",
                    ]
                )

            writer.writerow(
                [
                    bonds_year_left,
                    bonds_year_right,
                    notes_year_left,
                    notes_year_right,
                    CG_bonds_left,
                    CG_bonds_right,
                    CG_notes_left,
                    CG_notes_right,
                    CG_name_service,
                    town_bonds_left,
                    town_bonds_right,
                    town_notes_left,
                    town_notes_right,
                    town_name_service,
                    PC_bonds_left,
                    PC_bonds_right,
                    PC_notes_left,
                    PC_notes_right,
                    PC_name_service,
                    EPA_bonds_left,
                    EPA_bonds_right,
                    EPA_notes_left,
                    EPA_notes_right,
                    EPA_name_service,
                    HA_bonds_left,
                    HA_bonds_right,
                    HA_notes_left,
                    HA_notes_right,
                    HA_name_service,
                    ASA_bonds_left,
                    ASA_bonds_right,
                    ASA_notes_left,
                    ASA_notes_right,
                    ASA_name_service,
                    PBA_bonds_left,
                    PBA_bonds_right,
                    PBA_notes_left,
                    PBA_notes_right,
                    PBA_name_service,
                    PA_bonds_left,
                    PA_bonds_right,
                    PA_notes_left,
                    PA_notes_right,
                    PA_name_service,
                    TA_bonds_left,
                    TA_bonds_right,
                    TA_notes_left,
                    TA_notes_right,
                    TA_name_service,
                    IDC_bonds_left,
                    IDC_bonds_right,
                    IDC_notes_left,
                    IDC_notes_right,
                    IDC_name_service,
                    GDB_bonds_left,
                    GDB_bonds_right,
                    GDB_notes_left,
                    GDB_notes_right,
                    GDB_name_service,
                    HFC_bonds_left,
                    HFC_bonds_right,
                    HFC_notes_left,
                    HFC_notes_right,
                    HFC_name_service,
                    other,
                    other_bonds_left,
                    other_bonds_right,
                    other_notes_left,
                    other_notes_right,
                    other_name_service,
                    other_PC_1,
                    other_PC_1_bonds_left,
                    other_PC_1_bonds_right,
                    other_PC_1_notes_left,
                    other_PC_1_notes_right,
                    other_PC_1_name_service,
                    other_PC_2,
                    other_PC_2_bonds_left,
                    other_PC_2_bonds_right,
                    other_PC_2_notes_left,
                    other_PC_2_notes_right,
                    other_PC_2_name_service,
                    GNMA_bonds_left,
                    GNMA_bonds_right,
                    GNMA_notes_left,
                    GNMA_notes_right,
                    GNMA_name_service,
                    other5,
                    other5_bonds_left,
                    other5_bonds_right,
                    other5_notes_left,
                    other5_notes_right,
                    other5_name_service,
                    signature,
                    position,
                    date,
                    phone,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/balanza_de_pagos/JP-363.csv",
            dtypes={
                "bonds_year_left": int,
                "bonds_year_right": int,
                "notes_year_left": int,
                "notes_year_right": int,
                "CG_bonds_left": float,
                "CG_bonds_right": float,
                "CG_notes_left": float,
                "CG_notes_right": float,
                "CG_name_service": str,
                "town_bonds_left": float,
                "town_bonds_right": float,
                "town_notes_left": float,
                "town_notes_right": float,
                "town_name_service": str,
                "PC_bonds_left": float,
                "PC_bonds_right": float,
                "PC_notes_left": float,
                "PC_notes_right": float,
                "PC_name_service": str,
                "EPA_bonds_left": float,
                "EPA_bonds_right": float,
                "EPA_notes_left": float,
                "EPA_notes_right": float,
                "EPA_name_service": str,
                "HA_bonds_left": float,
                "HA_bonds_right": float,
                "HA_notes_left": float,
                "HA_notes_right": float,
                "HA_name_service": str,
                "ASA_bonds_left": float,
                "ASA_bonds_right": float,
                "ASA_notes_left": float,
                "ASA_notes_right": float,
                "ASA_name_service": str,
                "PBA_bonds_left": float,
                "PBA_bonds_right": float,
                "PBA_notes_left": float,
                "PBA_notes_right": float,
                "PBA_name_service": str,
                "PA_bonds_left": float,
                "PA_bonds_right": float,
                "PA_notes_left": float,
                "PA_notes_right": float,
                "PA_name_service": str,
                "TA_bonds_left": float,
                "TA_bonds_right": float,
                "TA_notes_left": float,
                "TA_notes_right": float,
                "TA_name_service": str,
                "IDC_bonds_left": float,
                "IDC_bonds_right": float,
                "IDC_notes_left": float,
                "IDC_notes_right": float,
                "IDC_name_service": str,
                "GDB_bonds_left": float,
                "GDB_bonds_right": float,
                "GDB_notes_left": float,
                "GDB_notes_right": float,
                "GDB_name_service": str,
                "HFC_bonds_left": float,
                "HFC_bonds_right": float,
                "HFC_notes_left": float,
                "HFC_notes_right": float,
                "HFC_name_service": str,
                "other": str,
                "other_bonds_left": float,
                "other_bonds_right": float,
                "other_notes_left": float,
                "other_notes_right": float,
                "other_name_service": str,
                "other_PC_1": str,
                "other_PC_1_bonds_left": float,
                "other_PC_1_bonds_right": float,
                "other_PC_1_notes_left": float,
                "other_PC_1_notes_right": float,
                "other_PC_1_name_service": str,
                "other_PC_2": str,
                "other_PC_2_bonds_left": float,
                "other_PC_2_bonds_right": float,
                "other_PC_2_notes_left": float,
                "other_PC_2_notes_right": float,
                "other_PC_2_name_service": str,
                "GNMA_bonds_left": float,
                "GNMA_bonds_right": float,
                "GNMA_notes_left": float,
                "GNMA_notes_right": float,
                "GNMA_name_service": str,
                "other5": str,
                "other5_bonds_left": float,
                "other5_bonds_right": float,
                "other5_notes_left": float,
                "other5_notes_right": float,
                "other5_name_service": str,
                "signature": str,
                "position": str,
                "date": str,
                "phone": str,
            },
            table_name="JP_363",
            table_id="11",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/balanza_de_pagos/JP-363.html")
