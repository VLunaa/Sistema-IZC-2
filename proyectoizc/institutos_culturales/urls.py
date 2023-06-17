from django.urls import path
from . import views
from .models import InstitutoCultural
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.mostrarInstitutos, name='institutos_culturales'),
    path('registrar_instituto/', views.registrarInstituto, name='registrar_instituto'),
    path('editar_instituto/<int:id>', views.editar_registroInstituto, name='editar_instituto'),
    path('detalle_instituto/<int:id>', views.vistaDetalladaInstituto, name='detalle_instituto'),
    path('eliminar_instituto/<int:id>', views.eliminarInstituto, name='eliminar_instituto'),
    path('georreferenciacion_institutos/', views.mapa_georreferenciacion_institutos, name='georreferenciacion_institutos'),
    path('geolocalizacion/', views.mostrar_institutos_geolocalizacion, name='geolocalizacion_institutos'),
    path('listado_institutos', views.listado_municipios_institutos, name='listado_institutos'),
    
    #talleres
    path('registrar_taller/', views.registrarTaller, name='registrar_taller'),
    path('talleres/', views.mostrarTalleres, name='talleres'),
    path('talleres/editar_taller/<int:id>', views.editar_registroTaller, name='editar_taller'),
    path('talleres/detalle_taller/<int:id>', views.vistaDetalladaTaller, name='detalle_taller'),
    path('talleres/eliminar_taller/<int:id>', views.eliminarTaller, name='eliminar_taller'),
    #exposiciones
    path('registrar_exposicion/', views.registrarExposicion, name='registrar_exposicion'),
    path('exposiciones/', views.mostrarExposiciones, name='exposiciones'),
    path('exposiciones/editar_exposicion/<int:id>', views.editar_registroExposicion, name='editar_exposicion'),
    path('exposiciones/detalle_exposicion/<int:id>', views.vistaDetalladaExposicion, name='detalle_exposicion'),
    path('exposiciones/eliminar_exposicion/<int:id>', views.vistaDetalladaExposicion, name='eliminar_exposicion'),
    #eventos
    path('registrar_eventosinst/', views.registrarEventosInst, name='registrar_eventosinst'),
    path('eventosinst/', views.mostrarEventosInst, name='eventosinst'),
    path('eventosinst/editar_eventosInst/<int:id>', views.editar_registroEventoInst, name='editar_eventoInst'),
    path('eventosinst/detalle_eventosInst/<int:id>', views.vistaDetalladaEventosInst, name='detalle_eventoInst'),
    path('eventosinst/eliminar_eventosInst/<int:id>', views.eliminarEventoInst, name='eliminar_eventoInst'),
    #producciones
    path('registrar_produccion/', views.registrarProduccionInst, name='registrar_produccion'),
    path('producciones/', views.mostrarProducciones, name='producciones'),
    path('eventosinst/editar_produccionInst/<int:id>', views.editar_registroProduccionInst, name='editar_produccionInst'),
    path('eventosinst/detalle_produccionInst/<int:id>', views.vistaDetalladaProduccionInst, name='detalle_produccionInst'),
    path('eventosinst/eliminar_eventosInst/<int:id>', views.eliminarEventoInst, name='eliminar_eventoInst'),
    
    
    
]  
