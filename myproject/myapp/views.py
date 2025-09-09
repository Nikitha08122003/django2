from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import forms
from . import models
# Create your views here.

def myfunction(request):
    return HttpResponse("hello")

def mydemo(request):
    a="hi niki"
    return render(request, 'index.html',{'value':a})


def formshow(request):
    f=forms.myform()
    if request.method=='GET':
        f1=forms.myform(request.GET)
        if f1.is_valid():
         f1.save()
    return render(request,'demoform.html',{'form':f})


def data(request):
   d= models.details.objects.all()
   return render(request,"data.html",{"data":d})

def update(request,id):
   d= models.details.objects.get(id=id)
   f=forms.myform(instance=d)
   if request.method=='POST':
        f1=forms.myform(request.POST,instance=d)
        if f1.is_valid():
           f1.save()
           return redirect("/myproject/leo/")
   return render(request,'demoform.html',{'form':f})


def delete(request,id):
   d= models.details.objects.get(id=id)
   d.delete()
   return redirect("/myproject/leo/")