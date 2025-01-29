from django.shortcuts import render
from src.dao.data_db_dao import DAO
import polars as pl

def cuestionario_viajero_spanish(request):

  if request.method == "POST":
    case_selection = request.POST.get("case_selection")
    age = request.POST.get("age")
    gender_identity = request.POST.get("gender_identity")
    sexual_orientation = request.POST.get("sexual_orientation")
    heritage = request.POST.get("heritage")
    hispanic_identity = request.POST.get("hispanic_identity")
    education_level = request.POST.get("education_level")
    income_level = request.POST.get("income_level")
    travel_companion = request.POST.get("travel_companion")
    number_of_companions = request.POST.get("number_of_companions")
    visitor_origin = request.POST.get("visitor_origin")
    country_selection = request.POST.get("country_selection")
    accomodation = request.POST.get("accomodation")
    visit_purpose = request.POST.get("visit_purpose")
    activities = request.POST.get("activities")
    discovery_method = request.POST.get("discovery_method")
    stay_duration = request.POST.get("stay_duration")
    main_municipality = request.POST.get("main_municipality")
    visited_municipalities = request.POST.get("visited_municipalities")
    safety_feeling = request.POST.get("safety_feeling")
    trip_expense = request.POST.get("trip_expense")
    priority_accommodation_1 = request.POST.get("priority_accommodation_1")
    priority_food_1 = request.POST.get("priority_food_1")
    priority_transportation_1 = request.POST.get("priority_transportation_1")
    priority_activities_1 = request.POST.get("priority_activities_1")
    priority_shopping_1 = request.POST.get("priority_shopping_1")
    travel_destination = request.POST.get("travel_destination")
    usa_states = request.POST.get("usa_states")
    countries = request.POST.get("countries")
    accommodation_1 = request.POST.get("accommodation_1")
    travel_purposes = request.POST.get("travel_purposes")
    planned_activities = request.POST.get("planned_activities")
    trip_duration = request.POST.get("trip_duration")
    estimated_expenses = request.POST.get("estimated_expenses")
    priority_accommodation_2 = request.POST.get("priority_accommodation_1")
    priority_food_2 = request.POST.get("priority_food_1")
    priority_transportation_2 = request.POST.get("priority_transportation_1")
    priority_activities_2 = request.POST.get("priority_activities_1")
    priority_shopping_2 = request.POST.get("priority_shopping_1")
    priority_other_1 = request.POST.get("priority_other_1")

    data = [
      pl.Series("case_selection", [case_selection], dtype=pl.Utf8),
      pl.Series("age", [age], dtype=pl.Int64),
      pl.Series("gender_identity", [gender_identity], dtype=pl.Utf8),
      pl.Series("sexual_orientation", [sexual_orientation], dtype=pl.Utf8),
      pl.Series("heritage", [heritage], dtype=pl.Utf8),
      pl.Series("hispanic_identity", [hispanic_identity], dtype=pl.Utf8),
      pl.Series("education_level", [education_level], dtype=pl.Utf8),
      pl.Series("income_level", [income_level], dtype=pl.Utf8),
      pl.Series("travel_companion", [travel_companion], dtype=pl.Utf8),
      pl.Series("number_of_companions", [number_of_companions], dtype=pl.Int64),
      pl.Series("visitor_origin", [visitor_origin], dtype=pl.Utf8),
      pl.Series("country_selection", [country_selection], dtype=pl.Utf8),
      pl.Series("accomodation", [accomodation], dtype=pl.Utf8),
      pl.Series("visit_purpose", [visit_purpose], dtype=pl.Utf8),
      pl.Series("activities", [activities], dtype=pl.Utf8),
      pl.Series("discovery_method", [discovery_method], dtype=pl.Utf8),
      pl.Series("stay_duration", [stay_duration], dtype=pl.Utf8),
      pl.Series("main_municipality", [main_municipality], dtype=pl.Utf8),
      pl.Series("visited_municipalities", [visited_municipalities], dtype=pl.Utf8),
      pl.Series("safety_feeling", [safety_feeling], dtype=pl.Utf8),
      pl.Series("trip_expense", [trip_expense], dtype=pl.Float64),
      pl.Series("priority_accommodation_1", [priority_accommodation_1], dtype=pl.Utf8),
      pl.Series("priority_food_1", [priority_food_1], dtype=pl.Utf8),
      pl.Series("priority_transportation_1", [priority_transportation_1], dtype=pl.Utf8),
      pl.Series("priority_activities_1", [priority_activities_1], dtype=pl.Utf8),
      pl.Series("priority_shopping_1", [priority_shopping_1], dtype=pl.Utf8),
      pl.Series("travel_destination", [travel_destination], dtype=pl.Utf8),
      pl.Series("usa_states", [usa_states], dtype=pl.Utf8),
      pl.Series("countries", [countries], dtype=pl.Utf8),
      pl.Series("accommodation_1", [accommodation_1], dtype=pl.Utf8),
      pl.Series("travel_purposes", [travel_purposes], dtype=pl.Utf8),
      pl.Series("planned_activities", [planned_activities], dtype=pl.Utf8),
      pl.Series("trip_duration", [trip_duration], dtype=pl.Utf8),
      pl.Series("estimated_expenses", [estimated_expenses], dtype=pl.Float64),
      pl.Series("priority_accommodation_2", [priority_accommodation_2], dtype=pl.Utf8),
      pl.Series("priority_food_2", [priority_food_2], dtype=pl.Utf8),
      pl.Series("priority_transportation_2", [priority_transportation_2], dtype=pl.Utf8),
      pl.Series("priority_activities_2", [priority_activities_2], dtype=pl.Utf8),
      pl.Series("priority_shopping_2", [priority_shopping_2], dtype=pl.Utf8),
      pl.Series("priority_other_1", [priority_other_1], dtype=pl.Utf8)

    ]


  return render(request, 'cuestionario_viajero_spanish.html')