from django.shortcuts import render
from .models import Producto
from django.views.decorators.csrf import csrf_exempt, csrf_protect

productos = []

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar.html', {'productos': productos})

# función para eliminar productos de la base de datos atraves de un formulario
@csrf_exempt
def delete_productos(request):
    productos = Producto.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        producto = Producto.objects.get(nombre=nombre)
        producto.delete()
    return render(request, 'delete.html', {'productos': productos})