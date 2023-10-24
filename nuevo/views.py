from django.shortcuts import render
from .forms import TableroForm

def crea_tablero(request):
    if request.method == 'POST':
        form = TableroForm(request.POST)
        if form.is_valid():
            filas = form.cleaned_data['filas']
            columnas = form.cleaned_data['columnas']
            # Aquí puedes hacer cualquier lógica para crear el tablero
            # y renderizarlo en un template.
    else:
        form = TableroForm()

    return render(request, 'crea_tablero.html', {'form': form})
