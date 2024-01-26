from django.http import HttpResponse
from django.shortcuts import render
from appcoder.models import Curso
from appcoder.forms import CursoFormulario


def saludo(request):
    return HttpResponse('Primera Vista')

def segunda_vista(request):
    return HttpResponse('Trabajo Preliminar')

def template(request):

    contexto = {
        "nombre": "German",
        "apellido": "Gonzalez",
        "edad": 33,
        "cursos": ["Python","Ingles",'HTML' ]
    }

    return render(request,'template1.html',contexto)
  
def index(request):
    return render (request, 'index.html')

def Profesores(request):
    return render (request, 'profesores.html')

def Estudiantes(request):
    return render (request, 'estudiantes.html')

def curso(request):
    return render (request, 'cursos.html')

def Entregables(request):
    return render (request, 'entregables.html')


"""""
def curso_formulario(request):

    

    if request.method == "POST":

        nombre = request.POST.get("curso")
        camada = request.POST.get("camada")
        
        print(f'El Curso: {nombre} y la camada {camada}')

        curso = Curso(nombre=nombre, camada=camada)

        curso.save()
        
        return render(request, 'index.html')
    
    return render(request, 'curso_formulario.html')
"""

def curso_formulario(request):

    if request.method == "POST":
        
        formulario = CursoFormulario(request.POST) 

        print("formulario")
        print(formulario)

        print(f" is valid : {formulario.is_valid}")
        if formulario.is_valid:

            datos = formulario.cleaned_data

            nombre = datos.get("curso")
            camada = datos.get("camada")

            curso = Curso(nombre=nombre,camada=camada)

            curso.save()

            return render(request, 'index.html')
        
    else:
        formulario = CursoFormulario()

    return render(request, 'curso_formulario.html', {"formulario": formulario })


def busqueda_camada(request):

    if request.method == "GET":
        
        camada =request.GET.get("camada")

        if camada is None:
            return HttpResponse("Enviar la camada a buscar")

        cursos = Curso.objects.filter(camada__icontains=camada)

        print(cursos)

        return HttpResponse(f"Se busco la camada: {camada}")

    return render(request, 'busqueda_camada.html')