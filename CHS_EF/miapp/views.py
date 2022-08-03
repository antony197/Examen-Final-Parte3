from django.shortcuts import render,HttpResponse

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
    return render(request, 'Crearproductos.html')

def crear_curso(request):
    return render(request, 'Crearcursos.html')
