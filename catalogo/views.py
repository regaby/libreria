from django.shortcuts import render, get_object_or_404
from . models import Libro
from django.http import Http404
from django.db.models import Avg, Min, Max


# Create your views here.
def index(request):
    libros = Libro.objects.all().order_by('puntaje')
    total_libros = libros.count()
    return render (request, 'catalogo/index.html', {
        'libros': libros,
        'total_libros': total_libros,
        'promedio': libros.aggregate(Avg("puntaje")),
        'min': libros.aggregate(Min("puntaje")),
        'max': libros.aggregate(Max("puntaje")),
    })

def libro(request, slug):
    # try:
    #     libro = Libro.objects.get(slug=slug)
    # except:
    #     raise Http404
    libro = get_object_or_404(Libro, slug=slug)
    return render (request, 'catalogo/libro.html', {
        'titulo': libro.titulo,
        'puntaje': libro.puntaje,
        'es_bestseller': libro.es_bestseller,
        'autor': libro.autor,
    })