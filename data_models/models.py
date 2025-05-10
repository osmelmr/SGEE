from django.db import models
from django.contrib.auth.models import AbstractUser

# ============================================================================

# ----------------------------------------
# Modelos de Gestión de Personal
# ----------------------------------------

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

# ============================================================================

# ----------------------------------------
# Modelos de Gestión de Reportes
# ----------------------------------------

class Reporte(models.Model):
    # Identificación
    grupo = models.CharField(max_length=10, blank=True, null=True)
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

    # Relación muchos a uno con Estrategia
    estrategia = models.ForeignKey(
        'Estrategia',
        on_delete=models.CASCADE,
        related_name='reportes'
    )

    def __str__(self):
        return f"Reporte {self.codigo or 'Sin Código'} - {self.grupo or 'Sin Grupo'}"

# ============================================================================

# ----------------------------------------
# Modelos de Gestión de Encuestas
# ----------------------------------------

class Encuesta(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=100, default="Desconocido")
    estado = models.CharField(
        max_length=10,
        choices=[
            ('activa', 'Activa'),
            ('inactiva', 'Inactiva'),
        ],
        default='activa'
    )

    def __str__(self):
        return self.titulo


class Pregunta(models.Model):
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE, related_name='preguntas')
    texto = models.CharField(max_length=255)

    def __str__(self):
        return f"Pregunta: {self.texto} (Encuesta: {self.encuesta.titulo})"

# ============================================================================

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
    encuestas = models.ManyToManyField(
        'Encuesta',
        related_name='usuarios',
        blank=True
    )
    eventos = models.ManyToManyField(
        'Evento',
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

# ----------------------------------------
# Modelos de Gestión Académica
# ----------------------------------------

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
        'Grupo',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='estrategia'
    )

    class Meta:
        unique_together = ('curso', 'grupo')

    def __str__(self):
        return f"Estrategia: {self.nombre or 'Sin nombre'} ({self.curso} - {self.anio_escolar} - {self.grupo})"


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
        'Profesor',
        on_delete=models.SET_NULL,
        related_name="eventos_asociados",
        blank=True,
        null=True
    )
    telefono_contacto = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre_evento


