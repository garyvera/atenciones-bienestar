# Generated by Django 4.1.5 on 2023-02-27 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionDocumentalApp', '0007_remove_documento_pendiente_documento_estadotramite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documento',
            name='estado',
        ),
        migrations.AlterField(
            model_name='documento',
            name='electronico',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='documento',
            name='estadotramite',
            field=models.CharField(choices=[(1, 'Recibido'), (2, 'Atendido'), (3, 'Archivado'), (3, 'S/N')], default=4, max_length=1),
        ),
    ]
