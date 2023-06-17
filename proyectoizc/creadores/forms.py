from django import forms
from .models import Creadores

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

class DateInput(forms.DateInput):
    input_type = 'date'

class CreadoresForm(forms.ModelForm):
    class Meta:
        model = Creadores
        fields = '__all__'
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "apellido_paterno": forms.TextInput(attrs={'class': 'form-control'}),
            "apellido_materno": forms.TextInput(attrs={'class': 'form-control'}),
            "fecha_nacimiento": forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}), 
            "genero": forms.Select(attrs={'class': 'form-control'}),
            "contacto": forms.TextInput(attrs={'class': 'form-control'}),
            "municipioCreador": forms.Select(attrs={'class': 'form-control'}),
            "localidadCreador": forms.TextInput(attrs={'class': 'form-control'}),
            "escolaridadCreador": forms.Select(attrs={'class': 'form-control'}),
            "disciplinaCreador": forms.Select(attrs={'class': 'form-control'}),
            "especialidadCreador": forms.TextInput(attrs={'class': 'form-control'}),
            "otraDisciplinaCreador": forms.TextInput(attrs={'class': 'form-control'}),
            "opcionCreador": forms.Select(attrs={'class': 'form-control'}),
            "gradoConocimientoCreador": forms.Select(attrs={'class': 'form-control'}),
            "lugarFormacionCreador": forms.TextInput(attrs={'class': 'form-control'}),
            "vigenciaCreador": forms.Select(attrs={'class': 'form-control'}),
            
        }

        

## Formulario para aplicar filtros a la vista de creador.
class FiltroCreadorForm(forms.Form):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Nombre del Creador'}),
        required=False
    )

    municipioCreador = forms.ChoiceField(
        required=False,
        choices = tuple([(u'', "Todos")] + MUNICIPIOS),
        widget = forms.Select(
            attrs={'class': 'form-control'}
        )
    )

