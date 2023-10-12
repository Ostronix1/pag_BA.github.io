from django.db import models


class Voluntario(models.Model):
    cedula = models.PositiveIntegerField()
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nombre


#======================================================================

class Asistencia(models.Model):
    cedula = models.PositiveIntegerField()
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    horas = models.PositiveIntegerField()
    kg_derivados = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nombre
