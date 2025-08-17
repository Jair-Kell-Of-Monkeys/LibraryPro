from django.db import models


class Category(models.Model):
    """Categoría opcional para clasificar libros."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "categoría"
        verbose_name_plural = "categorías"

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    """Libro del catálogo."""
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="books"
    )
    isbn = models.CharField(max_length=20, unique=True)
    year = models.PositiveIntegerField(null=True, blank=True)
    copies_total = models.PositiveIntegerField(default=1)
    copies_available = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "libro"
        verbose_name_plural = "libros"
        constraints = [
            # Mantener disponibles en [0, copies_total]
            models.CheckConstraint(
                check=models.Q(copies_available__gte=0),
                name="book_copies_available_non_negative",
            ),
            models.CheckConstraint(
                check=models.Q(copies_available__lte=models.F("copies_total")),
                name="book_copies_available_le_total",
            ),
        ]

    def __str__(self) -> str:
        return f"{self.title} — {self.author}"
