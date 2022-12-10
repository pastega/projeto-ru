
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView
from django.shortcuts import render

from .models import Refeicao, Estudante
from .utils import convert_list_dict, get_current_periodo
from .forms import RAForm

# Create your views here.

from datetime import date

@login_required
def home_view(request):

    form = RAForm()
    error = None

    if request.method == 'POST':
        form = RAForm(request.POST)

        # TODO: Handle errors in a better way

        if form.is_valid():
            ra = form.cleaned_data['ra']
            data = date.today()
            periodo = get_current_periodo()

            qs_refeicao_atual = Refeicao.objects.filter(data=data, periodo=periodo)
            if not qs_refeicao_atual:
                error = 'ERRO: Não há nenhuma refeição vigente atualmente'

            qs_estudante_refeicao = qs_refeicao_atual.filter(estudante__ra=ra)
        
            if qs_estudante_refeicao.exists():
                error = 'ERRO: O estudante já foi registrado na refeição atual'

            estudante = Estudante.objects.filter(ra=ra)[0]
            
            refeicao = qs_refeicao_atual[0]
            refeicao.estudante.add(estudante)

    context = {'form': form, 'error': error}
    return render(request, 'meals/gerenciar_alunos/home.html', context)

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