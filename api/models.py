from django.db import models


class Evento(models.Model):
    id_evento = models.IntegerField(primary_key=True)
    nombre_evento = models.CharField(max_length=255)
    descripcion_evento = models.TextField()
    fecha_evento = models.DateField()
    hora_inicio = models.TimeField()
    hora_finalizacion = models.TimeField()
    fecha_finalizacion = models.DateField()
    capacidad_total = models.IntegerField()

    def __str__(self):
        return self.nombre_evento


class Seccion(models.Model):
    id_seccion = models.IntegerField(primary_key=True)
    id_evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    nombre_seccion = models.CharField(max_length=255)
    capacidad_seccion = models.IntegerField()
    precio_asiento = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre_seccion
