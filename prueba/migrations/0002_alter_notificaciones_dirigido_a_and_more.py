# Generated by Django 5.0.6 on 2024-06-24 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificaciones',
            name='dirigido_a',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='notificaciones',
            name='recepcionista',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Colaborador',
        ),
        migrations.DeleteModel(
            name='Recepcionista',
        ),
    ]