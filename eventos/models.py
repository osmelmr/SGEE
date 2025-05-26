from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta

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
    telefono_contacto = models.CharField(max_length=15,null=True, blank=True)

    def clean(self):
        # Si las fechas son iguales, validar las horas
        if self.fecha_inicio == self.fecha_fin:
            if self.hora_inicio >= self.hora_fin:
                raise ValidationError("La hora de inicio debe ser menor que la hora de fin si la fecha es la misma.")
            # Calcular la diferencia en horas
            dt_inicio = datetime.combine(self.fecha_inicio, self.hora_inicio)
            dt_fin = datetime.combine(self.fecha_fin, self.hora_fin)
            if (dt_fin - dt_inicio) < timedelta(hours=2):
                raise ValidationError("Debe haber al menos 2 horas de diferencia entre la hora de inicio y fin si la fecha es la misma.")

    def __str__(self):
        return self.nombre_evento
