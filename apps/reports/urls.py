# apps/reports/urls.py
from django.urls import path
from . import views

app_name = "reports"

urlpatterns = [
    path("reports/", views.reports_index_placeholder, name="index"),
]
