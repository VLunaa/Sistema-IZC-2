from django.db import models

# Create your models here.

DISCIPLINA = [
    (0,'Cantante'),
    (1,'Pintor'),
    (2,'Danzante'),
    (3,'Artista plástico'),
    (4,'Escultor'),
    (5,'Músico'),
    (6,'Escritor'),
    (7,'Actor'),
    (8,'Cantautor'),
]


GENERO = [
    (0,"Femenino"),
    (1,"Masculino"),
    (2,"Otro")
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

ESCOLARIDAD = [
    (0,"Primaria"),
    (1,"Secundiaria"),
    (2,"Media superior"),
    (3,"Superior"),
    (4,"Posgrado"),
    (5,"Maestría"),
    (6,"Doctorado")
]

OPCIONES = [
    (0,'Individual'),
    (1,'Grupal'),
]

CONOCIMIENTO_ARTISTICO = [
    (0,"Licenciatura"),
    (1,"Empírico"),
    (2,"Talleres")
]

VIGENCIA = [
    (0, "Activo"),
    (1, "No activo")
]

class Creadores(models.Model):
    #INFORMACION PERSONAL
    nombre = models.CharField('Nombre', max_length=100)
    apellido_paterno = models.CharField('Apellido paterno',max_length=100)
    apellido_materno = models.CharField('Apellido materno', max_length=100)
    fecha_nacimiento = models.DateField('Fecha de nacimiento')
    genero = models.IntegerField('Género', choices=GENERO)
    contacto = models.CharField('Medio de contacto', max_length=100)
    municipioCreador = models.IntegerField('Municipio', choices=MUNICIPIOS)
    localidadCreador = models.CharField('Localidad', max_length=100)
    escolaridadCreador = models.IntegerField('Escolaridad',choices=ESCOLARIDAD)
    #INFORMACION ARTISTICA
    disciplinaCreador = models.IntegerField('Disciplina',choices=DISCIPLINA)
    especialidadCreador = models.CharField('Especialidad', blank=True, max_length=100)
    otraDisciplinaCreador = models.CharField('Otras disciplinas', blank = True, max_length=100) 
    opcionCreador = models.IntegerField('Como se desempeña', choices=OPCIONES) 
    gradoConocimientoCreador = models.IntegerField('Conocimiento artistico',choices=CONOCIMIENTO_ARTISTICO)
    lugarFormacionCreador = models.CharField('Lugar de formación', blank=True, max_length=100) 
    vigenciaCreador = models.IntegerField('Vigencia', choices=VIGENCIA)
    imagenCreador = models.ImageField('Imagen', null=True, blank=True, upload_to="images/")


    def __str__(self):
        return self.nombre

    def calculoEdad(self):
        today = date.today()
        age = today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        return age

   #def __str__(self):
        #return f"{self.edad()} años"

    class Meta:
        ordering=['nombre']



