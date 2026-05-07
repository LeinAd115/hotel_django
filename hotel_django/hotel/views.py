from django.shortcuts import render,get_object_or_404, redirect
from django.contrib import messages
from .models import Habitacion, Reservacion
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse



def index(request):
    return render(request, 'hotel/index.html')


def catalogo(request):
    habitaciones = Habitacion.objects.all()
    return render(request, 'hotel/catalogo.html', {
        'habitaciones': habitaciones
    })


def contacto(request):
    return render(request, 'hotel/contacto.html')


def reservacion(request):

    if request.method == "POST":

        Reservacion.objects.create(
            nombre_cliente=request.POST.get("nombre"),
            email=request.POST.get("email"),
            habitacion=request.POST.get("habitacion"),
            fecha_entrada=request.POST.get("entrada"),
            fecha_salida=request.POST.get("salida")
        )

        return render(request, 'hotel/reservacion.html', {
            'mensaje': 'Reservación guardada correctamente'
        })

    return render(request, 'hotel/reservacion.html')


def mision(request):
    return render(request, 'hotel/mision.html')


def vision(request):
    return render(request, 'hotel/vision.html')


def formulario(request):

    if request.method == "POST":

        habitacion = Habitacion.objects.create(
            nombre=request.POST.get("nombre"),
            descripcion=request.POST.get("descripcion"),
            precio=request.POST.get("precio"),
            tipo=request.POST.get("tipo"),
            imagen=request.POST.get("imagen")
        )

        return JsonResponse({
            "mensaje": "Habitación guardada correctamente",
            "nombre": habitacion.nombre,
            "precio": str(habitacion.precio)
        })

    habitaciones = Habitacion.objects.all()

    return render(request, "hotel/formulario.html", {
        "habitaciones": habitaciones
    })

def eliminar_habitacion(request, id):

    habitacion = get_object_or_404(Habitacion, id=id)
    habitacion.delete()

    messages.success(request, "Habitación eliminada correctamente")

    return redirect('formulario')

def login_usuario(request):

    if request.method == "POST":

        user = authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password")
        )

        if user is not None:
            login(request, user)
            return redirect("formulario")
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, "hotel/login.html")

def logout_usuario(request):
    logout(request)
    return redirect("login")