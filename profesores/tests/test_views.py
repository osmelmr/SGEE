from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from profesores.models import Profesor
from grupos.models import Grupo


class ProfesorViewsTestCase(TestCase):
    def setUp(self):
        # Crear usuario y profesor autenticado
        self.user = User.objects.create_user(username='prof_user', password='testpass')
        self.user.es_profesor = lambda: True  # Simula permiso de profesor
        self.client = Client()
        self.client.login(username='prof_user', password='testpass')

        # Crear profesor inicial
        self.profesor = Profesor.objects.create(
            nombre="Juana",
            primer_apellido="Martínez",
            segundo_apellido="Pérez",
            sexo="F",
            categoria_docente="Titular",
            asignatura="Matemáticas",
            solapin="12345",
            telefono="555-1234",
            correo="juana@example.com",
            descripcion="Profesora experimentada"
        )

        # Grupo de prueba
        self.grupo = Grupo.objects.create(
            nombre="Grupo A",
            direccion="Edificio B",
            curso="9no",
            anio_escolar="2025",
            caracterizacion="Grupo destacado",
            guia=self.profesor
        )

    def test_listar_profesores(self):
        response = self.client.get(reverse('p_profesores'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Juana")

    def test_busqueda_profesores(self):
        response = self.client.get(reverse('p_profesores'), {'q': 'Martínez'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Juana")

    def test_visualizar_profesor(self):
        response = self.client.get(reverse('visualizar_profesor', args=[self.profesor.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Juana")

    def test_crear_profesor_exitoso(self):
        grupo2 = Grupo.objects.create(
            nombre="Grupo B",
            direccion="Edif. 2",
            curso="10mo",
            anio_escolar="2025",
            caracterizacion="Innovador",
            guia=self.profesor
        )
        data = {
            'nombre': 'Carlos',
            'primer_apellido': 'Ramírez',
            'segundo_apellido': 'Soto',
            'sexo': 'M',
            'categoria_docente': 'Asistente',
            'asignatura': 'Historia',
            'solapin': '98765',
            'telefono': '555-6789',
            'correo': 'carlos@example.com',
            'descripcion': 'Nuevo profesor',
            'grupos': [grupo2.id],
            'grupo_asignado': grupo2.id
        }
        response = self.client.post(reverse('formular_profesor'), data)
        self.assertRedirects(response, reverse('p_profesores'))
        self.assertTrue(Profesor.objects.filter(nombre='Carlos').exists())

    def test_crear_profesor_invalido(self):
        response = self.client.post(reverse('formular_profesor'), {})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Todos los campos obligatorios")

    def test_modificar_profesor(self):
        data = {
            'nombre': 'Juana Actualizada',
            'primer_apellido': 'Martínez',
            'segundo_apellido': 'Pérez',
            'sexo': 'F',
            'categoria_docente': 'Titular',
            'asignatura': 'Física',
            'solapin': '12345',
            'telefono': '555-0000',
            'correo': 'juana.nueva@example.com',
            'descripcion': 'Actualización de datos',
            'grupos': [self.grupo.id]
        }
        response = self.client.post(reverse('modificar_profesor', args=[self.profesor.id]), data)
        self.assertRedirects(response, reverse('p_profesores'))
        self.profesor.refresh_from_db()
        self.assertEqual(self.profesor.nombre, 'Juana Actualizada')

    def test_eliminar_profesor(self):
        response = self.client.post(reverse('eliminar_profesor', args=[self.profesor.id]))
        self.assertRedirects(response, reverse('p_profesores'))
        self.assertFalse(Profesor.objects.filter(id=self.profesor.id).exists())

    def test_eliminar_profesores_multiples(self):
        profesor2 = Profesor.objects.create(
            nombre="Laura", primer_apellido="Sosa", segundo_apellido="Lopez",
            sexo="F", categoria_docente="Instructor", asignatura="Química",
            solapin="00002", telefono="555-4321", correo="laura@example.com", descripcion="Nueva profe"
        )
        data = {'profesores[]': [self.profesor.id, profesor2.id]}
        response = self.client.post(reverse('eliminar_profesores'), data)
        self.assertRedirects(response, reverse('p_profesores'))
        self.assertEqual(Profesor.objects.count(), 0)

    def test_eliminar_profesores_metodo_invalido(self):
        response = self.client.get(reverse('eliminar_profesores'))
        self.assertEqual(response.status_code, 405)
        self.assertJSONEqual(response.content, {'error': 'Método no permitido'})

    def test_requiere_autenticacion(self):
        self.client.logout()
        response = self.client.get(reverse('p_profesores'))
        self.assertRedirects(response, reverse('login'))

    def test_requiere_permiso_profesor(self):
        self.user.es_profesor = lambda: False
        response = self.client.get(reverse('p_profesores'))
        self.assertRedirects(response, reverse('pagina_principal'))
