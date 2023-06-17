from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import register_superuser

urlpatterns = [
    path('', views.myLogIn, name='myLogin'),
    path('logout', views.signout, name='logout'),
    path('gestion', views.lista_usuarios, name='gestion'),
    path('register/superuser/', register_superuser, name='register_superuser'),
    
    
    
    #password reset - cambio de contraseña URL's
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]

