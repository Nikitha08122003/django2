from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from django.contrib.auth import login,logout,authenticate
# Create your views here.
def signup(request):
    context={"error":" "}
    if request.method=="POST":
        check=User.objects.filter(username=request.POST['studentname'])
        if len(check)>0:
            context={"error":"studentname already exits"}
        else:    
            d=User(username=request.POST['studentname'],email=request.POST['email'])
            d.set_password(request.POST['password'])
            d.save()

    return render(request,'signup.html',context)

def userlogin(request):
    context={"error":" "}
    if request.method=="POST":
        boo=authenticate(username=request.POST['studentname'],password=request.POST['password'])
        if boo is not None:
            login(request,boo)
            return redirect("/user/use/")
        else :
             context={"error":"username or password is invalid"}

             return render(request,'login.html',context)
        
    return render(request,'login.html',context)    


def userlogout(request):
    logout(request)    
    return redirect("/myproject/result/")

def userd(request):
         return render(request,'user.html') 