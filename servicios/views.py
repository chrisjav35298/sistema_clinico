from django.shortcuts import render, redirect
import datetime
import requests
from .models import Servicios

from .forms import ServicioForm



def menu(request):
    fecha= datetime.datetime.now()
    return render(request, "servicios/menu_servicios.html", {"fecha": fecha})


def nuevo_servicio(request):
   if request.method == 'POST':
       form = ServicioForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect("servicios:listado_servicios")

   else:
       form = ServicioForm()
   return render(request, "servicios/crear_servicio.html", {"form": form})

def listado_servicios(request):
   servicios = Servicios.objects.all()
   dia= datetime.datetime.now().day

   return render(
       request,
       "servicios/lista_servicios.html",
       {"servicios": servicios,
        "dia": dia}
   )

def editar_servicio(request, servicio_id):
    servicio = Servicios.objects.get(id=servicio_id)
    if request.method == 'POST':
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect("servicios:listado_servicios")
    else:
        form = ServicioForm(instance=servicio)
    return render(request, "servicios/editar_servicio.html", {"form": form, "servicio": servicio})

def eliminar_servicio(request, servicio_id):
    servicio = Servicios.objects.get(id=servicio_id)
    if request.method == 'POST':
        servicio.delete()
        return redirect("servicios:listado_servicios")
    return render(request, "servicios/eliminar_servicio.html", {"servicio": servicio})
