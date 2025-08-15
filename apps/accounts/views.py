from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def members_list_placeholder(request):
    return render(request, "accounts/members_list_placeholder.html")
