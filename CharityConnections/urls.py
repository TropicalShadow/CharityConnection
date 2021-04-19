from django.contrib import admin
from django.urls import path, include
from .views import home,explorer

urlpatterns = [
    path('', home,name="home"),
    path('explorer/', explorer,name="explorer"),
    path('admin/', admin.site.urls),
    path('accounts/',include("accounts.urls")),
]
