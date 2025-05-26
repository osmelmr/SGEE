from data_models import models

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

class Respuesta(models.Model):
    # Relación con la tabla Pregunta
    pregunta = models.ForeignKey(
        'Pregunta',
        on_delete=models.CASCADE,
        related_name='respuestas'
    )
    
    # Relación con la tabla Encuesta
    encuesta = models.ForeignKey(
        'Encuesta',
        on_delete=models.CASCADE,
        related_name='respuestas'
    )
    # Contenido de la respuesta
    evaluacion = models.CharField(
        max_length=20, blank=True, null=True)
    fecha_respuesta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Respuesta de {self.usuario} a {self.pregunta.texto}"
# ============================================================================
