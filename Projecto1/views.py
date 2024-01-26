from django.http import HttpResponse
from django.shortcuts import render


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
    return render(request, 'index.html')

  