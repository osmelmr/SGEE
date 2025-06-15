from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from estrategias.models import Estrategia
from grupos.models import Grupo

User = get_user_model()

class EstrategiaViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

        # Crear grupo base
        self.grupo = Grupo.objects.create(
            nombre="Grupo 1", direccion="Aula 5", curso="10mo", anio_escolar="2024-2025",
            caracterizacion="Grupo experimental"
        )

        # Crear usuarios
        self.profesor = User.objects.create_user(username="profe", password="1234", rol='profesor_principal', sexo='masculino', solapin='12345')
        self.no_profesor = User.objects.create_user(username="alumno", password="1234", rol='usuario', sexo='femenino', solapin='12346')

        # Crear estrategia
        self.estrategia = Estrategia.objects.create(
            nombre="Estrategia Prueba",
            curso="10mo",
            anio_escolar="2024-2025",
            grupo=self.grupo,
            plan_estudios="Plan X",
            obj_estrategia="Objetivo",
            dir_grupo="Director",
            caract_grupo="Caracterización",
            colect_pedagogico="Colectivo",
            otros_aspectos="Aspectos",
            dim_curricular="Curricular",
            dim_extensionista="Extensionista",
            dim_politica="Política",
            conclusiones="Conclusión",
            obj_general="General",
            obj_dc="Obj DC",
            plan_dc="Plan DC",
            obj_de="Obj DE",
            plan_de="Plan DE",
            obj_dp="Obj DP",
            plan_dp="Plan DP",
            evaluacion="Evaluación",
            autor="Prof. A"
        )

    def test_visualizar_estrategias_profesor(self):
        self.client.login(username="profe", password="1234")
        response = self.client.get(reverse("p_estrategias"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Estrategia Prueba")

    def test_visualizar_estrategias_no_autenticado(self):
        response = self.client.get(reverse("p_estrategias"))
        self.assertRedirects(response, reverse("login"))

    def test_crear_estrategia_get(self):
        self.client.login(username="profe", password="1234")
        response = self.client.get(reverse("p_formular_estrategia"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "form")

    def test_crear_estrategia_post(self):
        self.client.login(username="profe", password="1234")
        response = self.client.post(reverse("p_formular_estrategia"), {
            "nombre": "Nueva Estrategia",
            "curso": "11mo",
            "anio_escolar": "2025-2026",
            "grupo": self.grupo.id,
            "plan_estudios": "Nuevo plan",
            "obj_estrategia": "Nuevo obj",
            "dir_grupo": "Dir",
            "caract_grupo": "Caracter",
            "colect_pedagogico": "Colectivo",
            "otros_aspectos": "Aspectos",
            "dim_curricular": "Dim C",
            "dim_extensionista": "Dim E",
            "dim_politica": "Dim P",
            "conclusiones": "Conclusión",
            "obj_general": "General",
            "obj_dc": "DC",
            "plan_dc": "Plan DC",
            "obj_de": "DE",
            "plan_de": "Plan DE",
            "obj_dp": "DP",
            "plan_dp": "Plan DP",
            "evaluacion": "Eval",
            "autor": "Prof. B"
        })
        self.assertRedirects(response, reverse("p_estrategias"))
        self.assertEqual(Estrategia.objects.count(), 2)

    def test_modificar_estrategia_post(self):
        self.client.login(username="profe", password="1234")
        response = self.client.post(reverse("p_modificar_estrategia", args=[self.estrategia.id]), {
            "nombre": "Modificada",
            "curso": "10mo",
            "anio_escolar": "2024-2025",
            "grupo": self.grupo.id,
            "plan_estudios": "Modificado",
            "obj_estrategia": "Mod obj",
            "dir_grupo": "Director",
            "caract_grupo": "Caract",
            "colect_pedagogico": "Colectivo",
            "otros_aspectos": "Aspectos",
            "dim_curricular": "Curr",
            "dim_extensionista": "Ext",
            "dim_politica": "Pol",
            "conclusiones": "Conclusión",
            "obj_general": "General",
            "obj_dc": "DC",
            "plan_dc": "Plan DC",
            "obj_de": "DE",
            "plan_de": "Plan DE",
            "obj_dp": "DP",
            "plan_dp": "Plan DP",
            "evaluacion": "Evaluación",
            "autor": "Prof. Mod"
        })
        self.assertRedirects(response, reverse("p_estrategias"))
        self.estrategia.refresh_from_db()
        self.assertEqual(self.estrategia.nombre, "Modificada")

    def test_visualizar_estrategia(self):
        self.client.login(username="profe", password="1234")
        response = self.client.get(reverse("p_visualizar_estrategia", args=[self.estrategia.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.estrategia.nombre)

    def test_eliminar_estrategia(self):
        self.client.login(username="profe", password="1234")
        response = self.client.post(reverse("p_eliminar_estrategia", args=[self.estrategia.id]))
        self.assertRedirects(response, reverse("p_estrategias"))
        self.assertFalse(Estrategia.objects.filter(id=self.estrategia.id).exists())

    def test_eliminar_estrategias_multiples(self):
        self.client.login(username="profe", password="1234")
        otra = Estrategia.objects.create(
            nombre="Otra", curso="11mo", anio_escolar="2025-2026",
            grupo=self.grupo, plan_estudios="Plan", obj_estrategia="Obj", dir_grupo="Dir",
            caract_grupo="Caract", colect_pedagogico="Colectivo", otros_aspectos="Aspectos",
            dim_curricular="Curr", dim_extensionista="Ext", dim_politica="Pol", conclusiones="Concl",
            obj_general="Gen", obj_dc="DC", plan_dc="DC Plan", obj_de="DE", plan_de="Plan DE",
            obj_dp="DP", plan_dp="Plan DP", evaluacion="Eval", autor="Prof. C"
        )
        response = self.client.post(reverse("p_eliminar_estrategias"), {
            "estrategias[]": [self.estrategia.id, otra.id]
        })
        self.assertRedirects(response, reverse("p_estrategias"))
        self.assertEqual(Estrategia.objects.count(), 0)
