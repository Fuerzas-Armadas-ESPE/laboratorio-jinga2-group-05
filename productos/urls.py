from django.urls import path
from . import views

urlpatterns = [
    # URLs de vistas normales
    path('', views.listar_productos, name='listar_productos'),
    path('create', views.crear_productos, name='crear_productos'),
    path('import', views.importar_productos, name='importar_productos'),
    path('update/<int:id>/', views.actualizar_productos, name='actualizar_productos'),
    path('delete', views.delete_productos, name='delete_productos'),
    path('export', views.export, name='export')
]