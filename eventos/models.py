from django.db import models

# Create your models here.
class Evento(models.Model):
    # Información básica
    nombre_evento = models.CharField(max_length=100)
    descripcion = models.TextField()
    
    # Fecha y hora
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    
    # Detalles del evento
    ubicacion_evento = models.CharField(max_length=100)
    tipo_evento = models.CharField(
        max_length=20,
        choices=[
            ('academico', 'Académico'),
            ('cultural', 'Cultural'),
            ('deportivo', 'Deportivo'),
            ('social', 'Social'),
        ]
    )
    
    # Contacto
    profesor_encargado = models.ForeignKey(
        'profesores.Profesor',
        on_delete=models.SET_NULL,
        related_name="eventos_asociados",
        blank=True,
        null=True
    )
    telefono_contacto = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre_evento
