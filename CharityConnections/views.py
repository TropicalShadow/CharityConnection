from django import views
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,"home.html")
    #return HttpResponse("Home")
def explorer(request):
    return render(request,"stolen/layout.html",{'categoryList':[]})