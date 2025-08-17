from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    join_date = models.DateField(auto_now_add=True)
    # Relación opcional con usuario del sistema
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="member_profile")

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "Socio"
        verbose_name_plural = "Socios"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
