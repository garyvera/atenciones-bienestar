# Generated by Django 4.1.5 on 2023-09-10 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procesos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrera',
            name='codigo',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
