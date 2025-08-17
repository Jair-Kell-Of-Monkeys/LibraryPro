from django.contrib import admin
from .models import Loan

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ("book", "member", "loan_date", "due_date", "return_date", "status", "fine_amount")
    search_fields = ("book__title", "member__first_name", "member__last_name")
    list_filter = ("status", "loan_date", "due_date")
