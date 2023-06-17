from django.urls import path
from . import views

from .models import Eventos
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.mostrarEventos, name='eventos'),
    path('registrar_evento/', views.registrarEvento, name='registrar_evento'),
    path('editar_evento/<int:id>', views.editar_registroEvento, name='editar_evento'),
    path('detalle_evento/<int:id>', views.vistaDetallada, name='detalle_evento'),
    path('eliminar_evento/<int:id>', views.eliminarEvento, name='eliminar_evento'),
    path('georreferenciacion_eventos', views.mapa_georreferenciacion_eventos, name='georreferenciacion_eventos'),
    path('eventos_por_municipio/', views.eventos_por_municipio, name='eventos_por_municipio'),
    


] 