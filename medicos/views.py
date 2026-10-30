from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import MedicoForm
from medicos.models import Medico
from django.views.generic import (ListView, DetailView, CreateView, UpdateView,  DeleteView)

from django.contrib.auth.mixins import ( LoginRequiredMixin, PermissionRequiredMixin)


class MedicoListView(LoginRequiredMixin, ListView):
    model = Medico
    template_name = "medicos/medico_list.html"
    context_object_name = "medicos"

class MedicoNewView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = "medicos/medico_form.html"
    success_url = reverse_lazy("medicos:listado_medicos")
    permission_required = "medicos.add_medico"


class MedicoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Medico
    template_name = "medicos/medico_detail.html"
    permission_required = "medicos.view_medico"


class MedicoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Medico
    form_class = MedicoForm
    template_name = "medicos/medico_form.html"
    success_url = reverse_lazy("medicos:listado_medicos")
    permission_required = "medicos.change_medico"

class MedicoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Medico
    template_name = "medicos/medico_confirm_delete.html"
    success_url = reverse_lazy("medicos:listado_medicos")

    permission_required = "medicos.delete_medico"


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