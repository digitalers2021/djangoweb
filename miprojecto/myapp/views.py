from django.shortcuts import render
from django.http import HttpResponse
from .forms import FormularioCurso

# Create your views here.
def hola_mundo(request):
    return HttpResponse(f"Hola mundo!, estas accediendo desde {request.path}")


def index(request):

    ctx = { "nombre": "Horacio", "path": "es un path" } 
    return render(request, "myapp/index.html", ctx)

def materias(request):

    ctx = { 
        "materias": ["python", "javascript", "html"]
    }
    return render(request, "myapp/materias.html",ctx)

def nuevo_curso(request):

    if request.method == "POST":
        # Se puede acceder a la informacion del POST de forma
        # manual
        # request.POST["nombre"])
        form = FormularioCurso(request.POST)
        if form.is_valid():
            return HttpResponse(f"El formulario es valido, enviaste: {request.POST['nombre']}, {request.POST['inscriptos']}") 
        else:
            return HttpResponse("El formulario es invalido") 
	

        
    form = FormularioCurso()
    ctx = { "formulario": form}
    return render(request, "myapp/nuevo_curso.html", ctx)



