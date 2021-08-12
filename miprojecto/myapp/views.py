from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hola_mundo(request):
    return HttpResponse(f"Hola mundo!, estas accediendo desde {request.path}")


def index(request):

    ctx = { "nombre": "Horacio"} 
    return render(request, "myapp/index.html", ctx)

def materias(request):

    ctx = { 
        "materias": ["python", "javascript", "html"]
    }
    return render(request, "myapp/materias.html",ctx)



