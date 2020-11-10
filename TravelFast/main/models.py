from django.db import models

# Create your models here.

opciones_consultas = [
    [0, "correo"],
    [1, "rut"],
    [2, "nombres"],
    [3, "apellidos"],
    [4, "telefono"],
    [5, "region"],
    [6, "comuna"],
    [7, "tipoViaje"]
]

class formularioRegistro(models.Model):
    Email = models.CharField(max_length=255)
    Rut = models.CharField(max_length=10)
    Nombres = models.CharField(max_length=255)
    Apellidos = models.CharField(max_length=255)
    Telefono = models.CharField(max_length=9)
    Region = models.CharField(max_length=255, default=0)
    Comuna = models.CharField(max_length=255, default=0)
    TipoViaje = models.CharField(max_length=255, default=0)

    def __str__(self):
        return self.Email + ' ' + self.Rut 
