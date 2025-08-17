# apps/catalog/forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "category",
            "isbn",
            "year",
            "copies_total",
            "copies_available",
        ]
        widgets = {
            "year": forms.NumberInput(attrs={"min": 0}),
            "copies_total": forms.NumberInput(attrs={"min": 0}),
            "copies_available": forms.NumberInput(attrs={"min": 0}),
        }
