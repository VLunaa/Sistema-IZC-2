from django import forms
from mapwidgets.widgets import GooglePointFieldWidget

from .models import EventosInstitutos, Exposiciones, InstitutoCultural, ProduccionEditorialInstitutos, Talleres
#eventos hacerlo en models

MUNICIPIOS = list(enumerate([
    "Apozol",
    "Apulco",
    "Atolinga",
    "Benito Juárez",
    "Calera",
    "Cañitas de Felipe Pescador",
    "Chalchihuites",
    "Concepción del Oro",
    "Cuauhtémoc",
    "El Plateado de Joaquín Amaro",
    "El Salvador",
    "Fresnillo",
    "Genaro Codina",
    "General Enrique Estrada",
    "General Francisco R. Murguía",
    "General Pánfilo Natera",
    "Guadalupe",
    "Huanusco",
    "Jalpa",
    "Jerez",
    "Jiménez del Teul",
    "Juan Aldama",
    "Juchipila",
    "Loreto",
    "Luis Moya",
    "Mazapil",
    "Melchor Ocampo",
    "Mezquital del Oro",
    "Miguel Auza",
    "Momax",
    "Monte Escobedo",
    "Morelos",
    "Moyahua de Estrada",
    "Nochistlán de Mejía",
    "Noria de Ángeles",
    "Ojocaliente",
    "Pánuco",
    "Pinos",
    "Río Grande",
    "Sain Alto",
    "Santa María de la Paz",
    "Sombrerete",
    "Susticacán",
    "Tabasco",
    "Tepechitlán",
    "Tepetongo",
    "Teúl de González Ortega",
    "Tlaltenango de Sánchez Román",
    "Trancoso",
    "Trinidad García de la Cadena",
    "Valparaíso",
    "Vetagrande",
    "Villa de Cos",
    "Villa García",
    "Villa González Ortega",
    "Villa Hidalgo",
    "Villanueva",
    "Zacatecas"
]))



class CustomGooglePointFieldWidget(GooglePointFieldWidget):
    template_name = 'map_template.html'

class InstitutoForm(forms.ModelForm):
    imagenInstituto = forms.ImageField()
    class Meta:
        model = InstitutoCultural
        fields = '__all__'
        widgets = {
            "nombreInstituto": forms.TextInput(attrs={'class': 'form-control'}),
            "datosGeneralesIns": forms.Textarea(attrs={'class': 'form-control'}),
            "municipioInstituto": forms.Select(attrs={'class': 'form-control'}),
            "directorInstituto": forms.TextInput(attrs={'class': 'form-control'}),
            "personalTotal": forms.TextInput(attrs={'class': 'form-control'}),
            'ubicacionInstituto': CustomGooglePointFieldWidget,
        }


## Formulario para aplicar filtros a la vista de platillos.
class FiltroInstitutoForm(forms.Form):
    nombreInstituto = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Nombre de instituto'}),
        required=False
    )

    municipioInstituto = forms.ChoiceField(
        required=False,
        choices = tuple([(u'', "Todos")] + MUNICIPIOS),
        widget = forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    
    institucionResponsable = forms.ModelChoiceField(
        queryset=InstitutoCultural.objects.all(),
        empty_label="Todos",
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )




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




class TalleresForm(forms.ModelForm):
    class Meta:
        model = Talleres
        fields = '__all__'
        widgets = {
            "nombreTaller": forms.TextInput(attrs={'class': 'form-control'}),
            "modalidadTaller": forms.Select(attrs={'class': 'form-control'}),
            "conduccionTaller": forms.Select(attrs={'class': 'form-control'}),
            "nivelTaller": forms.Select(attrs={'class': 'form-control'}),
            "generoTaller": forms.Select(attrs={'class': 'form-control'}),
            "disciplinaTaller": forms.TextInput(attrs={'class': 'form-control'}),
            "coberturaTaller": forms.TextInput(attrs={'class': 'form-control'}),
            "institucionResponsableTaller": forms.Select(attrs={'class': 'form-control'}),
            "foroEspacioTaller": forms.TextInput(attrs={'class': 'form-control'}),
            "municipioTaller": forms.Select(attrs={'class': 'form-control'}),
            "localidadTaller": forms.TextInput(attrs={'class': 'form-control'}),
            "frecuenciaTaller": forms.Select(attrs={'class': 'form-control'}),
            "fechaRealizacionTaller": forms.TextInput(attrs={'class': 'form-control'}),
            "nombreInstructorTaller": forms.TextInput(attrs={'class': 'form-control'}),
            "procedenciaInstructorTaller": forms.TextInput(attrs={'class': 'form-control'}),
            "ninosTaller": forms.TextInput(attrs={'class': 'form-control'}),
            "ninasTaller": forms.TextInput(attrs={'class': 'form-control'}),
            "jovenesHombresTaller": forms.TextInput(attrs={'class': 'form-control'}),
            "jovenesMujeresTaller": forms.TextInput(attrs={'class': 'form-control'}),
            "adultosHombresTaller": forms.TextInput(attrs={'class': 'form-control'}),
            "adultosMujeresTaller": forms.TextInput(attrs={'class': 'form-control'}),
            "fuenteInformacionTaller": forms.TextInput(attrs={'class': 'form-control'}),
            "observacionesTaller": forms.Textarea(attrs={'class': 'form-control'}),
            "evidenciasTaller": forms.TextInput(attrs={'class': 'form-control'}),
        }

        



class ExposicionesForm(forms.ModelForm):
    class Meta:
        model = Exposiciones
        fields = '__all__'
        widgets = {
            "tipoExposicion": forms.Select(attrs={'class': 'form-control'}),
            "nombreExposicion": forms.TextInput(attrs={'class': 'form-control'}),
            "generoExposicion": forms.Select(attrs={'class': 'form-control'}),
            "disciplinaTecnicaExposicion": forms.TextInput(attrs={'class': 'form-control'}),
            "nombreEspecialistaExposicion": forms.TextInput(attrs={'class': 'form-control'}),
            "procedenciaEspecialistaExposicion": forms.TextInput(attrs={'class': 'form-control'}),
            "numeroExpositores": forms.TextInput(attrs={'class': 'form-control'}),
            "institucionResponsableDeExposicion": forms.Select(attrs={'class': 'form-control'}),
            "foroEspacioExposicion": forms.TextInput(attrs={'class': 'form-control'}),
            "periodoExposicion": forms.TextInput(attrs={'class': 'form-control'}),
            "fechaInauguracionExposicion": forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}), 
            "municipioExposicion": forms.Select(attrs={'class': 'form-control'}),
            "localidadExposicion": forms.TextInput(attrs={'class': 'form-control'}),
            "coberturaExposicion": forms.TextInput(attrs={'class': 'form-control'}),
            "ninosExposicion": forms.TextInput(attrs={'class': 'form-control'}),
            "ninasExposicion": forms.TextInput(attrs={'class': 'form-control'}),
            "jovenesHombresExposicion": forms.TextInput(attrs={'class': 'form-control'}),
            "jovenesMujeresExposicion": forms.TextInput(attrs={'class': 'form-control'}),
            "adultosHombresExposicion": forms.TextInput(attrs={'class': 'form-control'}),
            "adultosMujeresExposicion": forms.TextInput(attrs={'class': 'form-control'}),
            "fuenteInformacionExposicion": forms.TextInput(attrs={'class': 'form-control'}),
            "observacionesExposicion": forms.Textarea(attrs={'class': 'form-control'}),
            "evidenciasExposicion": forms.TextInput(attrs={'class': 'form-control'}),
            
        }



class EventosInstitutosForm(forms.ModelForm):
    class Meta:
        model = EventosInstitutos
        fields = '__all__'
        widgets = {
            "nombreEventoInst": forms.TextInput(attrs={'class': 'form-control'}),
            "generoEventoInst": forms.Select(attrs={'class': 'form-control'}),
            "disciplinaEventoInst": forms.TextInput(attrs={'class': 'form-control'}),
            "institucionResponsableDeEventoInst": forms.Select(attrs={'class': 'form-control'}),
            "foroEspacioEventoInst": forms.TextInput(attrs={'class': 'form-control'}),
            "municipioEventoInst": forms.Select(attrs={'class': 'form-control'}),
            "localidadEventoInst": forms.TextInput(attrs={'class': 'form-control'}),
            "fechaRealizacionEventoInst": forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}), 
            
            "nombreCreadorEventoInst": forms.TextInput(attrs={'class': 'form-control'}),
            "procedenciaCreadorEventoInst": forms.TextInput(attrs={'class': 'form-control'}),
            "numeroCreadoresHombresEventoInst": forms.TextInput(attrs={'class': 'form-control'}),
            "numeroCreadoresMujeresEventoInst": forms.TextInput(attrs={'class': 'form-control'}),
            
            "ninosEventoInst": forms.TextInput(attrs={'class': 'form-control'}),
            "ninasEventoInst": forms.TextInput(attrs={'class': 'form-control'}),
            "jovenesHombresEventoInst": forms.TextInput(attrs={'class': 'form-control'}),
            "jovenesMujeresEventoInst": forms.TextInput(attrs={'class': 'form-control'}),
            "adultosHombresEventoInst": forms.TextInput(attrs={'class': 'form-control'}),
            "adultosMujeresEventoInst": forms.TextInput(attrs={'class': 'form-control'}),
            "fuenteInformacionEventoInst": forms.TextInput(attrs={'class': 'form-control'}),
            "observacionesEventoInst": forms.Textarea(attrs={'class': 'form-control'}),
            "evidenciasEventoInst": forms.TextInput(attrs={'class': 'form-control'}),
            
        }
        


class DateInput(forms.DateInput):
    input_type = 'date'
    
    
class ProduccionInstitutosForm(forms.ModelForm):
    class Meta:
        model = ProduccionEditorialInstitutos
        fields = '__all__'
        widgets = {
            "nombreProduccionInst": forms.TextInput(attrs={'class': 'form-control'}),
            "generoProduccionInst": forms.Select(attrs={'class': 'form-control'}),
            "disciplinaProduccionInst": forms.TextInput(attrs={'class': 'form-control'}),
            "cantidadTirajeInst": forms.TextInput(attrs={'class': 'form-control'}),
            "institucionResponsableDeProduccionInst": forms.Select(attrs={'class': 'form-control'}),
            "fechaDePublicacion": forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}),
            "nombreAutorInst": forms.TextInput(attrs={'class': 'form-control'}),
            "procedenciaAutorInst": forms.TextInput(attrs={'class': 'form-control'}),
            "numeroAutoresHombresInst": forms.TextInput(attrs={'class': 'form-control'}),
            "numeroAutoresMujeresInst": forms.TextInput(attrs={'class': 'form-control'}),
            "fuenteInformacionProduccionInst": forms.TextInput(attrs={'class': 'form-control'}),
            "observacionesProduccionInst": forms.Textarea(attrs={'class': 'form-control'}),
            "evidenciasProduccion": forms.TextInput(attrs={'class': 'form-control'}),
            
        }