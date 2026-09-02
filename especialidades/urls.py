from django.urls import path
from . import views


app_name = 'especialidades'

urlpatterns = [
    path('', views.menu, name='menu_especialidades'),
    path('nuevo/', views.nuevo, name='nueva_especialidad'),
    path('listado/', views.listado, name='listado_especialidades'),
    path('editar/<int:especialidad_id>/', views.editar, name='editar_especialidad'),
    path('eliminar/<int:especialidad_id>/', views.eliminar, name='eliminar_especialidad'),

]   