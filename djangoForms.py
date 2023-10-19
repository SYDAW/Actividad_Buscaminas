from django import forms

class formTabla(forms.Form):
    filas = forms.IntergerField(label="Inserta el número de filas: ")
    columnas = forms.IntergerField(label="Inserta el número de columnas: ")

    