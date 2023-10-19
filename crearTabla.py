from django.shortcuts import render
from .djangoForms import formTabla

def crear_tabla (pedir):
    if request.method == "POST":
        form = formTabla(request.POST)
        if from.es_valido():
            filas = form.cleaned_data["filas"]
            columnas = form.cleaned_data["columnas"]

            return redirect("tableroCreado", filas=filas, columnas=columnas)

    else:
        from = formTabla()

    return render(request, "index.html", {"form": form})
