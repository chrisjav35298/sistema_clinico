from django.contrib import admin
from .models import Especialidades

@admin.register(Especialidades)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)
    ordering = ('nombre',)