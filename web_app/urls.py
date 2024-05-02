from django.contrib import admin
from django.urls import path
from django.urls import include
from web_app import urls
from web_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signin/", views.signin, name="signin"),
]
