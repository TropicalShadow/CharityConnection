from .forms import CharityUserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django import views
from .models import PreferredCategory, PreferredAction

class RegisterView(CreateView):
    form_class = CharityUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/register.htm'

def view_profile(request):
    data = {}
    prefCats = PreferredCategory.objects.filter(user=request.user)
    prefActs = PreferredAction.objects.filter(user=request.user) 
    data["prefCats"] = prefCats
    data["prefActs"] = prefActs

    return render(request,"accounts/profileView.html",data)