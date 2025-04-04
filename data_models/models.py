from django.db import models

# ============================================================================
# Modelos de Gestión Académica
# ============================================================================

# ----------------------------------------
# Modelo para la gestión de estrategias educativas
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
    dir_brigada = models.CharField(max_length=255, blank=True, default="direccion_brigada_{id}")
    caract_brigada = models.TextField(blank=True, default="caracteristicas_brigada_{id}")
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

    # Restricción para evitar duplicación de curso, año escolar y grupo
    class Meta:
        unique_together = ('curso', 'anio_escolar', 'grupo')

    def __str__(self):
        return f"Estrategia: {self.nombre or 'Sin nombre'} ({self.curso} - {self.anio_escolar} - {self.grupo})"


# ----------------------------------------
# Modelo para la gestión de eventos académicos y extracurriculares
# ----------------------------------------
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
    profesor_cargo = models.CharField(max_length=50)
    telefono_contacto = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre_evento


# ============================================================================
# Modelos de Gestión de Personal
# ============================================================================

# ----------------------------------------
# Modelo para la gestión de información de profesores
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
    brigada_asignada = models.CharField(max_length=10)
    brigadas_impartir = models.CharField(max_length=50)
    
    # Contacto
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.primer_apellido} ({self.solapin})"


# ----------------------------------------
# Modelo para la gestión de brigadas estudiantiles
# ----------------------------------------
class Brigada(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    direccion = models.CharField(max_length=100)
    caracterizacion = models.TextField()
    profesores = models.ManyToManyField('Profesor', through='Colectivo', related_name='brigadas')

    def __str__(self):
        return self.nombre


# ----------------------------------------
# Modelo para la gestión de colectivos pedagógicos
# ----------------------------------------
class Colectivo(models.Model):
    profesor = models.ForeignKey('Profesor', on_delete=models.CASCADE)
    brigada = models.ForeignKey('Brigada', on_delete=models.CASCADE)
    rol = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.profesor} - {self.brigada}"


# ============================================================================
# Modelos de Gestión de Reportes
# ============================================================================

# ----------------------------------------
# Modelo para la gestión de reportes institucionales
# ----------------------------------------
class Reporte(models.Model):
    # Identificación
    brigada = models.CharField(max_length=10, blank=True, null=True)
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

    def __str__(self):
        return f"Reporte {self.codigo or 'Sin Código'} - {self.brigada or 'Sin Brigada'}"


# ----------------------------------------
# Modelo para la gestión de encuestas
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


# ----------------------------------------
# Modelo para la gestión de preguntas de encuestas
# ----------------------------------------
class Pregunta(models.Model):
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE, related_name='preguntas')
    texto = models.CharField(max_length=255)

    def __str__(self):
        return f"Pregunta: {self.texto} (Encuesta: {self.encuesta.titulo})"


# ============================================================================
# Modelos de Gestión de Usuarios
# ============================================================================

# ----------------------------------------
# Modelo para el registro y gestión de usuarios
# ----------------------------------------
class RegistroUsuario(models.Model):
    # Datos personales
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
    
    # Datos institucionales
    grupo = models.CharField(max_length=50)
    solapin = models.CharField(max_length=10)
    cargo = models.CharField(max_length=50)
    
    # Contacto
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(max_length=50)
    
    # Credenciales
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


