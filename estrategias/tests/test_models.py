from django.test import TestCase
from estrategias.models import Estrategia
from django.db.utils import IntegrityError
from django.utils.timezone import now
import time

class EstrategiaModelTest(TestCase):

    def setUp(self):
        self.estrategia = Estrategia.objects.create(
            curso="Curso 1",
            anio_escolar="primero",
            grupo="Grupo A"
        )

    def test_creacion_estrategia_valores_por_defecto(self):
        """Prueba que una estrategia se crea correctamente con valores por defecto."""
        self.assertEqual(self.estrategia.nombre, "Estrategia_{id}")
        self.assertEqual(self.estrategia.autor, "autor_{id}")
        self.assertEqual(self.estrategia.anio_escolar, "primero")
        self.assertIsNotNone(self.estrategia.fecha_creacion)
        self.assertIsNotNone(self.estrategia.fecha_modificacion)
        self.assertIn("Curso 1", str(self.estrategia))

    def test_str_representacion(self):
        """Prueba la representación string del modelo."""
        expected = f"Estrategia: {self.estrategia.nombre or 'Sin nombre'} (Curso 1 - primero - Grupo A)"
        self.assertEqual(str(self.estrategia), expected)

    def test_unique_constraint(self):
        """Prueba la restricción de unicidad en curso + grupo."""
        with self.assertRaises(IntegrityError):
            Estrategia.objects.create(
                curso="Curso 1",
                anio_escolar="segundo",  # mismo curso y grupo
                grupo="Grupo A"
            )

    def test_fecha_modificacion_actualizada(self):
        """Prueba que la fecha_modificacion cambia cuando se actualiza el modelo."""
        original_modificacion = self.estrategia.fecha_modificacion
        time.sleep(1)  # para asegurar que el timestamp cambia
        self.estrategia.nombre = "Estrategia actualizada"
        self.estrategia.save()
        self.assertGreater(self.estrategia.fecha_modificacion, original_modificacion)

    def test_actualizacion_campos_texto(self):
        """Prueba que los campos de texto se pueden actualizar correctamente."""
        self.estrategia.obj_general = "Nuevo objetivo general"
        self.estrategia.save()
        self.assertEqual(self.estrategia.obj_general, "Nuevo objetivo general")
