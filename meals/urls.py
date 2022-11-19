
from django.urls import path

from .views import (
    home_view,
    cardapio_view,
    gerenciar_cardapio_view,
    gerenciar_estoque_view)

app_name = 'meals'

urlpatterns = [
    path('', home_view, name='home'),
    path('cardapio/', cardapio_view, name='cardapio'),
    path('gerenciar_cardapio/', gerenciar_cardapio_view, name ='cardapio'),
    path('gerenciar_estoque/', gerenciar_estoque_view, name='estoque'),
]