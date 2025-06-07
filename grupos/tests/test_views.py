from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from profesores.models import Profesor
from grupos.models import Grupo


class GrupoViewsTestCase(TestCase):
    def setUp(self):
        # Crear usuario y profesor asociado
        self.user = User.objects.create_user(username='profesor1', password='testpass')
        self.user.es_profesor = lambda: True
        self.user.save()
        self.profesor = Profesor.objects.create(nombre="Ana", primer_apellido="Gomez", user=self.user)

        self.client = Client()
        self.client.login(username='profesor1', password='testpass')

        # Crear grupo de prueba
        self.grupo = Grupo.objects.create(
            nombre="Grupo A",
            direccion="Edificio 1",
            curso="6to",
            anio_escolar="2025",
            caracterizacion="Muy participativos",
            guia=self.profesor
        )
        self.grupo.profesores.add(self.profesor)

    def test_listar_grupos(self):
        response = self.client.get(reverse('p_grupos'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Grupo A")

    def test_visualizar_grupo(self):
        response = self.client.get(reverse('visualizar_grupo', args=[self.grupo.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Grupo A")

    def test_crear_grupo_valido(self):
        otro_profesor = Profesor.objects.create(nombre="Carlos", primer_apellido="Rios")
        data = {
            'nombre': 'Grupo B',
            'direccion': 'Edificio 2',
            'curso': '7mo',
            'anio_escolar': '2025',
            'caracterizacion': 'Curiosos',
            'guia': otro_profesor.id,
            'profesores': [self.profesor.id, otro_profesor.id]
        }
        response = self.client.post(reverse('p_formular_grupo'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Grupo.objects.filter(nombre='Grupo B').exists())

    def test_crear_grupo_con_guia_repetido(self):
        data = {
            'nombre': 'Grupo Duplicado',
            'direccion': 'Edificio 3',
            'curso': '8vo',
            'anio_escolar': '2025',
            'caracterizacion': 'Competitivos',
            'guia': self.profesor.id,
            'profesores': [self.profesor.id]
        }
        response = self.client.post(reverse('p_formular_grupo'), data)
        self.assertRedirects(response, reverse('p_formular_grupo'))
        self.assertEqual(Grupo.objects.filter(nombre='Grupo Duplicado').count(), 0)

    def test_modificar_grupo(self):
        nuevo_profesor = Profesor.objects.create(nombre="Laura", primer_apellido="Sanchez")
        data = {
            'nombre': 'Grupo A Modificado',
            'direccion': 'Edificio 1B',
            'curso': '6to',
            'anio_escolar': '2025',
            'caracterizacion': 'Motivados',
            'guia': self.profesor.id,
            'profesores': [nuevo_profesor.id]
        }
        response = self.client.post(reverse('modificar_grupo', args=[self.grupo.id]), data)
        self.assertRedirects(response, reverse('p_grupos'))
        self.grupo.refresh_from_db()
        self.assertEqual(self.grupo.nombre, 'Grupo A Modificado')
        self.assertIn(nuevo_profesor, self.grupo.profesores.all())

    def test_eliminar_grupo(self):
        grupo_id = self.grupo.id
        response = self.client.post(reverse('eliminar_grupo', args=[grupo_id]))
        self.assertRedirects(response, reverse('p_grupos'))
        self.assertFalse(Grupo.objects.filter(id=grupo_id).exists())

    def test_eliminar_grupos_multiples(self):
        grupo2 = Grupo.objects.create(
            nombre="Grupo Extra",
            direccion="Edificio X",
            curso="5to",
            anio_escolar="2025",
            caracterizacion="Activos",
            guia=Profesor.objects.create(nombre="Luis", primer_apellido="Morales")
        )
        grupo2.profesores.add(self.profesor)
        data = {'grupos[]': [self.grupo.id, grupo2.id]}
        response = self.client.post(reverse('eliminar_grupos'), data)
        self.assertRedirects(response, reverse('p_grupos'))
        self.assertEqual(Grupo.objects.count(), 0)

    def test_eliminar_grupos_metodo_no_permitido(self):
        response = self.client.get(reverse('eliminar_grupos'))
        self.assertEqual(response.status_code, 405)
        self.assertJSONEqual(response.content, {"error": "Método no permitido"})

    def test_acceso_denegado_para_no_autenticado(self):
        self.client.logout()
        response = self.client.get(reverse('p_grupos'))
        self.assertRedirects(response, reverse('login'))

    def test_acceso_denegado_sin_permiso(self):
        self.user.es_profesor = lambda: False
        response = self.client.get(reverse('p_grupos'))
        self.assertRedirects(response, reverse('pagina_principal'))
