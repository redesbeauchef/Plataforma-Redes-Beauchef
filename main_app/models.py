from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

#class Usuario():

class Carrera(models.Model):
    nombre = models.CharField(max_length=100)

class Empleo(models.Model):
    tipo = models.CharField(max_length=100)

class Empresa(models.Model):
    #Pyp?
    #logo = models.ImageField(upload_to=, null=True)
    ofertas = models.TextField() # supongo que vamos a guardar el json como string?
    descripcion = models.CharField(max_length=300)
    web = models.URLField()
    #rut =
    nombre = models.CharField(max_length=100)
    encuesta = models.URLField()

class ImagenEmpresa(models.Model):
    #imagen = models.ImageField(upload_to=, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
