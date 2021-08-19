from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('materias', views.materias, name='materias'),
    path('hola', views.hola_mundo, name='hola'),
    path('nuevo', views.nuevo_curso, name='nuevo_curso'),
]
