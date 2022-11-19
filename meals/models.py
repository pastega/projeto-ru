from django.db import models

from django.utils.translation import gettext_lazy as _

class Pessoa(models.Model):
    nome = models.CharField(max_length=120)
    cpf = models.IntegerField()

    class Meta:
        abstract = True

class Funcionario(Pessoa):

    class Funcao(models.TextChoices):
        ATENDENTE = 'AT', _('Atendente')
        NUTRICIONISTA = 'NT', _('Nutricionista')
        GERENTE = 'GR', _('Gerente')

    funcao = models.CharField(max_length=2, choices=Funcao.choices)

    def __str__(self):
        return f'{self.nome} [{self.funcao}]'

class Estudante(Pessoa):
    ra = models.IntegerField()

    class Curso(models.TextChoices):
        ENG_COMPUTACAO = 'EC', _('Engenharia de Computação')
        ENG_SOFTWARE = 'ES', _('Engenharia de Software')
        ENG_ELETRICA = 'EL', _('Engenharia Elétrica')
        ENG_ELETRONICA = 'EE', _('Engenharia Eletrônica')
        ENG_MECANICA = 'EM', _('Engenharia Mecânica')
        MATEMATICA = 'MA', _('Matemática')
        ANALISE_SISTEMAS = 'AS', _('Análise e Desenvolvimento de Sistemas')

    curso = models.CharField(max_length=2, choices=Curso.choices)

    def __str__(self):
        return f'{self.nome} [RA: {self.ra}] [{self.curso}]'

class ItemEstoque(models.Model):
    nome = models.CharField(max_length=50)
    peso_gramas = models.IntegerField()

    def __str__(self):
        return f'{self.nome} [{self.peso_gramas} g]'

    
class Cardapio(models.Model):
    prato_principal = models.ForeignKey(ItemEstoque, on_delete=models.CASCADE, related_name='prato_principal')
    acompanhamento = models.ForeignKey(ItemEstoque, on_delete=models.CASCADE, related_name='acompanhamento')
    sobremesa = models.ForeignKey(ItemEstoque, on_delete=models.CASCADE)

    nutricionista = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.prato_principal}-{self.acompanhamento}-{self.sobremesa}'

class Refeicao(models.Model):
    estudante = models.ManyToManyField(Estudante)
    cardapio = models.ForeignKey(Cardapio, on_delete=models.CASCADE)
    data = models.DateField()

    class Periodo(models.TextChoices):
        ALMOCO = 'A', _('Almoço')
        JANTAR = 'J', _('Jantar')

    periodo = models.CharField(max_length=1, choices=Periodo.choices)

    class DiaDaSemana(models.TextChoices):
        SEGUNDA = 'SEG', _('Segunda-feira')
        TERCA = 'TER', _('Terça-feira')
        QUARTA = 'QUA', _('Quarta-feira')
        QUINTA = 'QUI', _('Quinta-feira')
        SEXTA = 'SEX', _('Sexta-feira')
        SABADO = 'SAB', _('Sábado')
        DOMINGO = 'DOM', _('Domingo')

    dia_da_semana = models.CharField(max_length=3, choices=DiaDaSemana.choices)

    def __str__(self):
        return f'Refeição [{self.data}] > {self.cardapio}'