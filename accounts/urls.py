from django.urls import path, include
from .views import RegisterView, view_profile


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('view/', view_profile,name='profileView'),
    path('', include('django.contrib.auth.urls'))
]
