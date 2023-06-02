from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def arun(request):
    return render(request, 'arun.html')

