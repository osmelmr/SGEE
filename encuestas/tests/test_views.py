from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from encuestas.models import Encuesta

User = get_user_model()

class EncuestaViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

        # Crear usuario profesor
        self.profesor = User.objects.create_user(username="profe", password="1234", es_profesor=True)

        # Crear usuario no profesor
        self.no_profesor = User.objects.create_user(username="alumno", password="1234", es_profesor=False)

        # Encuesta de prueba
        self.encuesta = Encuesta.objects.create(
            titulo="Encuesta Test",
            descripcion="Desc Test",
            autor="Autor X",
            estado="Borrador"
        )

    def test_visualizar_encuestas_auth_profesor(self):
        self.client.login(username="profe", password="1234")
        response = self.client.get(reverse("p_encuestas"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Encuesta Test")

    def test_visualizar_encuestas_sin_login(self):
        response = self.client.get(reverse("p_encuestas"))
        self.assertRedirects(response, reverse("login"))

    def test_visualizar_encuestas_usuario_no_profesor(self):
        self.client.login(username="alumno", password="1234")
        response = self.client.get(reverse("p_encuestas"))
        self.assertRedirects(response, reverse("pagina_principal"))

    def test_crear_encuesta_post_valida(self):
        self.client.login(username="profe", password="1234")
        response = self.client.post(reverse("crear_encuesta"), {
            "titulo": "Nueva",
            "descripcion": "Descripcion",
            "autor": "Prof. A",
            "estado": "Activa",
            "preguntas[]": ["¿Pregunta 1?", "¿Pregunta 2?"]
        })
        self.assertRedirects(response, reverse("p_encuestas"))
        self.assertEqual(Encuesta.objects.count(), 2)

    def test_crear_encuesta_get(self):
        self.client.login(username="profe", password="1234")
        response = self.client.get(reverse("crear_encuesta"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<form")

    def test_modificar_encuesta(self):
        self.client.login(username="profe", password="1234")
        url = reverse("modificar_encuesta", args=[self.encuesta.id])
        response = self.client.post(url, {
            "titulo": "Modificado",
            "descripcion": "Desc nueva",
            "autor": "Mod",
            "estado": "Activa",
            "preguntas[]": ["Pregunta modificada"]
        })
        self.assertRedirects(response, reverse("p_encuestas"))
        self.encuesta.refresh_from_db()
        self.assertEqual(self.encuesta.titulo, "Modificado")

    def test_visualizar_encuesta(self):
        self.client.login(username="profe", password="1234")
        url = reverse("visualizar_encuesta", args=[self.encuesta.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.encuesta.titulo)

    def test_eliminar_encuesta(self):
        self.client.login(username="profe", password="1234")
        url = reverse("eliminar_encuesta", args=[self.encuesta.id])
        response = self.client.post(url)
        self.assertRedirects(response, reverse("p_encuestas"))
        self.assertFalse(Encuesta.objects.filter(id=self.encuesta.id).exists())

    def test_eliminar_encuestas_multiples(self):
        self.client.login(username="profe", password="1234")
        otra_encuesta = Encuesta.objects.create(
            titulo="Otra", descripcion="Desc", autor="X", estado="Borrador"
        )
        response = self.client.post(reverse("eliminar_encuestas"), {
            "encuestas[]": [self.encuesta.id, otra_encuesta.id]
        })
        self.assertRedirects(response, reverse("p_encuestas"))
        self.assertEqual(Encuesta.objects.count(), 0)
