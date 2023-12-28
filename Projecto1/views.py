from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    return HttpResponse('Primera Vista')

def segunda_vista(request):
    return HttpResponse('Trabajo Preliminar')

def template(request):

    mihtml = open(r'C:\Users\ggz99\Python\Django2\Tercera_Preentrega\Projecto1\templates\template1.html')

    plantilla = Template(mihtml.read())
    
    mihtml.close()

    miContexto =  Context()
    
    documento = plantilla.render(miContexto)

    return HttpResponse(documento)

