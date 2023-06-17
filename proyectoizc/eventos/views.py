from django.shortcuts import render, redirect
from .forms import EventoForm, FiltroEventoForm
from .models import MUNICIPIOS, Eventos
from django.core.serializers import serialize
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count

# Create your views here.
@login_required
def registrarEvento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'El evento ha sido registrado exitosamente.')
            return redirect('eventos')
        else:
            messages.error(request, 'Por favor corrija los errores del formulario.')
    else:
        form = EventoForm()
    return render(request, 'registrar_evento.html', {'form': form})

@login_required
def mostrarEventos(request):
    form = FiltroEventoForm()
    eventos = Eventos.objects.all()
    if request.method == 'POST':
        form = FiltroEventoForm(request.POST)
        nombreEvento = request.POST.get('nombreEvento', None)
        municipioEvento = request.POST.get('municipioEvento', None)

        if nombreEvento:
            eventos = eventos.filter(nombreEvento__contains=nombreEvento)
        if municipioEvento:
            eventos = eventos.filter(municipioEvento=municipioEvento)

    context = {
        'eventos':eventos,
        'form': form
    }

    return render(request, 'eventos.html', context)



@login_required
def mapa_georreferenciacion_eventos(request):
    eventos = Eventos.objects.all()
    municipios = [municipio[0] for municipio in MUNICIPIOS]
    conteo_eventos = []
    for municipio in municipios:
        conteo = {'municipioEvento': municipio, 'total': Eventos.objects.filter(municipioEvento=municipio).count()}
        conteo_eventos.append(conteo)
    return render(request, 'georreferenciacion_eventos.html', {'conteo_eventos': conteo_eventos})

@login_required
def editarEvento(request, id):
    evento = Eventos.objects.get(id=id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('editar_evento')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'editar_evento.html', {'form': form})

@login_required
def editar_registroEvento(request, id):
   registro = Eventos.objects.get(id=id)
   if request.method == 'POST':
      form = EventoForm(request.POST, request.FILES, instance=registro)  ## Se agregó la funcion request.FILES para que la imagen se cambie correctamente
      if form.is_valid():
         form.save()
         messages.success(request, 'El evento ha sido editado exitosamente.')
         return redirect('eventos')
   else:
    form = EventoForm(instance=registro)
   return render(request, 'editar_evento.html', {'form': form})

@login_required
def contar_eventos(request):
    count = Eventos.objects.count()
    return render(request, 'eventos.html', {'count': count})

@login_required
def vistaDetallada(request, id):
    evento = Eventos.objects.get(id=id)
    return render(request, 'detalle_evento.html', {'evento': evento})



@login_required
def eliminarEvento(request,id):
    Eventos.objects.get(id=id).delete()
    return redirect('eventos')


def mapaEventos(request):
    return render(request, 'mapa_eventos.html', {
    })


def eventos_por_municipio(request):
    eventos_por_municipio = Eventos.objects.values('municipioEvento').annotate(num_eventos=Count('id'))
    return render(request, 'eventos_por_municipio.html', {'eventos_por_municipio': eventos_por_municipio})



def mapaEventos(request):
    eventos_por_municipio = {}
    for municipio in dict(MUNICIPIOS):
        eventos_por_municipio[municipio] = Eventos.objects.filter(municipioEvento=municipio).count()
    context = {
        'eventos_por_municipio': eventos_por_municipio,
    }
    return render(request, 'mapa_eventos.html', context)