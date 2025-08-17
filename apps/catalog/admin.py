from django.contrib import admin
from .models import Book, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "description")

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "isbn", "year", "copies_total", "copies_available")
    search_fields = ("title", "author", "isbn")
    list_filter = ("category", "author", "year")
