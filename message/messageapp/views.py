from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Msg
# Create your views here.
def create(request):
    if(request.method=="GET"):
        return render(request,"index.html")
    else:
        username = request.POST['uname']
        contact = request.POST['mobile']
        email = request.POST['uemail']
        msg = request.POST['msg']
        m=Msg.objects.create(name=username,email=email,mobile=contact,msg=msg)
        m.save()

       
        return render(request,"index.html")

def dashboard(request):
    context={}   
    m=Msg.objects.all()  #fetch all the data from table Msg
    context['data']=m
    print(m)
    return render(request,"dashboard.html",context)


def edit(request,sid):
    if request.method == "GET":
        m=Msg.objects.filter(id=sid)
        context={}
        context['data']=m
        return render(request,"edit.html",context)
    else:
        username = request.POST['uname']
        contact = request.POST['mobile']
        email = request.POST['uemail']
        msg = request.POST['msg']
        m=Msg.objects.filter(id=sid).update(name=username,email=email,mobile=contact,msg=msg)
        return redirect("/dashboard")

def delete(request,did):
    m=Msg.objects.filter(id=did)
    m.delete()
    return redirect("/dashboard")


    