from django.shortcuts import render, redirect
from .forms import PlatilloForm, FiltroPlatilloForm
from .models import MUNICIPIOS, Platillos
from django.core.serializers import serialize
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
@login_required
def registrarPlatillo(request):
    
    if request.method == 'POST':
        form = PlatilloForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'El Platillo se ha registrado correctamente.')
                return redirect('platillos')
            except Exception as e:
                messages.error(request, 'Ocurrió un error al guardar el Platillo. Error: {}'.format(str(e)))
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        form = PlatilloForm()
    return render(request, 'registrar_platillo.html', {'form': form})


# Create your views here.
@login_required
def registrarEvento(request):
    if request.method == 'POST':
        form = PlatilloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'El evento ha sido registrado exitosamente.')
            return redirect('platillos')
        else:
            messages.error(request, 'Por favor corrija los errores del formulario.')
            return redirect('registrar_platillo')
    else:
        form = PlatilloForm()
    return render(request, 'registrar_platillo.html', {'form': form})

@login_required
def mostrarPlatillos(request):
    form = FiltroPlatilloForm()
    platillos = Platillos.objects.all()
    if request.method == 'POST':
        form = FiltroPlatilloForm(request.POST)
        nombrePlatillo = request.POST.get('nombrePlatillo', None)
        municipioPlatillo = request.POST.get('municipioPlatillo', None)

        if nombrePlatillo:
            platillos = platillos.filter(nombrePlatillo__contains=nombrePlatillo)
        if municipioPlatillo:
            platillos = platillos.filter(municipioPlatillo=municipioPlatillo)
            
    context = {
        'platillos':platillos,
        
        'form': form
    }

    return render(request, 'platillos.html', context)

@login_required
def listado_municipios_platillos(request):
    conteo_platillos = []
    for municipio_id, municipio_nombre in MUNICIPIOS:
        conteo = {
            'municipioPlatillo': municipio_id,
            'nombreMunicipio': municipio_nombre,
            'total': Platillos.objects.filter(municipioPlatillo=municipio_id).count()
        }
        conteo_platillos.append(conteo)

    # Configurar la paginación
    paginator = Paginator(conteo_platillos, 20)  # Mostrar 10 registros por página
    page_number = request.GET.get('page')  # Obtener el número de página actual
    page_obj = paginator.get_page(page_number)  # Obtener la página actual de los resultados

    return render(request, 'listado_platillos.html', {'page_obj': page_obj})


@login_required
def mapa_georreferenciacion_platillos(request):
    platillos = Platillos.objects.all()
    municipios = [municipio[0] for municipio in MUNICIPIOS]
    conteo_platillos = []
    for municipio in municipios:
        conteo = {'municipioPlatillo': municipio, 'total': Platillos.objects.filter(municipioPlatillo=municipio).count()}
        conteo_platillos.append(conteo)
    return render(request, 'georreferenciacion_platillos.html', {'conteo_platillos': conteo_platillos})

@login_required
def editarPlatillo(request, id):
    platillo = Platillos.objects.get(id=id)
    if request.method == 'POST':
        form = PlatilloForm(request.POST, request.FILES, instance=platillo)
        if form.is_valid():
            form.save()
            return redirect('platillos')
    else:
        form = PlatilloForm(instance=platillo)
    return render(request, 'editar_platillo.html', {'form': form})


@login_required
def paginaNoEncontrada(request):
    return render(request, '404.html')

@login_required
def contar_platillos(request):
    count = Platillos.objects.count()
    return render(request, 'platillos.html', {'count': count})

@login_required
def detallesPlatillo(request, id):
    platillo = Platillos.objects.get(id=id)
    return render(request, 'detalles_platillo.html', {'platillo': platillo})

@login_required
def eliminarPlatillo(request,id):
    Platillos.objects.get(id=id).delete()
    return redirect('platillos')

