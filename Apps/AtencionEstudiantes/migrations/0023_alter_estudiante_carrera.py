# Generated by Django 4.1.5 on 2024-04-08 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AtencionEstudiantes', '0022_remove_estudiante_estudiante_estudiante_carrera_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='carrera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AtencionEstudiantes.carrera'),
        ),
    ]
