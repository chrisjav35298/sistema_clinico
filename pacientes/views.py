from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import datetime, requests

from .forms import ContactoForm




# Analizando sin render ni loader
# def listado_pacientes(request):
#     pacientes = [
#         {"id": 1, "nombre": "Juan Pérez", "edad": 34},
#         {"id": 2, "nombre": "Ana Gómez", "edad": 28},
#         {"id": 3, "nombre": "Carlos Ruiz", "edad": 45},
#     ]
#     contenido = """
#         <h1>Listado de pacientes</h1>
#         <table border="1" cellpadding="8">
#         <tr>
#         <th>ID</th>
#         <th>Nombre</th>
#         <th>Edad</th>
#         </tr>
#         """
#     for paciente in pacientes:
#         contenido += f"""
#                 <tr>
#                 <td>{paciente['id']}</td>
#                 <td>{paciente['nombre']}</td>
#                 <td>{paciente['edad']}</td>
#                 </tr>
#                 """
#     contenido += "</table>"
#     return HttpResponse(contenido)


# Analizando sin render
# def listado_pacientes(request):
#     print('observamos la info que viene en el request:', request)
#     print('que tiene el request:', request)
#     pacientes = [
#         {"id": 1, "nombre": "Juan Pérez", "edad": 34},
#         {"id": 2, "nombre": "Ana Gómez", "edad": 28},
#         {"id": 3, "nombre": "Carlos Ruiz", "edad": 45},
#     ]
#     titulo='Listado de pacientes-envaido desde contexto'

#     template = loader.get_template("pacientes/listado.html")

#     contexto = {
#         "pacientes": pacientes, 
#         "titulo": titulo
#     }

#     html = template.render(contexto, request)

#     return HttpResponse(html)



def listado_pacientes(request):
    pacientes = [
        {"id": 1, "nombre": "Juan Pérez", "edad": 74},
        {"id": 2, "nombre": "Ana Gómez", "edad": 28},
        {"id": 3, "nombre": "Carlos Ruiz", "edad": 45},
    ]
    dia= datetime.datetime.now().day

    return render(
        request,
        "pacientes/listado.html",
        {"pacientes": pacientes,
         "dia": dia}
    )





def detalle_atencion(request):
    atencion = {
        "id": 1001,
        "paciente": "Juan Pérez",
        "medico": "Dra. Fernández",
        "motivo": "Control clínico",
        "fecha": "26/05/2025",
        "estado": "Finalizada"
    }

    return render(request, "pacientes/atencion.html", {"atencion": atencion}
    )

def detalle_paciente(request, id):
    return HttpResponse(f"Detalle del paciente {id}")

def buscar(request):
    nombre = request.GET.get("nombre", "sin nombre")
    return HttpResponse(f"Buscando paciente: {nombre}")

# def detalle_atencion(request):
#     atencion = {
#     "id": 1001,
#     "paciente": "Juan Pérez",
#     "medico": "Dra. Fernández",
#     "motivo": "Control clínico",
#     "fecha": "26/05/2025",
#     "estado": "Finalizada"
#     }
#     contenido = f"""
#         <h1>Detalle de atención clínica</h1>
#         <table border="1" cellpadding="8">
#         <tr>
#         <th>ID Atención</th>
#         <td>{atencion['id']}</td>
#         </tr>
#         <tr>
#         <th>Paciente</th>
#         <td>{atencion['paciente']}</td>
#         </tr>
#         <tr>
#         <th>Médico</th>
#         <td>{atencion['medico']}</td>
#         </tr>
#         <tr>
#         <th>Motivo</th>
#         <td>{atencion['motivo']}</td>
#         </tr>
#         <tr>
#         <th>Fecha</th>
#         <td>{atencion['fecha']}</td>
#         </tr>
#         <tr>
#         <th>Estado</th>
#         <td>{atencion['estado']}</td>
#         </tr>
#         </table>
#         """
#     return HttpResponse(contenido)






    return render(request, "pacientes/atencion.html", {"atencion": atencion}
    )


def menu(request):

    fecha= datetime.datetime.now()
    return render(request, "pacientes/menu_pacientes.html", {"fecha": fecha})





def detalle_usuarios(request):
    respuesta = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    usuarios = respuesta.json()

    return render(
        request,
        "pacientes/detalle_usuarios.html",
        {
            "usuarios": usuarios
        }
    )

def contacto(request):
    print('observamos la info que viene en el request:', request)
    print('que tiene el request:', request)
    print('valor de request.method:', request.method)
    print('valor de request.POST:', request.POST)
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            print('Formulario válido')
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']

            return HttpResponse(f"Gracias por tu mensaje, {nombre}. Nos pondremos en contacto con vos muy pronto.")
    else:
        form = ContactoForm()
    return render(request, "pacientes/contacto.html", {"form": form})   
