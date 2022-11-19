from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

def home_view(request):
    context = {}
    return render(request, 'meals/home.html', context)