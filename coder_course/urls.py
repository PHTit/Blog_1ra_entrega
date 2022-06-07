from django.urls import path
from coder_course import views

urlpatterns = [
    path('index-2', views.index2, name="home"),
    path('gastronomia', views.gastronomia, name="gastronomia"),
    path('libros', views.libros, name="libros"), 
    path('viajes', views.viajes, name="viajes"), 
    path('peliculas', views.peliculas, name="peliculas"),
    path('gastronomia-django-forms', views.gastronomia_forms_django, name='GastronomiaDjangoForms'),
    path('libros-django-forms', views.libros_forms_django, name='LibrosDjangoForms'),
    path('viajes-django-forms', views.viajes_forms_django, name='ViajesDjangoForms'),
    path('peliculas-django-forms', views.peliculas_forms_django, name='PeliculasDjangoForms'),
    path('search', views.search, name='Search'),
]