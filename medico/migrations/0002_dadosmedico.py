# Generated by Django 5.0.4 on 2024-04-15 19:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DadosMedico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crm', models.CharField(max_length=6)),
                ('nome', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=15)),
                ('rua', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('rg', models.ImageField(upload_to='rgs')),
                ('cedula_identidade_medica', models.ImageField(upload_to='cim')),
                ('foto', models.ImageField(upload_to='fotos_perfil')),
                ('descricao', models.TextField()),
                ('valor_consulta', models.FloatField(default=100)),
                ('especialidade', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='medico.especialidade')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
