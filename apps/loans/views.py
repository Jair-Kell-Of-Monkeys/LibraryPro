# apps/loans/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def loans_list_placeholder(request):
    return render(request, "loans/loans_list_placeholder.html")
