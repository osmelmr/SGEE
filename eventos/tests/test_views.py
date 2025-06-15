from django.test import TestCase, Client
from django.urls import reverse
from usuarios.models import Usuario
from profesores.models import Profesor
from eventos.models import Evento
from datetime import date, time

class EventoViewsTestCase(TestCase):
    def setUp(self):
        # Crear usuario correctamente
        self.user = Usuario.objects.create_user(
            username='profesor1',
            password='testpass',
            rol='profesor_principal',
            sexo='masculino',
            solapin='12345'
        )

        # Crear profesor
        self.profesor = Profesor.objects.create(
            nombre="Juan",
            primer_apellido="Perez",
            sexo="masculino",
            categoria_docente="titular",
            asignatura="Matemáticas",
            solapin="123456",
            telefono="5551234567",
            correo="juanperez@example.com",
            descripcion="Profesor con experiencia en matemáticas avanzadas."
        )

        # Crear cliente autenticado
        self.client = Client()
        self.client.login(username='profesor1', password='testpass')

        # Crear evento de ejemplo
        self.evento = Evento.objects.create(
            nombre_evento="Evento de Prueba",
            fecha_inicio=date.today(),
            fecha_fin=date.today(),
            hora_inicio=time(9, 0),
            hora_fin=time(11, 0),
            ubicacion_evento="Sala 101",
            tipo_evento="Conferencia",
            descripcion="Descripción de prueba",
            profesor_encargado=self.profesor,
            telefono_contacto="12345678"
        )

    def test_visualizar_eventos(self):
        response = self.client.get(reverse('eventos'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Evento de Prueba")

    def test_crear_evento(self):
        data = {
            'nombre_evento': "Nuevo Evento",
            'fecha_inicio': "2025-06-07",
            'fecha_fin': "2025-06-08",
            'hora_inicio': "10:00",
            'hora_fin': "12:00",
            'ubicacion_evento': "Sala 102",
            'tipo_evento': "Taller",
            'descripcion': "Un evento nuevo",
            'profesor_encargado': self.profesor.id,
            'telefono_contacto': "87654321"
        }
        response = self.client.post(reverse('p_formular_evento'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Evento.objects.filter(nombre_evento="Nuevo Evento").exists())

    def test_eliminar_evento(self):
        response = self.client.post(reverse('p_eliminar_evento', args=[self.evento.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Evento.objects.filter(id=self.evento.id).exists())

    def test_modificar_evento(self):
        data = {
            'nombre_evento': "Evento Modificado",
            'fecha_inicio': "2025-06-07",
            'fecha_fin': "2025-06-08",
            'hora_inicio': "10:00",
            'hora_fin': "12:00",
            'ubicacion_evento': "Sala 103",
            'tipo_evento': "academico",
            'descripcion': "Descripción modificada",
            'profesor_encargado': str(self.profesor.id),
            'telefono_contacto': "99999999"
        }
        response = self.client.post(reverse('p_modificar_evento', args=[self.evento.id]), data)  # <--- aquí agregas data
        self.assertEqual(response.status_code, 302)
        evento = Evento.objects.get(id=self.evento.id)
        self.assertEqual(evento.nombre_evento, "Evento Modificado")

    def test_visualizar_evento(self):
        response = self.client.get(reverse('visualizar_evento', args=[self.evento.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Evento de Prueba")

    def test_eliminar_eventos_multiples(self):
        otro_evento = Evento.objects.create(
            nombre_evento="Otro Evento",
            fecha_inicio=date.today(),
            fecha_fin=date.today(),
            hora_inicio=time(14, 0),
            hora_fin=time(16, 0),
            ubicacion_evento="Sala 105",
            tipo_evento="Charla",
            descripcion="Otro evento",
            profesor_encargado=self.profesor,
            telefono_contacto="11223344"
        )
        data = {'eventos[]': [self.evento.id, otro_evento.id]}
        response = self.client.post(reverse('p_eliminar_eventos'), data)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Evento.objects.filter(id=self.evento.id).exists())
        self.assertFalse(Evento.objects.filter(id=otro_evento.id).exists())
