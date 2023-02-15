from django.shortcuts import render
from django.http.response import HttpResponse

def homepage(request):
    return render(request,'country.html')

def India(request):
    return render(request,'india.html')

def Chaina(request):
    return render(request,'chainastates.html')

def Russia(request):
    return render(request,'russiastates.html')
