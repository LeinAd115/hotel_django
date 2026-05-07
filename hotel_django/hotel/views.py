from django.shortcuts import render,get_object_or_404, redirect
from django.contrib import messages
from .models import Habitacion, Reservacion


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

    mensaje = None

    if request.method == "POST":

        Habitacion.objects.create(
            nombre=request.POST.get("nombre"),
            descripcion=request.POST.get("descripcion"),
            precio=request.POST.get("precio"),
            tipo=request.POST.get("tipo"),
            imagen=request.POST.get("imagen")
        )

        mensaje = "Habitación guardada correctamente"

    habitaciones = Habitacion.objects.all()

    return render(request, "hotel/formulario.html", {
        "habitaciones": habitaciones,
        "mensaje": mensaje
    })

def eliminar_habitacion(request, id):

    habitacion = get_object_or_404(Habitacion, id=id)
    habitacion.delete()

    messages.success(request, "Habitación eliminada correctamente")

    return redirect('formulario')