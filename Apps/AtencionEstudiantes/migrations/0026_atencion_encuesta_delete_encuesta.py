# Generated by Django 4.1.5 on 2024-04-11 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AtencionEstudiantes', '0025_encuesta'),
    ]

    operations = [
        migrations.AddField(
            model_name='atencion',
            name='encuesta',
            field=models.CharField(choices=[('1', 'MUY BUENA'), ('2', 'BUENA'), ('3', 'REGULAR')], max_length=2, null=True),
        ),
        migrations.DeleteModel(
            name='Encuesta',
        ),
    ]
