from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),

    path('catalogo/', views.catalogo, name='catalogo'),

    path('contacto/', views.contacto, name='contacto'),

    path('reservacion/', views.reservacion, name='reservacion'),

    path('mision/', views.mision, name='mision'),

    path('vision/', views.vision, name='vision'),

    path('formulario/', views.formulario, name='formulario'),

]