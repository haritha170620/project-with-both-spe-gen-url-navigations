from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def haritha(request):
    return render(request, 'haritha.html')
def msd(requerst):
    return HttpResponse('<h1>This is http response of msd function</h1>')
