from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def prathima(request):
    return render(request,'prathima.html')
def mukundh(requerst):
    return HttpResponse('<h1>This is http rensponse of mukundh function</h1>')