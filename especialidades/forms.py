from django import forms
from .models import Especialidades


class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidades
        fields = [
            "nombre",
            "descripcion",
        ]