"""
URL configuration for hello_world project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('greetings.urls')),  # Include our app's URLs
]
