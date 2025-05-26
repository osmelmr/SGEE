from django.db import models

# Create your models here.
class Grupo(models.Model):
    # Información básica
    nombre = models.CharField(max_length=50, unique=True)
    direccion = models.CharField(max_length=100)
    curso = models.CharField(max_length=20)
    anio_escolar = models.CharField(max_length=10)
    caracterizacion = models.TextField()

    # Relaciones
    guia = models.OneToOneField(
        'Profesor',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='grupo_asignado'
    )
    profesores = models.ManyToManyField(
        'Profesor',
        related_name='grupos',
        blank=True
    )

    def __str__(self):
        return self.nombre

