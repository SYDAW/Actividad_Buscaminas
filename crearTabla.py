from django.shortcuts import render, redirect
from .djangoForms import formTabla

def crear_tabla (request):
    if request.method == "POST":
        form = formTabla(request.POST)
        if form.es_valido():
            filas = form.cleaned_data["filas"]
            columnas = form.cleaned_data["columnas"]

            return redirect("tableroCreado", filas=filas, columnas=columnas)

    else:
        form = formTabla()

    return render(request, "index.html", {"form": form})
