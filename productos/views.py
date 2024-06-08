from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.files import File
import csv
from django.http import HttpResponse

def listar_productos(request):
    # Consulta a la base de datos
    # Renderiza la plantilla listar.html
    productos = Producto.objects.all()
    return render(request, 'listar.html', {'productos': productos})

def export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    
    writer = csv.writer(response)
    productos = Producto.objects.all()
    for prod in productos:
        writer.writerow([prod.nombre, prod.precio, prod.cantidad])
    
    return response

# función para importar productos de un archivo csv
def importar_productos(request):
    if request.method == "POST":
        archivo = request.FILES["file"]
        for linea in archivo:
            linea = linea.decode("utf-8")
            nombre, precio, cantidad = linea.split(",")
            Producto.objects.create(nombre=nombre, precio=precio, cantidad=cantidad)
        return redirect('listar_productos')
    return render(request, 'crear.html')

def crear_productos(request):
    # Crea un nuevo producto
    # Guarda el producto en la base de datos
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        precio = request.POST.get("precio")
        cantidad = request.POST.get("cantidad")

        Producto.objects.create(nombre=nombre, precio=precio, cantidad=cantidad)

        return redirect('listar_productos')
    return render(request, 'crear.html')

def actualizar_productos(request, id):
    producto = get_object_or_404(Producto, id=id)
    
    if request.method == "POST":
        producto.nombre = request.POST.get("nombre")
        producto.precio = request.POST.get("precio")
        producto.cantidad = request.POST.get("cantidad")
        producto.save()
        return redirect('listar_productos')
    
    return render(request, 'actualizar.html', {'producto': producto})


# función para eliminar productos de la base de datos atraves de un formulario
def delete_productos(request):
    productos = Producto.objects.all()
    if request.method == 'POST':
        id = request.POST.get('id')
        producto = Producto.objects.get(id=id)
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'listar.html', {'productos': productos})
