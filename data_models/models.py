from django.db import models

# Create your models here.
class Estrategia(models.Model):
    # Campos únicos
    curso = models.CharField(max_length=20)
    anio_escolar = models.CharField(max_length=10)
    grupo = models.CharField(max_length=20)

    # Otros campos
    nombre = models.CharField(max_length=255, blank=True, default="Estrategia_{id}")
    plan_estudios = models.TextField(blank=True, default="plan_estudios_{id}")
    obj_estrategia = models.TextField(blank=True, default="objetivos_estrategia_{id}")
    dir_brigada = models.CharField(max_length=255, blank=True, default="direccion_brigada_{id}")
    caract_brigada = models.TextField(blank=True, default="caracteristicas_brigada_{id}")
    colect_pedagogico = models.TextField(blank=True, default="colectivo_pedagogico_{id}")
    otros_aspectos = models.TextField(blank=True, default="otros_aspectos_{id}")
    dim_curricular = models.TextField(blank=True, default="dimension_curricular_{id}")
    dim_extensionista = models.TextField(blank=True, default="dimension_extensionista_{id}")
    dim_politica = models.TextField(blank=True, default="dimension_politico_ideologica_{id}")
    conclusiones = models.TextField(blank=True, default="conclusiones_{id}")
    obj_general = models.TextField(blank=True, default="objetivo_general_{id}")
    obj_dc = models.TextField(blank=True, default="obj_dc_{id}")
    plan_dc = models.TextField(blank=True, default="plan_dc_{id}")
    obj_de = models.TextField(blank=True, default="obj_de_{id}")
    plan_de = models.TextField(blank=True, default="plan_de_{id}")
    obj_dp = models.TextField(blank=True, default="obj_dp_{id}")
    plan_dp = models.TextField(blank=True, default="plan_dp_{id}")
    evaluacion = models.TextField(blank=True, default="evaluacion_integral_{id}")
    autor = models.CharField(max_length=255, blank=True, default="autor_{id}")

    # Restricción para evitar duplicación de curso, año escolar y grupo
    class Meta:
        unique_together = ('curso', 'anio_escolar', 'grupo')

    # Representación de la estrategia
    def __str__(self):
        return f"Estrategia: {self.nombre or 'Sin nombre'} ({self.curso} - {self.anio_escolar} - {self.grupo})"

class Evento(models.Model):
    # Relación con Estrategia
    estrategia = models.ForeignKey('Estrategia', on_delete=models.CASCADE, related_name='eventos')

    # Campo: Nombre del Evento
    nombre_evento = models.CharField(max_length=100)

    # Campos: Fechas de Inicio y Fin
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    # Campos: Horas de Inicio y Fin
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    # Campo: Ubicación
    ubicacion_evento = models.CharField(max_length=100)

    # Campo: Tipo de Evento
    TIPOS_EVENTO = [
        ('academico', 'Académico'),
        ('cultural', 'Cultural'),
        ('deportivo', 'Deportivo'),
        ('social', 'Social')
    ]
    tipo_evento = models.CharField(max_length=20, choices=TIPOS_EVENTO)

    # Campo: Descripción
    descripcion_evento = models.TextField()

    # Campos: Profesor a Cargo y Teléfono de Contacto
    profesor_cargo = models.CharField(max_length=50)
    telefono_contacto = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre_evento

class Profesor(models.Model):
    # Nombre
    nombre = models.CharField(max_length=50)

    # Apellidos
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50, blank=True, null=True)

    # Sexo y Categoría Docente
    SEXO_CHOICES = [
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('otro', 'Otro'),
    ]
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES)

    CATEGORIA_CHOICES = [
        ('instructor', 'Instructor'),
        ('asistente', 'Asistente'),
        ('auxiliar', 'Auxiliar'),
        ('titular', 'Titular'),
    ]
    categoria_docente = models.CharField(max_length=10, choices=CATEGORIA_CHOICES)

    # Asignatura y Solapín
    asignatura = models.CharField(max_length=50)
    solapin = models.CharField(max_length=10)

    # Teléfono y Correo
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(max_length=50)

    # Brigada Asignada y Brigadas a Impartir
    brigada_asignada = models.CharField(max_length=10)
    brigadas_impartir = models.TextField()

    # Descripción
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.primer_apellido} ({self.categoria_docente})"

class Reporte(models.Model):
    brigada = models.CharField(max_length=10)
    codigo = models.CharField(max_length=10)
    periodo = models.CharField(max_length=10)
    fecha = models.DateField()
    autor = models.CharField(max_length=50)
    institucion = models.CharField(max_length=50)
    resumen = models.TextField()
    objetivos = models.TextField()
    actividades = models.TextField()
    resultados = models.TextField()
    analisis = models.TextField()
    desafios = models.TextField()
    proximos_pasos = models.TextField()
    anexos = models.FileField(upload_to='anexos/', blank=True, null=True)


class RegistroUsuario(models.Model):
    nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50, blank=True, null=True)
    sexo = models.CharField(
        max_length=10,
        choices=[
            ('masculino', 'Masculino'),
            ('femenino', 'Femenino'),
            ('otro', 'Otro')
        ]
    )
    grupo = models.CharField(max_length=50)
    solapin = models.CharField(max_length=10)
    cargo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(max_length=50)
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Encuesta(models.Model):
    pregunta1 = models.CharField(
        max_length=20,
        choices=[
            ('muy-bien', 'Muy bien'),
            ('bien', 'Bien'),
            ('normal', 'Normal'),
            ('mal', 'Mal'),
            ('pesimo', 'Pésimo')
        ]
    )
    pregunta2 = models.CharField(
        max_length=20,
        choices=[
            ('muy-bien', 'Muy bien'),
            ('bien', 'Bien'),
            ('normal', 'Normal'),
            ('mal', 'Mal'),
            ('pesimo', 'Pésimo')
        ]
    )
    pregunta3 = models.CharField(
        max_length=20,
        choices=[
            ('muy-bien', 'Muy bien'),
            ('bien', 'Bien'),
            ('normal', 'Normal'),
            ('mal', 'Mal'),
            ('pesimo', 'Pésimo')
        ]
    )
    pregunta4 = models.CharField(
        max_length=20,
        choices=[
            ('muy-bien', 'Muy bien'),
            ('bien', 'Bien'),
            ('normal', 'Normal'),
            ('mal', 'Mal'),
            ('pesimo', 'Pésimo')
        ]
    )
    pregunta5 = models.CharField(
        max_length=20,
        choices=[
            ('muy-bien', 'Muy bien'),
            ('bien', 'Bien'),
            ('normal', 'Normal'),
            ('mal', 'Mal'),
            ('pesimo', 'Pésimo')
        ]
    )
    pregunta6 = models.CharField(
        max_length=20,
        choices=[
            ('muy-bien', 'Muy bien'),
            ('bien', 'Bien'),
            ('normal', 'Normal'),
            ('mal', 'Mal'),
            ('pesimo', 'Pésimo')
        ]
    )


