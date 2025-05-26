from django.db import models

# Create your models here.
# ----------------------------------------
# Modelos de Gestión de Reportes
# ----------------------------------------

class Reporte(models.Model):
    # Identificación
    codigo = models.CharField(max_length=10, blank=True, null=True)
    periodo = models.CharField(max_length=10, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    
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
    anexos = models.FileField(upload_to='anexos/', blank=True, null=True)

    # Relación muchos a uno con Grupo
    grupo = models.ForeignKey(
        'grupos.Grupo',
        on_delete=models.CASCADE,
        related_name='reportes'
    )

    def __str__(self):
        return f"Reporte {self.codigo or 'Sin Código'} - {self.grupo or 'Sin Grupo'}"

# ============================================================================
