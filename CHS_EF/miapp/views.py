from django.shortcuts import render,HttpResponse
from miapp.models import Producto

# Create your views here.
def saludo(request):
    mensaje = "Bienvenidos a nuestro examen Final, Aprobados 2022-I"
    return render(request,'inicio.html',
    {'mensaje': mensaje })

def alumnnos(request):
    alumnos = [ 'Serna Malca Luis Alejandro' , 
                'Huancas Leuyac Anselmo Junior' , 
                'Ccaccya Huaman Antony']
    return render(request,'integrantes.html', 
    {'alumnos': alumnos,
        'titulo': 'LOS INTEGRANTES SON: '})

def crear_productos(request):
    producto = Producto(
	codigo = "05",
	nombre = "libro",
	precio_compra = "5.00",
	precio_venta = "6.00",
    Fecha_compra = "01/08/2022",
	estado = "A",
	)
    producto.save()
    return render(request, 'Crearproductos.html',
        {'producto' : producto})

def crear_curso(request):
    return render(request, 'Crearcursos.html')

	

