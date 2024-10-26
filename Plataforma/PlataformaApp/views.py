from django.shortcuts import render,redirect
from PlataformaApp.models import Plataforma
from PlataformaApp.forms import FormPlataforma
# Create your views here.

def index(request):
    return render(request, 'Templates_PlataformaApp/index.html')

def listadoPlataforma(request):
    plataformas = Plataforma.objects.all()
    data = {'plataformas': plataformas}
    return render(request, 'Templates_PlataformaApp/Plataformas.html', data)

def agregarPlataforma(request):
    form = FormPlataforma()
    if request.method == 'POST':
        form = FormPlataforma(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request,'Templates_PlataformaApp/agregarPlataforma.html', data)

def eliminarPlataforma(requuest,id):
    plataforma = Plataforma.objects.get(id = id)
    plataforma.delete()
    return redirect('../plataformas/')

def actualizarPlataforma(request, id):
    plataforma = Plataforma.objects.get(id = id)
    form = FormPlataforma(instance = plataforma)
    if request.method == 'POST':
        form = FormPlataforma(request.POST, instance = plataforma)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request,'Templates_PlataformaApp/agregarPlataforma.html', data)