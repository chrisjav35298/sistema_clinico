from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('pacientes/', include('pacientes.urls')),
    path('especialidades/', include('especialidades.urls')),
    path('servicios/', include('servicios.urls')),
    # path('turnos/', include('turnos.urls')),
]