from django.db import models
from datetime import date
# Create your models here.
# ----------------------------------------
# Modelos de Gestión de Reportes
# ----------------------------------------

class Reporte(models.Model):
    PERIODO_CHOICES = [
        ('primer_semestre', 'Primer Semestre'),
        ('segundo_semestre', 'Segundo Semestre'),
    ]
    # Identificación
    codigo = models.CharField(max_length=20, blank=True, null=True)
    periodo = models.CharField(max_length=20, choices=PERIODO_CHOICES, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True, default=date.today)
    
    # Responsables
    autor = models.CharField(max_length=50, blank=True, null=True)
    institucion = models.CharField(max_length=50, blank=True, null=True)
    
    # Contenido
    resumen = models.TextField(blank=True, null=True)
    objetivos = models.TextField(blank=True, null=True)
    actividades = models.TextField(blank=True, null=True)
    resultados = models.TextField(blank=True, null=True)
    analisis = models.TextField(blank=True, null=True)
    
    # Conclusiones
    desafios = models.TextField(blank=True, null=True)
    proximos_pasos = models.TextField(blank=True, null=True)
    anexos = models.FileField(upload_to='anexos_reportes/', blank=True, null=True)

    # Relación muchos a uno con Grupo
    grupo = models.ForeignKey(
        'grupos.Grupo',
        on_delete=models.CASCADE,
        related_name='reportes'
    )

    def __str__(self):
        return f"Reporte {self.codigo or 'Sin Código'} - {self.grupo or 'Sin Grupo'}"
