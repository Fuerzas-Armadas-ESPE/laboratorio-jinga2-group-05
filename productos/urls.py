from django.urls import path
from . import views

urlpatterns = [
    # URLs de vistas normales
    # Crear la URL de la vista index
    path('', views.crear_productos, name='crear_producto'),
    # Crear la URL de la vista crear_producto
    path('products/', views.listar_productos, name='listar_producto'),
    path('delete', views.delete_productos, name='delete_productos')
]