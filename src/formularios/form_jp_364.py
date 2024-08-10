from django.shortcuts import render
from src.dao.data_db_dao import DAO
import csv
import os


def JP_364(request):
    if request.method == "POST":
        # Retrieve form data
        year_bono1 = request.POST.get("year_bono1")
        year_bono2 = request.POST.get("year_bono2")
        year_paga1 = request.POST.get("year_paga1")
        year_paga2 = request.POST.get("year_paga2")
        ELA_bono1 = request.POST.get("ELA_bono1")
        ELA_bono2 = request.POST.get("ELA_bono2")
        ELA_paga1 = request.POST.get("ELA_paga1")
        ELA_paga2 = request.POST.get("ELA_paga2")
        ELA_agente = request.POST.get("ELA_agente")
        municipio_bono1 = request.POST.get("municipio_bono1")
        municipio_bono2 = request.POST.get("municipio_bono2")
        municipio_paga1 = request.POST.get("municipio_paga1")
        municipio_paga2 = request.POST.get("municipio_paga2")
        municipio_agente = request.POST.get("municipio_agente")
        corp_publicas_bono1 = request.POST.get("corp_publicas_bono1")
        corp_publicas_bono2 = request.POST.get("corp_publicas_bono2")
        corp_publicas_paga1 = request.POST.get("corp_publicas_paga1")
        corp_publicas_paga2 = request.POST.get("corp_publicas_paga2")
        corp_publicas_agente = request.POST.get("corp_publicas_agente")
        AEE_bono1 = request.POST.get("AEE_bono1")
        AEE_bono2 = request.POST.get("AEE_bono2")
        AEE_paga1 = request.POST.get("AEE_paga1")
        AEE_paga2 = request.POST.get("AEE_paga2")
        AEE_agente = request.POST.get("AEE_agente")
        Acarreteras_bono1 = request.POST.get("Acarreteras_bono1")
        Acarreteras_bono2 = request.POST.get("Acarreteras_bono2")
        Acarreteras_paga1 = request.POST.get("Acarreteras_paga1")
        Acarreteras_paga2 = request.POST.get("Acarreteras_paga2")
        Acarreteras_agente = request.POST.get("Acarreteras_agente")
        AAA_bono1 = request.POST.get("AAA_bono1")
        AAA_bono2 = request.POST.get("AAA_bono2")
        AAA_paga1 = request.POST.get("AAA_paga1")
        AAA_paga2 = request.POST.get("AAA_paga2")
        AAA_agente = request.POST.get("AAA_agente")
        AEP_bono1 = request.POST.get("AEP_bono1")
        AEP_bono2 = request.POST.get("AEP_bono2")
        AEP_paga1 = request.POST.get("AEP_paga1")
        AEP_paga2 = request.POST.get("AEP_paga2")
        AEP_agente = request.POST.get("AEP_agente")
        AP_bono1 = request.POST.get("AP_bono1")
        AP_bono2 = request.POST.get("AP_bono2")
        AP_paga1 = request.POST.get("AP_paga1")
        AP_paga2 = request.POST.get("AP_paga2")
        AP_agente = request.POST.get("AP_agente")
        AT_bono1 = request.POST.get("AT_bono1")
        AT_bono2 = request.POST.get("AT_bono2")
        AT_paga1 = request.POST.get("AT_paga1")
        AT_paga2 = request.POST.get("AT_paga2")
        AT_agente = request.POST.get("AT_agente")
        CFI_bono1 = request.POST.get("CFI_bono1")
        CFI_bono2 = request.POST.get("CFI_bono2")
        CFI_paga1 = request.POST.get("CFI_paga1")
        CFI_paga2 = request.POST.get("CFI_paga2")
        CFI_agente = request.POST.get("CFI_agente")
        BGF_bono1 = request.POST.get("BGF_bono1")
        BGF_bono2 = request.POST.get("BGF_bono2")
        BGF_paga1 = request.POST.get("BGF_paga1")
        BGF_paga2 = request.POST.get("BGF_paga2")
        BGF_agente = request.POST.get("BGF_agente")
        CFV_bono1 = request.POST.get("CFV_bono1")
        CFV_bono2 = request.POST.get("CFV_bono2")
        CFV_paga1 = request.POST.get("CFV_paga1")
        CFV_paga2 = request.POST.get("CFV_paga2")
        CFV_agente = request.POST.get("CFV_agente")
        otherk_title = request.POST.get("otherk_title")
        otherk_bono1 = request.POST.get("otherk_bono1")
        otherk_bono2 = request.POST.get("otherk_bono2")
        otherk_paga1 = request.POST.get("otherk_paga1")
        otherk_paga2 = request.POST.get("otherk_paga2")
        otherk_agente = request.POST.get("otherk_agente")
        otherl_title = request.POST.get("otherl_title")
        otherl_bono1 = request.POST.get("otherl_bono1")
        otherl_bono2 = request.POST.get("otherl_bono2")
        otherl_paga1 = request.POST.get("otherl_paga1")
        otherl_paga2 = request.POST.get("otherl_paga2")
        otherl_agente = request.POST.get("otherl_agente")
        otherm_title = request.POST.get("otherm_title")
        otherm_bono1 = request.POST.get("otherm_bono1")
        otherm_bono2 = request.POST.get("otherm_bono2")
        otherm_paga1 = request.POST.get("otherm_paga1")
        otherm_paga2 = request.POST.get("otherm_paga2")
        otherm_agente = request.POST.get("otherm_agente")

        year_balance1 = request.POST.get("year_balance1")
        year_balance2 = request.POST.get("year_balance2")
        FHA_balance1 = request.POST.get("FHA_balance1")
        FHA_balance2 = request.POST.get("FHA_balance2")
        FHA_agente = request.POST.get("FHA_agente")
        GAV_balance1 = request.POST.get("GAV_balance1")
        GAV_balance2 = request.POST.get("GAV_balance2")
        GAV_agente = request.POST.get("GAV_agente")
        convencionales_balance1 = request.POST.get("convencionales_balance1")
        convencionales_balance2 = request.POST.get("convencionales_balance2")
        convencionales_agente = request.POST.get("convencionales_agente")
        otras_instituciones_balance1 = request.POST.get("otras_instituciones_balance1")
        otras_instituciones_balance2 = request.POST.get("otras_instituciones_balance2")
        otras_instituciones_agente = request.POST.get("otras_instituciones_agente")
        prestamos_hipo_balance1 = request.POST.get("prestamos_hipo_balance1")
        prestamos_hipo_balance2 = request.POST.get("prestamos_hipo_balance2")
        prestamos_hipo_agente = request.POST.get("prestamos_hipo_agente")
        prestamos_comerciales_industriales_balance1 = request.POST.get(
            "prestamos_comerciales_industriales_balance1"
        )
        prestamos_comerciales_industriales_balance2 = request.POST.get(
            "prestamos_comerciales_industriales_balance2"
        )
        prestamos_comerciales_industriales_agente = request.POST.get(
            "prestamos_comerciales_industriales_agente"
        )
        prestamos_poliza_balance1 = request.POST.get("prestamos_poliza_balance1")
        prestamos_poliza_balance2 = request.POST.get("prestamos_poliza_balance2")
        prestamos_poliza_agente = request.POST.get("prestamos_poliza_agente")
        reservas_poliza_balance1 = request.POST.get("reservas_poliza_balance1")
        reservas_poliza_balance2 = request.POST.get("reservas_poliza_balance2")
        reservas_poliza_agente = request.POST.get("reservas_poliza_agente")
        dividendos_poliza_balance1 = request.POST.get("dividendos_poliza_balance1")
        dividendos_poliza_balance2 = request.POST.get("dividendos_poliza_balance2")
        dividendos_poliza_agente = request.POST.get("dividendos_poliza_agente")
        signature = request.POST.get("nombre_firma")
        phone = request.POST.get("phone")
        nombre_persona = request.POST.get("nombre_persona")

        csv_file_path = "data/cuestionarios/balanza_de_pagos/JP-364.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "year_bono1",
                        "year_bono2",
                        "year_paga1",
                        "year_paga2",
                        "ELA_bono1",
                        "ELA_bono2",
                        "ELA_paga1",
                        "ELA_paga2",
                        "ELA_agente",
                        "municipio_bono1",
                        "municipio_bono2",
                        "municipio_paga1",
                        "municipio_paga2",
                        "municipio_agente",
                        "corp_publicas_bono1",
                        "corp_publicas_bono2",
                        "corp_publicas_paga1",
                        "corp_publicas_paga2",
                        "corp_publicas_agente",
                        "AEE_bono1",
                        "AEE_bono2",
                        "AEE_paga1",
                        "AEE_paga2",
                        "AEE_agente",
                        "Acarreteras_bono1",
                        "Acarreteras_bono2",
                        "Acarreteras_paga1",
                        "Acarreteras_paga2",
                        "Acarreteras_agente",
                        "AAA_bono1",
                        "AAA_bono2",
                        "AAA_paga1",
                        "AAA_paga2",
                        "AAA_agente",
                        "AEP_bono1",
                        "AEP_bono2",
                        "AEP_paga1",
                        "AEP_paga2",
                        "AEP_agente",
                        "AP_bono1",
                        "AP_bono2",
                        "AP_paga1",
                        "AP_paga2",
                        "AP_agente",
                        "AT_bono1",
                        "AT_bono2",
                        "AT_paga1",
                        "AT_paga2",
                        "AT_agente",
                        "CFI_bono1",
                        "CFI_bono2",
                        "CFI_paga1",
                        "CFI_paga2",
                        "CFI_agente",
                        "BGF_bono1",
                        "BGF_bono2",
                        "BGF_paga1",
                        "BGF_paga2",
                        "BGF_agente",
                        "CFV_bono1",
                        "CFV_bono2",
                        "CFV_paga1",
                        "CFV_paga2",
                        "CFV_agente",
                        "otherk_title",
                        "otherk_bono1",
                        "otherk_bono2",
                        "otherk_paga1",
                        "otherk_paga2",
                        "otherk_agente",
                        "otherl_title",
                        "otherl_bono1",
                        "otherl_bono2",
                        "otherl_paga1",
                        "otherl_paga2",
                        "otherl_agente",
                        "otherm_title",
                        "otherm_bono1",
                        "otherm_bono2",
                        "otherm_paga1",
                        "otherm_paga2",
                        "otherm_agente",
                        "year_balance1",
                        "year_balance2",
                        "FHA_balance1",
                        "FHA_balance2",
                        "FHA_agente",
                        "GAV_balance1",
                        "GAV_balance2",
                        "GAV_agente",
                        "convencionales_balance1",
                        "convencionales_balance2",
                        "convencionales_agente",
                        "otras_instituciones_balance1",
                        "otras_instituciones_balance2",
                        "otras_instituciones_agente",
                        "prestamos_hipo_balance1",
                        "prestamos_hipo_balance2",
                        "prestamos_hipo_agente",
                        "prestamos_comerciales_industriales_balance1",
                        "prestamos_comerciales_industriales_balance2",
                        "prestamos_comerciales_industriales_agente",
                        "prestamos_poliza_balance1",
                        "prestamos_poliza_balance2",
                        "prestamos_poliza_agente",
                        "reservas_poliza_balance1",
                        "reservas_poliza_balance2",
                        "reservas_poliza_agente",
                        "dividendos_poliza_balance1",
                        "dividendos_poliza_balance2",
                        "dividendos_poliza_agente",
                        "signature",
                        "phone",
                        "nombre_persona",
                    ]
                )

            writer.writerow(
                [
                    year_bono1,
                    year_bono2,
                    year_paga1,
                    year_paga2,
                    ELA_bono1,
                    ELA_bono2,
                    ELA_paga1,
                    ELA_paga2,
                    ELA_agente,
                    municipio_bono1,
                    municipio_bono2,
                    municipio_paga1,
                    municipio_paga2,
                    municipio_agente,
                    corp_publicas_bono1,
                    corp_publicas_bono2,
                    corp_publicas_paga1,
                    corp_publicas_paga2,
                    corp_publicas_agente,
                    AEE_bono1,
                    AEE_bono2,
                    AEE_paga1,
                    AEE_paga2,
                    AEE_agente,
                    Acarreteras_bono1,
                    Acarreteras_bono2,
                    Acarreteras_paga1,
                    Acarreteras_paga2,
                    Acarreteras_agente,
                    AAA_bono1,
                    AAA_bono2,
                    AAA_paga1,
                    AAA_paga2,
                    AAA_agente,
                    AEP_bono1,
                    AEP_bono2,
                    AEP_paga1,
                    AEP_paga2,
                    AEP_agente,
                    AP_bono1,
                    AP_bono2,
                    AP_paga1,
                    AP_paga2,
                    AP_agente,
                    AT_bono1,
                    AT_bono2,
                    AT_paga1,
                    AT_paga2,
                    AT_agente,
                    CFI_bono1,
                    CFI_bono2,
                    CFI_paga1,
                    CFI_paga2,
                    CFI_agente,
                    BGF_bono1,
                    BGF_bono2,
                    BGF_paga1,
                    BGF_paga2,
                    BGF_agente,
                    CFV_bono1,
                    CFV_bono2,
                    CFV_paga1,
                    CFV_paga2,
                    CFV_agente,
                    otherk_title,
                    otherk_bono1,
                    otherk_bono2,
                    otherk_paga1,
                    otherk_paga2,
                    otherk_agente,
                    otherl_title,
                    otherl_bono1,
                    otherl_bono2,
                    otherl_paga1,
                    otherl_paga2,
                    otherl_agente,
                    otherm_title,
                    otherm_bono1,
                    otherm_bono2,
                    otherm_paga1,
                    otherm_paga2,
                    otherm_agente,
                    year_balance1,
                    year_balance2,
                    FHA_balance1,
                    FHA_balance2,
                    FHA_agente,
                    GAV_balance1,
                    GAV_balance2,
                    GAV_agente,
                    convencionales_balance1,
                    convencionales_balance2,
                    convencionales_agente,
                    otras_instituciones_balance1,
                    otras_instituciones_balance2,
                    otras_instituciones_agente,
                    prestamos_hipo_balance1,
                    prestamos_hipo_balance2,
                    prestamos_hipo_agente,
                    prestamos_comerciales_industriales_balance1,
                    prestamos_comerciales_industriales_balance2,
                    prestamos_comerciales_industriales_agente,
                    prestamos_poliza_balance1,
                    prestamos_poliza_balance2,
                    prestamos_poliza_agente,
                    reservas_poliza_balance1,
                    reservas_poliza_balance2,
                    reservas_poliza_agente,
                    dividendos_poliza_balance1,
                    dividendos_poliza_balance2,
                    dividendos_poliza_agente,
                    signature,
                    phone,
                    nombre_persona,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/balanza_de_pagos/JP-364.csv",
            dtypes={
                "year_bono1": int,
                "year_bono2": int,
                "year_paga1": int,
                "year_paga2": int,
                "ELA_bono1": float,
                "ELA_bono2": float,
                "ELA_paga1": float,
                "ELA_paga2": float,
                "ELA_agente": str,
                "municipio_bono1": float,
                "municipio_bono2": float,
                "municipio_paga1": float,
                "municipio_paga2": float,
                "municipio_agente": str,
                "corp_publicas_bono1": float,
                "corp_publicas_bono2": float,
                "corp_publicas_paga1": float,
                "corp_publicas_paga2": float,
                "corp_publicas_agente": str,
                "AEE_bono1": float,
                "AEE_bono2": float,
                "AEE_paga1": float,
                "AEE_paga2": float,
                "AEE_agente": str,
                "Acarreteras_bono1": float,
                "Acarreteras_bono2": float,
                "Acarreteras_paga1": float,
                "Acarreteras_paga2": float,
                "Acarreteras_agente": str,
                "AAA_bono1": float,
                "AAA_bono2": float,
                "AAA_paga1": float,
                "AAA_paga2": float,
                "AAA_agente": str,
                "AEP_bono1": float,
                "AEP_bono2": float,
                "AEP_paga1": float,
                "AEP_paga2": float,
                "AEP_agente": str,
                "AP_bono1": float,
                "AP_bono2": float,
                "AP_paga1": float,
                "AP_paga2": float,
                "AP_agente": str,
                "AT_bono1": float,
                "AT_bono2": float,
                "AT_paga1": float,
                "AT_paga2": float,
                "AT_agente": str,
                "CFI_bono1": float,
                "CFI_bono2": float,
                "CFI_paga1": float,
                "CFI_paga2": float,
                "CFI_agente": str,
                "BGF_bono1": float,
                "BGF_bono2": float,
                "BGF_paga1": float,
                "BGF_paga2": float,
                "BGF_agente": str,
                "CFV_bono1": float,
                "CFV_bono2": float,
                "CFV_paga1": float,
                "CFV_paga2": float,
                "CFV_agente": str,
                "otherk_title": str,
                "otherk_bono1": float,
                "otherk_bono2": float,
                "otherk_paga1": float,
                "otherk_paga2": float,
                "otherk_agente": str,
                "otherl_title": str,
                "otherl_bono1": float,
                "otherl_bono2": float,
                "otherl_paga1": float,
                "otherl_paga2": float,
                "otherl_agente": str,
                "otherm_title": str,
                "otherm_bono1": float,
                "otherm_bono2": float,
                "otherm_paga1": float,
                "otherm_paga2": float,
                "otherm_agente": str,
                "year_balance1": int,
                "year_balance2": int,
                "FHA_balance1": float,
                "FHA_balance2": float,
                "FHA_agente": str,
                "GAV_balance1": float,
                "GAV_balance2": float,
                "GAV_agente": str,
                "convencionales_balance1": float,
                "convencionales_balance2": float,
                "convencionales_agente": str,
                "otras_instituciones_balance1": float,
                "otras_instituciones_balance2": float,
                "otras_instituciones_agente": str,
                "prestamos_hipo_balance1": float,
                "prestamos_hipo_balance2": float,
                "prestamos_hipo_agente": str,
                "prestamos_comerciales_industriales_balance1": float,
                "prestamos_comerciales_industriales_balance2": float,
                "prestamos_comerciales_industriales_agente": str,
                "prestamos_poliza_balance1": float,
                "prestamos_poliza_balance2": float,
                "prestamos_poliza_agente": str,
                "reservas_poliza_balance1": float,
                "reservas_poliza_balance2": float,
                "reservas_poliza_agente": str,
                "dividendos_poliza_balance1": float,
                "dividendos_poliza_balance2": float,
                "dividendos_poliza_agente": str,
                "signature": str,
                "phone": str,
                "nombre_persona": str,
            },
            table_name="JP_364",
            table_id="4",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/balanza_de_pagos/JP-364.html")
