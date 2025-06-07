from django.test import TestCase
from grupos.models import Grupo
from profesores.models import Profesor
from django.db import IntegrityError

class GrupoModelTest(TestCase):
    
    def setUp(self):
        self.profesor1 = Profesor.objects.create(
            nombre="Ana",
            apellido="Gómez",
            email="ana@example.com"
        )
        self.profesor2 = Profesor.objects.create(
            nombre="Luis",
            apellido="Martínez",
            email="luis@example.com"
        )

    def test_creacion_grupo_valido(self):
        """Debe poder crear un grupo válido con profesores relacionados."""
        grupo = Grupo.objects.create(
            nombre="Grupo A",
            direccion="Edificio 1",
            curso="Matemática",
            anio_escolar="primero",
            caracterizacion="Estudiantes motivados.",
            guia=self.profesor1
        )
        grupo.profesores.add(self.profesor1, self.profesor2)
        grupo.save()

        self.assertEqual(grupo.__str__(), "Grupo A")
        self.assertIn(self.profesor2, grupo.profesores.all())
        self.assertEqual(grupo.guia, self.profesor1)

    def test_nombre_grupo_unico(self):
        """Debe evitar la creación de dos grupos con el mismo nombre."""
        Grupo.objects.create(
            nombre="Grupo B",
            direccion="Edificio 2",
            curso="Historia",
            anio_escolar="segundo",
            caracterizacion="Alto nivel académico.",
            guia=self.profesor1
        )
        with self.assertRaises(IntegrityError):
            Grupo.objects.create(
                nombre="Grupo B",  # Mismo nombre
                direccion="Edificio 3",
                curso="Geografía",
                anio_escolar="tercero",
                caracterizacion="Otro grupo",
                guia=self.profesor2
            )

    def test_guia_unico_por_grupo(self):
        """Debe permitir que un profesor sea guía solo de un grupo."""
        grupo1 = Grupo.objects.create(
            nombre="Grupo C",
            direccion="Edificio 4",
            curso="Biología",
            anio_escolar="cuarto",
            caracterizacion="Buen desempeño general.",
            guia=self.profesor1
        )
        grupo2 = Grupo(
            nombre="Grupo D",
            direccion="Edificio 5",
            curso="Física",
            anio_escolar="tercero",
            caracterizacion="Nuevo grupo",
            guia=self.profesor1  # Misma guía
        )
        with self.assertRaises(Exception):
            grupo2.full_clean()  # Puede lanzar error si validas manualmente en el admin
            grupo2.save()

    def test_profesores_many_to_many(self):
        """Debe permitir agregar múltiples profesores a un grupo."""
        grupo = Grupo.objects.create(
            nombre="Grupo E",
            direccion="Edificio 6",
            curso="Química",
            anio_escolar="segundo",
            caracterizacion="Grupo mixto.",
            guia=self.profesor2
        )
        grupo.profesores.set([self.profesor1, self.profesor2])
        grupo.save()

        self.assertEqual(grupo.profesores.count(), 2)
        self.assertTrue(self.profesor1 in grupo.profesores.all())
