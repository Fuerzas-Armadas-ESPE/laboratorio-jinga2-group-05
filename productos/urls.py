from django.urls import path
from . import views

urlpatterns = [
    # URLs de vistas normales
    path('', views.listar_productos, name='listar_productos'),
    path('/create', views.crear_productos, name='crear_productos'),
    path('delete', views.delete_productos, name='delete_productos')
]