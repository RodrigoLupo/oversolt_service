from django.db import models
from django.contrib.auth.models import User

class Empresa(models.Model):
    nombre = models.CharField(max_length=150, null=False)
    ubicacion = models.CharField(max_length=250, null=False)
    RUC = models.CharField(max_length=11, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Administrador(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Administrador: {self.usuario.username}"

class Inspector(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Inspector: {self.usuario.username}"

class Analista(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Analista: {self.usuario.username}"

class Cliente(models.Model):
    DNI = models.CharField(max_length=45, null=True, blank=True)
    NOMBRE = models.CharField(max_length=45, null=True, blank=True)
    APELLIDO = models.CharField(max_length=45, null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.NOMBRE} {self.APELLIDO} ({self.empresa.nombre})"
