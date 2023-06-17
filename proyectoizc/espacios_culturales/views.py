from django.shortcuts import render, redirect
from .forms import CasaCulturaForm, FiltroNombreMunicipio, EspaciosEventosForm
from .models import CasaCultura, EspaciosEventos, MUNICIPIOS
from django.core.serializers import serialize
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count

# Create your views here.

## Inicio vistas para casas de Cultura

@login_required
def registrar_casa_cultura(request):
    
    if request.method == 'POST':
        form = CasaCulturaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('casas')
    else:
        form = CasaCulturaForm()
    return render(request, 'casas/registrar_casa.html', {'form': form})


@login_required
def mostrar_casas_geolocalizacion(request):
    form = FiltroNombreMunicipio()
    casas = CasaCultura.objects.all()
    if request.method == 'POST':
        form = FiltroNombreMunicipio(request.POST)
        nombreCasa= request.POST.get('nombre', None)
        municipioCasa = request.POST.get('municipio', None)

        if nombreCasa:
            casas = casas.filter(nombreCasa__contains=nombreCasa)
        if municipioCasa:
            casas = casas.filter(municipioCasa=municipioCasa)
    context = {
        'casas':casas,
        'form': form
    }

    return render(request, 'casas/geolocalizacion_casas.html', context)


@login_required
def mapa_georreferenciacion_espacios_eventos(request):
    espaciosEventos = EspaciosEventos.objects.all()
    municipios = [municipio[0] for municipio in MUNICIPIOS]
    conteo_espacios_eventos = []
    for municipio in municipios:
        conteo = {'municipioEspacio': municipio, 'total': EspaciosEventos.objects.filter(municipioEspacio=municipio).count()}
        conteo_espacios_eventos.append(conteo)
    return render(request, 'espacios_eventos/georreferenciacion_espacios_eventos.html', {'conteo_espacios_eventos': conteo_espacios_eventos})

def mostrar_casas_lista(request):
    form = FiltroNombreMunicipio()
    casas = CasaCultura.objects.all()
    if request.method == 'POST':
        form = FiltroNombreMunicipio(request.POST)
        nombreCasa= request.POST.get('nombre', None)
        municipioCasa = request.POST.get('municipio', None)

        if nombreCasa:
            casas = casas.filter(nombreCasa__contains=nombreCasa)
        if municipioCasa:
            casas = casas.filter(municipioCasa=municipioCasa)
    context = {
        'casas':casas,
        'form': form
    }

    return render(request, 'casas/casas.html', context)


def detalle_casa_cultura(request, id):
    casa = CasaCultura.objects.get(id=id)
    return render(request, 'casas/detalle_casa.html', {'casa': casa})

@login_required
def editar_casa_cultura(request, id):
    casa_cultura = CasaCultura.objects.get(id=id)
    if request.method == 'POST':
        form = CasaCulturaForm(request.POST, request.FILES, instance=casa_cultura)  ## Se agregó la funcion request.FILES para que la imagen se cambie correctamente
        if form.is_valid():
            form.save()
            return redirect('casas')

    else:
        form = CasaCulturaForm(instance=casa_cultura)
        return render(request, 'casas/editar_casa.html', {'form': form})



def mapa_georreferenciacion_casas(request):
    casas = CasaCultura.objects.all()
    municipios = [municipio[0] for municipio in MUNICIPIOS]
    conteo_casas = []
    for municipio in municipios:
        conteo = {'municipioCasa': municipio, 'total': CasaCultura.objects.filter(municipioCasa=municipio).count()}
        conteo_casas.append(conteo)
    #print("---------------------------------")
    #print("Lista Municipios: ")
    #print(municipios)
    #print("---------------------------------")
    #print("Lista Registros por municipios: ")
    #print(conteo_casas)
    return render(request, 'casas/georreferenciacion_casas.html', {'conteo_casas': conteo_casas})

@login_required
def eliminar_casa(request,id):
    CasaCultura.objects.get(id=id).delete()
    return redirect('casas')
## Fin Vistas casas de cultura


## Inicio vistas de espacios para eventos

@login_required
def registrar_espacio_eventos(request):
    
    if request.method == 'POST':
        form = EspaciosEventosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('espacios')
    else:
        form = EspaciosEventosForm()
    return render(request, 'espacios_eventos/registrar_espacio.html', {'form': form})

@login_required
def editar_espacio(request, id):
    espacio = EspaciosEventos.objects.get(id=id)
    if request.method == 'POST':
        form = EspaciosEventosForm(request.POST, request.FILES, instance=espacio)
        if form.is_valid():
            form.save()
            return redirect('espacios')

    else:
        form = EspaciosEventosForm(instance=espacio)
        return render(request, 'espacios_eventos/editar_espacio.html', {'form': form})

@login_required
def mostrar_espacios_lista(request):
    form = FiltroNombreMunicipio()
    espacios = EspaciosEventos.objects.all()
    if request.method == 'POST':
        form = FiltroNombreMunicipio(request.POST)
        nombreEspacio= request.POST.get('nombre', None)
        municipioEspacio = request.POST.get('municipio', None)

        if nombreEspacio:
            espacios = espacios.filter(nombreEspacio__contains=nombreEspacio)
        if municipioEspacio:
            espacios = espacios.filter(municipioEspacio=municipioEspacio)
    context = {
        'espacios':espacios,
        'form': form
    }

    return render(request, 'espacios_eventos/espacios.html', context)

@login_required
def mostrar_espacios_geolocalizacion(request):
    form = FiltroNombreMunicipio()
    espacios = EspaciosEventos.objects.all()
    if request.method == 'POST':
        form = FiltroNombreMunicipio(request.POST)
        nombreEspacio= request.POST.get('nombre', None)
        municipioEspacio = request.POST.get('municipio', None)

        if nombreEspacio:
            espacios = espacios.filter(nombreEspacio__contains=nombreEspacio)
        if municipioEspacio:
            espacios = espacios.filter(municipioEspacio=municipioEspacio)
    context = {
        'espacios':espacios,
        'form': form
    }

    return render(request, 'espacios_eventos/geolocalizacion_espacios.html', context)

@login_required
def detalle_espacio(request, id):
    espacio = EspaciosEventos.objects.get(id=id)
    return render(request, 'espacios_eventos/detalle_espacio.html', {'espacio': espacio})

@login_required
def eliminar_espacio(request,id):
    EspaciosEventos.objects.get(id=id).delete()
    return redirect('espacios')