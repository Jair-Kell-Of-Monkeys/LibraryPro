from decimal import Decimal

from django.core.exceptions import ValidationError
from django.db import models, transaction
from django.utils import timezone

from apps.accounts.models import Member
from apps.catalog.models import Book


class Loan(models.Model):
    """Préstamo de un libro a un socio."""

    STATUS_ACTIVE = "ACTIVE"
    STATUS_RETURNED = "RETURNED"
    STATUS_LATE = "LATE"

    STATUS_CHOICES = [
        (STATUS_ACTIVE, "Activo"),
        (STATUS_RETURNED, "Devuelto"),
        (STATUS_LATE, "Atrasado"),
    ]

    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name="loans")
    member = models.ForeignKey(Member, on_delete=models.PROTECT, related_name="loans")
    loan_date = models.DateField(default=timezone.localdate)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_ACTIVE)
    fine_amount = models.DecimalField(
        max_digits=8, decimal_places=2, default=Decimal("0.00")
    )

    class Meta:
        ordering = ["-loan_date"]
        verbose_name = "préstamo"
        verbose_name_plural = "préstamos"

    def __str__(self) -> str:
        return f"{self.book} → {self.member} ({self.status})"

    # --- Validaciones de negocio básicas
    def clean(self):
        super().clean()
        # En creación: no permitir si no hay copias
        if self.pk is None and self.book_id:
            # Bloqueo explícito no aquí (va en save), solo validación “rápida”
            book = Book.objects.only("id", "copies_available").get(pk=self.book_id)
            if book.copies_available <= 0:
                raise ValidationError("No hay copias disponibles de este libro.")

        # Fechas consistentes
        if self.due_date and self.loan_date and self.due_date < self.loan_date:
            raise ValidationError("La fecha de vencimiento no puede ser anterior al préstamo.")

    # --- Lógica de disponibilidad y estado con bloqueo de fila
    def save(self, *args, **kwargs):
        is_create = self.pk is None

        with transaction.atomic():
            if is_create:
                # Tomamos y bloqueamos la fila del libro para evitar carreras
                book = Book.objects.select_for_update().get(pk=self.book_id)
                if book.copies_available <= 0:
                    raise ValidationError("No hay copias disponibles de este libro.")
                # Reservar una copia
                book.copies_available = max(book.copies_available - 1, 0)
                book.save(update_fields=["copies_available"])
                self.status = self.STATUS_ACTIVE
            else:
                # Si marcamos devolución y aún no estaba devuelto, liberar una copia
                if self.return_date and self.status != self.STATUS_RETURNED:
                    book = Book.objects.select_for_update().get(pk=self.book_id)
                    # Devolver la copia respetando el límite superior
                    book.copies_available = min(book.copies_available + 1, book.copies_total)
                    book.save(update_fields=["copies_available"])
                    self.status = self.STATUS_RETURNED

            # Atraso (simple): si venció y no está devuelto
            if self.status == self.STATUS_ACTIVE and self.due_date and self.due_date < timezone.localdate():
                self.status = self.STATUS_LATE

            super().save(*args, **kwargs)
