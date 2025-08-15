from django.urls import path
from . import views

app_name = "loans"

urlpatterns = [
    path("", views.loans_list_placeholder, name="loans_list"),
]
