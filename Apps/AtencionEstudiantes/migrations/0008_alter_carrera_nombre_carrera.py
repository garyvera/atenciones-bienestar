# Generated by Django 4.1.5 on 2024-04-05 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AtencionEstudiantes', '0007_remove_estudiante_fechanacimiento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrera',
            name='nombre_carrera',
            field=models.CharField(max_length=50),
        ),
    ]