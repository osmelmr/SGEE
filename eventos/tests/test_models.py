from django.test import TestCase
from eventos.models import Evento
from profesores.models import Profesor  # Asegúrate que el modelo exista
from django.core.exceptions import ValidationError
from datetime import date, time, timedelta

class EventoModelTest(TestCase):

    def setUp(self):
        self.profesor = Profesor.objects.create(
            nombre="Juan",
            primer_apellido="Pérez",
            segundo_apellido="Gómez",
            sexo="masculino",
            categoria_docente="titular",
            asignatura="Matemáticas",
            solapin="123456",
            telefono="5551234567",
            correo="juanperez@example.com",
            descripcion="Profesor con experiencia en matemáticas avanzadas."
        )

    def test_creacion_evento_valido(self):
        """Debe permitir crear un evento válido con duración mínima de 2 horas."""
        evento = Evento(
            nombre_evento="Conferencia Académica",
            descripcion="Conferencia sobre inteligencia artificial.",
            fecha_inicio=date.today(),
            fecha_fin=date.today(),
            hora_inicio=time(10, 0),
            hora_fin=time(12, 0),
            ubicacion_evento="Aula Magna",
            tipo_evento="academico",
            profesor_encargado=self.profesor,
            telefono_contacto="5551234567"
        )
        evento.full_clean()  # No debe lanzar errores
        evento.save()
        self.assertEqual(str(evento), "Conferencia Académica")

    def test_error_misma_fecha_hora_invalida(self):
        """Debe lanzar un error si hora_fin <= hora_inicio en la misma fecha."""
        evento = Evento(
            nombre_evento="Evento Inválido",
            descripcion="Horas inválidas.",
            fecha_inicio=date.today(),
            fecha_fin=date.today(),
            hora_inicio=time(15, 0),
            hora_fin=time(14, 0),
            ubicacion_evento="Sala B",
            tipo_evento="social",
            profesor_encargado=self.profesor
        )
        with self.assertRaises(ValidationError) as context:
            evento.full_clean()
        self.assertIn("La hora de inicio debe ser menor que la hora de fin", str(context.exception))

    def test_error_misma_fecha_duracion_insuficiente(self):
        """Debe lanzar error si duración es menor a 2 horas con misma fecha."""
        evento = Evento(
            nombre_evento="Evento Corto",
            descripcion="Duración menor a 2 horas.",
            fecha_inicio=date.today(),
            fecha_fin=date.today(),
            hora_inicio=time(10, 0),
            hora_fin=time(11, 0),
            ubicacion_evento="Biblioteca",
            tipo_evento="cultural",
            profesor_encargado=self.profesor
        )
        with self.assertRaises(ValidationError) as context:
            evento.full_clean()
        self.assertIn("Debe haber al menos 2 horas de diferencia", str(context.exception))

    def test_evento_fechas_diferentes_permite_cualquier_hora(self):
        """Si las fechas son diferentes, no se debe validar la duración mínima."""
        evento = Evento(
            nombre_evento="Evento de Dos Días",
            descripcion="No necesita validación de horas.",
            fecha_inicio=date.today(),
            fecha_fin=date.today() + timedelta(days=1),
            hora_inicio=time(22, 0),
            hora_fin=time(1, 0),
            ubicacion_evento="Gimnasio",
            tipo_evento="deportivo",
            profesor_encargado=self.profesor
        )
        evento.full_clean()  # No debe lanzar errores
        evento.save()
        self.assertTrue(Evento.objects.filter(nombre_evento="Evento de Dos Días").exists())
