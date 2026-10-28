from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to Django!</h1>
    <p>made by python</p>")

# In myproject/urls.py:
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
]
