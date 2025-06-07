from django.test import TestCase
from profesores.models import Profesor
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError

class ProfesorModelTest(TestCase):

    def setUp(self):
        self.profesor_data = {
            "nombre": "Juan",
            "primer_apellido": "Pérez",
            "segundo_apellido": "García",
            "sexo": "masculino",
            "categoria_docente": "titular",
            "asignatura": "Matemáticas",
            "solapin": "JP123",
            "telefono": "555123456",
            "correo": "juan.perez@example.com",
            "descripcion": "Profesor con amplia experiencia."
        }

    def test_creacion_profesor_valido(self):
        profesor = Profesor.objects.create(**self.profesor_data)
        self.assertEqual(profesor.nombre, "Juan")
        self.assertEqual(profesor.solapin, "JP123")
        self.assertEqual(str(profesor), "Juan Pérez (JP123)")

    def test_solapin_unico(self):
        Profesor.objects.create(**self.profesor_data)
        with self.assertRaises(IntegrityError):
            Profesor.objects.create(**{**self.profesor_data, "correo": "otro@example.com", "solapin": "JP123"})

    def test_opciones_validas_para_sexo(self):
        for sexo in ['masculino', 'femenino', 'otro']:
            data = {**self.profesor_data, 'sexo': sexo, 'solapin': f'ID_{sexo}', 'correo': f'{sexo}@test.com'}
            profesor = Profesor.objects.create(**data)
            self.assertEqual(profesor.sexo, sexo)

    def test_opciones_validas_para_categoria_docente(self):
        categorias = ['instructor', 'asistente', 'auxiliar', 'titular']
        for i, categoria in enumerate(categorias):
            data = {**self.profesor_data, 'categoria_docente': categoria, 'solapin': f'CAT{i}', 'correo': f'cat{i}@test.com'}
            profesor = Profesor.objects.create(**data)
            self.assertEqual(profesor.categoria_docente, categoria)

    def test_longitud_maxima_solapin(self):
        profesor = Profesor(**self.profesor_data)
        profesor.solapin = "ABCDEFGHIJK"  # 11 caracteres (excede el límite de 10)
        with self.assertRaises(ValidationError):
            profesor.full_clean()

    def test_segundo_apellido_opcional(self):
        data = self.profesor_data.copy()
        data["solapin"] = "JP124"
        data["correo"] = "juan2@example.com"
        data["segundo_apellido"] = None
        profesor = Profesor.objects.create(**data)
        self.assertIsNone(profesor.segundo_apellido)
