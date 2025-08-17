from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Book
from .forms import BookForm


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    paginate_by = 10
    template_name = "catalog/book_list.html"
    context_object_name = "books"   # <- IMPORTANTE


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = "catalog/book_detail.html"


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = "catalog/book_form.html"
    success_url = reverse_lazy("catalog:book_list")


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = "catalog/book_form.html"
    success_url = reverse_lazy("catalog:book_list")


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = "catalog/book_confirm_delete.html"
    success_url = reverse_lazy("catalog:book_list")
