# Generated by Django 4.1.5 on 2023-02-27 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestionDocumentalApp', '0004_documento_electronico'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documento',
            old_name='formato',
            new_name='tipodocumento',
        ),
        migrations.RenameField(
            model_name='documento',
            old_name='codigo',
            new_name='titulo',
        ),
    ]
