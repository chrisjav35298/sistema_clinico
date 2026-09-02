from django.urls import path
from . import views

# ojo, usar aca este formato de app_name:nombre_url para poder usarlo.
app_name = "servicios"

urlpatterns = [
   path('', views.menu, name='menu'),
   path('listado/', views.listado_servicios, name='listado_servicios'),
   path('nuevo/', views.nuevo_servicio, name='nuevo_servicio'),
   path('editar/<int:servicio_id>/', views.editar_servicio, name='editar_servicio'),
   path('eliminar/<int:servicio_id>/', views.eliminar_servicio, name='eliminar_servicio')
]  
