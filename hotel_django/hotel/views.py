from django.shortcuts import render
from .models import Habitacion

def index(request):
    return render(request, 'hotel/index.html')

def catalogo(request):

    habitaciones = Habitacion.objects.all()

    return render(
        request,
        'hotel/catalogo.html',
        {
            'habitaciones': habitaciones
        }
    )

def contacto(request):
    return render(request, 'hotel/contacto.html')

def reservacion(request):
    return render(request, 'hotel/reservacion.html')

def mision(request):
    return render(request, 'hotel/mision.html')

def vision(request):
    return render(request, 'hotel/vision.html')

def formulario(request):
    return render(request, 'hotel/formulario.html')