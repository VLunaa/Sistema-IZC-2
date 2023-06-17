from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreadoresForm, FiltroCreadorForm
from .models import Creadores, MUNICIPIOS
from django.core.paginator import Paginator
from django.contrib import messages

@login_required
def registrarCreador(request):
    if request.method == 'POST':
        form = CreadoresForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'El creador se ha registrado correctamente.')
                return redirect('creadores')
            except Exception as e:
                messages.error(request, 'Ocurrió un error al guardar el creador. Error: {}'.format(str(e)))
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        form = CreadoresForm()
    return render(request, 'registrar_creador.html', {'form': form})



@login_required
def mostrarCreadores(request):
    form = FiltroCreadorForm()
    creadores = Creadores.objects.all()
    if request.method == 'POST':
        form = FiltroCreadorForm(request.POST)
        nombre = request.POST.get('nombre', None)
        municipioCreador = request.POST.get('municipioCreador', None)

        if nombre:
            creadores = creadores.filter(nombre__contains=nombre)
        if municipioCreador:
            creadores = creadores.filter(municipioCreador=municipioCreador)

    context = {
        'creadores':creadores,
        'form': form
    }

    return render(request, 'creadores.html', context)


@login_required
def mapa_georreferenciacion_creadores(request):
    creadores = Creadores.objects.all()
    municipios = [municipio[0] for municipio in MUNICIPIOS]
    conteo_creadores = []
    for municipio in municipios:
        conteo = {'municipioCreador': municipio, 'total': Creadores.objects.filter(municipioCreador=municipio).count()}
        conteo_creadores.append(conteo)
    return render(request, 'georreferenciacion_creadores.html', {'conteo_creadores': conteo_creadores})

@login_required
def listado_municipios(request):
    conteo_creadores = []
    for municipio_id, municipio_nombre in MUNICIPIOS:
        conteo = {
            'municipioCreador': municipio_id,
            'nombreMunicipio': municipio_nombre,
            'total': Creadores.objects.filter(municipioCreador=municipio_id).count()
        }
        conteo_creadores.append(conteo)

    # Configurar la paginación
    paginator = Paginator(conteo_creadores, 20)  # Mostrar 10 registros por página
    page_number = request.GET.get('page')  # Obtener el número de página actual
    page_obj = paginator.get_page(page_number)  # Obtener la página actual de los resultados

    return render(request, 'listado_creadores.html', {'page_obj': page_obj})



@login_required
def contar_creadores(request):
    count = Creadores.objects.count()
    return render(request, 'creadores.html', {'count': count})

@login_required
def vista_detalle_creador(request, id):
    creador = Creadores.objects.get(id=id)
    return render(request, 'detalle_creador.html', {'creador': creador})

@login_required
def editarCreadores(request, id):
    creadores_zac = Creadores.objects.get(id=id)
    if request.method == 'POST':
        form = CreadoresForm(request.POST, request.FILES, instance=creadores_zac)  ## Se agregó la funcion request.FILES para que la imagen se cambie correctamente
        if form.is_valid():
            form.save()
            return redirect('creadores')

    else:
        form = CreadoresForm(instance=creadores_zac)
        return render(request, 'editar_creador.html', {'form': form})



@login_required
def eliminarCreador(request,id):
    Creadores.objects.get(id=id).delete()
    return redirect('creadores')

@login_required
def listado_creadores(request):
    return render(request, 'listado_creadores.html')