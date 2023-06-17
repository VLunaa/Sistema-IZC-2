from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from creadores.models import Creadores
from platillos.models import Platillos
from institutos_culturales.models import InstitutoCultural,Talleres, EventosInstitutos, Exposiciones
from espacios_culturales.models import CasaCultura




@login_required
def home(request):
    cantidad_platillos = Platillos.objects.count()
    cantidad_institutos = InstitutoCultural.objects.count()
    cantidad_talleres = Talleres.objects.count()
    cantidad_eventosinst = EventosInstitutos.objects.count()
    cantidad_exposiciones = Exposiciones.objects.count()
    
    #Espacios culturales
    cantidad_espacios_casas = CasaCultura.objects.count()
    
    
    #creadores
    creadores = Creadores.objects.count()
    cantidad_artistas = Creadores.objects.count()
    
    return render(request, 'home.html', {
        'cantidad_platillos': cantidad_platillos,
        'cantidad_institutos': cantidad_institutos,
        'cantidad_talleres': cantidad_talleres,
        'cantidad_eventosinst': cantidad_eventosinst,
        'cantidad_exposiciones': cantidad_exposiciones,
        #casas
        'cantidad_espacios_casas': cantidad_espacios_casas,
        
        
        #creadores
        'cantidad_artistas': cantidad_artistas
    })


def mapa(request):

    return render(request, 'mapa.html', {

    })