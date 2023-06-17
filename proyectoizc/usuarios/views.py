from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SuperuserCreationForm


# Create your views here.


# Función para loguearse.
# Se nombra diferente a la función de iniciar sesión de django.
def myLogIn(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
            
        if user is None:  # Si el usuario no existe o la contraseña es incorrecta
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o la contraseña son incorrectos'
            })
        
        else:
            # Guarda cookie para saber si el usuario está logueado o no.
            
                
            login(request, user)
            return redirect('home')


# Función para cerrar sesión.
@login_required
# Se nombra diferente a la función de cerrar sesión de django.
def signout(request):
    logout(request)
    return redirect('myLogin')



def lista_usuarios(request):
    users = User.objects.all()
    return render(request, 'lista_usuarios.html', {'users': users})



def reinicio_contraseña(request):
    return render(request, 'reset_password.html')


def register_superuser(request):
    if request.method == 'POST':
        form = SuperuserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion')  # Redirige a una página de éxito o a donde desees
    else:
        form = SuperuserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'registro_usuarios.html', context)
