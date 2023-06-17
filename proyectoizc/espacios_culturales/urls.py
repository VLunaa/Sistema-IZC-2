from django.urls import path
from . import views

from .models import CasaCultura
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    ## CASAS DE CULTURA
    path('casas/', views.mostrar_casas_lista, name='casas'),
    path('casas/registrar_casa/', views.registrar_casa_cultura, name='registrar_casa'),
    path('casas/geolocalizacion/', views.mostrar_casas_geolocalizacion, name='geolocalizacion_casas'),
    path('casas/detalle_casa/<int:id>', views.detalle_casa_cultura, name='detalle_casa'),
    path('casas/editar_casa/<int:id>', views.editar_casa_cultura, name='editar_casa'),
    path('casas/eliminar_casa/<int:id>', views.eliminar_casa, name='eliminar_casa'),
    path('casas/georreferenciacion/', views.mapa_georreferenciacion_casas, name='georreferenciacion_casas'),
    
    ## ESPACIOS PARA EVENTOS
    path('espacios_eventos/', views.mostrar_espacios_lista, name='espacios'),
    path('espacios_eventos/registrar_espacio/', views.registrar_espacio_eventos, name='registrar_espacio'),
    path('espacios_eventos/editar_espacio/<int:id>', views.editar_espacio, name='editar_espacio'),
    path('espacios_eventos/geolocalizacion/', views.mostrar_espacios_geolocalizacion, name='geolocalizacion_espacios'),
    path('espacios_eventos/georreferenciacion_teatros_auditorios/', views.mapa_georreferenciacion_espacios_eventos, name='georreferenciacion_teatros_auditorios'),
    path('espacios_eventos/detalle_espacio/<int:id>', views.detalle_espacio, name='detalle_espacio'),
    path('espacios_eventos/eliminar_espacio/<int:id>', views.eliminar_espacio, name='eliminar_espacio'),

] 