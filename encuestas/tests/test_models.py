from django.test import TestCase
from encuestas.models import Encuesta, Pregunta, Respuesta
from django.utils import timezone

class EncuestaModelTest(TestCase):

    def setUp(self):
        self.encuesta = Encuesta.objects.create(
            titulo="Encuesta de Satisfacción",
            descripcion="Evaluación del servicio",
            autor="Profesor X"
        )

    def test_creacion_encuesta(self):
        self.assertEqual(self.encuesta.titulo, "Encuesta de Satisfacción")
        self.assertEqual(self.encuesta.estado, "activa")
        self.assertIsNotNone(self.encuesta.fecha_creacion)
        self.assertEqual(str(self.encuesta), "Encuesta de Satisfacción")

    def test_estado_por_defecto(self):
        nueva = Encuesta.objects.create(titulo="Otra", descripcion="desc")
        self.assertEqual(nueva.estado, "activa")

class PreguntaModelTest(TestCase):

    def setUp(self):
        self.encuesta = Encuesta.objects.create(
            titulo="Encuesta", descripcion="Prueba"
        )
        self.pregunta = Pregunta.objects.create(
            encuesta=self.encuesta,
            texto="¿Qué tan satisfecho estás?"
        )

    def test_pregunta_asociada_a_encuesta(self):
        self.assertEqual(self.pregunta.encuesta, self.encuesta)
        self.assertEqual(str(self.pregunta), f"Pregunta: {self.pregunta.texto} (Encuesta: {self.encuesta.titulo})")

    def test_eliminar_encuesta_elimina_preguntas(self):
        self.encuesta.delete()
        self.assertEqual(Pregunta.objects.count(), 0)

class RespuestaModelTest(TestCase):

    def setUp(self):
        self.encuesta = Encuesta.objects.create(titulo="Encuesta", descripcion="Prueba")
        self.pregunta = Pregunta.objects.create(encuesta=self.encuesta, texto="¿Cómo calificas?")
        self.respuesta = Respuesta.objects.create(
            encuesta=self.encuesta,
            pregunta=self.pregunta,
            evaluacion="Buena"
        )

    def test_creacion_respuesta(self):
        self.assertEqual(self.respuesta.pregunta, self.pregunta)
        self.assertEqual(self.respuesta.encuesta, self.encuesta)
        self.assertEqual(self.respuesta.evaluacion, "Buena")
        self.assertIsNotNone(self.respuesta.fecha_respuesta)

    def test_eliminar_encuesta_elimina_respuestas(self):
        self.encuesta.delete()
        self.assertEqual(Respuesta.objects.count(), 0)

    def test_eliminar_pregunta_elimina_respuestas(self):
        self.pregunta.delete()
        self.assertEqual(Respuesta.objects.count(), 0)

