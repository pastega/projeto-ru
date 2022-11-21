
from django.urls import path

from .views import (
    home_view,
    CardapioView,
    GerenciarCardapioView,
    gerenciar_estoque_view)

app_name = 'meals'

urlpatterns = [
    path('', home_view, name='home'),
    
    path('cardapio/', CardapioView.as_view(), name='cardapio'),
    
    path('gerenciar_cardapio/', GerenciarCardapioView.as_view(), name ='gerenciar_cardapio'),
    
    path('gerenciar_estoque/', gerenciar_estoque_view, name='estoque'),
]