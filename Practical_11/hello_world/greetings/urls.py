from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Route to the home view
]
