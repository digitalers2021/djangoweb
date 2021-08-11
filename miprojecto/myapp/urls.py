from django.urls import path

from . import views

urlpatterns = [
    path('html', views.mi_template, name='htmltemplate'),
    path('', views.index, name='index'),
]
