# Generated by Django 4.0.2 on 2023-06-01 02:48

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosMuseo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_museo', models.CharField(max_length=150, verbose_name='Nombre de Museo')),
                ('datos_generales', models.CharField(max_length=150, verbose_name='Datos generales')),
                ('municipioMuseo', models.IntegerField(choices=[(0, 'Apozol'), (1, 'Apulco'), (2, 'Atolinga'), (3, 'Benito Juárez'), (4, 'Calera'), (5, 'Cañitas de Felipe Pescador'), (6, 'Chalchihuites'), (7, 'Concepción del Oro'), (8, 'Cuauhtémoc'), (9, 'El Plateado de Joaquín Amaro'), (10, 'El Salvador'), (11, 'Fresnillo'), (12, 'Genaro Codina'), (13, 'General Enrique Estrada'), (14, 'General Francisco R. Murguía'), (15, 'General Pánfilo Natera'), (16, 'Guadalupe'), (17, 'Huanusco'), (18, 'Jalpa'), (19, 'Jerez'), (20, 'Jiménez del Teul'), (21, 'Juan Aldama'), (22, 'Juchipila'), (23, 'Loreto'), (24, 'Luis Moya'), (25, 'Mazapil'), (26, 'Melchor Ocampo'), (27, 'Mezquital del Oro'), (28, 'Miguel Auza'), (29, 'Momax'), (30, 'Monte Escobedo'), (31, 'Morelos'), (32, 'Moyahua de Estrada'), (33, 'Nochistlán de Mejía'), (34, 'Noria de Ángeles'), (35, 'Ojocaliente'), (36, 'Pánuco'), (37, 'Pinos'), (38, 'Río Grande'), (39, 'Sain Alto'), (40, 'Santa María de la Paz'), (41, 'Sombrerete'), (42, 'Susticacán'), (43, 'Tabasco'), (44, 'Tepechitlán'), (45, 'Tepetongo'), (46, 'Teúl de González Ortega'), (47, 'Tlaltenango de Sánchez Román'), (48, 'Trancoso'), (49, 'Trinidad García de la Cadena'), (50, 'Valparaíso'), (51, 'Vetagrande'), (52, 'Villa de Cos'), (53, 'Villa García'), (54, 'Villa González Ortega'), (55, 'Villa Hidalgo'), (56, 'Villanueva'), (57, 'Zacatecas')], verbose_name='Municipio')),
                ('direccionMuseo', models.CharField(max_length=100, verbose_name='Dirección')),
                ('ubicacionDeMuseo', django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='Ubicación')),
                ('imagenMuseo', models.ImageField(blank=True, null=True, upload_to='museos/', verbose_name='Imagen')),
            ],
            options={
                'ordering': ['nombre_museo'],
            },
        ),
        migrations.CreateModel(
            name='AsistenciaMuseo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.IntegerField(choices=[(0, 'Enero'), (1, 'Febrero'), (2, 'Marzo'), (3, 'Abril'), (4, 'Mayo'), (5, 'Junio'), (6, 'Julio'), (7, 'Agosto'), (8, 'Septiembre'), (9, 'Octubre'), (10, 'Noviembre'), (11, 'Diciembre')], verbose_name='Mes')),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('locales_hombres', models.IntegerField(verbose_name='Cantidad de visitantes')),
                ('locales_mujeres', models.IntegerField(verbose_name='Cantidad de visitantes')),
                ('nacionales_hombres', models.IntegerField(verbose_name='Cantidad de visitantes')),
                ('nacionales_mujeres', models.IntegerField(verbose_name='Cantidad de visitantes')),
                ('extranjeros_hombres', models.IntegerField(verbose_name='Cantidad de visitantes')),
                ('extranjeros_mujeres', models.IntegerField(verbose_name='Cantidad de visitantes')),
                ('museo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asistencias', to='museos.datosmuseo')),
            ],
            options={
                'unique_together': {('museo', 'mes', 'anio')},
            },
        ),
    ]
