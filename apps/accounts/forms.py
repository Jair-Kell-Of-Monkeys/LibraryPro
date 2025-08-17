# apps/accounts/forms.py
from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        # OJO: NO incluir join_date porque es no editable en el modelo
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "is_active",
            "user",
        ]
