# Generated by Django 4.1.5 on 2024-01-28 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AtencionEstudiantes', '0002_rename_estudiante_estudiantes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiantes',
            name='carrera',
        ),
        migrations.RemoveField(
            model_name='estudiantes',
            name='sexo',
        ),
        migrations.AlterField(
            model_name='estudiantes',
            name='fechaNacimiento',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.DeleteModel(
            name='Carrera',
        ),
    ]
