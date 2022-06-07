from dataclasses import dataclass
from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from coder_course.models import Gastronomia, Viajes, Libros, Peliculas
from coder_course.forms import GastronomiaForm, ViajesForm, LibrosForm, PeliculasForm
#Programa Blog

def gastronomia(request):
    gastronomia = Gastronomia.objects.all()
    context_dict = {
        'gastronomia': gastronomia
    }

    return render(
        request=request,
        context=context_dict,
        template_name="coder_course\gastronomia.html" #Cambiar nombre de template
    )
def viajes(request):
    viajes = Viajes.objects.all()
    context_dict = {
        'viajes': viajes
    }

    return render(
        request=request,
        context=context_dict,
        template_name="coder_course\Viajes.html"#Cambiar nombre de template
    )
def libros(request):
    libros = Libros.objects.all()
    context_dict = {
        'libros': libros
    }

    return render(
        request=request,
        context=context_dict,
        template_name="coder_course\libros.html"
    )
def peliculas(request):
    peliculas = Peliculas.objects.all()
    context_dict = {
        'peliculas': peliculas
    }

    return render(
        request=request,
        context=context_dict,
        template_name="coder_course\peliculas.html"
    )
def index2(request):
    return render(request, "coder_course\index.html")

def gastronomia_forms_django(request):
    if request.method == 'POST':
        course_form = GastronomiaForm(request.POST)
        if course_form.is_valid():
            data = course_form.cleaned_data
            course = Gastronomia(
                name=data['name'], plot=data['plot'],)
            course.save()

            gas_var = Gastronomia.objects.all()
            context_dict = {
                'gastronomia': gas_var
            }
        return render(
            request=request,
            context=context_dict,
            template_name="coder_course/gastronomia.html"
        )
    gastronomia_form = GastronomiaForm(request.POST)
    context_dict = {
    'gastronomia_form': gastronomia_form
        }
    return render(
        request=request,
        context=context_dict,
        template_name='coder_course/gastronomia_django_forms.html'
    )

    
def viajes_forms_django(request):
    if request.method == 'POST':
        course_form = ViajesForm(request.POST)
        if course_form.is_valid():
            data = course_form.cleaned_data
            course = Viajes(name=data['name'], plot=data['plot'],)
            course.save()

            viajes_var = Viajes.objects.all()
            context_dict = {
                'viajes': viajes_var
            }
        return render(
        request=request,
        context=context_dict,
        template_name="coder_course/Viajes.html"
        )

    viajes_form = ViajesForm(request.POST)
    context_dict = {
    'viajes_form': viajes_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='coder_course/viajes_django_forms.html'
    )
def libros_forms_django(request):
    if request.method == 'POST':
        course_form = LibrosForm(request.POST)
        if course_form.is_valid():
            data = course_form.cleaned_data
            course = Libros(name=data['name'], plot=data['plot'],)
            course.save()

            libros_var = Libros.objects.all()
            context_dict = {
                'libros': libros_var
            }
        return render(
            request=request,
            context=context_dict,
            template_name="coder_course/libros.html"
            )

    libros_form = ViajesForm(request.POST)
    context_dict = {
    'libros_form': libros_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='coder_course/libros_django_forms.html'
    )

def peliculas_forms_django(request):
    if request.method == 'POST':
        course_form = PeliculasForm(request.POST)
        if course_form.is_valid():
            data = course_form.cleaned_data
            course = Peliculas(name=data['name'], plot=data['plot'],)
            course.save()

            pelis_var = Peliculas.objects.all()
            context_dict = {
                'peliculas': pelis_var
            }
        return render(
            request=request,
            context=context_dict,
            template_name="coder_course/peliculas.html"
            )

    peliculas_form = PeliculasForm(request.POST)
    context_dict = {
    'peliculas_form': peliculas_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='coder_course/peliculas_django_forms.html'
    )


def search(request):
    context_dict = dict()
    if request.GET['text_search']:
        search_param = request.GET['text_search']
        viajes = Viajes.objects.filter(name__contains=search_param)
        context_dict = {
            'viajes': viajes
        }
    return render(
        request=request,
        context=context_dict,
        template_name="coder_course/Viajes.html",
    )