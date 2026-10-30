from django.urls import path
from . import views

app_name = "medicos"

urlpatterns = [
    # Ejemplo para ver lazy loading
    path("listado/", views.MedicoListView.as_view(), name="listado_medicos"),
    path("nuevo/", views.MedicoNewView.as_view(), name="nuevo_medico"),
    path("<int:pk>/", views.MedicoDetailView.as_view(), name="detalle_medico"),
    path("<int:pk>/editar/", views.MedicoUpdateView.as_view(), name="editar_medico"),
    path("<int:pk>/eliminar/", views.MedicoDeleteView.as_view(), name="eliminar_medico"),
    path("prueba-lazy-loading/", views.detalle_medico, name="prueba_lazy_loading"),

]