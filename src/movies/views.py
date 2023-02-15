from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .models import kgfMovieTicket,beastMovieTicket,rrrMovieTicket

def homepage(request):
    return render(request,'movies.html')

def kgf(request):
    if request.method=='GET':
        kgfdata=kgfMovieTicket.objects.all()
        return render(request,'kgfticket.html',{'kgfdata':kgfdata})
    else:
        kgfMovieTicket(
        Name=request.POST.get('name'),
        Tickets=request.POST.get('seat')
        ).save()
        return redirect('kgf')
def updatekgf(request,id):
    kgfdata=kgfMovieTicket.objects.get(id = id)
    return render(request,'updatekgf.html',{'kgfdata':kgfdata})

def save_updatedkgf(request,id):
    kgfdata=kgfMovieTicket.objects.get(id = id)
    kgfdata.Name=request.POST.get('name')
    kgfdata.Tickets=request.POST.get('seat')
    kgfdata.save()
    return redirect('kgf')

def deletekgf(request,id):
    kgfdata=kgfMovieTicket.objects.get(id = id)
    kgfdata.delete()
    return redirect('kgf')

def beast(request):
    if request.method=='GET':
        beastdata=beastMovieTicket.objects.all()
        return render(request,'beastticket.html',{'beastdata':beastdata})
    else:
        beastMovieTicket(
        Name=request.POST.get('name'),
        Tickets=request.POST.get('seat')
        ).save()
        return redirect('beast')
def updatebeast(request,id):
    beastdata=beastMovieTicket.objects.get(id=id)
    return render(request,'updatebeast.html',{'beastdata':beastdata})
def save_updatebest(request,id):
    beastdata=beastMovieTicket.objects.get(id=id)
    beastdata.Name=request.POST.get('name')
    beastdata.Tickets=request.POST.get('seat')
    beastdata.save()
    return redirect('beast')
def deletebeast(request,id):
    beastdata=beastMovieTicket.objects.get(id=id)
    beastdata.delete()
    return redirect('beast')





def rrr(request):
    if request.method=='GET':
        return render(request,'rrrticket.html')
    else:
        rrrMovieTicket(
        Name=request.POST.get('name'),
        Tickets=request.POST.get('seat')
        ).save()
        return redirect('rrr')
