# Generated by Django 4.1.5 on 2024-04-05 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AtencionEstudiantes', '0010_registro_nivel_registro_sexo_alter_registro_carrera_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='apellido_materno',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='apellido_paterno',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='dni',
            field=models.CharField(max_length=10),
        ),
    ]
