# Generated by Django 5.0.6 on 2024-06-24 16:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_colaborador', models.CharField(max_length=50)),
                ('apellido_colaborador', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Recepcionista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_recepcionista', models.CharField(max_length=50)),
                ('apellido_recepcionista', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Notificaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('fecha_recepcion', models.DateTimeField(auto_now_add=True)),
                ('hora_recepcion', models.DateTimeField(auto_now=True)),
                ('entidad', models.CharField(max_length=100)),
                ('numero_exp', models.IntegerField()),
                ('fecha_hora_entrega_interna', models.DateTimeField(blank=True, null=True)),
                ('fecha_hora_entrega', models.DateTimeField(blank=True, null=True)),
                ('dirigido_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones', to='prueba.colaborador')),
                ('recepcionista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones', to='prueba.recepcionista')),
            ],
        ),
    ]
