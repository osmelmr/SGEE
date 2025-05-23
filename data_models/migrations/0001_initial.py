# Generated by Django 5.2 on 2025-05-03 01:30

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('autor', models.CharField(default='Desconocido', max_length=100)),
                ('estado', models.CharField(choices=[('activa', 'Activa'), ('inactiva', 'Inactiva')], default='activa', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_evento', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('ubicacion_evento', models.CharField(max_length=100)),
                ('tipo_evento', models.CharField(choices=[('academico', 'Académico'), ('cultural', 'Cultural'), ('deportivo', 'Deportivo'), ('social', 'Social')], max_length=20)),
                ('telefono_contacto', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('direccion', models.CharField(max_length=100)),
                ('curso', models.CharField(max_length=20)),
                ('anio_escolar', models.CharField(max_length=10)),
                ('caracterizacion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('primer_apellido', models.CharField(max_length=50)),
                ('segundo_apellido', models.CharField(blank=True, max_length=50, null=True)),
                ('sexo', models.CharField(choices=[('masculino', 'Masculino'), ('femenino', 'Femenino'), ('otro', 'Otro')], max_length=20)),
                ('categoria_docente', models.CharField(choices=[('instructor', 'Instructor'), ('asistente', 'Asistente'), ('auxiliar', 'Auxiliar'), ('titular', 'Titular')], max_length=20)),
                ('asignatura', models.CharField(max_length=50)),
                ('solapin', models.CharField(max_length=10, unique=True)),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('cargo', models.CharField(choices=[('profesor_principal', 'Profesor_Principal'), ('usuario', 'Usuario')], max_length=20)),
                ('sexo', models.CharField(choices=[('masculino', 'Masculino'), ('femenino', 'Femenino'), ('otro', 'Otro')], max_length=10)),
                ('grupo', models.CharField(blank=True, max_length=50, null=True)),
                ('solapin', models.CharField(max_length=10, unique=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('encuestas', models.ManyToManyField(blank=True, related_name='usuarios', to='data_models.encuesta')),
                ('eventos', models.ManyToManyField(blank=True, related_name='usuarios', to='data_models.evento')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Estrategia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(max_length=20)),
                ('anio_escolar', models.CharField(max_length=10)),
                ('nombre', models.CharField(blank=True, default='Estrategia_{id}', max_length=255)),
                ('autor', models.CharField(blank=True, default='autor_{id}', max_length=255)),
                ('plan_estudios', models.TextField(blank=True, default='plan_estudios_{id}')),
                ('obj_general', models.TextField(blank=True, default='objetivo_general_{id}')),
                ('obj_estrategia', models.TextField(blank=True, default='objetivos_estrategia_{id}')),
                ('dir_grupo', models.CharField(blank=True, default='direccion_grupo_{id}', max_length=255)),
                ('caract_grupo', models.TextField(blank=True, default='caracteristicas_grupo_{id}')),
                ('colect_pedagogico', models.TextField(blank=True, default='colectivo_pedagogico_{id}')),
                ('dim_curricular', models.TextField(blank=True, default='dimension_curricular_{id}')),
                ('dim_extensionista', models.TextField(blank=True, default='dimension_extensionista_{id}')),
                ('dim_politica', models.TextField(blank=True, default='dimension_politico_ideologica_{id}')),
                ('obj_dc', models.TextField(blank=True, default='obj_dc_{id}')),
                ('plan_dc', models.TextField(blank=True, default='plan_dc_{id}')),
                ('obj_de', models.TextField(blank=True, default='obj_de_{id}')),
                ('plan_de', models.TextField(blank=True, default='plan_de_{id}')),
                ('obj_dp', models.TextField(blank=True, default='obj_dp_{id}')),
                ('plan_dp', models.TextField(blank=True, default='plan_dp_{id}')),
                ('evaluacion', models.TextField(blank=True, default='evaluacion_integral_{id}')),
                ('otros_aspectos', models.TextField(blank=True, default='otros_aspectos_{id}')),
                ('conclusiones', models.TextField(blank=True, default='conclusiones_{id}')),
                ('grupo', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='estrategia', to='data_models.grupo')),
            ],
            options={
                'unique_together': {('curso', 'anio_escolar', 'grupo')},
            },
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=255)),
                ('encuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preguntas', to='data_models.encuesta')),
            ],
        ),
        migrations.AddField(
            model_name='grupo',
            name='guia',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='grupo_asignado', to='data_models.profesor'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='profesores',
            field=models.ManyToManyField(blank=True, related_name='grupos', to='data_models.profesor'),
        ),
        migrations.AddField(
            model_name='evento',
            name='profesor_encargado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='eventos_asociados', to='data_models.profesor'),
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo', models.CharField(blank=True, max_length=10, null=True)),
                ('codigo', models.CharField(blank=True, max_length=10, null=True)),
                ('periodo', models.CharField(blank=True, max_length=10, null=True)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('autor', models.CharField(blank=True, max_length=50, null=True)),
                ('institucion', models.CharField(blank=True, max_length=50, null=True)),
                ('resumen', models.TextField(blank=True, null=True)),
                ('objetivos', models.TextField(blank=True, null=True)),
                ('actividades', models.TextField(blank=True, null=True)),
                ('resultados', models.TextField(blank=True, null=True)),
                ('analisis', models.TextField(blank=True, null=True)),
                ('desafios', models.TextField(blank=True, null=True)),
                ('proximos_pasos', models.TextField(blank=True, null=True)),
                ('anexos', models.FileField(blank=True, null=True, upload_to='anexos/')),
                ('estrategia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reportes', to='data_models.estrategia')),
            ],
        ),
    ]
