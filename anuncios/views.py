from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria
from .models import Anuncio
from django.shortcuts import get_object_or_404


# Create your views here.
def home(request):
#
    site=""
    anuncios = Anuncio.objects.all()[:6]
    categorias = Categoria.objects.all()
    return render(request, 'home.html',{'categorias':categorias,
    'anuncios':anuncios,
    'site':site,
    })

def categoria(request,categoria_id):
#
    site="../"
    categorias = Categoria.objects.all()
    categoria= get_object_or_404(Categoria,id=categoria_id)
    anuncios = Anuncio.objects.filter(categoria=categoria)
    return render(request, 'home.html',{'categorias':categorias,
    'anuncios':anuncios,
    'categoria':categoria,
    'site':site,
    })

def anuncio(request,anuncio_id):
    site="../"
    categorias = Categoria.objects.all()
    anuncio= get_object_or_404(Anuncio,id=anuncio_id)
    return render(request, 'anuncio.html',{'categorias':categorias,
    'anuncio':anuncio,
    'site':site,
    })