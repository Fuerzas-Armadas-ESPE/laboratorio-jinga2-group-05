from django.shortcuts import render, redirect
from .models import Producto
from django.views.decorators.csrf import csrf_exempt, csrf_protect

def listar_productos(request):
    # Consulta a la base de datos
    # Renderiza la plantilla listar.html
    productos = Producto.objects.all()
    return render(request, 'listar.html', {'productos': productos})

def crear_productos(request):
    # Crea un nuevo producto
    # Guarda el producto en la base de datos
    # Renderiza la plantilla listar.html
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        precio = request.POST.get("precio")
        cantidad = request.POST.get("cantidad")

        Producto.objects.create(nombre=nombre, precio=precio, cantidad=cantidad)

        return redirect('listar_productos')
    return render(request, 'crear.html')

#def actualizar_productos(request):
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
