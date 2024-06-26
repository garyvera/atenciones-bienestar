# Generated by Django 4.1.5 on 2024-04-05 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AtencionEstudiantes', '0009_alter_registro_estudiante'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='nivel',
            field=models.CharField(choices=[('1', 'PRIMER'), ('2', 'SEGUNDO'), ('3', 'TERCER'), ('4', 'CUARTO'), ('5', 'QUINTO'), ('6', 'SEXTO'), ('7', 'SEPTIMO'), ('8', 'OCTAVO'), ('9', 'NOVENO'), ('10', 'DECIMO')], default=1, max_length=2),
        ),
        migrations.AddField(
            model_name='registro',
            name='sexo',
            field=models.CharField(choices=[('1', 'HOMBRE'), ('2', 'MUJER'), ('3', 'NO BINARIO')], default=1, max_length=2),
        ),
        migrations.AlterField(
            model_name='registro',
            name='carrera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AtencionEstudiantes.carrera'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='fecha',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='registro',
            name='motivo',
            field=models.CharField(choices=[('1', 'APOYO SOCIOECONOMICO (BECAS)'), ('2', 'ORIENTACIÓN VOCACIONAL Y DESARROLLO'), ('3', 'ATENCIÓN PSICOLÓGICA'), ('4', 'SEGURO ESTUDIANTIL'), ('5', 'MEDIACIÓN'), ('6', 'TRABAJO SOCIAL'), ('7', 'INCLUSIÓN'), ('8', 'ATENCIÓN MÉDICA'), ('9', 'ATENCIÓN ODONTOLÓGICA'), ('10', 'DEPORTE'), ('11', 'MÚSICA'), ('12', 'DANZA')], default=1, max_length=2),
        ),
    ]
