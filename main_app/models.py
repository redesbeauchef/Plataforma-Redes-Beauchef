from django.db import models
from django.urls import reverse
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, User
from datetime import datetime
from django.utils import timezone


class Carrera(models.Model):
    plan = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.plan


class Empleo(models.Model):
    tipo = models.CharField(max_length=200)

    def __str__(self):
        return self.tipo


def user_cv_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/cv/user_<id>/<filename>
    return 'cv/user_{0}/{1}'.format(instance.usuario.id, filename)

def user_foto_perfil_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/cv/user_<id>/<filename>
    return 'foto_perfil/user_{0}/{1}'.format(instance.usuario.id, filename)

class Perfil(models.Model):

    class Meta:
        verbose_name_plural = 'Perfiles'

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    egresado = models.BooleanField()
    rut = models.CharField(max_length=20)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    empleo = models.ForeignKey(Empleo, on_delete=models.CASCADE)
    cv = models.FileField(upload_to=user_cv_path, null=False)
    foto_perfil = models.ImageField(upload_to=user_foto_perfil_path, null=False)
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

    def __str__(self):
        return self.nombre


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
    fecha = models.DateField(default=datetime.today())
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)



class EspecialidadOferta(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)


class EmpleoOferta(models.Model):
    empleo = models.ForeignKey(Empleo, on_delete=models.CASCADE)
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)


class Entrevista(models.Model):
    hora_inicio = models.DateTimeField(unique=True)
    hora_cierre = models.DateTimeField(unique=True, default=timezone.now())
    entrevistados = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)
    OPCIONES_ASISTENCIA = (
        (0, "Si"),
        (1, "No"),
        (2, "Pendiente")
    )
    asistencia = models.IntegerField(choices=OPCIONES_ASISTENCIA)

class Requerimientos(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=500)
    representante = models.CharField(max_length=150)
    celular = models.CharField(max_length=12)
    email = models.CharField(max_length=150)
    dia_asistencia = models.CharField(max_length=100)
    tipo_stand = models.CharField(max_length=100)
    stand_propio = models.BooleanField()
    entrevistadores = models.IntegerField()
    almuerzos_normales = models.IntegerField()
    almuerzos_vegetarianos = models.IntegerField()


class Stand(models.Model):
    requerimiento = models.ForeignKey(Requerimientos, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

class CarrerasRequeridas(models.Model):
    requerimiento = models.ForeignKey(Requerimientos, on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)

class CantidadPorOferta(models.Model):
    requeridas = models.ForeignKey(CarrerasRequeridas, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

