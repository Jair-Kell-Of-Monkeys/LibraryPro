# LibraryPro/LibraryPro/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    # Home simple
    path("", TemplateView.as_view(template_name="home.html"), name="home"),

    # Auth (login/logout, password reset, etc.)
    path("", include("django.contrib.auth.urls")),

    # Apps
    path("", include("apps.catalog.urls")),   # /books/...
    path("", include("apps.accounts.urls")),  # /members/...
    path("", include("apps.loans.urls")),     # placeholder / (si luego agregas rutas, se expanden)
    path("", include("apps.reports.urls")),   # placeholder /
]
