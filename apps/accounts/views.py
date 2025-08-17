# apps/accounts/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Member
from .forms import MemberForm

class MemberListView(LoginRequiredMixin, ListView):
    model = Member
    paginate_by = 10
    template_name = "accounts/member_list.html"

class MemberDetailView(LoginRequiredMixin, DetailView):
    model = Member
    template_name = "accounts/member_detail.html"

class MemberCreateView(LoginRequiredMixin, CreateView):
    model = Member
    form_class = MemberForm
    template_name = "accounts/member_form.html"
    success_url = reverse_lazy("accounts:member_list")

class MemberUpdateView(LoginRequiredMixin, UpdateView):
    model = Member
    form_class = MemberForm
    template_name = "accounts/member_form.html"
    success_url = reverse_lazy("accounts:member_list")

class MemberDeleteView(LoginRequiredMixin, DeleteView):
    model = Member
    template_name = "accounts/member_confirm_delete.html"
    success_url = reverse_lazy("accounts:member_list")
