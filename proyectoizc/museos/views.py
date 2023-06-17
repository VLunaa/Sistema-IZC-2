from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from museos.models import MUNICIPIOS
from museos.forms import FiltroAsistenciaForm
from museos.forms import AsistenciaMuseoForm
from museos.models import DatosMuseo, FiltroNombreMunicipio, AsistenciaMuseo
from django.contrib import messages
from museos.forms import MuseoForm


# Create your views here.
def menu_datos(request):
    return render(request, 'datos_historicos.html', {
    })
    

@login_required
def editar_registroMuseo(request, id):
    registro = DatosMuseo.objects.get(id=id)
    if request.method == 'POST':
        form = MuseoForm(request.POST, request.FILES, instance=registro)  ## Se agregó la funcion request.FILES para que la imagen se cambie correctamente
        if form.is_valid():
            form.save()
            messages.success(request, 'El evento ha sido editado exitosamente.')
            return redirect('museos')
    else:
        form = MuseoForm(instance=registro)
    return render(request, 'editar_museo.html', {'form': form})



@login_required
def editar_registroAsistencia(request, id):
    asistencia = AsistenciaMuseo.objects.get(id=id)
    if request.method == 'POST':
        form = AsistenciaMuseoForm(request.POST, request.FILES, instance=asistencia)  ## Se agregó la funcion request.FILES para que la imagen se cambie correctamente
        if form.is_valid():
            form.save()
            messages.success(request, 'El evento ha sido editado exitosamente.')
            return redirect('asistencias')
    else:
        form = AsistenciaMuseoForm(instance=asistencia)
    return render(request, 'editar_asistencia.html', {'form': form})



@login_required
def eliminarAsistencia(request,id):
    AsistenciaMuseo.objects.get(id=id).delete()
    return redirect('asistencias')



# registrar museo o lugar para dato historico
@login_required
def registrarDatosMuseo(request):
    if request.method == 'POST':
        form = MuseoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'El evento ha sido registrado exitosamente.')
            return redirect('museos')
        else:
            messages.error(request, 'Por favor corrija los errores del formulario.')
    else:
        form = MuseoForm()
    return render(request, 'registrar_datos.html', {'form': form})



@login_required
def eliminarMuseo(request,id):
    DatosMuseo.objects.get(id=id).delete()
    return redirect('museos')

@login_required
def detalle_museo(request, id):
    museo = DatosMuseo.objects.get(id=id)
    return render(request, 'detalle_museo.html', {'museo': museo})

@login_required
def mostrar_museos(request):
    form = FiltroNombreMunicipio()
    museos = DatosMuseo.objects.all()
    if request.method == 'POST':
        form = FiltroNombreMunicipio(request.POST)
        nombre_museo= request.POST.get('nombre', None)
        municipioMuseo = request.POST.get('municipio', None)

        if nombre_museo:
            museos = museos.filter(nombre_museo__contains=nombre_museo)
        if municipioMuseo:
            museos = museos.filter(municipioMuseo=municipioMuseo)
    context = {
        'museos':museos,
        'form': form
    }

    return render(request, 'museos.html', context)



# registrar museo o lugar para dato historico
@login_required
def registrar_asistencia(request):
    if request.method == 'POST':
        form = AsistenciaMuseoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'La asistencia ha sido registrado exitosamente.')
            return redirect('museos')
            # Realiza alguna redirección o muestra un mensaje de éxito
    else:
        form = AsistenciaMuseoForm()
    
    return render(request, 'registrar_asistencia.html', {'form': form})
@login_required
def mostrar_asistencias(request):
    form = FiltroAsistenciaForm()
    asistencias = AsistenciaMuseo.objects.all()
    
    if request.method == 'POST':
        form = FiltroAsistenciaForm(request.POST)
        nombre_museo = request.POST.get('nombre', None)
        anio_registro = request.POST.get('añoRegistro', None)
        municipio_museo = request.POST.get('municipioMuseo', None)
        museo_seleccionado = request.POST.get('museoDatos', None)

        if nombre_museo:
            asistencias = asistencias.filter(museo__nombre_museo__contains=nombre_museo)
        if anio_registro:
            asistencias = asistencias.filter(anio=anio_registro)
        if municipio_museo:
            asistencias = asistencias.filter(museo__municipioMuseo=municipio_museo)
        if museo_seleccionado:
            asistencias = asistencias.filter(museo=museo_seleccionado)
            
    context = {
        'asistencias': asistencias,
        'form': form
    }

    return render(request, 'asistencias_museos.html', context)




@login_required
def detalle_asistencias(request, id):
    asistencia = AsistenciaMuseo.objects.get(id=id)
    return render(request, 'detalle_asistencia.html', {'asistencia': asistencia})




@login_required
def mostrar_museos_geolocalizacion(request):
    form = FiltroNombreMunicipio()
    museos = DatosMuseo.objects.all()
    if request.method == 'POST':
        form = FiltroNombreMunicipio(request.POST)
        nombreMuseo= request.POST.get('nombre', None)
        municipioMuseo = request.POST.get('municipio', None)

        if nombreMuseo:
            museos = museos.filter(nombreMuseo__contains=nombreMuseo)
        if municipioMuseo:
            museos = museos.filter(municipioCasa=municipioMuseo)
    context = {
        'museos':museos,
        'form': form
    }

    return render(request, 'geolocalizacion_museos.html', context)




@login_required
def mapa_georreferenciacion_museos(request):
    municipios = [municipio[0] for municipio in MUNICIPIOS]
    conteo_museos = []
    for municipio in municipios:
        conteo = {'municipioMuseo': municipio, 'total': DatosMuseo.objects.filter(municipioMuseo=municipio).count()}
        conteo_museos.append(conteo)
    return render(request, 'georreferenciacion_museos.html', {'conteo_museos': conteo_museos})
