from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria
from .models import Anuncio
# Create your views here.
def home(request):
    #
    anuncios = Anuncio.objects.all()[:6]
    categorias = Categoria.objects.all()
    return render(request, 'home.html',{'categorias':categorias,
    'anuncios':anuncios,
    })