from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def sobre(request):
    return render(request, 'sobre.html')

def proyectos(request):
    return render(request, 'proyectos.html')

def estudios(request):
    return render(request, 'estudios.html')

def contacto(request):
    return render(request, 'contacto.html')
