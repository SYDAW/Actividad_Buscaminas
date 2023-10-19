from django.shortcuts import render

def enseñarTablero(request, filas, columnas):
    return render(request, "tableroCreado.html", {"filas": filas, "columnas": columnas, "datosTabla": datosTabla})