from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import (ListView, DetailView, CreateView, UpdateView,  DeleteView)
from django.urls import reverse_lazy
from .forms import MedicoForm
from medicos.models import Medico



def detalle_medico(request):
    # 1. Recuperamos un médico de la base de datos
    medico = Medico.objects.get(dni="123456")

    print("Médico:", medico.nombre, medico.apellido)

    # 2. Accedemos a sus especialidades relacionadas
    especialidades = medico.especialidades.all()

    # 3. Necesitamos los datos de esas especialidades
    for especialidad in especialidades:
        print(especialidad.nombre)

    return HttpResponse("Revisá la terminal")


class MedicoListView(ListView):
    model = Medico
    template_name = "medicos/medico_list.html"
    context_object_name = "medicos"


class MedicoNewView(CreateView):
    model = Medico
    form_class = MedicoForm 

    template_name = 'medicos/medico_form.html'
    success_url = reverse_lazy('medicos:listado_medicos')



class MedicoListView(ListView):
    model = Medico
    template_name = 'medicos/medico_list.html'
    context_object_name = 'medicos'


class MedicoDetailView(DetailView):
    model = Medico
    template_name = 'medicos/medico_detail.html'


class MedicoUpdateView(UpdateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medicos/medico_form.html'
    success_url = reverse_lazy('medicos:listado_medicos')

class MedicoDeleteView(DeleteView):
    model = Medico
    template_name = 'medicos/medico_confirm_delete.html'
    success_url = reverse_lazy('medicos:listado_medicos')