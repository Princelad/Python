from django.shortcuts import render

def home(request):
    """View function for home page of site."""
    return render(request, 'greetings/home.html')
