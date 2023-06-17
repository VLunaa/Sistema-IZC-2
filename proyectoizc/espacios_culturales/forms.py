from django import forms
from mapwidgets.widgets import GooglePointFieldWidget

from .models import CasaCultura, EspaciosEventos

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

## FORMS CASAS DE CULTURA
class CasaCulturaForm(forms.ModelForm):
    class Meta:
        model = CasaCultura
        fields = '__all__'
        widgets = {
            "nombreCasa": forms.TextInput(attrs={'class': 'form-control'}),
            'datosGenerales': forms.Textarea(attrs={'class': 'form-control'}),
            'municipioCasa': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'ubicacion': CustomGooglePointFieldWidget,
        }

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

## FORMS ESPACIOS PARA EVENTOS
class EspaciosEventosForm(forms.ModelForm):
    class Meta:
        model = EspaciosEventos
        fields = '__all__'
        widgets = {
            "nombreEspacio": forms.TextInput(attrs={'class': 'form-control'}),
            'datosGenerales': forms.Textarea(attrs={'class': 'form-control'}),
            'municipioEspacio': forms.Select(attrs={'class': 'form-control'}),
            'tipoEspacio': forms.Select(attrs={'class': 'form-control'}),
            'ubicacion': CustomGooglePointFieldWidget,
            'aforo': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
        }