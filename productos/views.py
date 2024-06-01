from django.shortcuts import render, redirect
from .models import Producto

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
    