from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MUNICIPIOS, EventosInstitutos, Exposiciones, InstitutoCultural, ProduccionEditorialInstitutos, Talleres
from .forms import EventosInstitutosForm, ExposicionesForm, FiltroInstitutoForm, InstitutoForm, ProduccionInstitutosForm, TalleresForm,FiltroNombreMunicipio
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

@login_required
def mostrarInstitutos(request):
    form = FiltroInstitutoForm()
    institutos = InstitutoCultural.objects.all()
    if request.method == 'POST':
        form = FiltroInstitutoForm(request.POST)
        nombreInstituto = request.POST.get('nombreInstituto', None)
        municipioInstituto = request.POST.get('municipioInstituto', None)

        if nombreInstituto:
            institutos = institutos.filter(nombreInstituto__contains=nombreInstituto)
        if municipioInstituto:
            institutos = institutos.filter(municipioInstituto=municipioInstituto)

    context = {
        'institutos':institutos,
        'form': form
    }

    return render(request, 'institutos_culturales.html', context)


@login_required
def mostrar_institutos_geolocalizacion(request):
    form = FiltroNombreMunicipio()
    institutos = InstitutoCultural.objects.all()
    if request.method == 'POST':
        form = FiltroNombreMunicipio(request.POST)
        nombreInstituto= request.POST.get('nombre', None)
        municipioInstituto = request.POST.get('municipio', None)

        if nombreInstituto:
            institutos = institutos.filter(nombreInstituto__contains=nombreInstituto)
        if municipioInstituto:
            institutos = institutos.filter(municipioCasa=municipioInstituto)
    context = {
        'institutos':institutos,
        'form': form
    }

    return render(request, 'geolocalizacion_institutos.html', context)


@login_required
def listado_municipios_institutos(request):
    conteo_institutos = []
    for municipio_id, municipio_nombre in MUNICIPIOS:
        conteo = {
            'municipioInstituto': municipio_id,
            'nombreMunicipio': municipio_nombre,
            'total': InstitutoCultural.objects.filter(municipioInstituto=municipio_id).count()
        }
        conteo_institutos.append(conteo)

    # Configurar la paginación
    paginator = Paginator(conteo_institutos, 20)  # Mostrar 10 registros por página
    page_number = request.GET.get('page')  # Obtener el número de página actual
    page_obj = paginator.get_page(page_number)  # Obtener la página actual de los resultados

    return render(request, 'listado_institutos.html', {'page_obj': page_obj})


# Create your views here.
@login_required
def registrarInstituto(request):
    if request.method == 'POST':
        form = InstitutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'El Instituto ha sido registrado exitosamente.')
            return redirect('institutos_culturales')
    else:
        form = InstitutoForm()
    return render(request, 'registrar_instituto.html', {'form': form})


@login_required
def editar_registroInstituto(request, id):
    registro = InstitutoCultural.objects.get(id=id)
    if request.method == 'POST':
        form = InstitutoForm(request.POST, request.FILES, instance=registro)  ## Se agregó la funcion request.FILES para que la imagen se cambie correctamente
        if form.is_valid():
            form.save()
            messages.success(request, 'El evento ha sido editado exitosamente.')
            return redirect('institutos_culturales')
    else:
        form = InstitutoForm(instance=registro)
    return render(request, 'editar_instituto.html', {'form': form})


@login_required
def vistaDetalladaInstituto(request, id):
    instituto = InstitutoCultural.objects.get(id=id)
    return render(request, 'detalle_instituto.html', {'instituto': instituto})


@login_required
def eliminarInstituto(request,id):
    InstitutoCultural.objects.get(id=id).delete()
    return redirect('institutos_culturales')


def mapa(request):
    return render(request, 'georreferenciacion_institutos.html')


@login_required
def mapa_georreferenciacion_institutos(request):
    municipios = [municipio[0] for municipio in MUNICIPIOS]
    conteo_institutos = []
    for municipio in municipios:
        conteo = {'municipioInstituto': municipio, 'total': InstitutoCultural.objects.filter(municipioInstituto=municipio).count()}
        conteo_institutos.append(conteo)
    return render(request, 'georreferenciacion_institutos.html', {'conteo_institutos': conteo_institutos})

#-------------------------------------------------------------
# TALLERES
@login_required
def registrarTaller(request):
    if request.method == 'POST':
        form = TalleresForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'El taller ha sido registrado exitosamente.')
            return redirect('talleres')
        else:
            messages.error(request, 'Por favor corrija los errores del formulario.')
    else:
        form = TalleresForm()
    return render(request, 'registrar_talleres.html', {'form': form})


@login_required
def mostrarTalleres(request):
    form = FiltroInstitutoForm()
    talleres = Talleres.objects.all()

    if request.method == 'POST':
        form = FiltroInstitutoForm(request.POST)
        nombreInstituto = request.POST.get('institucionResponsable', None)
        municipioInstituto = request.POST.get('municipioInstituto', None)

        if nombreInstituto:
            talleres = talleres.filter(institucionResponsableTaller=nombreInstituto)
        if municipioInstituto:
            talleres = talleres.filter(municipioTaller=municipioInstituto)

    context = {
        'talleres': talleres,
        'form': form
    }

    return render(request, 'talleres.html', context)



@login_required
def editar_registroTaller(request, id):
   registro = Talleres.objects.get(id=id)
   if request.method == 'POST':
      form = TalleresForm(request.POST, request.FILES, instance=registro)  ## Se agregó la funcion request.FILES para que la imagen se cambie correctamente
      if form.is_valid():
         form.save()
         messages.success(request, 'El taller ha sido editado exitosamente.')
         return redirect('talleres')
   else:
    form = TalleresForm(instance=registro)
   return render(request, 'editar_taller.html', {'form': form})



@login_required
def vistaDetalladaTaller(request, id):
    taller = Talleres.objects.get(id=id)
    return render(request, 'detalle_taller.html', {'taller': taller})


@login_required
def eliminarTaller(request,id):
    Talleres.objects.get(id=id).delete()
    return redirect('talleres')



#-------------------------------------------------------------
# EXPOSICIONES
@login_required
def registrarExposicion(request):
    if request.method == 'POST':
        form = ExposicionesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'La exposición ha sido registrado exitosamente.')
            return redirect('exposiciones')
        else:
            messages.error(request, 'Por favor corrija los errores del formulario.')
    else:
        form = ExposicionesForm()
    return render(request, 'registrar_exposiciones.html', {'form': form})


@login_required
def mostrarExposiciones(request):
    exposicionesForm = FiltroInstitutoForm()
    exposiciones = Exposiciones.objects.all()
    if request.method == 'POST':
        exposicionesForm = FiltroInstitutoForm(request.POST)
        nombreInstituto = request.POST.get('institucionResponsable', None)
        municipioInstituto = request.POST.get('municipioInstituto', None)

        if nombreInstituto:
            exposiciones = exposiciones.filter(institucionResponsableDeExposicion=nombreInstituto)
        if municipioInstituto:
            exposiciones = exposiciones.filter(municipioExposicion=municipioInstituto)
    
    context = {
        'exposiciones': exposiciones,
        'exposicionesForm': exposicionesForm
    }

    return render(request, 'exposiciones.html', context)




@login_required
def editar_registroExposicion(request, id):
    registro = Exposiciones.objects.get(id=id)
    if request.method == 'POST':
        form = ExposicionesForm(request.POST, request.FILES, instance=registro)  ## Se agregó la funcion request.FILES para que la imagen se cambie correctamente
        if form.is_valid():
            form.save()
            messages.success(request, 'El taller ha sido editado exitosamente.')
            return redirect('exposiciones')
    else:
        form = ExposicionesForm(instance=registro)
    return render(request, 'editar_exposicion.html', {'form': form})



@login_required
def vistaDetalladaExposicion(request, id):
    exposicion = Exposiciones.objects.get(id=id)
    return render(request, 'detalle_exposicion.html', {'exposicion': exposicion})


@login_required
def eliminarExposicion(request,id):
    Exposiciones.objects.get(id=id).delete()
    return redirect('exposiciones')

# EXPOSICIONES END
#-------------------------------------------------------------

# EVENTOS
@login_required
def registrarEventosInst(request):
    if request.method == 'POST':
        form = EventosInstitutosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'La exposición ha sido registrado exitosamente.')
            return redirect('eventosinst')
        else:
            messages.error(request, 'Por favor corrija los errores del formulario.')
    else:
        form = EventosInstitutosForm()
    return render(request, 'registrar_eventosinst.html', {'form': form})



@login_required
def mostrarEventosInst(request):
    form = FiltroInstitutoForm()
    eventosinst = EventosInstitutos.objects.all()
    if request.method == 'POST':
        form = FiltroInstitutoForm(request.POST)
        nombreInstituto = request.POST.get('institucionResponsable', None)
        municipioInstituto = request.POST.get('municipioInstituto', None)

        if nombreInstituto:
            eventosinst = eventosinst.filter(institucionResponsableDeEventoInst=nombreInstituto)
        if municipioInstituto:
            eventosinst = eventosinst.filter(municipioEventoInst=municipioInstituto)
    

    context = {
        'eventosinst':eventosinst,
        'form': form
    }

    return render(request, 'eventosinst.html', context)



@login_required
def editar_registroEventoInst(request, id):
    eventoInst = EventosInstitutos.objects.get(id=id)
    if request.method == 'POST':
        form = EventosInstitutosForm(request.POST, request.FILES, instance=eventoInst)  ## Se agregó la funcion request.FILES para que la imagen se cambie correctamente
        if form.is_valid():
            form.save()
            messages.success(request, 'El evento ha sido editado exitosamente.')
            return redirect('eventosinst')
    else:
        form = EventosInstitutosForm(instance=eventoInst)
    return render(request, 'editar_eventoInst.html', {'form': form})



@login_required
def vistaDetalladaEventosInst(request, id):
    eventosInst = EventosInstitutos.objects.get(id=id)
    return render(request, 'detalle_eventosinst.html', {'eventosInst': eventosInst})


@login_required
def eliminarEventoInst(request,id):
    EventosInstitutos.objects.get(id=id).delete()
    return redirect('eventosinst')



# PRODUCCION EDITORIAL
@login_required
def registrarProduccionInst(request):
    if request.method == 'POST':
        form = ProduccionInstitutosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'La producción ha sido registrado exitosamente.')
            return redirect('producciones')
        else:
            messages.error(request, 'Por favor corrija los errores del formulario.')
    else:
        form = ProduccionInstitutosForm()
    return render(request, 'registrar_produccion.html', {'form': form})



@login_required
def mostrarProducciones(request):
    form = FiltroInstitutoForm()
    produccionesinst = ProduccionEditorialInstitutos.objects.all()
    if request.method == 'POST':
        form = FiltroInstitutoForm(request.POST)
        nombreInstituto = request.POST.get('institucionResponsable', None)
        municipioInstituto = request.POST.get('municipioInstituto', None)

        if nombreInstituto:
            produccionesinst = produccionesinst.filter(institucionResponsableDeProduccionInst=nombreInstituto)
        if municipioInstituto:
            produccionesinst = produccionesinst.filter(municipioEventoInst=municipioInstituto)

    context = {
        'produccionesinst':produccionesinst,
        'form': form
    }

    return render(request, 'producciones.html', context)



@login_required
def editar_registroProduccionInst(request, id):
    produccioninst = ProduccionEditorialInstitutos.objects.get(id=id)
    if request.method == 'POST':
        form = ProduccionInstitutosForm(request.POST, request.FILES, instance=produccioninst)  ## Se agregó la funcion request.FILES para que la imagen se cambie correctamente
        if form.is_valid():
            form.save()
            messages.success(request, 'La produccion ha sido editada exitosamente.')
            return redirect('producciones')
    else:
        form = ProduccionInstitutosForm(instance=produccioninst)
    return render(request, 'editar_produccion.html', {'form': form})



@login_required
def vistaDetalladaProduccionInst(request, id):
    produccioninst = ProduccionEditorialInstitutos.objects.get(id=id)
    return render(request, 'detalle_produccion.html', {'produccioninst': produccioninst})


@login_required
def eliminarProduccionInst(request,id):
    ProduccionEditorialInstitutos.objects.get(id=id).delete()
    return redirect('producciones')
