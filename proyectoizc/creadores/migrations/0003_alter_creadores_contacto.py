# Generated by Django 4.0.2 on 2023-05-21 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creadores', '0002_alter_creadores_vigenciacreador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creadores',
            name='contacto',
            field=models.CharField(max_length=100, verbose_name='Medio de contacto'),
        ),
    ]
