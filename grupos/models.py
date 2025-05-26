from django.db import models

# Create your models here.
class Grupo(models.Model):
    ANIO_CHOICES = [
        ('primero', 'Primero'),
        ('segundo', 'Segundo'),
        ('tercero', 'Tercero'),
        ('cuarto', 'Cuarto'),
    ]
    # Información básica
    nombre = models.CharField(max_length=50, unique=True)
    direccion = models.CharField(max_length=100)
    curso = models.CharField(max_length=20)
    anio_escolar = models.CharField(max_length=10, choices=ANIO_CHOICES)
    caracterizacion = models.TextField()

    # Relaciones
    guia = models.OneToOneField(
        'profesores.Profesor',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='grupo_asignado'
    )
    profesores = models.ManyToManyField(
        'profesores.Profesor',
        related_name='grupos',
        blank=True
    )

    def __str__(self):
        return self.nombre

