from django.urls import path
from .views import home, editar, criar, atualizar, deletar, index, pesquisar, mostrarTodes

urlpatterns = [
    path('', index),
    path('home', home),
    path('criar', criar, name="criar"),
    path('editar/<int:id>', editar, name='editar'),
    path('atualizar/<int:id>', atualizar, name="atualizar"),
    path('deletar/<int:id>', deletar, name='deletar'),
    path('pesquisar', pesquisar, name='pesquisar'),
    path('mostrarTodes', mostrarTodes, name='mostrarTodes')
]


