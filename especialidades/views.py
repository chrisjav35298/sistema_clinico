from django.shortcuts import render, redirect
import datetime
from .models import Especialidades
from .forms import EspecialidadForm


def menu(request):

    fecha= datetime.datetime.now()
    return render(request, "especialidades/menu_especialidades.html", {"fecha": fecha})

def nuevo(request):
    if request.method == 'POST':
        form = EspecialidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("especialidades:listado_especialidades")

    else:
        form = EspecialidadForm()
    return render(request, "especialidades/crear_especialidad.html", {"form": form})



# def listado(request):
#     especialidades = Especialidades.objects.all()
#     dia= datetime.datetime.now().day

#     return render(
#         request,
#         "especialidades/lista_especialidades.html",
#         {"especialidades": especialidades,
#          "dia": dia}
#     )

def listado(request):
    nombre = request.GET.get('nombre', '')
    especialidades = Especialidades.objects.filter(
        nombre__icontains=nombre
    )
    dia = datetime.datetime.now().day
    return render(
        request,
        "especialidades/lista_especialidades.html",
        {
            "especialidades": especialidades,
            "dia": dia,
            "nombre": nombre,
        }
    )




def editar(request, especialidad_id):
    especialidad = Especialidades.objects.get(id=especialidad_id)
    if request.method == 'POST':
        form = EspecialidadForm(request.POST, instance=especialidad)
        if form.is_valid():
            form.save()
            return redirect("especialidades:listado_especialidades")
    else:
        form = EspecialidadForm(instance=especialidad)
    return render(request, "especialidades/editar_especialidad.html", {"form": form, "especialidad": especialidad})

def eliminar(request, especialidad_id):
    especialidad = Especialidades.objects.get(id=especialidad_id)
    if request.method == 'POST':
        especialidad.delete()
        return redirect("especialidades:listado_especialidades")
    return render(request, "especialidades/eliminar_especialidad.html", {"especialidad": especialidad})



def lista_filter(request):
    nombre = request.GET.get('nombre', '')
    descripcion = request.GET.get('descripcion', '')

    # Consulta inicial
    especialidades = Especialidades.objects.all()

    # Agregamos filtros según los parámetros recibidos
    if nombre:
        especialidades = especialidades.filter(
            nombre__icontains=nombre
        )

    if descripcion:
        especialidades = especialidades.filter(
            descripcion__icontains=descripcion
        )

    # Ordenamos los resultados
    especialidades = especialidades.order_by('nombre')

    return render(
        request,
        "especialidades/lista_filter.html",
        {
            "especialidades": especialidades,
            "nombre": nombre,
            "descripcion": descripcion,
        }
    )
