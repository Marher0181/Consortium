# Generated by Django 5.0.6 on 2024-06-24 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0002_alter_notificaciones_dirigido_a_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='notificaciones',
            name='numero_exp',
            field=models.CharField(max_length=100),
        ),
    ]