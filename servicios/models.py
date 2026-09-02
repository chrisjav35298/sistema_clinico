from django.db import models

# Create your models here.
class Servicios(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    # un servicio puede estar asociado a una especialidad
    especialidad = models.ForeignKey(
        'especialidades.Especialidades',
        on_delete=models.PROTECT,
        related_name='servicios', null=True, blank=True
    )

    def __str__(self):
        return self.nombre