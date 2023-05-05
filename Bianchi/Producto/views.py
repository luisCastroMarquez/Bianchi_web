from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from django.contrib import messages

# Create your views here.


def home(request):
    productosListados = Producto.objects.all()

    # Cantidad de productos por página
    productosPorPagina = 6

    # Obtener la página actual
    paginaActual = request.GET.get('page')

    # Crear el objeto paginator
    paginator = Paginator(productosListados, productosPorPagina)

    # Obtener los productos para la página actual
    productos = paginator.get_page(paginaActual)

    return render(request, "gestionProductos.html", {"productos": productos})

def registro_producto(request):
    codigo=request.POST ['txtCodigo']
    nombre=request.POST ['txtNombre']
    cantidad=request.POST ['numCantidad']

    producto=Producto.objects.create(
    codigo=codigo, nombre=nombre, cantidad=cantidad)

    messages.success(request, '¡Productos registrados!')
    return redirect('/')

def edicion_producto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    return render(request, "edicionProducto.html", {"producto": producto})

def editar_producto(request):
    codigo=request.POST ['txtCodigo']
    nombre=request.POST ['txtNombre']
    cantidad=request.POST ['numCantidad']

    producto = Producto.objects.get(codigo=codigo)
    producto.nombre = nombre
    producto.cantidad = cantidad
    producto.save()

    messages.success(request, '¡Producto Editado!')
    return redirect('/')

def eliminar_producto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    messages.success(request, '¡Producto Eliminado!')
    return redirect('/')


