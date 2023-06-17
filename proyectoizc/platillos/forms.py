from django import forms
from .models import Platillos

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

class PlatilloForm(forms.ModelForm):
    class Meta:
        model = Platillos
        fields = '__all__'
        widgets = {
            "municipioPlatillo": forms.Select(attrs={'class': 'form-control'}),
            'nombrePlatillo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcionPlatillo': forms.Textarea(attrs={'class': 'form-control'}),
            'ingredientesPlatillo': forms.Textarea(attrs={'class': 'form-control'}),
        }


## Formulario para aplicar filtros a la vista de platillos.
class FiltroPlatilloForm(forms.Form):
    nombrePlatillo = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Nombre del platillo'}),
        required=False
    )

    municipioPlatillo = forms.ChoiceField(
        required=False,
        choices = tuple([(u'', "Todos")] + MUNICIPIOS),
        widget = forms.Select(
            attrs={'class': 'form-control'}
        )
    )
