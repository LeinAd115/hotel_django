from django.shortcuts import render

def index(request):
    return render(request, 'hotel/index.html')

def catalogo(request):
    return render(request, 'hotel/catalogo.html')

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