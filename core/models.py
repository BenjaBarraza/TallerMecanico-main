from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Atencion(models.Model):
    mecanico = models.ForeignKey(User, on_delete=models.CASCADE)
    nombreCliente = models.CharField(max_length=150)
    Descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="mecanicos")
    aprovacion = models.BooleanField(null=True)


    def __str__(self):
        return self.nombreCliente