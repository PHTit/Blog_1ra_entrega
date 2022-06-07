from django.db import models

class Libros(models.Model):
    name = models.CharField(max_length=40)
    plot = models.CharField(max_length=150)

class Peliculas(models.Model):
    name = models.CharField(max_length=40)
    plot = models.CharField(max_length=150)
    
class Gastronomia(models.Model):
    name = models.CharField(max_length=40)
    plot = models.CharField(max_length=150)

class Viajes(models.Model):
    name = models.CharField(max_length=40)
    plot = models.CharField(max_length=150)
