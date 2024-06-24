from django.urls import path
from .views import listar, listarC, listarR, mostraA, crearN, mostrarC, crearC

urlpatterns = [
    path('', listar),
    path('colaborador', listarC),
    path('recepcionista', listarR),
    path('add', mostraA),
    path('add/aniadir/', crearN),
    path('addC', mostrarC),
    path('addC/aniadirC/', crearC)
]