from django.shortcuts import render
from src.dao.data_db_dao import DAO
import csv
import os


def JP_544_2(request):
    if request.method == "POST":
        # Retrieve form data
        university_name = request.POST.get("university_name")
        phone = request.POST.get("phone")
        contact_person = request.POST.get("contact_person")
        direction = request.POST.get("direction")
        email = request.POST.get("email")

        federal_agency_name_1 = request.POST.get("federal_agency_name_1")
        federal_program_1 = request.POST.get("federal_program_1")
        federal_recieved_amount_1 = request.POST.get("federal_recieved_amount_1")
        federal_date_receipt_1 = request.POST.get("federal_date_receipt_1")

        federal_agency_name_2 = request.POST.get("federal_agency_name_2")
        federal_program_2 = request.POST.get("federal_program_2")
        federal_recieved_amount_2 = request.POST.get("federal_recieved_amount_2")
        federal_date_receipt_2 = request.POST.get("federal_date_receipt_2")

        federal_agency_name_3 = request.POST.get("federal_agency_name_3")
        federal_program_3 = request.POST.get("federal_program_3")
        federal_recieved_amount_3 = request.POST.get("federal_recieved_amount_3")
        federal_date_receipt_3 = request.POST.get("federal_date_receipt_3")

        federal_agency_name_4 = request.POST.get("federal_agency_name_4")
        federal_program_4 = request.POST.get("federal_program_4")
        federal_recieved_amount_4 = request.POST.get("federal_recieved_amount_4")
        federal_date_receipt_4 = request.POST.get("federal_date_receipt_4")

        federal_agency_name_5 = request.POST.get("federal_agency_name_5")
        federal_program_5 = request.POST.get("federal_program_5")
        federal_recieved_amount_5 = request.POST.get("federal_recieved_amount_5")
        federal_date_receipt_5 = request.POST.get("federal_date_receipt_5")

        federal_agency_name_6 = request.POST.get("federal_agency_name_6")
        federal_program_6 = request.POST.get("federal_program_6")
        federal_recieved_amount_6 = request.POST.get("federal_recieved_amount_6")
        federal_date_receipt_6 = request.POST.get("federal_date_receipt_6")

        federal_agency_name_7 = request.POST.get("federal_agency_name_7")
        federal_program_7 = request.POST.get("federal_program_7")
        federal_recieved_amount_7 = request.POST.get("federal_recieved_amount_7")
        federal_date_receipt_7 = request.POST.get("federal_date_receipt_7")

        federal_agency_name_8 = request.POST.get("federal_agency_name_8")
        federal_program_8 = request.POST.get("federal_program_8")
        federal_recieved_amount_8 = request.POST.get("federal_recieved_amount_8")
        federal_date_receipt_8 = request.POST.get("federal_date_receipt_8")

        local_agency_name_1 = request.POST.get("local_agency_name_1")
        agency_program_1 = request.POST.get("agency_program_1")
        agency_recieved_amount_1 = request.POST.get("agency_recieved_amount_1")
        agency_date_receipt_1 = request.POST.get("agency_date_receipt_1")

        local_agency_name_2 = request.POST.get("local_agency_name_2")
        agency_program_2 = request.POST.get("agency_program_2")
        agency_recieved_amount_2 = request.POST.get("agency_recieved_amount_2")
        agency_date_receipt_2 = request.POST.get("agency_date_receipt_2")

        local_agency_name_3 = request.POST.get("local_agency_name_3")
        agency_program_3 = request.POST.get("agency_program_3")
        agency_recieved_amount_3 = request.POST.get("agency_recieved_amount_3")
        agency_date_receipt_3 = request.POST.get("agency_date_receipt_3")

        local_agency_name_4 = request.POST.get("local_agency_name_4")
        agency_program_4 = request.POST.get("agency_program_4")
        agency_recieved_amount_4 = request.POST.get("agency_recieved_amount_4")
        agency_date_receipt_4 = request.POST.get("agency_date_receipt_4")

        local_agency_name_5 = request.POST.get("local_agency_name_5")
        agency_program_5 = request.POST.get("agency_program_5")
        agency_recieved_amount_5 = request.POST.get("agency_recieved_amount_5")
        agency_date_receipt_5 = request.POST.get("agency_date_receipt_5")

        total_students_enrolled = request.POST.get("total_students_enrolled")
        students_recived_amount = request.POST.get("students_recived_amount")

        total_pell_grant_students = request.POST.get("total_pell_grant_students")
        pell_grant_students_amount = request.POST.get("pell_grant_students_amount")

        total_no_resident_student = request.POST.get("total_no_resident_student")
        no_resident_student_amount = request.POST.get("no_resident_student_amount")

        no_resident_students_bills = request.POST.get("no_resident_students_bills")

        loans_granted = request.POST.get("loans_granted")
        loans_granted_amount = request.POST.get("loans_granted_amount")

        donations_institution_name_1 = request.POST.get("donations_institution_name_1")
        donations_amount_1 = request.POST.get("donations_amount_1")
        donations_date_1 = request.POST.get("donations_date_1")

        donations_institution_name_2 = request.POST.get("donations_institution_name_2")
        donations_amount_2 = request.POST.get("donations_amount_2")
        donations_date_2 = request.POST.get("donations_date_2")

        donations_institution_name_3 = request.POST.get("donations_institution_name_3")
        donations_amount_3 = request.POST.get("donations_amount_3")
        donations_date_3 = request.POST.get("donations_date_3")

        donations_institution_name_4 = request.POST.get("donations_institution_name_4")
        donations_amount_4 = request.POST.get("donations_amount_4")
        donations_date_4 = request.POST.get("donations_date_4")

        donations_institution_name_5 = request.POST.get("donations_institution_name_5")
        donations_amount_5 = request.POST.get("donations_amount_5")
        donations_date_5 = request.POST.get("donations_date_5")

        profesional_services_amount = request.POST.get("profesional_services_amount")
        profesional_services_payment = request.POST.get("profesional_services_payment")

        other_payment_relations_1 = request.POST.get("other_payment_relations_1")
        other_payment_relations_amount_1 = request.POST.get(
            "other_payment_relations_amount_1"
        )
        other_payment_relations_payment_1 = request.POST.get(
            "other_payment_relations_payment_1"
        )

        other_payment_relations_2 = request.POST.get("other_payment_relations_2")
        other_payment_relations_amount_2 = request.POST.get(
            "other_payment_relations_amount_2"
        )
        other_payment_relations_payment_2 = request.POST.get(
            "other_payment_relations_payment_2"
        )

        other_payment_relations_3 = request.POST.get("other_payment_relations_3")
        other_payment_relations_amount_3 = request.POST.get(
            "other_payment_relations_amount_3"
        )
        other_payment_relations_payment_3 = request.POST.get(
            "other_payment_relations_payment_3"
        )

        other_payment_relations_4 = request.POST.get("other_payment_relations_4")
        other_payment_relations_amount_4 = request.POST.get(
            "other_payment_relations_amount_4"
        )
        other_payment_relations_payment_4 = request.POST.get(
            "other_payment_relations_payment_4"
        )

        acquired_value = request.POST.get("acquired_value")
        investment_amount = request.POST.get("investment_amount")
        recived_interest = request.POST.get("recived_interest")

        csv_file_path = "data/cuestionarios/balanza_de_pagos/JP-544-2.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "university_name",
                        "phone",
                        "contact_person",
                        "direction",
                        "email",
                        "federal_agency_name_1",
                        "federal_program_1",
                        "federal_recieved_amount_1",
                        "federal_date_receipt_1",
                        "federal_agency_name_2",
                        "federal_program_2",
                        "federal_recieved_amount_2",
                        "federal_date_receipt_2",
                        "federal_agency_name_3",
                        "federal_program_3",
                        "federal_recieved_amount_3",
                        "federal_date_receipt_3",
                        "federal_agency_name_4",
                        "federal_program_4",
                        "federal_recieved_amount_4",
                        "federal_date_receipt_4",
                        "federal_agency_name_5",
                        "federal_program_5",
                        "federal_recieved_amount_5",
                        "federal_date_receipt_5",
                        "federal_agency_name_6",
                        "federal_program_6",
                        "federal_recieved_amount_6",
                        "federal_date_receipt_6",
                        "federal_agency_name_7",
                        "federal_program_7",
                        "federal_recieved_amount_7",
                        "federal_date_receipt_7",
                        "federal_agency_name_8",
                        "federal_program_8",
                        "federal_recieved_amount_8",
                        "federal_date_receipt_8",
                        "local_agency_name_1",
                        "agency_program_1",
                        "agency_recieved_amount_1",
                        "agency_date_receipt_1",
                        "local_agency_name_2",
                        "agency_program_2",
                        "agency_recieved_amount_2",
                        "agency_date_receipt_2",
                        "local_agency_name_3",
                        "agency_program_3",
                        "agency_recieved_amount_3",
                        "agency_date_receipt_3",
                        "local_agency_name_4",
                        "agency_program_4",
                        "agency_recieved_amount_4",
                        "agency_date_receipt_4",
                        "local_agency_name_5",
                        "agency_program_5",
                        "agency_recieved_amount_5",
                        "agency_date_receipt_5",
                        "total_students_enrolled",
                        "students_recived_amount",
                        "total_pell_grant_students",
                        "pell_grant_students_amount",
                        "total_no_resident_student",
                        "no_resident_student_amount",
                        "no_resident_students_bills",
                        "loans_granted",
                        "loans_granted_amount",
                        "donations_institution_name_1",
                        "donations_amount_1",
                        "donations_date_1",
                        "donations_institution_name_2",
                        "donations_amount_2",
                        "donations_date_2",
                        "donations_institution_name_3",
                        "donations_amount_3",
                        "donations_date_3",
                        "donations_institution_name_4",
                        "donations_amount_4",
                        "donations_date_4",
                        "donations_institution_name_5",
                        "donations_amount_5",
                        "donations_date_5",
                        "profesional_services_amount",
                        "profesional_services_payment",
                        "other_payment_relations_1",
                        "other_payment_relations_amount_1",
                        "other_payment_relations_payment_1",
                        "other_payment_relations_2",
                        "other_payment_relations_amount_2",
                        "other_payment_relations_payment_2",
                        "other_payment_relations_3",
                        "other_payment_relations_amount_3",
                        "other_payment_relations_payment_3",
                        "other_payment_relations_4",
                        "other_payment_relations_amount_4",
                        "other_payment_relations_payment_4",
                        "acquired_value",
                        "investment_amount",
                        "recived_interest",
                    ]
                )

            writer.writerow(
                [
                    university_name,
                    phone,
                    contact_person,
                    direction,
                    email,
                    federal_agency_name_1,
                    federal_program_1,
                    federal_recieved_amount_1,
                    federal_date_receipt_1,
                    federal_agency_name_2,
                    federal_program_2,
                    federal_recieved_amount_2,
                    federal_date_receipt_2,
                    federal_agency_name_3,
                    federal_program_3,
                    federal_recieved_amount_3,
                    federal_date_receipt_3,
                    federal_agency_name_4,
                    federal_program_4,
                    federal_recieved_amount_4,
                    federal_date_receipt_4,
                    federal_agency_name_5,
                    federal_program_5,
                    federal_recieved_amount_5,
                    federal_date_receipt_5,
                    federal_agency_name_6,
                    federal_program_6,
                    federal_recieved_amount_6,
                    federal_date_receipt_6,
                    federal_agency_name_7,
                    federal_program_7,
                    federal_recieved_amount_7,
                    federal_date_receipt_7,
                    federal_agency_name_8,
                    federal_program_8,
                    federal_recieved_amount_8,
                    federal_date_receipt_8,
                    local_agency_name_1,
                    agency_program_1,
                    agency_recieved_amount_1,
                    agency_date_receipt_1,
                    local_agency_name_2,
                    agency_program_2,
                    agency_recieved_amount_2,
                    agency_date_receipt_2,
                    local_agency_name_3,
                    agency_program_3,
                    agency_recieved_amount_3,
                    agency_date_receipt_3,
                    local_agency_name_4,
                    agency_program_4,
                    agency_recieved_amount_4,
                    agency_date_receipt_4,
                    local_agency_name_5,
                    agency_program_5,
                    agency_recieved_amount_5,
                    agency_date_receipt_5,
                    total_students_enrolled,
                    students_recived_amount,
                    total_pell_grant_students,
                    pell_grant_students_amount,
                    total_no_resident_student,
                    no_resident_student_amount,
                    no_resident_students_bills,
                    loans_granted,
                    loans_granted_amount,
                    donations_institution_name_1,
                    donations_amount_1,
                    donations_date_1,
                    donations_institution_name_2,
                    donations_amount_2,
                    donations_date_2,
                    donations_institution_name_3,
                    donations_amount_3,
                    donations_date_3,
                    donations_institution_name_4,
                    donations_amount_4,
                    donations_date_4,
                    donations_institution_name_5,
                    donations_amount_5,
                    donations_date_5,
                    profesional_services_amount,
                    profesional_services_payment,
                    other_payment_relations_1,
                    other_payment_relations_amount_1,
                    other_payment_relations_payment_1,
                    other_payment_relations_2,
                    other_payment_relations_amount_2,
                    other_payment_relations_payment_2,
                    other_payment_relations_3,
                    other_payment_relations_amount_3,
                    other_payment_relations_payment_3,
                    other_payment_relations_4,
                    other_payment_relations_amount_4,
                    other_payment_relations_payment_4,
                    acquired_value,
                    investment_amount,
                    recived_interest,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/balanza_de_pagos/JP-544-2.csv",
            dtypes={
                "university_name": str,
                "phone": str,
                "contact_person": str,
                "direction": str,
                "email": str,
                "federal_agency_name_1": str,
                "federal_program_1": str,
                "federal_recieved_amount_1": int,
                "federal_date_receipt_1": str,
                "federal_agency_name_2": str,
                "federal_program_2": str,
                "federal_recieved_amount_2": int,
                "federal_date_receipt_2": str,
                "federal_agency_name_3": str,
                "federal_program_3": str,
                "federal_recieved_amount_3": int,
                "federal_date_receipt_3": str,
                "federal_agency_name_4": str,
                "federal_program_4": str,
                "federal_recieved_amount_4": int,
                "federal_date_receipt_4": str,
                "federal_agency_name_5": str,
                "federal_program_5": str,
                "federal_recieved_amount_5": int,
                "federal_date_receipt_5": str,
                "federal_agency_name_6": str,
                "federal_program_6": str,
                "federal_recieved_amount_6": int,
                "federal_date_receipt_6": str,
                "federal_agency_name_7": str,
                "federal_program_7": str,
                "federal_recieved_amount_7": int,
                "federal_date_receipt_7": str,
                "federal_agency_name_8": str,
                "federal_program_8": str,
                "federal_recieved_amount_8": int,
                "federal_date_receipt_8": str,
                "local_agency_name_1": str,
                "agency_program_1": str,
                "agency_recieved_amount_1": int,
                "agency_date_receipt_1": str,
                "local_agency_name_2": str,
                "agency_program_2": str,
                "agency_recieved_amount_2": int,
                "agency_date_receipt_2": str,
                "local_agency_name_3": str,
                "agency_program_3": str,
                "agency_recieved_amount_3": int,
                "agency_date_receipt_3": str,
                "local_agency_name_4": str,
                "agency_program_4": str,
                "agency_recieved_amount_4": int,
                "agency_date_receipt_4": str,
                "local_agency_name_5": str,
                "agency_program_5": str,
                "agency_recieved_amount_5": int,
                "agency_date_receipt_5": str,
                "total_students_enrolled": int,
                "students_recived_amount": float,
                "total_pell_grant_students": int,
                "pell_grant_students_amount": float,
                "total_no_resident_student": int,
                "no_resident_student_amount": float,
                "no_resident_students_bills": float,
                "loans_granted": int,
                "loans_granted_amount": float,
                "donations_institution_name_1": str,
                "donations_amount_1": float,
                "donations_date_1": str,
                "donations_institution_name_2": str,
                "donations_amount_2": float,
                "donations_date_2": str,
                "donations_institution_name_3": str,
                "donations_amount_3": float,
                "donations_date_3": str,
                "donations_institution_name_4": str,
                "donations_amount_4": float,
                "donations_date_4": str,
                "donations_institution_name_5": str,
                "donations_amount_5": float,
                "donations_date_5": str,
                "profesional_services_amount": int,
                "profesional_services_payment": float,
                "other_payment_relations_1": str,
                "other_payment_relations_amount_1": int,
                "other_payment_relations_payment_1": float,
                "other_payment_relations_2": str,
                "other_payment_relations_amount_2": int,
                "other_payment_relations_payment_2": float,
                "other_payment_relations_3": str,
                "other_payment_relations_amount_3": int,
                "other_payment_relations_payment_3": float,
                "other_payment_relations_4": str,
                "other_payment_relations_amount_4": int,
                "other_payment_relations_payment_4": float,
                "acquired_value": float,
                "investment_amount": float,
                "recived_interest": float,
            },
            table_name="JP_544_1",
            table_id=28,
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/balanza_de_pagos/JP-544-2.html")
