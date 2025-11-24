from django.db import models

# CLASE DE POO: PRUEBA ACADÉMICA
class Proyecto(models.Model):
    """Clase que usa POO (Clases y Herencia) para definir la estructura de un proyecto."""
    titulo = models.CharField(max_length=100)
    tecnologia_inicial = models.CharField(max_length=50) 
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo