from django.urls import path, include
from .views import RegisterView


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('', include('django.contrib.auth.urls'))
]
