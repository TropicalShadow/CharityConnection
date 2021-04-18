from django import views
from django.http import HttpResponse



def home(request):
    return HttpResponse("Home")