from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hii user")

def showform(request): 
    return render(request, "index.html")

def getform(request): 
    if request.method == "POST": 
        age=request.POST['age'] 
        name=request.POST['name'] 
    return HttpResponse("Name:{} Age:{}".format(name, age))