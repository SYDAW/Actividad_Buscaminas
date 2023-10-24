from django import forms
from .models import TableroForm

class TableroForm(forms.ModelForm):
    class Meta:
        model = TableroForm
        fields = ['filas', 'columnas']
