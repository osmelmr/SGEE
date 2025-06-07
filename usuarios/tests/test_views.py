from django.test import TestCase, Client
from django.urls import reverse
from usuarios.models import Usuario
from grupos.models import Grupo

class UsuarioViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.grupo = Grupo.objects.create(nombre="Grupo A")
        self.profesor = Usuario.objects.create_user(
            username='profesor1', password='pass1234', rol='profesor', grupo=self.grupo
        )
        self.usuario_test = Usuario.objects.create_user(
            username='testuser', password='12345', rol='estudiante', grupo=self.grupo
        )

    def login_profesor(self):
        self.client.login(username='profesor1', password='pass1234')

    def test_visualizar_usuarios(self):
        self.login_profesor()
        response = self.client.get(reverse('p_usuarios'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profesor_principal/listar_usuarios.html')

    def test_crear_usuario(self):
        self.login_profesor()
        response = self.client.post(reverse('crear_usuario'), data={
            'username': 'nuevo_usuario',
            'password': 'testpass',
            'first_name': 'Nuevo',
            'last_name': 'Usuario',
            'second_last_name': 'Test',
            'sexo': 'M',
            'grupo': self.grupo.id,
            'solapin': '12345678',
            'rol': 'estudiante',
            'telefono': '5551234',
            'email': 'nuevo@example.com'
        })
        self.assertRedirects(response, reverse('p_usuarios'))
        self.assertTrue(Usuario.objects.filter(username='nuevo_usuario').exists())

    def test_eliminar_usuario(self):
        self.login_profesor()
        response = self.client.get(reverse('eliminar_usuario', args=[self.usuario_test.id]))
        self.assertRedirects(response, reverse('p_usuarios'))
        self.assertFalse(Usuario.objects.filter(id=self.usuario_test.id).exists())

    def test_eliminar_usuarios_multiple(self):
        self.login_profesor()
        u2 = Usuario.objects.create_user(username='test2', password='pass', grupo=self.grupo)
        response = self.client.post(reverse('eliminar_usuarios'), data={'ids': [self.usuario_test.id, u2.id]})
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'success': True})
        self.assertFalse(Usuario.objects.filter(id=self.usuario_test.id).exists())
        self.assertFalse(Usuario.objects.filter(id=u2.id).exists())

    def test_modificar_usuario(self):
        self.login_profesor()
        response = self.client.post(reverse('modificar_usuario', args=[self.usuario_test.id]), data={
            'username': 'modificado',
            'first_name': 'Mod',
            'last_name': 'User',
            'sexo': 'F',
            'grupo': self.grupo.id,
            'rol': 'estudiante',
            'solapin': '87654321',
            'telefono': '123123',
            'email': 'mod@example.com'
        })
        self.assertRedirects(response, reverse('p_usuarios'))
        self.usuario_test.refresh_from_db()
        self.assertEqual(self.usuario_test.username, 'modificado')

    def test_visualizar_usuario_detalle(self):
        self.login_profesor()
        response = self.client.get(reverse('visualizar_usuario', args=[self.usuario_test.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profesor_principal/visualizar_usuario.html')
