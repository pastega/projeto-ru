from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

def home_view(request):
    context = {}
    return render(request, 'meals/gerenciar_alunos/home.html', context)

def cardapio_view(request):
    return render(request, 'meals/cardapio/cardapio.html', {})

def gerenciar_cardapio_view(request):
    return render(request, 'meals/cardapio/gerenciar_cardapio.html', {})

def gerenciar_estoque_view(request):
    return render(request, 'meals/estoque/gerenciar_estoque.html')




