from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("members/", views.members_list_placeholder, name="members_list"),
]
