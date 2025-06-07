from django.test import TestCase
from reportes.models import Reporte
from grupos.models import Grupo
from datetime import date
from django.core.files.uploadedfile import SimpleUploadedFile

class ReporteModelTest(TestCase):

    def setUp(self):
        self.grupo = Grupo.objects.create(
            nombre="Grupo A",
            direccion="Edificio 1",
            curso="Matemática",
            anio_escolar="primero",
            caracterizacion="Grupo destacado"
        )

        self.reporte_data = {
            "codigo": "RPT001",
            "periodo": "primer_semestre",
            "fecha": date.today(),
            "autor": "Juan Pérez",
            "institucion": "Escuela Técnica",
            "resumen": "Resumen del reporte",
            "objetivos": "Objetivos generales",
            "actividades": "Actividades realizadas",
            "resultados": "Resultados obtenidos",
            "analisis": "Análisis detallado",
            "desafios": "Desafíos enfrentados",
            "proximos_pasos": "Pasos a seguir",
            "grupo": self.grupo,
        }

    def test_creacion_reporte_valido(self):
        reporte = Reporte.objects.create(**self.reporte_data)
        self.assertEqual(reporte.codigo, "RPT001")
        self.assertEqual(reporte.periodo, "primer_semestre")
        self.assertEqual(reporte.grupo.nombre, "Grupo A")
        self.assertEqual(str(reporte), "Reporte RPT001 - Grupo A")

    def test_fecha_por_defecto(self):
        self.reporte_data["fecha"] = None
        reporte = Reporte.objects.create(**self.reporte_data)
        self.assertIsInstance(reporte.fecha, date)

    def test_reporte_sin_codigo_str(self):
        self.reporte_data["codigo"] = None
        reporte = Reporte.objects.create(**self.reporte_data)
        self.assertIn("Reporte Sin Código", str(reporte))

    def test_anexos_filefield_opcional(self):
        # Crea un archivo falso
        fake_file = SimpleUploadedFile("reporte.pdf", b"Contenido del archivo")
        self.reporte_data["anexos"] = fake_file
        reporte = Reporte.objects.create(**self.reporte_data)
        self.assertTrue(reporte.anexos.name.startswith("anexos_reportes/"))

    def test_grupo_es_requerido(self):
        self.reporte_data["grupo"] = None
        with self.assertRaises(Exception):
            Reporte.objects.create(**self.reporte_data)
