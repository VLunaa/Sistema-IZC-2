from django import forms
from django.contrib.gis.db import models

# Create your models here.


MES = [
    (0, "Enero"),
    (1, "Febrero"),
    (2, "Marzo"),
    (3, "Abril"),
    (4, "Mayo"),
    (5, "Junio"),
    (6, "Julio"),
    (7, "Agosto"),
    (8, "Septiembre"),
    (9, "Octubre"),
    (10, "Noviembre"),
    (11, "Diciembre"),
    
]
MUNICIPIOS = [
        (0,'Apozol'),
    (1,'Apulco'),
    (2,'Atolinga'),
    (3,'Benito Juárez'),
    (4,'Calera'),
    (5,'Cañitas de Felipe Pescador'),
    (6,'Chalchihuites'),
    (7,'Concepción del Oro'),
    (8,'Cuauhtémoc'),
    (9,'El Plateado de Joaquín Amaro'),
    (10,'El Salvador'),
    (11,'Fresnillo'),
    (12,'Genaro Codina'),
    (13,'General Enrique Estrada'),
    (14,'General Francisco R. Murguía'),
    (15,'General Pánfilo Natera'),
    (16,'Guadalupe'),
    (17,'Huanusco'),
    (18,'Jalpa'),
    (19,'Jerez'),
    (20,'Jiménez del Teul'),
    (21,'Juan Aldama'),
    (22,'Juchipila'),
    (23,'Loreto'),
    (24,'Luis Moya'),
    (25,'Mazapil'),
    (26,'Melchor Ocampo'),
    (27,'Mezquital del Oro'),
    (28,'Miguel Auza'),
    (29,'Momax'),
    (30,'Monte Escobedo'),
    (31,'Morelos'),
    (32,'Moyahua de Estrada'),
    (33,'Nochistlán de Mejía'),
    (34,'Noria de Ángeles'),
    (35,'Ojocaliente'),
    (36,'Pánuco'),
    (37,'Pinos'),
    (38,'Río Grande'),
    (39,'Sain Alto'),
    (40,'Santa María de la Paz'),
    (41,'Sombrerete'),
    (42,'Susticacán'),
    (43,'Tabasco'),
    (44,'Tepechitlán'),
    (45,'Tepetongo'),
    (46,'Teúl de González Ortega'),
    (47,'Tlaltenango de Sánchez Román'),
    (48,'Trancoso'),
    (49,'Trinidad García de la Cadena'),
    (50,'Valparaíso'),
    (51,'Vetagrande'),
    (52,'Villa de Cos'),
    (53,'Villa García'),
    (54,'Villa González Ortega'),
    (55,'Villa Hidalgo'),
    (56,'Villanueva'),
    (57,'Zacatecas'),
]



class DatosMuseo(models.Model):
    #INFORMACION PERSONAL
    nombre_museo = models.CharField('Nombre de Museo', max_length=150)
    datos_generales = models.CharField('Datos generales', max_length=600)
    municipioMuseo = models.IntegerField('Municipio', choices=MUNICIPIOS)
    direccionMuseo = models.CharField('Dirección', blank=False, max_length=100)
    horariosMuseo = models.CharField('Horarios', blank=False, max_length=100)
    costoMuseo = models.CharField('Costo de entrada', blank=False, max_length=100)
    ubicacionDeMuseo = models.PointField('Ubicación')
    #INFORMACION ARTISTICA
    imagenMuseo = models.ImageField('Imagen', null=True, blank=True, upload_to="museos/")

    def __str__(self):
        return self.nombre_museo
    class Meta:
        ordering = ['nombre_museo']
        

class AsistenciaMuseo(models.Model):
    museo = models.ForeignKey(DatosMuseo, on_delete=models.CASCADE, related_name='asistencias')
    anio = models.IntegerField('Año')
    locales_hombres = models.IntegerField('Locales hombres')
    locales_mujeres = models.IntegerField('Locales mujeres')
    nacionales_hombres = models.IntegerField('Nacionales hombres')
    nacionales_mujeres = models.IntegerField('Nacionales mujeres')
    extranjeros_hombres = models.IntegerField('Extranjeros hombres')
    extranjeros_mujeres = models.IntegerField('Extranjeros mujeres')
    

    class Meta:
        unique_together = (('museo', 'anio'),)



class FiltroNombreMunicipio(forms.Form):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Buscar por nombre'}),
        required=False
    )

    municipio = forms.ChoiceField(
        required=False,
        choices = tuple([(u'', "Todos")] + MUNICIPIOS),
        widget = forms.Select(
            attrs={'class': 'form-control'}
        )
    )