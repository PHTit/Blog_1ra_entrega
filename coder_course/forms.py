import datetime
from django import forms
from django.forms import ModelForm
from coder_course.models import Libros, Peliculas, Gastronomia, Viajes

class LibrosForm(forms.Form):
    name = forms.CharField(max_length=40,min_length=3,label="Titulo")
    plot = forms.CharField(max_length=150,min_length=3,label="Reseña")
    

class PeliculasForm(forms.Form):
    name = forms.CharField(max_length=40,min_length=3,label="Titulo")
    plot = forms.CharField(max_length=150,min_length=3,label="Reseña")
    

class GastronomiaForm(forms.Form):
    name = forms.CharField(max_length=40,min_length=3,label="Titulo")
    plot = forms.CharField(max_length=150,min_length=3,label="Reseña")
    

class ViajesForm(forms.Form):
    name = forms.CharField(max_length=40,min_length=3,label="Titulo")
    plot = forms.CharField(max_length=150,min_length=3,label="Reseña")
    

