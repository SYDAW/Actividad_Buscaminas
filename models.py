from django.db import models

class TableroForm(models.Model):
    filas = models.PositiveIntegerField()
    columnas = models.PositiveIntegerField()

    def clean(self):
        if self.filas < 1 or self.columnas < 1:
            raise ValidationError("Los valores no pueden ser negativos.")
        if self.filas > 20 or self.columnas > 15:
            raise ValidationError("Las filas no pueden ser más de 20 y las columnas no pueden ser más de 15.")
