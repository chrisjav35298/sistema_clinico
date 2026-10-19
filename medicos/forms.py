from django import forms
from .models import Medico


class MedicoForm(forms.ModelForm):

    class Meta:
        model = Medico
        fields = [
            'nombre',
            'apellido',
            'dni',
            'matricula',
            'especialidades'
        ]