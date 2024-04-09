# Generated by Django 4.1.5 on 2024-04-09 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AtencionEstudiantes', '0023_alter_estudiante_carrera'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atencion',
            name='estudiante',
            field=models.ForeignKey(default='Buscar', on_delete=django.db.models.deletion.CASCADE, to='AtencionEstudiantes.estudiante'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='dni',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
