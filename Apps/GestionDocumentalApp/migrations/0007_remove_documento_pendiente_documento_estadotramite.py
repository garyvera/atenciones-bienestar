# Generated by Django 4.1.5 on 2023-02-27 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionDocumentalApp', '0006_remove_documento_departamento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documento',
            name='pendiente',
        ),
        migrations.AddField(
            model_name='documento',
            name='estadotramite',
            field=models.CharField(choices=[(1, 'Recibido'), (2, 'Atendido'), (3, 'S/N')], default=3, max_length=1),
        ),
    ]
