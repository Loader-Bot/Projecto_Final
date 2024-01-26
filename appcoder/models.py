from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length = 10)
    camada = models.IntegerField()


    def __str__(self):
        return f"{self.nombre} --- {self.camada}"


class Entregable(models.Model):
    nombre = models.CharField(max_length = 10)
    fecha = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return f"{self.nombre} --- {self.entregado}"

class Profesor(models.Model):

    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 30)
    email = models.EmailField

    class Meta:
        verbose_name_plural = "Profesores"
        ordering =["nombre"]


class Estudiante (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
    
