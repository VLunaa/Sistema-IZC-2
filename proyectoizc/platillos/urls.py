from django.urls import path
from . import views

from .models import Platillos
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.mostrarPlatillos, name='platillos'),
    path('registrar_platillo/', views.registrarPlatillo, name='registrar_platillo'),
    path('editar_platillo/<int:id>', views.editarPlatillo, name='editar_platillo'),
    path('detalles_platillo/<int:id>', views.detallesPlatillo, name='detalles_platillo'),
    path('eliminar_platillo/<int:id>', views.eliminarPlatillo, name='eliminar_platillo'),
    path('mapa_platillos/', views.mapa_georreferenciacion_platillos, name='mapa_platillos'),
    path('listado_platillos', views.listado_municipios_platillos, name='listado_platillos'),

    
    

    
] 