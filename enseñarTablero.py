from django.shortcuts import render

def enseñarTablero(request, filas, columnas):
    tabla_datos = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            celda = f"Fila {i}, Columna {j}"
            fila.append(celda)
        tabla_datos.append(fila)
        
    return render(request, "tableroCreado.html", {"filas": filas, "columnas": columnas, "tabla_datos": tabla_datos})