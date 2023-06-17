
from django.contrib.gis.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

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


MODALIDADES = [
    (0,'Regular'),
    (1,'Libre'),
]

NIVEL = [
    (0,'Profesional'),
    (1,'Iniciación'),
    (2,'Producción'),
    (3,'Técnico'),
]


CONDUCCION = [
    (0,'Presencial'),
    (1,'A Distancia'),
]


TIPOEXPOSICION = [
    (0,'Permanente'),
    (1,'Temporal'),
    (2,'Itirenante'),
    (3,'Colectiva'),
    
]

GENEROTALLERES = [
    (0,'Música'),
    (1,'Artes visuales'),
    (2,'Teatro'),
    (3,'Danza'),
    (4,'Literatura'),
    (5,'Cine'),
]

FRECUENCIATALLER=[
    (0,'Unica ocasión'),
    (1,'Semanal'),
    (2,'Mensual'),
    (3,'Trimestral'),
    (4,'Otro'),
]
    
TIPOEXPOSICION = [
    (0,'Permanente'),
    (1,'Temporal'),
    (2,'Itirenante'),
    (3,'Colectiva'),
    
]

GENEROEXPOSICION = [
    (0,'Artes visuales'),
    (1,'Historia'),
    (2,'Antroplogía'),
    (3,'Artes plásticas'),
    (4,'Multidisciplinario'),
    
]

GENEROEVENTOS = [
    (0,'Música'),
    (1,'Artes visuales'),
    (2,'Artes escénicas'),
    (3,'Danza'),
    (4,'Literatira'),
    (5,'Filosofía'),
    (6,'Historia'),
    (7,'Antroplogía'),
    (8,'Artes plásticas'),
    (9,'Oratoria'),
    (10,'Multidisciplinario'),
]



GENEROPRODUCCION = [
    (0,'Musica'),
    (1,'Artes visuales'),
    (3,'Teatro'),
    (4,'Danza'),
    (5,'Literatura'),
    (6,'Cine'),
    (6,'Historia'),
    (7,'Gastronomía'),
    (8,'Monografía'),
    (9,'Otro'),
]



class InstitutoCultural(models.Model):
    nombreInstituto = models.CharField('Nombre', max_length=100, unique=True, blank=False, null=False) 
    datosGeneralesIns = models.TextField('Datos Generales', blank=True, null=False)
    municipioInstituto = models.IntegerField('Municipio', choices=MUNICIPIOS)
    directorInstituto = models.CharField('Director',max_length=100, unique=True, blank=True, null=True)
    personalTotal = models.CharField('Personal',max_length=100, unique=True, blank=True, null=True)
    ubicacionInstituto = models.PointField('Ubicación')
    imagenInstituto = models.ImageField('Imagen', null=True, blank=True, upload_to="images/")
    
    def __str__(self):
        return self.nombreInstituto  # Reemplaza "nombre" con el campo apropiado del modelo que deseas mostrar en el select
    

class Talleres(models.Model):
    #datos generales de taller
    modalidadTaller = models.IntegerField('Modalidad', choices=MODALIDADES)
    conduccionTaller = models.IntegerField('Conduccion', choices=CONDUCCION)
    nivelTaller = models.IntegerField('Nivel', choices=NIVEL)
    nombreTaller = models.CharField('Nombre', max_length=100, blank=False, null=True) 
    generoTaller = models.IntegerField('Género', choices=GENEROTALLERES)
    disciplinaTaller = models.CharField('Disciplina', max_length=100, blank=False, null=True) 
    coberturaTaller = models.CharField('Cobertura', max_length=100, blank=False, null=True)
    institucionResponsableTaller = models.ForeignKey(InstitutoCultural, on_delete=models.CASCADE, verbose_name='Institucion responsable') 
    foroEspacioTaller = models.CharField('Foro o Espacio', max_length=100, blank=False, null=True) 
    municipioTaller = models.IntegerField('Municipio', choices=MUNICIPIOS)
    localidadTaller = models.CharField('Localidad', max_length=100, blank=False, null=True)
    frecuenciaTaller =models.IntegerField('Frecuencia', choices=FRECUENCIATALLER)
    fechaRealizacionTaller = models.CharField('Fecha', max_length=100, blank=False, null=True)
    #instructores
    nombreInstructorTaller = models.CharField('Nombre del Instructor', max_length=100, blank=False, null=True) 
    procedenciaInstructorTaller = models.CharField('Procedencia del Instructor', max_length=100, blank=False, null=True) 
    #alumnos del taller
    ninosTaller = models.CharField('Alumnos niños', max_length=100, blank=False, null=True) 
    ninasTaller = models.CharField('Alumnos niñas', max_length=100, blank=False, null=True) 
    jovenesHombresTaller = models.CharField('Jovenes hombres', max_length=100, blank=False, null=True) 
    jovenesMujeresTaller = models.CharField('Jovenes mujeres', max_length=100, blank=False, null=True) 
    adultosHombresTaller = models.CharField('Adultos hombres', max_length=100, blank=False, null=True) 
    adultosMujeresTaller = models.CharField('Adultos mujeres', max_length=100, blank=False, null=True) 
    #datos extras
    fuenteInformacionTaller = models.CharField('Fuente de información', max_length=100, blank=False, null=True) 
    observacionesTaller = models.TextField('Observaciones', blank=False, null=True)
    evidenciasTaller = models.CharField('Evidencias del Taller', max_length=300, blank=False, null=True) 
    
    

class Exposiciones(models.Model):
    #datos generales de taller
    tipoExposicion = models.IntegerField('Tipo', choices=TIPOEXPOSICION)
    nombreExposicion = models.CharField('Nombre', max_length=100, blank=False, null=True) 
    generoExposicion = models.IntegerField('Género', choices=GENEROEXPOSICION)
    disciplinaTecnicaExposicion = models.CharField('Disciplina', max_length=100, blank=False, null=True) 
    nombreEspecialistaExposicion = models.CharField('Nombre del especialista', max_length=100, blank=False, null=True) 
    procedenciaEspecialistaExposicion = models.CharField('Procedencia del especialista', max_length=100, blank=False, null=True) 
    numeroExpositores = models.CharField('Numero de Expositores', max_length=100, blank=False, null=True) 
    institucionResponsableDeExposicion = models.ForeignKey(InstitutoCultural, on_delete=models.CASCADE, verbose_name='Institucion responsable') 
    foroEspacioExposicion= models.CharField('Foro o Espacio', max_length=100, blank=False, null=True) 
    periodoExposicion= models.CharField('Periodo de Exposicion', max_length=100, blank=False, null=True) 
    fechaInauguracionExposicion= models.CharField('Fecha de Inauguración', max_length=100, blank=False, null=True) 
    municipioExposicion = models.IntegerField('Municipio:', choices=MUNICIPIOS)
    localidadExposicion = models.CharField('Localidad', max_length=100, blank=False, null=True)
    coberturaExposicion = models.CharField('Cobertura', max_length=100, blank=False, null=True)
    #benificiarios expo
    ninosExposicion= models.CharField('Alumnos niños', max_length=100, blank=False, null=True) 
    ninasExposicion = models.CharField('Alumnos niñas', max_length=100, blank=False, null=True) 
    jovenesHombresExposicion = models.CharField('Jovenes hombres', max_length=100, blank=False, null=True) 
    jovenesMujeresExposicion = models.CharField('Jovenes mujeres', max_length=100, blank=False, null=True) 
    adultosHombresExposicion = models.CharField('Adultos hombres', max_length=100, blank=False, null=True) 
    adultosMujeresExposicion = models.CharField('Adultos mujeres', max_length=100, blank=False, null=True) 
    #datos extras
    fuenteInformacionExposicion = models.CharField('Fuente de información', max_length=100, blank=False, null=True) 
    observacionesExposicion = models.CharField('Observaciones', max_length=100, blank=False, null=True) 
    evidenciasExposicion = models.CharField('Evidencias', max_length=300, blank=False, null=True) 


class EventosInstitutos(models.Model):
    #datos generales de evento
    nombreEventoInst = models.CharField('Nombre', max_length=100, blank=False, null=True) 
    generoEventoInst = models.IntegerField('Género', choices=GENEROEVENTOS)
    disciplinaEventoInst = models.CharField('Disciplina', max_length=100, blank=False, null=True) 
    institucionResponsableDeEventoInst = models.ForeignKey(InstitutoCultural, on_delete=models.CASCADE, verbose_name='Institucion responsable') 
    foroEspacioEventoInst= models.CharField('Foro o Espacio', max_length=100, blank=False, null=True) 
    municipioEventoInst = models.IntegerField('Municipio', choices=MUNICIPIOS)
    localidadEventoInst = models.CharField('Localidad', max_length=100, blank=False, null=True)
    fechaRealizacionEventoInst = models.CharField('Fecha', max_length=100, blank=False, null=True)
    #creadores
    nombreCreadorEventoInst = models.CharField('Artista y/o grupo', max_length=100, blank=False, null=True) 
    procedenciaCreadorEventoInst = models.CharField('Procedencia', max_length=100, blank=False, null=True) 
    numeroCreadoresHombresEventoInst = models.CharField('No.Hombres', max_length=100, blank=False, null=True) 
    numeroCreadoresMujeresEventoInst = models.CharField('No. Mujeres', max_length=100, blank=False, null=True) 
    #benificiarios expo
    ninosEventoInst= models.CharField('Niños', max_length=100, blank=False, null=True) 
    ninasEventoInst = models.CharField('Niñas', max_length=100, blank=False, null=True) 
    jovenesHombresEventoInst = models.CharField('Jovenes hombres', max_length=100, blank=False, null=True) 
    jovenesMujeresEventoInst = models.CharField('Jovenes mujeres', max_length=100, blank=False, null=True) 
    adultosHombresEventoInst = models.CharField('Adultos hombres', max_length=100, blank=False, null=True) 
    adultosMujeresEventoInst = models.CharField('Adultos mujeres', max_length=100, blank=False, null=True) 
    #datos extras
    fuenteInformacionEventoInst = models.CharField('Fuente de información', max_length=100, blank=False, null=True) 
    observacionesEventoInst = models.CharField('Observaciones', max_length=100, blank=False, null=True)
    evidenciasEventoInst = models.CharField('Evidencias', max_length=300, blank=False, null=True)
    


class ProduccionEditorialInstitutos(models.Model):
    #datos generales de evento
    nombreProduccionInst = models.CharField('Nombre', max_length=100, blank=False, null=True) 
    generoProduccionInst = models.IntegerField('Genero', choices=GENEROPRODUCCION)
    disciplinaProduccionInst = models.CharField('Disciplina', max_length=100, blank=False, null=True) 
    cantidadTirajeInst = models.CharField('Cobertura', max_length=100, blank=False, null=True)
    institucionResponsableDeProduccionInst = models.ForeignKey(InstitutoCultural, on_delete=models.CASCADE, verbose_name='Institucion responsable')
    #datos de elaboracion
    fechaDePublicacion = models.CharField('Fecha', max_length=100, blank=False, null=True)

    #Datos del autor de la publicación
    nombreAutorInst = models.CharField('Nombre del Autor', max_length=100, blank=False, null=True) 
    procedenciaAutorInst = models.CharField('Procedencia del Autor', max_length=100, blank=False, null=True) 
    numeroAutoresHombresInst = models.CharField('No. Autores Hombres', max_length=100, blank=False, null=True) 
    numeroAutoresMujeresInst = models.CharField('No. Autores Mujeres', max_length=100, blank=False, null=True) 
    #datos extras
    fuenteInformacionProduccionInst = models.CharField('Fuente de información', max_length=100, blank=False, null=True) 
    observacionesProduccionInst = models.CharField('Observaciones', max_length=100, blank=False, null=True) 
    evidenciasProduccion = models.CharField('Observaciones', max_length=100, blank=False, null=True) 
    