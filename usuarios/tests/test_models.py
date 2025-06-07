from django.test import TestCase
from usuarios.models import Usuario
from encuestas.models import Encuesta
from eventos.models import Evento

class UsuarioModelTest(TestCase):

    def setUp(self):
        self.usuario_data = {
            "username": "juanperez",
            "password": "testpass123",
            "rol": "usuario",
            "sexo": "masculino",
            "solapin": "JP123",
            "telefono": "555-1234",
        }

        self.profesor_data = {
            "username": "profesorx",
            "password": "testpass456",
            "rol": "profesor_principal",
            "sexo": "femenino",
            "solapin": "PX456",
        }

    def test_crear_usuario_normal(self):
        usuario = Usuario.objects.create_user(**self.usuario_data)
        self.assertEqual(usuario.username, "juanperez")
        self.assertFalse(usuario.is_staff)
        self.assertFalse(usuario.is_superuser)
        self.assertTrue(usuario.es_usuario())
        self.assertFalse(usuario.es_profesor())

    def test_crear_profesor_principal(self):
        profesor = Usuario.objects.create_user(**self.profesor_data)
        profesor.save()
        self.assertEqual(profesor.username, "profesorx")
        self.assertTrue(profesor.is_staff)
        self.assertTrue(profesor.is_superuser)
        self.assertTrue(profesor.es_profesor())
        self.assertFalse(profesor.es_usuario())

    def test_str_representation(self):
        usuario = Usuario.objects.create_user(**self.usuario_data)
        self.assertEqual(str(usuario), "juanperez (usuario)")

    def test_username_unique(self):
        Usuario.objects.create_user(**self.usuario_data)
        with self.assertRaises(Exception):
            Usuario.objects.create_user(**self.usuario_data)

    def test_many_to_many_encuestas_eventos(self):
        user = Usuario.objects.create_user(**self.usuario_data)
        encuesta = Encuesta.objects.create(
            titulo="Encuesta 1",
            descripcion="Prueba",
            autor="admin"
        )
        evento = Evento.objects.create(
            nombre_evento="Evento 1",
            descripcion="Descripción",
            fecha_inicio="2025-06-10",
            fecha_fin="2025-06-10",
            hora_inicio="08:00:00",
            hora_fin="10:30:00",
            ubicacion_evento="Auditorio",
            tipo_evento="academico"
        )
        user.encuestas_realizadas.add(encuesta)
        user.eventos.add(evento)
        self.assertIn(encuesta, user.encuestas_realizadas.all())
        self.assertIn(evento, user.eventos.all())
