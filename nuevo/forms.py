from django import forms
from django.core.exceptions import ValidationError

from .models import TableroForm

class TableroForm(forms.ModelForm):
    class Meta:
        model = TableroForm
        fields = ['filas', 'columnas']
