from django.urls import path
from django.contrib.auth import views as auth_views
from .views import agregar_vehiculo
from .views import *
from . import views


urlpatterns = [
    path('', index, name='index'),

    path('agregar_vehiculo/', views.agregar_vehiculo, name='agregar_vehiculo'),

     # Rutas de autenticación
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('registro/', views.registro, name='registro'), 
    path('vehiculo_catalogo/', views.vehiculo_catalogo, name='vehiculo_catalogo'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),

    ]