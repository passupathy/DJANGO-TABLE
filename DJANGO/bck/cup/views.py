from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import form

# Create your views here.

def home(request):
    mydata=form.objects.all()
    if (mydata!=""):
        return render(request,"home.html",{'num':mydata})
    else:
        return render(request,"home.html")

def add(request):

    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        mail=request.POST['mail']
        address=request.POST['address']

        obj=form()
        obj.NAME=name
        obj.AGE=age
        obj.MAIL=mail
        obj.ADDRESS=address
        obj.save()

        mydata=form.objects.all()
        return redirect("home")
    return render(request,"home.html")

def update(request,id):
    mydata=form.objects.get(id=id)

    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        mail=request.POST['mail']
        address=request.POST['address']

        mydata.NAME=name
        mydata.AGE=age
        mydata.MAIL=mail
        mydata.ADDRESS=address
        mydata.save()

        return redirect("home")
    return render(request,"update.html",{'val':mydata})

def delete(request,id):
    mydata=form.objects.get(id=id)
    mydata.delete()
    return redirect("home")



        



