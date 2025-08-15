from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def reports_index_placeholder(request):
    return render(request, "reports/index_placeholder.html")
