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

    path('habitacion/eliminar/<int:id>/', views.eliminar_habitacion, name='eliminar_habitacion'),

    path('login/', views.login_usuario, name='login'),

    path('logout/', views.logout_usuario, name='logout'),
    
    path('recepcion/', views.recepcion_panel, name='recepcion'),

]