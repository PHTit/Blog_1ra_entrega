from django.contrib import admin
from django.forms import modelformset_factory
from coder_course.models import Gastronomia, Viajes, Libros, Peliculas
# Register your models here.

admin.site.register(Gastronomia)

admin.site.register(Viajes)

admin.site.register(Libros)

admin.site.register(Peliculas)