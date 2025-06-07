import tempfile
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from reportes.models import Reporte
from grupos.models import Grupo
from django.core.files.uploadedfile import SimpleUploadedFile

class ReporteViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.password = "testpassword"
        self.user = User.objects.create_user(username="profesor1", password=self.password)

        # Simular que el usuario es un profesor
        self.user.es_profesor = lambda: True

        self.client.login(username="profesor1", password=self.password)

        self.grupo = Grupo.objects.create(nombre="Grupo 1")
        self.reporte = Reporte.objects.create(
            grupo=self.grupo,
            periodo="2024",
            autor="Autor Test",
            institucion="Instituto Test",
            resumen="Resumen...",
            objetivos="Objetivos...",
            actividades="Actividades...",
            resultados="Resultados...",
            analisis="Análisis...",
            desafios="Desafíos...",
            proximos_pasos="Próximos pasos..."
        )

    def test_visualizar_reportes(self):
        response = self.client.get(reverse('p_reportes'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Autor Test")

    def test_visualizar_reporte(self):
        response = self.client.get(reverse('visualizar_reporte', args=[self.reporte.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Resumen")

    def test_crear_reporte(self):
        with tempfile.NamedTemporaryFile(suffix=".jpg") as tmp_file:
            tmp_file.write(b"\x00\x01\x02")
            tmp_file.seek(0)
            image = SimpleUploadedFile("image.jpg", tmp_file.read(), content_type="image/jpeg")
            data = {
                "grupo": self.grupo.id,
                "periodo": "2025",
                "autor": "Nuevo Autor",
                "institucion": "Nueva Institución",
                "resumen": "Resumen test",
                "objetivos": "Objetivos test",
                "actividades": "Actividades test",
                "resultados": "Resultados test",
                "analisis": "Analisis test",
                "desafios": "Desafios test",
                "proximos_pasos": "Pasos test",
                "anexos": image,
            }
            response = self.client.post(reverse("crear_reporte"), data, follow=True)
            self.assertEqual(response.status_code, 200)
            self.assertTrue(Reporte.objects.filter(autor="Nuevo Autor").exists())

    def test_modificar_reporte(self):
        data = {
            "grupo": self.grupo.id,
            "periodo": "2026",
            "autor": "Modificado",
            "institucion": "Inst Mod",
            "resumen": "Resumen mod",
            "objetivos": "Objetivos mod",
            "actividades": "Actividades mod",
            "resultados": "Resultados mod",
            "analisis": "Analisis mod",
            "desafios": "Desafios mod",
            "proximos_pasos": "Pasos mod",
        }
        response = self.client.post(reverse("modificar_reporte", args=[self.reporte.id]), data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.reporte.refresh_from_db()
        self.assertEqual(self.reporte.autor, "Modificado")

    def test_eliminar_reporte(self):
        response = self.client.get(reverse("eliminar_reporte", args=[self.reporte.id]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Reporte.objects.filter(id=self.reporte.id).exists())

    def test_eliminar_reportes_multiple(self):
        reporte2 = Reporte.objects.create(
            grupo=self.grupo,
            periodo="2024",
            autor="Otro",
            institucion="x",
            resumen="x",
            objetivos="x",
            actividades="x",
            resultados="x",
            analisis="x",
            desafios="x",
            proximos_pasos="x"
        )
        data = {"reportes[]": [self.reporte.id, reporte2.id]}
        response = self.client.post(reverse("eliminar_reportes"), data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Reporte.objects.filter(id__in=[self.reporte.id, reporte2.id]).exists())
