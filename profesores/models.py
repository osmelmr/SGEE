from django.db import models

# Create your models here.
class Profesor(models.Model):
    # Datos personales
    nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50, blank=True, null=True)
    sexo = models.CharField(
        max_length=20,
        choices=[
            ('masculino', 'Masculino'),
            ('femenino', 'Femenino'),
            ('otro', 'Otro')
        ]
    )
    
    # Datos académicos
    categoria_docente = models.CharField(
        max_length=20,
        choices=[
            ('instructor', 'Instructor'),
            ('asistente', 'Asistente'),
            ('auxiliar', 'Auxiliar'),
            ('titular', 'Titular')
        ]
    )
    asignatura = models.CharField(max_length=50)
    
    # Datos institucionales
    solapin = models.CharField(max_length=10, unique=True) 
    # Contacto
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.primer_apellido} ({self.solapin})"

