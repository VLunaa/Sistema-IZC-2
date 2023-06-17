from django.urls import path
from . import views

from .models import Creadores
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.mostrarCreadores, name='creadores'),
    path('registrar_creador/', views.registrarCreador, name='registrar_creador'),
    path('detalle_creador/<int:id>', views.vista_detalle_creador, name='detalle_creador'),
    path('editar_creador/<int:id>', views.editarCreadores, name='editar_creador'),
    path('eliminar_creador/<int:id>', views.eliminarCreador, name='eliminar_creador'),
    path('mapa_creadores', views.mapa_georreferenciacion_creadores, name='mapa_creadores'),
    path('listado_creadores', views.listado_municipios, name='listado_creadores'),
    
    

] 