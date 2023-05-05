from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarProducto/', views.registro_producto),
    path('edicionProducto/<codigo>', views.edicion_producto),
    path('editarProducto/', views.editar_producto),
    path('eliminarProducto/<codigo>', views.eliminar_producto)
]
