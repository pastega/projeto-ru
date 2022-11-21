from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.shortcuts import render
from .models import Refeicao
from datetime import date, timedelta

# Create your views here.

def home_view(request):
    context = {}
    return render(request, 'meals/gerenciar_alunos/home.html', context)

class CardapioView(ListView):
    model = Refeicao
    template_name = 'meals/cardapio/cardapio.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {'now': date.today(), 'limit':date.today()+timedelta(7)}
        return context

# def cardapio_view(request):
#     return render(request, 'meals/cardapio/cardapio.html', {})

class GerenciarCardapioView(ListView):
    model = Refeicao
    template_name = 'meals/cardapio/gerenciar_cardapio.html'


def gerenciar_estoque_view(request):
    return render(request, 'meals/estoque/gerenciar_estoque.html')




