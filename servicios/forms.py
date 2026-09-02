from django import forms
from .models import  Servicios

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicios
        fields = [
            "nombre",
            "descripcion",
            "especialidad"
        ]
