from django.urls import path
from .views import categoria
from .views import home
from .views import anuncio
from .views import searchbar
urlpatterns =[
    path('', home, name='home'),
    path('categoria/<int:categoria_id>', categoria, name='categoria'),
    path('anuncio/<int:anuncio_id>', anuncio, name='anuncio'),
    path('searchbar/', searchbar, name='searchbar'),
]