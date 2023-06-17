from django import forms
from .models import MUNICIPIOS, AsistenciaMuseo, DatosMuseo
from mapwidgets.widgets import GooglePointFieldWidget

#eventos hacerlo en models

class CustomGooglePointFieldWidget(GooglePointFieldWidget):
    template_name = 'map_template.html'
    
class MuseoForm(forms.ModelForm):
    imagenMuseo = forms.ImageField()
    class Meta:
        model = DatosMuseo
        fields = '__all__'
        widgets = {
            "nombre_museo": forms.TextInput(attrs={'class': 'form-control'}),
            "datos_generales": forms.Textarea(attrs={'class': 'form-control'}),
            "municipioMuseo": forms.Select(attrs={'class': 'form-control'}),
            "direccionMuseo": forms.TextInput(attrs={'class': 'form-control'}),
            "horariosMuseo": forms.Textarea(attrs={'class': 'form-control'}),
            "costoMuseo": forms.TextInput(attrs={'class': 'form-control'}),
            'ubicacionDeMuseo': CustomGooglePointFieldWidget,
        }
        
    def clean_datos_generales(self):
        datos_generales = self.cleaned_data['datos_generales']
        if len(datos_generales) > 600:
            datos_generales = datos_generales[:600]
        return datos_generales
        


class AsistenciaMuseoForm(forms.ModelForm):
    class Meta:
        model = AsistenciaMuseo
        fields = '__all__'
        widgets = {
            "museo": forms.Select(attrs={'class': 'form-control'}),
            "anio": forms.NumberInput(attrs={'class': 'form-control'}),
            "locales_hombres": forms.NumberInput(attrs={'class': 'form-control'}),
            "locales_mujeres": forms.NumberInput(attrs={'class': 'form-control'}),
            "nacionales_hombres": forms.NumberInput(attrs={'class': 'form-control'}),
            "nacionales_mujeres": forms.NumberInput(attrs={'class': 'form-control'}),
            "extranjeros_hombres": forms.NumberInput(attrs={'class': 'form-control'}),
            "extranjeros_mujeres": forms.NumberInput(attrs={'class': 'form-control'}),
            
        }
        



## Formulario para aplicar filtros a la vista de platillos.
class FiltroAsistenciaForm(forms.Form):
    añoRegistro = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Año'}),
        required=False
    )

    municipioMuseo = forms.ChoiceField(
        required=False,
        choices = tuple([(u'', "Todos")] + MUNICIPIOS),
        widget = forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    
    museoDatos = forms.ModelChoiceField(
        queryset=DatosMuseo.objects.all(),
        empty_label="Todos",
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )