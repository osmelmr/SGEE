from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# ----------------------------------------
# Modelos de Gestión de Usuarios
# ----------------------------------------

class Usuario(AbstractUser):
    # Opciones
    CARGO_CHOICES = [
        ('profesor_principal', 'Profesor_Principal'),
        ('usuario', 'Usuario'),
    ]
    SEXO_CHOICES = [
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('otro', 'Otro'),
    ]

    # Campos adicionales
    cargo = models.CharField(max_length=20, choices=CARGO_CHOICES)
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES)
    grupo = models.CharField(max_length=50, blank=True, null=True)
    solapin = models.CharField(max_length=10, unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    # Relaciones
    encuestas_realizadas = models.ManyToManyField(
        'encuestas.Encuesta',
        related_name='usuarios',
        blank=True
    )
    eventos = models.ManyToManyField(
        'eventos.Evento',
        related_name='usuarios',
        blank=True
    )
    
    # Sobrescribir el método save
    def save(self, *args, **kwargs):
        if self.cargo == 'profesor_principal':
            self.is_staff = True
            self.is_superuser = True  # Convertir en superusuario
        else:
            self.is_staff = False
            self.is_superuser = False  # Asegurarse de que no sea superusuario
        super().save(*args, **kwargs)

    def es_profesor(self):
        return self.cargo == 'profesor_principal'

    def es_usuario(self):
        return self.cargo == 'usuario'

    def __str__(self):
        return f"{self.username} ({self.cargo})"

# ============================================================================
