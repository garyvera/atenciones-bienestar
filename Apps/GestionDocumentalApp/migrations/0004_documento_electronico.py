# Generated by Django 4.1.5 on 2023-02-27 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionDocumentalApp', '0003_detalleexpediente'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='electronico',
            field=models.BooleanField(default=False),
        ),
    ]