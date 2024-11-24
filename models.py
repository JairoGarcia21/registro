from django.db import models

class User(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()
    usuario = models.CharField(max_length=30, unique=True)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.usuario}"
