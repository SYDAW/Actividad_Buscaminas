from django.shortcuts import render
from .forms import crearTableroForm


def welcome(request):
    return render(request, 'blog/index.html', {})

def crearTablero(request):
    if request.method == 'GET':
        form = crearTableroForm(request.GET)
        if form.is_valid():
            filas = form.cleaned_data['filas']
            columnas = form.cleaned_data['columnas']
            return render(request, 'blog/mostrarTablero.html', {'filas':filas, 'columnas':columnas, 'rango_filas':range(filas), 'rango_columnas': range(columnas)})

    return render(request, 'blog/crearTablero.html', {'form':form})