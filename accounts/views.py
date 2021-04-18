from django import views
from .forms import CharityUserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

class RegisterView(CreateView):
    form_class = CharityUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/register.htm'

