"""
URL configuration for myproject project.
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def home(request):
    return HttpResponse(
        "<!doctype html>"
        "<html lang='en'>"
        "<head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'>"
        "<title>My Django Website</title></head>"
        "<body style='font-family:Arial,sans-serif;max-width:760px;margin:80px auto;padding:24px;'>"
        "<h1>Welcome to Django!</h1>"
        "<p>Your Django website is running successfully.</p>"
        "<p>Next, you can build your own pages and features.</p>"
        "</body></html>"
    )


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
]
