from django.db import models


class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    matricula = models.CharField(max_length=50, unique=True)

    especialidades = models.ManyToManyField(
        'especialidades.Especialidades',
        related_name='medicos'
    )

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

