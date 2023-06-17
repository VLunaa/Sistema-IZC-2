from django.db import models

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


TIPOEVENTO = list(enumerate([
    "Ferias del libro",
    "Festivales",
    "Festividades",
    "Otro"
]))



TIPOEVENTOSUB = list(enumerate([
    "Multidiciplinaria",
    "Danza",
    "Teatro",
    "Música",
    "Literatura",
    "Otro"
]))



class Eventos(models.Model):
    nombreEvento = models.CharField('Evento', max_length=100, unique=True, null=False)
    informesEvento = models.TextField('Informes',null=True)
    municipioEvento = models.IntegerField('Municipio', choices=MUNICIPIOS)
    tipoEvento = models.IntegerField('Tipo de evento', choices=TIPOEVENTO)
    subTipoEvento = models.IntegerField('Categoría de evento', choices=TIPOEVENTOSUB)
    descripcionEvento = models.TextField('Descripción', null=True)
    sedeEvento = models.CharField('Sede', max_length=100, null=True)
    fechaDeEvento = models.TextField('Fecha del evento', null=True)
    institucionOrganizadora = models.CharField('Institucion organizadora', max_length=100, null=True)
    institucionCoadyuvante = models.CharField('Instituciones coadyuvantes',max_length=100, null=True)
    imagenEvento = models.ImageField('Imagen', null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.nombreEvento

    class Meta:
        ordering = ['nombreEvento']
    


