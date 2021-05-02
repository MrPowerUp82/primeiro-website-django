from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria
from .models import Anuncio
from django.shortcuts import get_object_or_404


# Create your views here.
def home(request):
#   def search(request):
    anuncios = Anuncio.objects.all()[:6]
    categorias = Categoria.objects.all()
    site=""
    return render(request, 'home.html',{'categorias':categorias,
    'anuncios':anuncios,
    'site':site,
    })

def categoria(request,categoria_id):
#
    site="../"
    categorias = Categoria.objects.all()
    #categoria= get_object_or_404(Categoria,id=categoria_id)
    try:
        categoria= Categoria.objects.get(id=categoria_id)
        anuncios = Anuncio.objects.filter(categoria=categoria)
    except:
        return render(request, '404.html')
    return render(request, 'home.html',{'categorias':categorias,
    'anuncios':anuncios,
    'categoria':categoria,
    'site':site,
    })

def anuncio(request,anuncio_id):
    site="../"
    categorias = Categoria.objects.all()
    try:
        anuncio= Anuncio.objects.get(id=anuncio_id)
    except:
        return render(request, '404.html')
    return render(request, 'anuncio.html',{'categorias':categorias,
    'anuncio':anuncio,
    'site':site,
    })


def searchbar(request):
    if request.method == "GET":
        site="../"
        search = request.GET.get('search')
        categorias = Categoria.objects.all()
        anuncios = Anuncio.objects.all().filter(titulo=search)
        if anuncios.count() <= 0:
            try:
                cate = Categoria.objects.only('id').get(titulo=search).id
                anuncios = Anuncio.objects.all().filter(categoria_id=cate)
            except:
                anuncio = Anuncio.objects.all()
                categoria = Categoria.objects.all()
                searchup=search[0].upper()+search[1:]
                searchlw=search.lower()
                palavra=search
                if " " in palavra:
                    palavra=palavra.split(' ')
                    n=len(palavra)
                    i=0
                    palavras=''
                    while i < n:
                        palavras= palavras + str(palavra[i][0].upper()+palavra[i][1:]) + ' '
                        i+=1
                n=len(palavras)
                n=n-1
                palavras=palavras[:n]

                for anun in anuncio:
                    if search in anun.titulo or search in anun.descricao or searchup in anun.titulo or searchup in anun.descricao or searchlw in anun.titulo or searchlw in anun.descricao or palavras in anun.titulo or palavras in anun.descricao:
                        anun_id=anun.categoria_id
                        anuncios = Anuncio.objects.all().filter(categoria_id=anun_id)
        return render(request, 'home.html',{'categorias':categorias,
    'anuncios':anuncios,
    'site':site,
    })