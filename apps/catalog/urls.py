from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("books/", views.books_list_placeholder, name="books_list"),
]
