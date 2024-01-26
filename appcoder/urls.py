from django.urls import path

from appcoder.views import *

urlpatterns = [
    path("profesor/", Profesores, name='Profesores'),
    path("Estudiantes/", Estudiantes, name='Estudiantes'),
    path('curso/', curso, name ='Cursos'),
    path('entregables/', Entregables, name='Entregables'),
    path('cursoFormulario', curso_formulario, name='curso_formulario' ),
    path('busquedaCamada', busqueda_camada, name="busqueda_camada"),
    path('', index, name='index'),



    
]



