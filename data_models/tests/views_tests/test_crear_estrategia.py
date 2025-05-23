'''
python manage.py test data_models.tests.views_tests.test_crear_estrategia

'''

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from data_models.models import Usuario, Grupo, Estrategia

class TestCrearEstrategia(TestCase):
    def setUp(self):
        self.client = Client()

        # Crear usuario profesor
        self.profesor = Usuario.objects.create_user(
            username="profesor1",
            password="1234",
            cargo="profesor_principal",
            sexo="masculino",
            solapin="12345",
            telefono="5551234"
        )

        # Crear grupo de prueba
        self.grupo = Grupo.objects.create(
            nombre="IDF301",
            direccion="Jefe De Brigada",
            curso="2024-2025",
            anio_escolar="tercero",
            caracterizacion="Grupo activo y participativo"
        )

        self.url = reverse("formular_estrategia")
        self.client.login(username="profesor1", password="1234")

    def test_get_formulario_renderiza_correctamente(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form')
        self.assertContains(response, 'name="nombre"')

    def test_post_formulario_crea_estrategia_correctamente(self):
        form_data = {
            "nombre": "Mi Estrategia",
            "curso": "2024-2025",
            "anio_escolar": "tercero",
            "grupo": self.grupo.nombre,
            "plan_estudios": "plan de estudios",
            "obj_estrategia": "objetivos",
            "dir_grupo": "direccion",
            "caract_grupo": "caracteristicas",
            "colect_pedagogico": "colectivo",
            "otros_aspectos": "otros",
            "dim_curricular": "dim 1",
            "dim_extensionista": "dim 2",
            "dim_politica": "dim 3",
            "conclusiones": "conclusiones",
            "obj_general": "objetivo general",
            "obj_dc": "obj dc",
            "plan_dc": "plan dc",
            "obj_de": "obj de",
            "plan_de": "plan de",
            "obj_dp": "obj dp",
            "plan_dp": "plan dp",
            "evaluacion": "evaluacion",
            "autor": "profesor1"
        }

        response = self.client.post(self.url, data=form_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Estrategia.objects.filter(nombre="Mi Estrategia").exists())

        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("Estrategia registrada correctamente." in str(m) for m in messages))

    def test_usuario_no_autenticado_redirige_a_login(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertRedirects(response, reverse("login"))

    def test_usuario_sin_permiso_redirige_con_error(self):
        self.client.logout()
        no_profesor = Usuario.objects.create_user(
            username="normaluser",
            password="abcd",
            cargo="usuario",
            sexo="otro",
            solapin="54321"
        )
        self.client.login(username="normaluser", password="abcd")
        response = self.client.get(self.url, follow=True)
        self.assertContains(response, "No tienes permiso para crear estrategias.")

    def test_post_con_datos_invalidos_muestra_error(self):
        form_data = {
            "nombre": "",  # nombre vacío intencionalmente
            "grupo": self.grupo.nombre
        }
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Error al registrar la estrategia")
