from django.urls import path
from . import views


app_name = 'pacientes'

urlpatterns = [
    path('', views.menu, name='menu'),
    path('listado/', views.listado_pacientes, name='listado_pacientes'),
    path('buscar/', views.buscar, name='buscar_paciente'),
    path('atencion/', views.detalle_atencion, name='detalle_atencion'),
    path('<int:id>/', views.detalle_paciente, name='detalle_paciente'),
    path('usuarios/', views.detalle_usuarios, name='detalle_usuarios'),

]   