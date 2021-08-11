from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(f"Hola mundo!, estas accediendo desde {request.path}")

def mi_template(request):
    return render(request, "myapp/index2.html")



