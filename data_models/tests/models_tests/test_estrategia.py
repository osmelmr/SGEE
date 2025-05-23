# tests/test_model_estrategia.py

from django.test import TestCase
from data_models.models import Estrategia, Grupo

class EstrategiaModelTest(TestCase):

    def setUp(self):
        self.estrategia = Estrategia.objects.create(
            curso="10A",
            anio_escolar="2025",
            grupo="A"
        )

    def test_creacion_estrategia_basica(self):
        """Se puede crear una Estrategia básica y se guarda correctamente"""
        self.assertEqual(self.estrategia.curso, "10A")
        self.assertEqual(self.estrategia.anio_escolar, "2025")
        self.assertEqual(self.estrategia.grupo, "A")

    def test_campos_por_defecto_usan_id_placeholder(self):
        """Campos de texto deben tener valores por defecto con {id}"""
        self.assertIn("{id}", self.estrategia.nombre)
        self.assertIn("{id}", self.estrategia.autor)
        self.assertIn("{id}", self.estrategia.plan_estudios)

    def test_str_retorna_formato_correcto(self):
        """El método __str__ devuelve el formato esperado"""
        esperado = f"Estrategia: {self.estrategia.nombre or 'Sin nombre'} (10A - 2025 - A)"
        self.assertEqual(str(self.estrategia), esperado)

    def test_relacion_con_grupo_es_nula_por_defecto(self):
        """La relación con Grupo debe ser nula si no se define"""
        self.assertIsNone(self.estrategia.grupo_id)

    def test_relacion_uno_a_uno_con_grupo(self):
        """Se puede asociar una estrategia a un grupo"""
        grupo = Grupo.objects.create(nombre="Grupo X")
        self.estrategia.grupo_id = grupo
        self.estrategia.save()
        self.assertEqual(self.estrategia.grupo_id.nombre, "Grupo X")

    def test_unique_together_en_curso_y_grupo(self):
        """No se pueden repetir curso + grupo en estrategias"""
        with self.assertRaises(Exception):
            Estrategia.objects.create(
                curso="10A",
                anio_escolar="2026",  # año distinto, pero mismo curso + grupo
                grupo="A"
            )

    def test_dimensiones_y_objetivos_tienen_valor_por_defecto(self):
        """Las dimensiones y objetivos deben tener valores iniciales"""
        self.assertIn("{id}", self.estrategia.dim_curricular)
        self.assertIn("{id}", self.estrategia.obj_dp)

    def test_editar_texto_objetivo_general(self):
        """Se puede actualizar obj_general"""
        self.estrategia.obj_general = "Nuevo objetivo general"
        self.estrategia.save()
        self.assertEqual(self.estrategia.obj_general, "Nuevo objetivo general")

    def test_creacion_multiple(self):
        """Pueden crearse varias estrategias con curso y grupo diferentes"""
        Estrategia.objects.create(curso="11B", anio_escolar="2025", grupo="B")
        Estrategia.objects.create(curso="12C", anio_escolar="2026", grupo="C")
        self.assertEqual(Estrategia.objects.count(), 3)

    def test_eliminar_estrategia_no_elimina_grupo(self):
        """Eliminar una estrategia no debe eliminar su grupo relacionado"""
        grupo = Grupo.objects.create(nombre="Grupo Y")
        self.estrategia.grupo_id = grupo
        self.estrategia.save()
        self.estrategia.delete()
        self.assertTrue(Grupo.objects.filter(nombre="Grupo Y").exists())
