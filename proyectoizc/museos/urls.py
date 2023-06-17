from django.urls import path
from museos import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.mostrar_museos, name='museos' ),
    path('registrar_datos', views.registrarDatosMuseo, name='registrar_datos' ),
    path('detalle_museo/<int:id>', views.detalle_museo, name='detalle_museo'),
    path('editar_museo/<int:id>', views.editar_registroMuseo, name='editar_museo'),
    path('eliminar_museo/<int:id>', views.eliminarMuseo, name='eliminar_museo'),
    path('registrar_asistencia/', views.registrar_asistencia, name='registrar_asistencia'),
    path('asistencias/', views.mostrar_asistencias, name='asistencias'),
    path('detalle_asistencias/<int:id>', views.detalle_asistencias, name='detalle_asistencias'),
    path('editar_asistencia/<int:id>', views.editar_registroAsistencia, name='editar_asistencia'),
    path('eliminar_asistencia/<int:id>', views.eliminarAsistencia, name='eliminar_asistencia'),
    path('georreferenciacion_museos/', views.mapa_georreferenciacion_museos, name='georreferenciacion_museos'),
    path('geolocalizacion_museos/', views.mostrar_museos_geolocalizacion, name='geolocalizacion_museos'),
    
    
] 