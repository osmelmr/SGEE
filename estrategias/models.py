from django.db import models

# Create your models here.
class Estrategia(models.Model):
    # Campos únicos
    curso = models.CharField(max_length=20)
    anio_escolar = models.CharField(max_length=10)
    grupo = models.CharField(max_length=20)

    # Información general
    nombre = models.CharField(max_length=255, blank=True, default="Estrategia_{id}")
    autor = models.CharField(max_length=255, blank=True, default="autor_{id}")
    plan_estudios = models.TextField(blank=True, default="plan_estudios_{id}")
    
    # Objetivos y características
    obj_general = models.TextField(blank=True, default="objetivo_general_{id}")
    obj_estrategia = models.TextField(blank=True, default="objetivos_estrategia_{id}")
    dir_grupo = models.CharField(max_length=255, blank=True, default="direccion_grupo_{id}")
    caract_grupo = models.TextField(blank=True, default="caracteristicas_grupo_{id}")
    colect_pedagogico = models.TextField(blank=True, default="colectivo_pedagogico_{id}")
    
    # Dimensiones
    dim_curricular = models.TextField(blank=True, default="dimension_curricular_{id}")
    dim_extensionista = models.TextField(blank=True, default="dimension_extensionista_{id}")
    dim_politica = models.TextField(blank=True, default="dimension_politico_ideologica_{id}")
    
    # Objetivos específicos y planes
    obj_dc = models.TextField(blank=True, default="obj_dc_{id}")
    plan_dc = models.TextField(blank=True, default="plan_dc_{id}")
    obj_de = models.TextField(blank=True, default="obj_de_{id}")
    plan_de = models.TextField(blank=True, default="plan_de_{id}")
    obj_dp = models.TextField(blank=True, default="obj_dp_{id}")
    plan_dp = models.TextField(blank=True, default="plan_dp_{id}")
    
    # Evaluación y otros aspectos
    evaluacion = models.TextField(blank=True, default="evaluacion_integral_{id}")
    otros_aspectos = models.TextField(blank=True, default="otros_aspectos_{id}")
    conclusiones = models.TextField(blank=True, default="conclusiones_{id}")

    # Relación uno a uno con Grupo (opcional)
    grupo_id = models.OneToOneField(
        'grupos.Grupo',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='estrategia'
    )

    class Meta:
        unique_together = ('curso', 'grupo')

    def __str__(self):
        return f"Estrategia: {self.nombre or 'Sin nombre'} ({self.curso} - {self.anio_escolar} - {self.grupo})"
