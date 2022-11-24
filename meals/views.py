
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView
from django.shortcuts import render

from .models import Refeicao
from .models import Estudante
from .utils import convert_list_dict, get_current_time
from .forms import TestForm

from django.http import HttpResponseRedirect
from datetime import date
import time
# Create your views here.



def home_view(request):
    
    qs = Refeicao.objects.all()
    qsE = Estudante.objects.all()
    form = TestForm()

    if request.method == 'POST':
        form = TestForm(data=request.POST)

        if form.is_valid():
            date_today = date.today()
            current_time = get_current_time()
            print(date_today)
            print(current_time)
            print(form.cleaned_data['ra'])
            
            for obj in qs:
                print(current_time)
                if obj.data == date_today and current_time >=5:
                    print('pass1')
                    for aluno in qsE:
                        if aluno.ra == form.cleaned_data['ra']:
                            obj.estudante.add(aluno)
                            print('sucesso')
                        

            

    context = {'form': form, 'error_message': error_message}

    return render(request, 'meals/gerenciar_alunos/teste.html', context)
    

    
    
    
class CardapioView(LoginRequiredMixin, ListView):
    model = Refeicao
    template_name = 'meals/cardapio/cardapio.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dates = convert_list_dict()
        for key in dates:
            context[f'{key}'] = dates[key]
        return context


class GerenciarCardapioView(LoginRequiredMixin, ListView):
    model = Refeicao
    template_name = 'meals/cardapio/gerenciar_cardapio.html'

@login_required
def gerenciar_estoque_view(request):
    return render(request, 'meals/estoque/gerenciar_estoque.html')