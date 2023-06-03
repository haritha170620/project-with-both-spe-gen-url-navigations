from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def arun(request):
    return render(request, 'arun.html')
def richa(requerst):
    return HttpResponse('<h1>This is http response of richa function </h1>')