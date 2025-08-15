from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),

    # Auth de Django
    path("accounts/", include("django.contrib.auth.urls")),

    # Nuestras apps (placeholders por ahora)
    path("accounts/", include("apps.accounts.urls")),
    path("catalog/", include("apps.catalog.urls")),
    path("loans/", include("apps.loans.urls")),
    path("reports/", include("apps.reports.urls")),
]
