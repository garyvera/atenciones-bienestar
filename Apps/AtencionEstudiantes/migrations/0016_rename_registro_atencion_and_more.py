# Generated by Django 4.1.5 on 2024-04-07 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AtencionEstudiantes', '0015_author_category_book'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Registro',
            new_name='Atencion',
        ),
        migrations.RenameField(
            model_name='carrera',
            old_name='nombre_carrera',
            new_name='nombre',
        ),
    ]