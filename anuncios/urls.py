from django.urls import path
from .views import categoria
from .views import home
urlpatterns =[
    path('', home, name='home'),
    path('categoria/<int:categoria_id>', categoria, name='categoria'),
]