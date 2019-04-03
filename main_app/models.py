from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class Carrera(models.Model):
    plan = models.CharField(max_length=150)


class Empleo(models.Model):
    tipo = models.CharField(max_length=200)


class Usuario(AbstractBaseUser):
    egresados = models.BooleanField()
    rut = models.CharField(max_length=20)
    email = models.CharField(max_length=500)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    empleo = models.ForeignKey(Empleo, on_delete=models.CASCADE)
    cv = models.FileField(upload_to='cv/', null=False)
    foto_perfil = models.ImageField(upload_to='perfil/', null=False)
    perfil_pro = models.TextField(max_length=500)
    fecha_union = models.DateTimeField(auto_now_add=True)
    ano_ingreso = models.IntegerField()
    ano_egreso = models.IntegerField()
    ultima_conex = models.DateTimeField(auto_now=True)
    spam = models.BooleanField()
    eula = models.BooleanField()

class Empresa(models.Model):
    privado = models.BooleanField()
    logo = models.ImageField(upload_to='logos/', null=True)
    ofertas = models.TextField()  # supongo que vamos a guardar el json como string?
    descripcion = models.TextField(max_length=500)
    web = models.URLField()
    rut = models.CharField(max_length=20)
    nombre = models.CharField(max_length=200)
    encuesta = models.URLField()


class ImagenEmpresa(models.Model):
    imagen = models.ImageField(upload_to='imagenes/', null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

class Oferta(models.Model):
    cargo = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200)
    duracion = models.CharField(max_length=150)
    descripcion = models.TextField(max_length=500)
    requisitos =  models.TextField(max_length=500)
    remuneracion = models.CharField(max_length=200)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)



class EspecialidadOferta(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)

class EmpleoOferta(models.Model):
    empleo = models.ForeignKey(Empleo, on_delete=models.CASCADE)
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)

class Entrevista(models.Model):
    hora_inicio = models.TimeField()
    entrevistados = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)
    OPCIONES_ASISTENCIA = (
        (0, "Si"),
        (1, "No"),
        (2, "Pendiente")
    )
    asistencia = models.IntegerField(choices=OPCIONES_ASISTENCIA)
