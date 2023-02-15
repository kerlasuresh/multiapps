from django.shortcuts import render
from django.http.response import HttpResponse

def homepage(request):
    return render(request,'courses.html')

def python(request):
    return render(request,'pythonabout.html')

def django(request):
    return render(request,'djangoabout.html')

def javascript(request):
    return render(request,'javascriptabout.html')
