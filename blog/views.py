from django.shortcuts import render
from .forms import crearTableroForm


def welcome(request):
    return render(request, 'index.html', {})

def crearTablero(request):
    tablero_form = crearTableroForm()
    if request.method == 'GET':
        tablero_form = crearTableroForm(request.GET)

        if tablero_form.is_valid():
            columnas = tablero_form.cleaned_data['columnas']
            filas = tablero_form.cleaned_data['filas']
            return render(request, 'mostrarTablero.html',
                          {'filas':filas,'columnas':columnas,
                                    'rango_filas':range(filas), 'rango_columnas': range(columnas)})

    return render(request, 'crearTablero.html', {'form':tablero_form})