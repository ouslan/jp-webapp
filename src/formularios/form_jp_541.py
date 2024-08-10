from django.shortcuts import render
from src.dao.data_db_dao import DAO
import csv
import os


def JP_541(request):
    if request.method == "POST":
        # Retrieve form data

        # TABLE 1
        encuesta_1 = request.POST.get("encuesta_1")
        fiscal_year_1 = request.POST.get("fiscal_year_1")
        company_name_1 = request.POST.get("company_name_1")
        liaison_officer_1 = request.POST.get("liaison_officer_1")
        tel_1 = request.POST.get("tel_1")
        project_1 = request.POST.get("project_1")
        branches_1 = request.POST.get("branches_1")

        project_name_1_1 = request.POST.get("project_name_1_1")
        city_1_1 = request.POST.get("city_1_1")
        total_number_project_1_1 = request.POST.get("total_number_project_1_1")
        total_cost_1_1 = request.POST.get("total_cost_1_1")
        start_date_1_1 = request.POST.get("start_date_1_1")
        end_date_1_1 = request.POST.get("end_date_1_1")
        value_first_trimester_1_1 = request.POST.get("value_first_trimester_1_1")
        value_second_trimester_1_1 = request.POST.get("value_second_trimester_1_1")
        value_third_trimester_1_1 = request.POST.get("value_third_trimester_1_1")
        value_fourth_trimester_1_1 = request.POST.get("value_fourth_trimester_1_1")

        project_name_1_2 = request.POST.get("project_name_1_2")
        city_1_2 = request.POST.get("city_1_2")
        total_number_project_1_2 = request.POST.get("total_number_project_1_2")
        total_cost_1_2 = request.POST.get("total_cost_1_2")
        start_date_1_2 = request.POST.get("start_date_1_2")
        end_date_1_2 = request.POST.get("end_date_1_2")
        value_first_trimester_1_2 = request.POST.get("value_first_trimester_1_2")
        value_second_trimester_1_2 = request.POST.get("value_second_trimester_1_2")
        value_third_trimester_1_2 = request.POST.get("value_third_trimester_1_2")
        value_fourth_trimester_1_2 = request.POST.get("value_fourth_trimester_1_2")

        project_name_1_3 = request.POST.get("project_name_1_3")
        city_1_3 = request.POST.get("city_1_3")
        total_number_project_1_3 = request.POST.get("total_number_project_1_3")
        total_cost_1_3 = request.POST.get("total_cost_1_3")
        start_date_1_3 = request.POST.get("start_date_1_3")
        end_date_1_3 = request.POST.get("end_date_1_3")
        value_first_trimester_1_3 = request.POST.get("value_first_trimester_1_3")
        value_second_trimester_1_3 = request.POST.get("value_second_trimester_1_3")
        value_third_trimester_1_3 = request.POST.get("value_third_trimester_1_3")
        value_fourth_trimester_1_3 = request.POST.get("value_fourth_trimester_1_3")

        project_name_1_4 = request.POST.get("project_name_1_4")
        city_1_4 = request.POST.get("city_1_4")
        total_number_project_1_4 = request.POST.get("total_number_project_1_4")
        total_cost_1_4 = request.POST.get("total_cost_1_4")
        start_date_1_4 = request.POST.get("start_date_1_4")
        end_date_1_4 = request.POST.get("end_date_1_4")
        value_first_trimester_1_4 = request.POST.get("value_first_trimester_1_4")
        value_second_trimester_1_4 = request.POST.get("value_second_trimester_1_4")
        value_third_trimester_1_4 = request.POST.get("value_third_trimester_1_4")
        value_fourth_trimester_1_4 = request.POST.get("value_fourth_trimester_1_4")

        project_name_1_5 = request.POST.get("project_name_1_5")
        city_1_5 = request.POST.get("city_1_5")
        total_number_project_1_5 = request.POST.get("total_number_project_1_5")
        total_cost_1_5 = request.POST.get("total_cost_1_5")
        start_date_1_5 = request.POST.get("start_date_1_5")
        end_date_1_5 = request.POST.get("end_date_1_5")
        value_first_trimester_1_5 = request.POST.get("value_first_trimester_1_5")
        value_second_trimester_1_5 = request.POST.get("value_second_trimester_1_5")
        value_third_trimester_1_5 = request.POST.get("value_third_trimester_1_5")
        value_fourth_trimester_1_5 = request.POST.get("value_fourth_trimester_1_5")

        project_name_1_6 = request.POST.get("project_name_1_6")
        city_1_6 = request.POST.get("city_1_6")
        total_number_project_1_6 = request.POST.get("total_number_project_1_6")
        total_cost_1_6 = request.POST.get("total_cost_1_6")
        start_date_1_6 = request.POST.get("start_date_1_6")
        end_date_1_6 = request.POST.get("end_date_1_6")
        value_first_trimester_1_6 = request.POST.get("value_first_trimester_1_6")
        value_second_trimester_1_6 = request.POST.get("value_second_trimester_1_6")
        value_third_trimester_1_6 = request.POST.get("value_third_trimester_1_6")
        value_fourth_trimester_1_6 = request.POST.get("value_fourth_trimester_1_6")

        project_name_1_7 = request.POST.get("project_name_1_7")
        city_1_7 = request.POST.get("city_1_7")
        total_number_project_1_7 = request.POST.get("total_number_project_1_7")
        total_cost_1_7 = request.POST.get("total_cost_1_7")
        start_date_1_7 = request.POST.get("start_date_1_7")
        end_date_1_7 = request.POST.get("end_date_1_7")
        value_first_trimester_1_7 = request.POST.get("value_first_trimester_1_7")
        value_second_trimester_1_7 = request.POST.get("value_second_trimester_1_7")
        value_third_trimester_1_7 = request.POST.get("value_third_trimester_1_7")
        value_fourth_trimester_1_7 = request.POST.get("value_fourth_trimester_1_7")

        project_name_1_8 = request.POST.get("project_name_1_8")
        city_1_8 = request.POST.get("city_1_8")
        total_number_project_1_8 = request.POST.get("total_number_project_1_8")
        total_cost_1_8 = request.POST.get("total_cost_1_8")
        start_date_1_8 = request.POST.get("start_date_1_8")
        end_date_1_8 = request.POST.get("end_date_1_8")
        value_first_trimester_1_8 = request.POST.get("value_first_trimester_1_8")
        value_second_trimester_1_8 = request.POST.get("value_second_trimester_1_8")
        value_third_trimester_1_8 = request.POST.get("value_third_trimester_1_8")
        value_fourth_trimester_1_8 = request.POST.get("value_fourth_trimester_1_8")

        project_name_1_9 = request.POST.get("project_name_1_9")
        city_1_9 = request.POST.get("city_1_9")
        total_number_project_1_9 = request.POST.get("total_number_project_1_9")
        total_cost_1_9 = request.POST.get("total_cost_1_9")
        start_date_1_9 = request.POST.get("start_date_1_9")
        end_date_1_9 = request.POST.get("end_date_1_9")
        value_first_trimester_1_9 = request.POST.get("value_first_trimester_1_9")
        value_second_trimester_1_9 = request.POST.get("value_second_trimester_1_9")
        value_third_trimester_1_9 = request.POST.get("value_third_trimester_1_9")
        value_fourth_trimester_1_9 = request.POST.get("value_fourth_trimester_1_9")

        project_name_1_10 = request.POST.get("project_name_1_10")
        city_1_10 = request.POST.get("city_1_10")
        total_number_project_1_10 = request.POST.get("total_number_project_1_10")
        total_cost_1_10 = request.POST.get("total_cost_1_10")
        start_date_1_10 = request.POST.get("start_date_1_10")
        end_date_1_10 = request.POST.get("end_date_1_10")
        value_first_trimester_1_10 = request.POST.get("value_first_trimester_1_10")
        value_second_trimester_1_10 = request.POST.get("value_second_trimester_1_10")
        value_third_trimester_1_10 = request.POST.get("value_third_trimester_1_10")
        value_fourth_trimester_1_10 = request.POST.get("value_fourth_trimester_1_10")

        # TABLE 2
        encuesta_2 = request.POST.get("encuesta_2")
        fiscal_year_2 = request.POST.get("fiscal_year_2")
        company_name_2 = request.POST.get("company_name_2")
        liaison_officer_2 = request.POST.get("liaison_officer_2")
        tel_2 = request.POST.get("tel_2")
        project_2 = request.POST.get("project_2")
        branches_2 = request.POST.get("branches_2")

        project_name_2_1 = request.POST.get("project_name_2_1")
        city_2_1 = request.POST.get("city_2_1")
        total_number_project_2_1 = request.POST.get("total_number_project_2_1")
        total_cost_2_1 = request.POST.get("total_cost_2_1")
        start_date_2_1 = request.POST.get("start_date_2_1")
        end_date_2_1 = request.POST.get("end_date_2_1")
        value_first_trimester_2_1 = request.POST.get("value_first_trimester_2_1")
        value_second_trimester_2_1 = request.POST.get("value_second_trimester_2_1")
        value_third_trimester_2_1 = request.POST.get("value_third_trimester_2_1")
        value_fourth_trimester_2_1 = request.POST.get("value_fourth_trimester_2_1")

        project_name_2_2 = request.POST.get("project_name_2_2")
        city_2_2 = request.POST.get("city_2_2")
        total_number_project_2_2 = request.POST.get("total_number_project_2_2")
        total_cost_2_2 = request.POST.get("total_cost_2_2")
        start_date_2_2 = request.POST.get("start_date_2_2")
        end_date_2_2 = request.POST.get("end_date_2_2")
        value_first_trimester_2_2 = request.POST.get("value_first_trimester_2_2")
        value_second_trimester_2_2 = request.POST.get("value_second_trimester_2_2")
        value_third_trimester_2_2 = request.POST.get("value_third_trimester_2_2")
        value_fourth_trimester_2_2 = request.POST.get("value_fourth_trimester_2_2")

        project_name_2_3 = request.POST.get("project_name_2_3")
        city_2_3 = request.POST.get("city_2_3")
        total_number_project_2_3 = request.POST.get("total_number_project_2_3")
        total_cost_2_3 = request.POST.get("total_cost_2_3")
        start_date_2_3 = request.POST.get("start_date_2_3")
        end_date_2_3 = request.POST.get("end_date_2_3")
        value_first_trimester_2_3 = request.POST.get("value_first_trimester_2_3")
        value_second_trimester_2_3 = request.POST.get("value_second_trimester_2_3")
        value_third_trimester_2_3 = request.POST.get("value_third_trimester_2_3")
        value_fourth_trimester_2_3 = request.POST.get("value_fourth_trimester_2_3")

        project_name_2_4 = request.POST.get("project_name_2_4")
        city_2_4 = request.POST.get("city_2_4")
        total_number_project_2_4 = request.POST.get("total_number_project_2_4")
        total_cost_2_4 = request.POST.get("total_cost_2_4")
        start_date_2_4 = request.POST.get("start_date_2_4")
        end_date_2_4 = request.POST.get("end_date_2_4")
        value_first_trimester_2_4 = request.POST.get("value_first_trimester_2_4")
        value_second_trimester_2_4 = request.POST.get("value_second_trimester_2_4")
        value_third_trimester_2_4 = request.POST.get("value_third_trimester_2_4")
        value_fourth_trimester_2_4 = request.POST.get("value_fourth_trimester_2_4")

        project_name_2_5 = request.POST.get("project_name_2_5")
        city_2_5 = request.POST.get("city_2_5")
        total_number_project_2_5 = request.POST.get("total_number_project_2_5")
        total_cost_2_5 = request.POST.get("total_cost_2_5")
        start_date_2_5 = request.POST.get("start_date_2_5")
        end_date_2_5 = request.POST.get("end_date_2_5")
        value_first_trimester_2_5 = request.POST.get("value_first_trimester_2_5")
        value_second_trimester_2_5 = request.POST.get("value_second_trimester_2_5")
        value_third_trimester_2_5 = request.POST.get("value_third_trimester_2_5")
        value_fourth_trimester_2_5 = request.POST.get("value_fourth_trimester_2_5")

        project_name_2_6 = request.POST.get("project_name_2_6")
        city_2_6 = request.POST.get("city_2_6")
        total_number_project_2_6 = request.POST.get("total_number_project_2_6")
        total_cost_2_6 = request.POST.get("total_cost_2_6")
        start_date_2_6 = request.POST.get("start_date_2_6")
        end_date_2_6 = request.POST.get("end_date_2_6")
        value_first_trimester_2_6 = request.POST.get("value_first_trimester_2_6")
        value_second_trimester_2_6 = request.POST.get("value_second_trimester_2_6")
        value_third_trimester_2_6 = request.POST.get("value_third_trimester_2_6")
        value_fourth_trimester_2_6 = request.POST.get("value_fourth_trimester_2_6")

        project_name_2_7 = request.POST.get("project_name_2_7")
        city_2_7 = request.POST.get("city_2_7")
        total_number_project_2_7 = request.POST.get("total_number_project_2_7")
        total_cost_2_7 = request.POST.get("total_cost_2_7")
        start_date_2_7 = request.POST.get("start_date_2_7")
        end_date_2_7 = request.POST.get("end_date_2_7")
        value_first_trimester_2_7 = request.POST.get("value_first_trimester_2_7")
        value_second_trimester_2_7 = request.POST.get("value_second_trimester_2_7")
        value_third_trimester_2_7 = request.POST.get("value_third_trimester_2_7")
        value_fourth_trimester_2_7 = request.POST.get("value_fourth_trimester_2_7")

        project_name_2_8 = request.POST.get("project_name_2_8")
        city_2_8 = request.POST.get("city_2_8")
        total_number_project_2_8 = request.POST.get("total_number_project_2_8")
        total_cost_2_8 = request.POST.get("total_cost_2_8")
        start_date_2_8 = request.POST.get("start_date_2_8")
        end_date_2_8 = request.POST.get("end_date_2_8")
        value_first_trimester_2_8 = request.POST.get("value_first_trimester_2_8")
        value_second_trimester_2_8 = request.POST.get("value_second_trimester_2_8")
        value_third_trimester_2_8 = request.POST.get("value_third_trimester_2_8")
        value_fourth_trimester_2_8 = request.POST.get("value_fourth_trimester_2_8")

        project_name_2_9 = request.POST.get("project_name_2_9")
        city_2_9 = request.POST.get("city_2_9")
        total_number_project_2_9 = request.POST.get("total_number_project_2_9")
        total_cost_2_9 = request.POST.get("total_cost_2_9")
        start_date_2_9 = request.POST.get("start_date_2_9")
        end_date_2_9 = request.POST.get("end_date_2_9")
        value_first_trimester_2_9 = request.POST.get("value_first_trimester_2_9")
        value_second_trimester_2_9 = request.POST.get("value_second_trimester_2_9")
        value_third_trimester_2_9 = request.POST.get("value_third_trimester_2_9")
        value_fourth_trimester_2_9 = request.POST.get("value_fourth_trimester_2_9")

        project_name_2_10 = request.POST.get("project_name_2_10")
        city_2_10 = request.POST.get("city_2_10")
        total_number_project_2_10 = request.POST.get("total_number_project_2_10")
        total_cost_2_10 = request.POST.get("total_cost_2_10")
        start_date_2_10 = request.POST.get("start_date_2_10")
        end_date_2_10 = request.POST.get("end_date_2_10")
        value_first_trimester_2_10 = request.POST.get("value_first_trimester_2_10")
        value_second_trimester_2_10 = request.POST.get("value_second_trimester_2_10")
        value_third_trimester_2_10 = request.POST.get("value_third_trimester_2_10")
        value_fourth_trimester_2_10 = request.POST.get("value_fourth_trimester_2_10")

        # TABLE 3
        encuesta_3 = request.POST.get("encuesta_3")
        fiscal_year_3 = request.POST.get("fiscal_year_3")
        company_name_3 = request.POST.get("company_name_3")
        liaison_officer_3 = request.POST.get("liaison_officer_3")
        tel_3 = request.POST.get("tel_3")
        project_3 = request.POST.get("project_3")
        branches_3 = request.POST.get("branches_3")

        project_name_3_1 = request.POST.get("project_name_3_1")
        city_3_1 = request.POST.get("city_3_1")
        total_number_project_3_1 = request.POST.get("total_number_project_3_1")
        total_cost_3_1 = request.POST.get("total_cost_3_1")
        start_date_3_1 = request.POST.get("start_date_3_1")
        end_date_3_1 = request.POST.get("end_date_3_1")
        value_first_trimester_3_1 = request.POST.get("value_first_trimester_3_1")
        value_second_trimester_3_1 = request.POST.get("value_second_trimester_3_1")
        value_third_trimester_3_1 = request.POST.get("value_third_trimester_3_1")
        value_fourth_trimester_3_1 = request.POST.get("value_fourth_trimester_3_1")

        project_name_3_2 = request.POST.get("project_name_3_2")
        city_3_2 = request.POST.get("city_3_2")
        total_number_project_3_2 = request.POST.get("total_number_project_3_2")
        total_cost_3_2 = request.POST.get("total_cost_3_2")
        start_date_3_2 = request.POST.get("start_date_3_2")
        end_date_3_2 = request.POST.get("end_date_3_2")
        value_first_trimester_3_2 = request.POST.get("value_first_trimester_3_2")
        value_second_trimester_3_2 = request.POST.get("value_second_trimester_3_2")
        value_third_trimester_3_2 = request.POST.get("value_third_trimester_3_2")
        value_fourth_trimester_3_2 = request.POST.get("value_fourth_trimester_3_2")

        project_name_3_3 = request.POST.get("project_name_3_3")
        city_3_3 = request.POST.get("city_3_3")
        total_number_project_3_3 = request.POST.get("total_number_project_3_3")
        total_cost_3_3 = request.POST.get("total_cost_3_3")
        start_date_3_3 = request.POST.get("start_date_3_3")
        end_date_3_3 = request.POST.get("end_date_3_3")
        value_first_trimester_3_3 = request.POST.get("value_first_trimester_3_3")
        value_second_trimester_3_3 = request.POST.get("value_second_trimester_3_3")
        value_third_trimester_3_3 = request.POST.get("value_third_trimester_3_3")
        value_fourth_trimester_3_3 = request.POST.get("value_fourth_trimester_3_3")

        project_name_3_4 = request.POST.get("project_name_3_4")
        city_3_4 = request.POST.get("city_3_4")
        total_number_project_3_4 = request.POST.get("total_number_project_3_4")
        total_cost_3_4 = request.POST.get("total_cost_3_4")
        start_date_3_4 = request.POST.get("start_date_3_4")
        end_date_3_4 = request.POST.get("end_date_3_4")
        value_first_trimester_3_4 = request.POST.get("value_first_trimester_3_4")
        value_second_trimester_3_4 = request.POST.get("value_second_trimester_3_4")
        value_third_trimester_3_4 = request.POST.get("value_third_trimester_3_4")
        value_fourth_trimester_3_4 = request.POST.get("value_fourth_trimester_3_4")

        project_name_3_5 = request.POST.get("project_name_3_5")
        city_3_5 = request.POST.get("city_3_5")
        total_number_project_3_5 = request.POST.get("total_number_project_3_5")
        total_cost_3_5 = request.POST.get("total_cost_3_5")
        start_date_3_5 = request.POST.get("start_date_3_5")
        end_date_3_5 = request.POST.get("end_date_3_5")
        value_first_trimester_3_5 = request.POST.get("value_first_trimester_3_5")
        value_second_trimester_3_5 = request.POST.get("value_second_trimester_3_5")
        value_third_trimester_3_5 = request.POST.get("value_third_trimester_3_5")
        value_fourth_trimester_3_5 = request.POST.get("value_fourth_trimester_3_5")

        project_name_3_6 = request.POST.get("project_name_3_6")
        city_3_6 = request.POST.get("city_3_6")
        total_number_project_3_6 = request.POST.get("total_number_project_3_6")
        total_cost_3_6 = request.POST.get("total_cost_3_6")
        start_date_3_6 = request.POST.get("start_date_3_6")
        end_date_3_6 = request.POST.get("end_date_3_6")
        value_first_trimester_3_6 = request.POST.get("value_first_trimester_3_6")
        value_second_trimester_3_6 = request.POST.get("value_second_trimester_3_6")
        value_third_trimester_3_6 = request.POST.get("value_third_trimester_3_6")
        value_fourth_trimester_3_6 = request.POST.get("value_fourth_trimester_3_6")

        project_name_3_7 = request.POST.get("project_name_3_7")
        city_3_7 = request.POST.get("city_3_7")
        total_number_project_3_7 = request.POST.get("total_number_project_3_7")
        total_cost_3_7 = request.POST.get("total_cost_3_7")
        start_date_3_7 = request.POST.get("start_date_3_7")
        end_date_3_7 = request.POST.get("end_date_3_7")
        value_first_trimester_3_7 = request.POST.get("value_first_trimester_3_7")
        value_second_trimester_3_7 = request.POST.get("value_second_trimester_3_7")
        value_third_trimester_3_7 = request.POST.get("value_third_trimester_3_7")
        value_fourth_trimester_3_7 = request.POST.get("value_fourth_trimester_3_7")

        project_name_3_8 = request.POST.get("project_name_3_8")
        city_3_8 = request.POST.get("city_3_8")
        total_number_project_3_8 = request.POST.get("total_number_project_3_8")
        total_cost_3_8 = request.POST.get("total_cost_3_8")
        start_date_3_8 = request.POST.get("start_date_3_8")
        end_date_3_8 = request.POST.get("end_date_3_8")
        value_first_trimester_3_8 = request.POST.get("value_first_trimester_3_8")
        value_second_trimester_3_8 = request.POST.get("value_second_trimester_3_8")
        value_third_trimester_3_8 = request.POST.get("value_third_trimester_3_8")
        value_fourth_trimester_3_8 = request.POST.get("value_fourth_trimester_3_8")

        project_name_3_9 = request.POST.get("project_name_3_9")
        city_3_9 = request.POST.get("city_3_9")
        total_number_project_3_9 = request.POST.get("total_number_project_3_9")
        total_cost_3_9 = request.POST.get("total_cost_3_9")
        start_date_3_9 = request.POST.get("start_date_3_9")
        end_date_3_9 = request.POST.get("end_date_3_9")
        value_first_trimester_3_9 = request.POST.get("value_first_trimester_3_9")
        value_second_trimester_3_9 = request.POST.get("value_second_trimester_3_9")
        value_third_trimester_3_9 = request.POST.get("value_third_trimester_3_9")
        value_fourth_trimester_3_9 = request.POST.get("value_fourth_trimester_3_9")

        project_name_3_10 = request.POST.get("project_name_3_10")
        city_3_10 = request.POST.get("city_3_10")
        total_number_project_3_10 = request.POST.get("total_number_project_3_10")
        total_cost_3_10 = request.POST.get("total_cost_3_10")
        start_date_3_10 = request.POST.get("start_date_3_10")
        end_date_3_10 = request.POST.get("end_date_3_10")
        value_first_trimester_3_10 = request.POST.get("value_first_trimester_3_10")
        value_second_trimester_3_10 = request.POST.get("value_second_trimester_3_10")
        value_third_trimester_3_10 = request.POST.get("value_third_trimester_3_10")
        value_fourth_trimester_3_10 = request.POST.get("value_fourth_trimester_3_10")

        # TABLE 4
        encuesta_4 = request.POST.get("encuesta_4")
        fiscal_year_4 = request.POST.get("fiscal_year_4")
        company_name_4 = request.POST.get("company_name_4")
        liaison_officer_4 = request.POST.get("liaison_officer_4")
        tel_4 = request.POST.get("tel_4")
        project_4 = request.POST.get("project_4")
        branches_4 = request.POST.get("branches_4")

        project_name_4_1 = request.POST.get("project_name_4_1")
        city_4_1 = request.POST.get("city_4_1")
        total_number_project_4_1 = request.POST.get("total_number_project_4_1")
        total_cost_4_1 = request.POST.get("total_cost_4_1")
        start_date_4_1 = request.POST.get("start_date_4_1")
        end_date_4_1 = request.POST.get("end_date_4_1")
        value_first_trimester_4_1 = request.POST.get("value_first_trimester_4_1")
        value_second_trimester_4_1 = request.POST.get("value_second_trimester_4_1")
        value_third_trimester_4_1 = request.POST.get("value_third_trimester_4_1")
        value_fourth_trimester_4_1 = request.POST.get("value_fourth_trimester_4_1")

        project_name_4_2 = request.POST.get("project_name_4_2")
        city_4_2 = request.POST.get("city_4_2")
        total_number_project_4_2 = request.POST.get("total_number_project_4_2")
        total_cost_4_2 = request.POST.get("total_cost_4_2")
        start_date_4_2 = request.POST.get("start_date_4_2")
        end_date_4_2 = request.POST.get("end_date_4_2")
        value_first_trimester_4_2 = request.POST.get("value_first_trimester_4_2")
        value_second_trimester_4_2 = request.POST.get("value_second_trimester_4_2")
        value_third_trimester_4_2 = request.POST.get("value_third_trimester_4_2")
        value_fourth_trimester_4_2 = request.POST.get("value_fourth_trimester_4_2")

        project_name_4_3 = request.POST.get("project_name_4_3")
        city_4_3 = request.POST.get("city_4_3")
        total_number_project_4_3 = request.POST.get("total_number_project_4_3")
        total_cost_4_3 = request.POST.get("total_cost_4_3")
        start_date_4_3 = request.POST.get("start_date_4_3")
        end_date_4_3 = request.POST.get("end_date_4_3")
        value_first_trimester_4_3 = request.POST.get("value_first_trimester_4_3")
        value_second_trimester_4_3 = request.POST.get("value_second_trimester_4_3")
        value_third_trimester_4_3 = request.POST.get("value_third_trimester_4_3")
        value_fourth_trimester_4_3 = request.POST.get("value_fourth_trimester_4_3")

        project_name_4_4 = request.POST.get("project_name_4_4")
        city_4_4 = request.POST.get("city_4_4")
        total_number_project_4_4 = request.POST.get("total_number_project_4_4")
        total_cost_4_4 = request.POST.get("total_cost_4_4")
        start_date_4_4 = request.POST.get("start_date_4_4")
        end_date_4_4 = request.POST.get("end_date_4_4")
        value_first_trimester_4_4 = request.POST.get("value_first_trimester_4_4")
        value_second_trimester_4_4 = request.POST.get("value_second_trimester_4_4")
        value_third_trimester_4_4 = request.POST.get("value_third_trimester_4_4")
        value_fourth_trimester_4_4 = request.POST.get("value_fourth_trimester_4_4")

        project_name_4_5 = request.POST.get("project_name_4_5")
        city_4_5 = request.POST.get("city_4_5")
        total_number_project_4_5 = request.POST.get("total_number_project_4_5")
        total_cost_4_5 = request.POST.get("total_cost_4_5")
        start_date_4_5 = request.POST.get("start_date_4_5")
        end_date_4_5 = request.POST.get("end_date_4_5")
        value_first_trimester_4_5 = request.POST.get("value_first_trimester_4_5")
        value_second_trimester_4_5 = request.POST.get("value_second_trimester_4_5")
        value_third_trimester_4_5 = request.POST.get("value_third_trimester_4_5")
        value_fourth_trimester_4_5 = request.POST.get("value_fourth_trimester_4_5")

        project_name_4_6 = request.POST.get("project_name_4_6")
        city_4_6 = request.POST.get("city_4_6")
        total_number_project_4_6 = request.POST.get("total_number_project_4_6")
        total_cost_4_6 = request.POST.get("total_cost_4_6")
        start_date_4_6 = request.POST.get("start_date_4_6")
        end_date_4_6 = request.POST.get("end_date_4_6")
        value_first_trimester_4_6 = request.POST.get("value_first_trimester_4_6")
        value_second_trimester_4_6 = request.POST.get("value_second_trimester_4_6")
        value_third_trimester_4_6 = request.POST.get("value_third_trimester_4_6")
        value_fourth_trimester_4_6 = request.POST.get("value_fourth_trimester_4_6")

        project_name_4_7 = request.POST.get("project_name_4_7")
        city_4_7 = request.POST.get("city_4_7")
        total_number_project_4_7 = request.POST.get("total_number_project_4_7")
        total_cost_4_7 = request.POST.get("total_cost_4_7")
        start_date_4_7 = request.POST.get("start_date_4_7")
        end_date_4_7 = request.POST.get("end_date_4_7")
        value_first_trimester_4_7 = request.POST.get("value_first_trimester_4_7")
        value_second_trimester_4_7 = request.POST.get("value_second_trimester_4_7")
        value_third_trimester_4_7 = request.POST.get("value_third_trimester_4_7")
        value_fourth_trimester_4_7 = request.POST.get("value_fourth_trimester_4_7")

        project_name_4_8 = request.POST.get("project_name_4_8")
        city_4_8 = request.POST.get("city_4_8")
        total_number_project_4_8 = request.POST.get("total_number_project_4_8")
        total_cost_4_8 = request.POST.get("total_cost_4_8")
        start_date_4_8 = request.POST.get("start_date_4_8")
        end_date_4_8 = request.POST.get("end_date_4_8")
        value_first_trimester_4_8 = request.POST.get("value_first_trimester_4_8")
        value_second_trimester_4_8 = request.POST.get("value_second_trimester_4_8")
        value_third_trimester_4_8 = request.POST.get("value_third_trimester_4_8")
        value_fourth_trimester_4_8 = request.POST.get("value_fourth_trimester_4_8")

        project_name_4_9 = request.POST.get("project_name_4_9")
        city_4_9 = request.POST.get("city_4_9")
        total_number_project_4_9 = request.POST.get("total_number_project_4_9")
        total_cost_4_9 = request.POST.get("total_cost_4_9")
        start_date_4_9 = request.POST.get("start_date_4_9")
        end_date_4_9 = request.POST.get("end_date_4_9")
        value_first_trimester_4_9 = request.POST.get("value_first_trimester_4_9")
        value_second_trimester_4_9 = request.POST.get("value_second_trimester_4_9")
        value_third_trimester_4_9 = request.POST.get("value_third_trimester_4_9")
        value_fourth_trimester_4_9 = request.POST.get("value_fourth_trimester_4_9")

        project_name_4_10 = request.POST.get("project_name_4_10")
        city_4_10 = request.POST.get("city_4_10")
        total_number_project_4_10 = request.POST.get("total_number_project_4_10")
        total_cost_4_10 = request.POST.get("total_cost_4_10")
        start_date_4_10 = request.POST.get("start_date_4_10")
        end_date_4_10 = request.POST.get("end_date_4_10")
        value_first_trimester_4_10 = request.POST.get("value_first_trimester_4_10")
        value_second_trimester_4_10 = request.POST.get("value_second_trimester_4_10")
        value_third_trimester_4_10 = request.POST.get("value_third_trimester_4_10")
        value_fourth_trimester_4_10 = request.POST.get("value_fourth_trimester_4_10")

        csv_file_path = "data/cuestionarios/construcción/JP-541.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, "a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "encuesta_1",
                        "fiscal_year_1",
                        "company_name_1",
                        "liaison_officer_1",
                        "tel_1",
                        "project_1",
                        "branches_1",
                        "project_name_1_1",
                        "city_1_1",
                        "total_number_project_1_1",
                        "total_cost_1_1",
                        "start_date_1_1",
                        "end_date_1_1",
                        "value_first_trimester_1_1",
                        "value_second_trimester_1_1",
                        "value_third_trimester_1_1",
                        "value_fourth_trimester_1_1",
                        "project_name_1_2",
                        "city_1_2",
                        "total_number_project_1_2",
                        "total_cost_1_2",
                        "start_date_1_2",
                        "end_date_1_2",
                        "value_first_trimester_1_2",
                        "value_second_trimester_1_2",
                        "value_third_trimester_1_2",
                        "value_fourth_trimester_1_2",
                        "project_name_1_3",
                        "city_1_3",
                        "total_number_project_1_3",
                        "total_cost_1_3",
                        "start_date_1_3",
                        "end_date_1_3",
                        "value_first_trimester_1_3",
                        "value_second_trimester_1_3",
                        "value_third_trimester_1_3",
                        "value_fourth_trimester_1_3",
                        "project_name_1_4",
                        "city_1_4",
                        "total_number_project_1_4",
                        "total_cost_1_4",
                        "start_date_1_4",
                        "end_date_1_4",
                        "value_first_trimester_1_4",
                        "value_second_trimester_1_4",
                        "value_third_trimester_1_4",
                        "value_fourth_trimester_1_4",
                        "project_name_1_5",
                        "city_1_5",
                        "total_number_project_1_5",
                        "total_cost_1_5",
                        "start_date_1_5",
                        "end_date_1_5",
                        "value_first_trimester_1_5",
                        "value_second_trimester_1_5",
                        "value_third_trimester_1_5",
                        "value_fourth_trimester_1_5",
                        "project_name_1_6",
                        "city_1_6",
                        "total_number_project_1_6",
                        "total_cost_1_6",
                        "start_date_1_6",
                        "end_date_1_6",
                        "value_first_trimester_1_6",
                        "value_second_trimester_1_6",
                        "value_third_trimester_1_6",
                        "value_fourth_trimester_1_6",
                        "project_name_1_7",
                        "city_1_7",
                        "total_number_project_1_7",
                        "total_cost_1_7",
                        "start_date_1_7",
                        "end_date_1_7",
                        "value_first_trimester_1_7",
                        "value_second_trimester_1_7",
                        "value_third_trimester_1_7",
                        "value_fourth_trimester_1_7",
                        "project_name_1_8",
                        "city_1_8",
                        "total_number_project_1_8",
                        "total_cost_1_8",
                        "start_date_1_8",
                        "end_date_1_8",
                        "value_first_trimester_1_8",
                        "value_second_trimester_1_8",
                        "value_third_trimester_1_8",
                        "value_fourth_trimester_1_8",
                        "project_name_1_9",
                        "city_1_9",
                        "total_number_project_1_9",
                        "total_cost_1_9",
                        "start_date_1_9",
                        "end_date_1_9",
                        "value_first_trimester_1_9",
                        "value_second_trimester_1_9",
                        "value_third_trimester_1_9",
                        "value_fourth_trimester_1_9",
                        "project_name_1_10",
                        "city_1_10",
                        "total_number_project_1_10",
                        "total_cost_1_10",
                        "start_date_1_10",
                        "end_date_1_10",
                        "value_first_trimester_1_10",
                        "value_second_trimester_1_10",
                        "value_third_trimester_1_10",
                        "value_fourth_trimester_1_10",
                        "encuesta_2",
                        "fiscal_year_2",
                        "company_name_2",
                        "liaison_officer_2",
                        "tel_2",
                        "project_2",
                        "branches_2",
                        "project_name_2_1",
                        "city_2_1",
                        "total_number_project_2_1",
                        "total_cost_2_1",
                        "start_date_2_1",
                        "end_date_2_1",
                        "value_first_trimester_2_1",
                        "value_second_trimester_2_1",
                        "value_third_trimester_2_1",
                        "value_fourth_trimester_2_1",
                        "project_name_2_2",
                        "city_2_2",
                        "total_number_project_2_2",
                        "total_cost_2_2",
                        "start_date_2_2",
                        "end_date_2_2",
                        "value_first_trimester_2_2",
                        "value_second_trimester_2_2",
                        "value_third_trimester_2_2",
                        "value_fourth_trimester_2_2",
                        "project_name_2_3",
                        "city_2_3",
                        "total_number_project_2_3",
                        "total_cost_2_3",
                        "start_date_2_3",
                        "end_date_2_3",
                        "value_first_trimester_2_3",
                        "value_second_trimester_2_3",
                        "value_third_trimester_2_3",
                        "value_fourth_trimester_2_3",
                        "project_name_2_4",
                        "city_2_4",
                        "total_number_project_2_4",
                        "total_cost_2_4",
                        "start_date_2_4",
                        "end_date_2_4",
                        "value_first_trimester_2_4",
                        "value_second_trimester_2_4",
                        "value_third_trimester_2_4",
                        "value_fourth_trimester_2_4",
                        "project_name_2_5",
                        "city_2_5",
                        "total_number_project_2_5",
                        "total_cost_2_5",
                        "start_date_2_5",
                        "end_date_2_5",
                        "value_first_trimester_2_5",
                        "value_second_trimester_2_5",
                        "value_third_trimester_2_5",
                        "value_fourth_trimester_2_5",
                        "project_name_2_6",
                        "city_2_6",
                        "total_number_project_2_6",
                        "total_cost_2_6",
                        "start_date_2_6",
                        "end_date_2_6",
                        "value_first_trimester_2_6",
                        "value_second_trimester_2_6",
                        "value_third_trimester_2_6",
                        "value_fourth_trimester_2_6",
                        "project_name_2_7",
                        "city_2_7",
                        "total_number_project_2_7",
                        "total_cost_2_7",
                        "start_date_2_7",
                        "end_date_2_7",
                        "value_first_trimester_2_7",
                        "value_second_trimester_2_7",
                        "value_third_trimester_2_7",
                        "value_fourth_trimester_2_7",
                        "project_name_2_8",
                        "city_2_8",
                        "total_number_project_2_8",
                        "total_cost_2_8",
                        "start_date_2_8",
                        "end_date_2_8",
                        "value_first_trimester_2_8",
                        "value_second_trimester_2_8",
                        "value_third_trimester_2_8",
                        "value_fourth_trimester_2_8",
                        "project_name_2_9",
                        "city_2_9",
                        "total_number_project_2_9",
                        "total_cost_2_9",
                        "start_date_2_9",
                        "end_date_2_9",
                        "value_first_trimester_2_9",
                        "value_second_trimester_2_9",
                        "value_third_trimester_2_9",
                        "value_fourth_trimester_2_9",
                        "project_name_2_10",
                        "city_2_10",
                        "total_number_project_2_10",
                        "total_cost_2_10",
                        "start_date_2_10",
                        "end_date_2_10",
                        "value_first_trimester_2_10",
                        "value_second_trimester_2_10",
                        "value_third_trimester_2_10",
                        "value_fourth_trimester_2_10",
                        "encuesta_3",
                        "fiscal_year_3",
                        "company_name_3",
                        "liaison_officer_3",
                        "tel_3",
                        "project_3",
                        "branches_3",
                        "project_name_3_1",
                        "city_3_1",
                        "total_number_project_3_1",
                        "total_cost_3_1",
                        "start_date_3_1",
                        "end_date_3_1",
                        "value_first_trimester_3_1",
                        "value_second_trimester_3_1",
                        "value_third_trimester_3_1",
                        "value_fourth_trimester_3_1",
                        "project_name_3_2",
                        "city_3_2",
                        "total_number_project_3_2",
                        "total_cost_3_2",
                        "start_date_3_2",
                        "end_date_3_2",
                        "value_first_trimester_3_2",
                        "value_second_trimester_3_2",
                        "value_third_trimester_3_2",
                        "value_fourth_trimester_3_2",
                        "project_name_3_3",
                        "city_3_3",
                        "total_number_project_3_3",
                        "total_cost_3_3",
                        "start_date_3_3",
                        "end_date_3_3",
                        "value_first_trimester_3_3",
                        "value_second_trimester_3_3",
                        "value_third_trimester_3_3",
                        "value_fourth_trimester_3_3",
                        "project_name_3_4",
                        "city_3_4",
                        "total_number_project_3_4",
                        "total_cost_3_4",
                        "start_date_3_4",
                        "end_date_3_4",
                        "value_first_trimester_3_4",
                        "value_second_trimester_3_4",
                        "value_third_trimester_3_4",
                        "value_fourth_trimester_3_4",
                        "project_name_3_5",
                        "city_3_5",
                        "total_number_project_3_5",
                        "total_cost_3_5",
                        "start_date_3_5",
                        "end_date_3_5",
                        "value_first_trimester_3_5",
                        "value_second_trimester_3_5",
                        "value_third_trimester_3_5",
                        "value_fourth_trimester_3_5",
                        "project_name_3_6",
                        "city_3_6",
                        "total_number_project_3_6",
                        "total_cost_3_6",
                        "start_date_3_6",
                        "end_date_3_6",
                        "value_first_trimester_3_6",
                        "value_second_trimester_3_6",
                        "value_third_trimester_3_6",
                        "value_fourth_trimester_3_6",
                        "project_name_3_7",
                        "city_3_7",
                        "total_number_project_3_7",
                        "total_cost_3_7",
                        "start_date_3_7",
                        "end_date_3_7",
                        "value_first_trimester_3_7",
                        "value_second_trimester_3_7",
                        "value_third_trimester_3_7",
                        "value_fourth_trimester_3_7",
                        "project_name_3_8",
                        "city_3_8",
                        "total_number_project_3_8",
                        "total_cost_3_8",
                        "start_date_3_8",
                        "end_date_3_8",
                        "value_first_trimester_3_8",
                        "value_second_trimester_3_8",
                        "value_third_trimester_3_8",
                        "value_fourth_trimester_3_8",
                        "project_name_3_9",
                        "city_3_9",
                        "total_number_project_3_9",
                        "total_cost_3_9",
                        "start_date_3_9",
                        "end_date_3_9",
                        "value_first_trimester_3_9",
                        "value_second_trimester_3_9",
                        "value_third_trimester_3_9",
                        "value_fourth_trimester_3_9",
                        "project_name_3_10",
                        "city_3_10",
                        "total_number_project_3_10",
                        "total_cost_3_10",
                        "start_date_3_10",
                        "end_date_3_10",
                        "value_first_trimester_3_10",
                        "value_second_trimester_3_10",
                        "value_third_trimester_3_10",
                        "value_fourth_trimester_3_10",
                        "encuesta_4",
                        "trimestre_4",
                        "company_name_4",
                        "liaison_officer_4",
                        "tel_4",
                        "project_4",
                        "branches_4",
                        "project_name_4_1",
                        "city_4_1",
                        "total_number_project_4_1",
                        "total_cost_4_1",
                        "start_date_4_1",
                        "end_date_4_1",
                        "value_first_trimester_4_1",
                        "value_second_trimester_4_1",
                        "value_third_trimester_4_1",
                        "value_fourth_trimester_4_1",
                        "project_name_4_2",
                        "city_4_2",
                        "total_number_project_4_2",
                        "total_cost_4_2",
                        "start_date_4_2",
                        "end_date_4_2",
                        "value_first_trimester_4_2",
                        "value_second_trimester_4_2",
                        "value_third_trimester_4_2",
                        "value_fourth_trimester_4_2",
                        "project_name_4_3",
                        "city_4_3",
                        "total_number_project_4_3",
                        "total_cost_4_3",
                        "start_date_4_3",
                        "end_date_4_3",
                        "value_first_trimester_4_3",
                        "value_second_trimester_4_3",
                        "value_third_trimester_4_3",
                        "value_fourth_trimester_4_3",
                        "project_name_4_4",
                        "city_4_4",
                        "total_number_project_4_4",
                        "total_cost_4_4",
                        "start_date_4_4",
                        "end_date_4_4",
                        "value_first_trimester_4_4",
                        "value_second_trimester_4_4",
                        "value_third_trimester_4_4",
                        "value_fourth_trimester_4_4",
                        "project_name_4_5",
                        "city_4_5",
                        "total_number_project_4_5",
                        "total_cost_4_5",
                        "start_date_4_5",
                        "end_date_4_5",
                        "value_first_trimester_4_5",
                        "value_second_trimester_4_5",
                        "value_third_trimester_4_5",
                        "value_fourth_trimester_4_5",
                        "project_name_4_6",
                        "city_4_6",
                        "total_number_project_4_6",
                        "total_cost_4_6",
                        "start_date_4_6",
                        "end_date_4_6",
                        "value_first_trimester_4_6",
                        "value_second_trimester_4_6",
                        "value_third_trimester_4_6",
                        "value_fourth_trimester_4_6",
                        "project_name_4_7",
                        "city_4_7",
                        "total_number_project_4_7",
                        "total_cost_4_7",
                        "start_date_4_7",
                        "end_date_4_7",
                        "value_first_trimester_4_7",
                        "value_second_trimester_4_7",
                        "value_third_trimester_4_7",
                        "value_fourth_trimester_4_7",
                        "project_name_4_8",
                        "city_4_8",
                        "total_number_project_4_8",
                        "total_cost_4_8",
                        "start_date_4_8",
                        "end_date_4_8",
                        "value_first_trimester_4_8",
                        "value_second_trimester_4_8",
                        "value_third_trimester_4_8",
                        "value_fourth_trimester_4_8",
                        "project_name_4_9",
                        "city_4_9",
                        "total_number_project_4_9",
                        "total_cost_4_9",
                        "start_date_4_9",
                        "end_date_4_9",
                        "value_first_trimester_4_9",
                        "value_second_trimester_4_9",
                        "value_third_trimester_4_9",
                        "value_fourth_trimester_4_9",
                        "project_name_4_10",
                        "city_4_10",
                        "total_number_project_4_10",
                        "total_cost_4_10",
                        "start_date_4_10",
                        "end_date_4_10",
                        "value_first_trimester_4_10",
                        "value_second_trimester_4_10",
                        "value_third_trimester_4_10",
                        "value_fourth_trimester_4_10",
                    ]
                )

            writer.writerow(
                [
                    encuesta_1,
                    fiscal_year_1,
                    company_name_1,
                    liaison_officer_1,
                    tel_1,
                    project_1,
                    branches_1,
                    project_name_1_1,
                    city_1_1,
                    total_number_project_1_1,
                    total_cost_1_1,
                    start_date_1_1,
                    end_date_1_1,
                    value_first_trimester_1_1,
                    value_second_trimester_1_1,
                    value_third_trimester_1_1,
                    value_fourth_trimester_1_1,
                    project_name_1_2,
                    city_1_2,
                    total_number_project_1_2,
                    total_cost_1_2,
                    start_date_1_2,
                    end_date_1_2,
                    value_first_trimester_1_2,
                    value_second_trimester_1_2,
                    value_third_trimester_1_2,
                    value_fourth_trimester_1_2,
                    project_name_1_3,
                    city_1_3,
                    total_number_project_1_3,
                    total_cost_1_3,
                    start_date_1_3,
                    end_date_1_3,
                    value_first_trimester_1_3,
                    value_second_trimester_1_3,
                    value_third_trimester_1_3,
                    value_fourth_trimester_1_3,
                    project_name_1_4,
                    city_1_4,
                    total_number_project_1_4,
                    total_cost_1_4,
                    start_date_1_4,
                    end_date_1_4,
                    value_first_trimester_1_4,
                    value_second_trimester_1_4,
                    value_third_trimester_1_4,
                    value_fourth_trimester_1_4,
                    project_name_1_5,
                    city_1_5,
                    total_number_project_1_5,
                    total_cost_1_5,
                    start_date_1_5,
                    end_date_1_5,
                    value_first_trimester_1_5,
                    value_second_trimester_1_5,
                    value_third_trimester_1_5,
                    value_fourth_trimester_1_5,
                    project_name_1_6,
                    city_1_6,
                    total_number_project_1_6,
                    total_cost_1_6,
                    start_date_1_6,
                    end_date_1_6,
                    value_first_trimester_1_6,
                    value_second_trimester_1_6,
                    value_third_trimester_1_6,
                    value_fourth_trimester_1_6,
                    project_name_1_7,
                    city_1_7,
                    total_number_project_1_7,
                    total_cost_1_7,
                    start_date_1_7,
                    end_date_1_7,
                    value_first_trimester_1_7,
                    value_second_trimester_1_7,
                    value_third_trimester_1_7,
                    value_fourth_trimester_1_7,
                    project_name_1_8,
                    city_1_8,
                    total_number_project_1_8,
                    total_cost_1_8,
                    start_date_1_8,
                    end_date_1_8,
                    value_first_trimester_1_8,
                    value_second_trimester_1_8,
                    value_third_trimester_1_8,
                    value_fourth_trimester_1_8,
                    project_name_1_9,
                    city_1_9,
                    total_number_project_1_9,
                    total_cost_1_9,
                    start_date_1_9,
                    end_date_1_9,
                    value_first_trimester_1_9,
                    value_second_trimester_1_9,
                    value_third_trimester_1_9,
                    value_fourth_trimester_1_9,
                    project_name_1_10,
                    city_1_10,
                    total_number_project_1_10,
                    total_cost_1_10,
                    start_date_1_10,
                    end_date_1_10,
                    value_first_trimester_1_10,
                    value_second_trimester_1_10,
                    value_third_trimester_1_10,
                    value_fourth_trimester_1_10,
                    encuesta_2,
                    fiscal_year_2,
                    company_name_2,
                    liaison_officer_2,
                    tel_2,
                    project_2,
                    branches_2,
                    project_name_2_1,
                    city_2_1,
                    total_number_project_2_1,
                    total_cost_2_1,
                    start_date_2_1,
                    end_date_2_1,
                    value_first_trimester_2_1,
                    value_second_trimester_2_1,
                    value_third_trimester_2_1,
                    value_fourth_trimester_2_1,
                    project_name_2_2,
                    city_2_2,
                    total_number_project_2_2,
                    total_cost_2_2,
                    start_date_2_2,
                    end_date_2_2,
                    value_first_trimester_2_2,
                    value_second_trimester_2_2,
                    value_third_trimester_2_2,
                    value_fourth_trimester_2_2,
                    project_name_2_3,
                    city_2_3,
                    total_number_project_2_3,
                    total_cost_2_3,
                    start_date_2_3,
                    end_date_2_3,
                    value_first_trimester_2_3,
                    value_second_trimester_2_3,
                    value_third_trimester_2_3,
                    value_fourth_trimester_2_3,
                    project_name_2_4,
                    city_2_4,
                    total_number_project_2_4,
                    total_cost_2_4,
                    start_date_2_4,
                    end_date_2_4,
                    value_first_trimester_2_4,
                    value_second_trimester_2_4,
                    value_third_trimester_2_4,
                    value_fourth_trimester_2_4,
                    project_name_2_5,
                    city_2_5,
                    total_number_project_2_5,
                    total_cost_2_5,
                    start_date_2_5,
                    end_date_2_5,
                    value_first_trimester_2_5,
                    value_second_trimester_2_5,
                    value_third_trimester_2_5,
                    value_fourth_trimester_2_5,
                    project_name_2_6,
                    city_2_6,
                    total_number_project_2_6,
                    total_cost_2_6,
                    start_date_2_6,
                    end_date_2_6,
                    value_first_trimester_2_6,
                    value_second_trimester_2_6,
                    value_third_trimester_2_6,
                    value_fourth_trimester_2_6,
                    project_name_2_7,
                    city_2_7,
                    total_number_project_2_7,
                    total_cost_2_7,
                    start_date_2_7,
                    end_date_2_7,
                    value_first_trimester_2_7,
                    value_second_trimester_2_7,
                    value_third_trimester_2_7,
                    value_fourth_trimester_2_7,
                    project_name_2_8,
                    city_2_8,
                    total_number_project_2_8,
                    total_cost_2_8,
                    start_date_2_8,
                    end_date_2_8,
                    value_first_trimester_2_8,
                    value_second_trimester_2_8,
                    value_third_trimester_2_8,
                    value_fourth_trimester_2_8,
                    project_name_2_9,
                    city_2_9,
                    total_number_project_2_9,
                    total_cost_2_9,
                    start_date_2_9,
                    end_date_2_9,
                    value_first_trimester_2_9,
                    value_second_trimester_2_9,
                    value_third_trimester_2_9,
                    value_fourth_trimester_2_9,
                    project_name_2_10,
                    city_2_10,
                    total_number_project_2_10,
                    total_cost_2_10,
                    start_date_2_10,
                    end_date_2_10,
                    value_first_trimester_2_10,
                    value_second_trimester_2_10,
                    value_third_trimester_2_10,
                    value_fourth_trimester_2_10,
                    encuesta_3,
                    fiscal_year_3,
                    company_name_3,
                    liaison_officer_3,
                    tel_3,
                    project_3,
                    branches_3,
                    project_name_3_1,
                    city_3_1,
                    total_number_project_3_1,
                    total_cost_3_1,
                    start_date_3_1,
                    end_date_3_1,
                    value_first_trimester_3_1,
                    value_second_trimester_3_1,
                    value_third_trimester_3_1,
                    value_fourth_trimester_3_1,
                    project_name_3_2,
                    city_3_2,
                    total_number_project_3_2,
                    total_cost_3_2,
                    start_date_3_2,
                    end_date_3_2,
                    value_first_trimester_3_2,
                    value_second_trimester_3_2,
                    value_third_trimester_3_2,
                    value_fourth_trimester_3_2,
                    project_name_3_3,
                    city_3_3,
                    total_number_project_3_3,
                    total_cost_3_3,
                    start_date_3_3,
                    end_date_3_3,
                    value_first_trimester_3_3,
                    value_second_trimester_3_3,
                    value_third_trimester_3_3,
                    value_fourth_trimester_3_3,
                    project_name_3_4,
                    city_3_4,
                    total_number_project_3_4,
                    total_cost_3_4,
                    start_date_3_4,
                    end_date_3_4,
                    value_first_trimester_3_4,
                    value_second_trimester_3_4,
                    value_third_trimester_3_4,
                    value_fourth_trimester_3_4,
                    project_name_3_5,
                    city_3_5,
                    total_number_project_3_5,
                    total_cost_3_5,
                    start_date_3_5,
                    end_date_3_5,
                    value_first_trimester_3_5,
                    value_second_trimester_3_5,
                    value_third_trimester_3_5,
                    value_fourth_trimester_3_5,
                    project_name_3_6,
                    city_3_6,
                    total_number_project_3_6,
                    total_cost_3_6,
                    start_date_3_6,
                    end_date_3_6,
                    value_first_trimester_3_6,
                    value_second_trimester_3_6,
                    value_third_trimester_3_6,
                    value_fourth_trimester_3_6,
                    project_name_3_7,
                    city_3_7,
                    total_number_project_3_7,
                    total_cost_3_7,
                    start_date_3_7,
                    end_date_3_7,
                    value_first_trimester_3_7,
                    value_second_trimester_3_7,
                    value_third_trimester_3_7,
                    value_fourth_trimester_3_7,
                    project_name_3_8,
                    city_3_8,
                    total_number_project_3_8,
                    total_cost_3_8,
                    start_date_3_8,
                    end_date_3_8,
                    value_first_trimester_3_8,
                    value_second_trimester_3_8,
                    value_third_trimester_3_8,
                    value_fourth_trimester_3_8,
                    project_name_3_9,
                    city_3_9,
                    total_number_project_3_9,
                    total_cost_3_9,
                    start_date_3_9,
                    end_date_3_9,
                    value_first_trimester_3_9,
                    value_second_trimester_3_9,
                    value_third_trimester_3_9,
                    value_fourth_trimester_3_9,
                    project_name_3_10,
                    city_3_10,
                    total_number_project_3_10,
                    total_cost_3_10,
                    start_date_3_10,
                    end_date_3_10,
                    value_first_trimester_3_10,
                    value_second_trimester_3_10,
                    value_third_trimester_3_10,
                    value_fourth_trimester_3_10,
                    encuesta_4,
                    fiscal_year_4,
                    company_name_4,
                    liaison_officer_4,
                    tel_4,
                    project_4,
                    branches_4,
                    project_name_4_1,
                    city_4_1,
                    total_number_project_4_1,
                    total_cost_4_1,
                    start_date_4_1,
                    end_date_4_1,
                    value_first_trimester_4_1,
                    value_second_trimester_4_1,
                    value_third_trimester_4_1,
                    value_fourth_trimester_4_1,
                    project_name_4_2,
                    city_4_2,
                    total_number_project_4_2,
                    total_cost_4_2,
                    start_date_4_2,
                    end_date_4_2,
                    value_first_trimester_4_2,
                    value_second_trimester_4_2,
                    value_third_trimester_4_2,
                    value_fourth_trimester_4_2,
                    project_name_4_3,
                    city_4_3,
                    total_number_project_4_3,
                    total_cost_4_3,
                    start_date_4_3,
                    end_date_4_3,
                    value_first_trimester_4_3,
                    value_second_trimester_4_3,
                    value_third_trimester_4_3,
                    value_fourth_trimester_4_3,
                    project_name_4_4,
                    city_4_4,
                    total_number_project_4_4,
                    total_cost_4_4,
                    start_date_4_4,
                    end_date_4_4,
                    value_first_trimester_4_4,
                    value_second_trimester_4_4,
                    value_third_trimester_4_4,
                    value_fourth_trimester_4_4,
                    project_name_4_5,
                    city_4_5,
                    total_number_project_4_5,
                    total_cost_4_5,
                    start_date_4_5,
                    end_date_4_5,
                    value_first_trimester_4_5,
                    value_second_trimester_4_5,
                    value_third_trimester_4_5,
                    value_fourth_trimester_4_5,
                    project_name_4_6,
                    city_4_6,
                    total_number_project_4_6,
                    total_cost_4_6,
                    start_date_4_6,
                    end_date_4_6,
                    value_first_trimester_4_6,
                    value_second_trimester_4_6,
                    value_third_trimester_4_6,
                    value_fourth_trimester_4_6,
                    project_name_4_7,
                    city_4_7,
                    total_number_project_4_7,
                    total_cost_4_7,
                    start_date_4_7,
                    end_date_4_7,
                    value_first_trimester_4_7,
                    value_second_trimester_4_7,
                    value_third_trimester_4_7,
                    value_fourth_trimester_4_7,
                    project_name_4_8,
                    city_4_8,
                    total_number_project_4_8,
                    total_cost_4_8,
                    start_date_4_8,
                    end_date_4_8,
                    value_first_trimester_4_8,
                    value_second_trimester_4_8,
                    value_third_trimester_4_8,
                    value_fourth_trimester_4_8,
                    project_name_4_9,
                    city_4_9,
                    total_number_project_4_9,
                    total_cost_4_9,
                    start_date_4_9,
                    end_date_4_9,
                    value_first_trimester_4_9,
                    value_second_trimester_4_9,
                    value_third_trimester_4_9,
                    value_fourth_trimester_4_9,
                    project_name_4_10,
                    city_4_10,
                    total_number_project_4_10,
                    total_cost_4_10,
                    start_date_4_10,
                    end_date_4_10,
                    value_first_trimester_4_10,
                    value_second_trimester_4_10,
                    value_third_trimester_4_10,
                    value_fourth_trimester_4_10,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/construcción/JP-541.csv",
            dtypes={
                "encuesta_1": str,
                "fiscal_year_1": str,
                "company_name_1": str,
                "liaison_officer_1": str,
                "tel_1": str,
                "project_1": str,
                "branches_1": str,
                "project_name_1_1": str,
                "city_1_1": str,
                "total_number_project_1_1": str,
                "total_cost_1_1": str,
                "start_date_1_1": str,
                "end_date_1_1": str,
                "value_first_trimester_1_1": str,
                "value_second_trimester_1_1": str,
                "value_third_trimester_1_1": str,
                "value_fourth_trimester_1_1": str,
                "project_name_1_2": str,
                "city_1_2": str,
                "total_number_project_1_2": str,
                "total_cost_1_2": str,
                "start_date_1_2": str,
                "end_date_1_2": str,
                "value_first_trimester_1_2": str,
                "value_second_trimester_1_2": str,
                "value_third_trimester_1_2": str,
                "value_fourth_trimester_1_2": str,
                "project_name_1_3": str,
                "city_1_3": str,
                "total_number_project_1_3": str,
                "total_cost_1_3": str,
                "start_date_1_3": str,
                "end_date_1_3": str,
                "value_first_trimester_1_3": str,
                "value_second_trimester_1_3": str,
                "value_third_trimester_1_3": str,
                "value_fourth_trimester_1_3": str,
                "project_name_1_4": str,
                "city_1_4": str,
                "total_number_project_1_4": str,
                "total_cost_1_4": str,
                "start_date_1_4": str,
                "end_date_1_4": str,
                "value_first_trimester_1_4": str,
                "value_second_trimester_1_4": str,
                "value_third_trimester_1_4": str,
                "value_fourth_trimester_1_4": str,
                "project_name_1_5": str,
                "city_1_5": str,
                "total_number_project_1_5": str,
                "total_cost_1_5": str,
                "start_date_1_5": str,
                "end_date_1_5": str,
                "value_first_trimester_1_5": str,
                "value_second_trimester_1_5": str,
                "value_third_trimester_1_5": str,
                "value_fourth_trimester_1_5": str,
                "project_name_1_6": str,
                "city_1_6": str,
                "total_number_project_1_6": str,
                "total_cost_1_6": str,
                "start_date_1_6": str,
                "end_date_1_6": str,
                "value_first_trimester_1_6": str,
                "value_second_trimester_1_6": str,
                "value_third_trimester_1_6": str,
                "value_fourth_trimester_1_6": str,
                "project_name_1_7": str,
                "city_1_7": str,
                "total_number_project_1_7": str,
                "total_cost_1_7": str,
                "start_date_1_7": str,
                "end_date_1_7": str,
                "value_first_trimester_1_7": str,
                "value_second_trimester_1_7": str,
                "value_third_trimester_1_7": str,
                "value_fourth_trimester_1_7": str,
                "project_name_1_8": str,
                "city_1_8": str,
                "total_number_project_1_8": str,
                "total_cost_1_8": str,
                "start_date_1_8": str,
                "end_date_1_8": str,
                "value_first_trimester_1_8": str,
                "value_second_trimester_1_8": str,
                "value_third_trimester_1_8": str,
                "value_fourth_trimester_1_8": str,
                "project_name_1_9": str,
                "city_1_9": str,
                "total_number_project_1_9": str,
                "total_cost_1_9": str,
                "start_date_1_9": str,
                "end_date_1_9": str,
                "value_first_trimester_1_9": str,
                "value_second_trimester_1_9": str,
                "value_third_trimester_1_9": str,
                "value_fourth_trimester_1_9": str,
                "project_name_1_10": str,
                "city_1_10": str,
                "total_number_project_1_10": str,
                "total_cost_1_10": str,
                "start_date_1_10": str,
                "end_date_1_10": str,
                "value_first_trimester_1_10": str,
                "value_second_trimester_1_10": str,
                "value_third_trimester_1_10": str,
                "value_fourth_trimester_1_10": str,
                "encuesta_2": str,
                "fiscal_year_2": str,
                "company_name_2": str,
                "liaison_officer_2": str,
                "tel_2": str,
                "project_2": str,
                "branches_2": str,
                "project_name_2_1": str,
                "city_2_1": str,
                "total_number_project_2_1": str,
                "total_cost_2_1": str,
                "start_date_2_1": str,
                "end_date_2_1": str,
                "value_first_trimester_2_1": str,
                "value_second_trimester_2_1": str,
                "value_third_trimester_2_1": str,
                "value_fourth_trimester_2_1": str,
                "project_name_2_2": str,
                "city_2_2": str,
                "total_number_project_2_2": str,
                "total_cost_2_2": str,
                "start_date_2_2": str,
                "end_date_2_2": str,
                "value_first_trimester_2_2": str,
                "value_second_trimester_2_2": str,
                "value_third_trimester_2_2": str,
                "value_fourth_trimester_2_2": str,
                "project_name_2_3": str,
                "city_2_3": str,
                "total_number_project_2_3": str,
                "total_cost_2_3": str,
                "start_date_2_3": str,
                "end_date_2_3": str,
                "value_first_trimester_2_3": str,
                "value_second_trimester_2_3": str,
                "value_third_trimester_2_3": str,
                "value_fourth_trimester_2_3": str,
                "project_name_2_4": str,
                "city_2_4": str,
                "total_number_project_2_4": str,
                "total_cost_2_4": str,
                "start_date_2_4": str,
                "end_date_2_4": str,
                "value_first_trimester_2_4": str,
                "value_second_trimester_2_4": str,
                "value_third_trimester_2_4": str,
                "value_fourth_trimester_2_4": str,
                "project_name_2_5": str,
                "city_2_5": str,
                "total_number_project_2_5": str,
                "total_cost_2_5": str,
                "start_date_2_5": str,
                "end_date_2_5": str,
                "value_first_trimester_2_5": str,
                "value_second_trimester_2_5": str,
                "value_third_trimester_2_5": str,
                "value_fourth_trimester_2_5": str,
                "project_name_2_6": str,
                "city_2_6": str,
                "total_number_project_2_6": str,
                "total_cost_2_6": str,
                "start_date_2_6": str,
                "end_date_2_6": str,
                "value_first_trimester_2_6": str,
                "value_second_trimester_2_6": str,
                "value_third_trimester_2_6": str,
                "value_fourth_trimester_2_6": str,
                "project_name_2_7": str,
                "city_2_7": str,
                "total_number_project_2_7": str,
                "total_cost_2_7": str,
                "start_date_2_7": str,
                "end_date_2_7": str,
                "value_first_trimester_2_7": str,
                "value_second_trimester_2_7": str,
                "value_third_trimester_2_7": str,
                "value_fourth_trimester_2_7": str,
                "project_name_2_8": str,
                "city_2_8": str,
                "total_number_project_2_8": str,
                "total_cost_2_8": str,
                "start_date_2_8": str,
                "end_date_2_8": str,
                "value_first_trimester_2_8": str,
                "value_second_trimester_2_8": str,
                "value_third_trimester_2_8": str,
                "value_fourth_trimester_2_8": str,
                "project_name_2_9": str,
                "city_2_9": str,
                "total_number_project_2_9": str,
                "total_cost_2_9": str,
                "start_date_2_9": str,
                "end_date_2_9": str,
                "value_first_trimester_2_9": str,
                "value_second_trimester_2_9": str,
                "value_third_trimester_2_9": str,
                "value_fourth_trimester_2_9": str,
                "project_name_2_10": str,
                "city_2_10": str,
                "total_number_project_2_10": str,
                "total_cost_2_10": str,
                "start_date_2_10": str,
                "end_date_2_10": str,
                "value_first_trimester_2_10": str,
                "value_second_trimester_2_10": str,
                "value_third_trimester_2_10": str,
                "value_fourth_trimester_2_10": str,
                "encuesta_3": str,
                "fiscal_year_3": str,
                "company_name_3": str,
                "liaison_officer_3": str,
                "tel_3": str,
                "project_3": str,
                "branches_3": str,
                "project_name_3_1": str,
                "city_3_1": str,
                "total_number_project_3_1": str,
                "total_cost_3_1": str,
                "start_date_3_1": str,
                "end_date_3_1": str,
                "value_first_trimester_3_1": str,
                "value_second_trimester_3_1": str,
                "value_third_trimester_3_1": str,
                "value_fourth_trimester_3_1": str,
                "project_name_3_2": str,
                "city_3_2": str,
                "total_number_project_3_2": str,
                "total_cost_3_2": str,
                "start_date_3_2": str,
                "end_date_3_2": str,
                "value_first_trimester_3_2": str,
                "value_second_trimester_3_2": str,
                "value_third_trimester_3_2": str,
                "value_fourth_trimester_3_2": str,
                "project_name_3_3": str,
                "city_3_3": str,
                "total_number_project_3_3": str,
                "total_cost_3_3": str,
                "start_date_3_3": str,
                "end_date_3_3": str,
                "value_first_trimester_3_3": str,
                "value_second_trimester_3_3": str,
                "value_third_trimester_3_3": str,
                "value_fourth_trimester_3_3": str,
                "project_name_3_4": str,
                "city_3_4": str,
                "total_number_project_3_4": str,
                "total_cost_3_4": str,
                "start_date_3_4": str,
                "end_date_3_4": str,
                "value_first_trimester_3_4": str,
                "value_second_trimester_3_4": str,
                "value_third_trimester_3_4": str,
                "value_fourth_trimester_3_4": str,
                "project_name_3_5": str,
                "city_3_5": str,
                "total_number_project_3_5": str,
                "total_cost_3_5": str,
                "start_date_3_5": str,
                "end_date_3_5": str,
                "value_first_trimester_3_5": str,
                "value_second_trimester_3_5": str,
                "value_third_trimester_3_5": str,
                "value_fourth_trimester_3_5": str,
                "project_name_3_6": str,
                "city_3_6": str,
                "total_number_project_3_6": str,
                "total_cost_3_6": str,
                "start_date_3_6": str,
                "end_date_3_6": str,
                "value_first_trimester_3_6": str,
                "value_second_trimester_3_6": str,
                "value_third_trimester_3_6": str,
                "value_fourth_trimester_3_6": str,
                "project_name_3_7": str,
                "city_3_7": str,
                "total_number_project_3_7": str,
                "total_cost_3_7": str,
                "start_date_3_7": str,
                "end_date_3_7": str,
                "value_first_trimester_3_7": str,
                "value_second_trimester_3_7": str,
                "value_third_trimester_3_7": str,
                "value_fourth_trimester_3_7": str,
                "project_name_3_8": str,
                "city_3_8": str,
                "total_number_project_3_8": str,
                "total_cost_3_8": str,
                "start_date_3_8": str,
                "end_date_3_8": str,
                "value_first_trimester_3_8": str,
                "value_second_trimester_3_8": str,
                "value_third_trimester_3_8": str,
                "value_fourth_trimester_3_8": str,
                "project_name_3_9": str,
                "city_3_9": str,
                "total_number_project_3_9": str,
                "total_cost_3_9": str,
                "start_date_3_9": str,
                "end_date_3_9": str,
                "value_first_trimester_3_9": str,
                "value_second_trimester_3_9": str,
                "value_third_trimester_3_9": str,
                "value_fourth_trimester_3_9": str,
                "project_name_3_10": str,
                "city_3_10": str,
                "total_number_project_3_10": str,
                "total_cost_3_10": str,
                "start_date_3_10": str,
                "end_date_3_10": str,
                "value_first_trimester_3_10": str,
                "value_second_trimester_3_10": str,
                "value_third_trimester_3_10": str,
                "value_fourth_trimester_3_10": str,
                "encuesta_4": str,
                "trimestre_4": str,
                "company_name_4": str,
                "liaison_officer_4": str,
                "tel_4": str,
                "project_4": str,
                "branches_4": str,
                "project_name_4_1": str,
                "city_4_1": str,
                "total_number_project_4_1": str,
                "total_cost_4_1": str,
                "start_date_4_1": str,
                "end_date_4_1": str,
                "value_first_trimester_4_1": str,
                "value_second_trimester_4_1": str,
                "value_third_trimester_4_1": str,
                "value_fourth_trimester_4_1": str,
                "project_name_4_2": str,
                "city_4_2": str,
                "total_number_project_4_2": str,
                "total_cost_4_2": str,
                "start_date_4_2": str,
                "end_date_4_2": str,
                "value_first_trimester_4_2": str,
                "value_second_trimester_4_2": str,
                "value_third_trimester_4_2": str,
                "value_fourth_trimester_4_2": str,
                "project_name_4_3": str,
                "city_4_3": str,
                "total_number_project_4_3": str,
                "total_cost_4_3": str,
                "start_date_4_3": str,
                "end_date_4_3": str,
                "value_first_trimester_4_3": str,
                "value_second_trimester_4_3": str,
                "value_third_trimester_4_3": str,
                "value_fourth_trimester_4_3": str,
                "project_name_4_4": str,
                "city_4_4": str,
                "total_number_project_4_4": str,
                "total_cost_4_4": str,
                "start_date_4_4": str,
                "end_date_4_4": str,
                "value_first_trimester_4_4": str,
                "value_second_trimester_4_4": str,
                "value_third_trimester_4_4": str,
                "value_fourth_trimester_4_4": str,
                "project_name_4_5": str,
                "city_4_5": str,
                "total_number_project_4_5": str,
                "total_cost_4_5": str,
                "start_date_4_5": str,
                "end_date_4_5": str,
                "value_first_trimester_4_5": str,
                "value_second_trimester_4_5": str,
                "value_third_trimester_4_5": str,
                "value_fourth_trimester_4_5": str,
                "project_name_4_6": str,
                "city_4_6": str,
                "total_number_project_4_6": str,
                "total_cost_4_6": str,
                "start_date_4_6": str,
                "end_date_4_6": str,
                "value_first_trimester_4_6": str,
                "value_second_trimester_4_6": str,
                "value_third_trimester_4_6": str,
                "value_fourth_trimester_4_6": str,
                "project_name_4_7": str,
                "city_4_7": str,
                "total_number_project_4_7": str,
                "total_cost_4_7": str,
                "start_date_4_7": str,
                "end_date_4_7": str,
                "value_first_trimester_4_7": str,
                "value_second_trimester_4_7": str,
                "value_third_trimester_4_7": str,
                "value_fourth_trimester_4_7": str,
                "project_name_4_8": str,
                "city_4_8": str,
                "total_number_project_4_8": str,
                "total_cost_4_8": str,
                "start_date_4_8": str,
                "end_date_4_8": str,
                "value_first_trimester_4_8": str,
                "value_second_trimester_4_8": str,
                "value_third_trimester_4_8": str,
                "value_fourth_trimester_4_8": str,
                "project_name_4_9": str,
                "city_4_9": str,
                "total_number_project_4_9": str,
                "total_cost_4_9": str,
                "start_date_4_9": str,
                "end_date_4_9": str,
                "value_first_trimester_4_9": str,
                "value_second_trimester_4_9": str,
                "value_third_trimester_4_9": str,
                "value_fourth_trimester_4_9": str,
                "project_name_4_10": str,
                "city_4_10": str,
                "total_number_project_4_10": str,
                "total_cost_4_10": str,
                "start_date_4_10": str,
                "end_date_4_10": str,
                "value_first_trimester_4_10": str,
                "value_second_trimester_4_10": str,
                "value_third_trimester_4_10": str,
                "value_fourth_trimester_4_10": str,
            },
            table_name="JP_541",
            table_id="7",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/quaterly/construcción/JP-541.html")
