from django.db import models

from django.utils.translation import gettext_lazy as _

class Pessoa(models.Model):
    nome = models.CharField(max_length=120)
    cpf = models.IntegerField()

    class Meta:
        abstract = True
        verbose_name_plural = 'Pessoas'

class Funcionario(Pessoa):

    class Funcao(models.TextChoices):
        ATENDENTE = 'AT', _('Atendente')
        NUTRICIONISTA = 'NT', _('Nutricionista')
        GERENTE = 'GR', _('Gerente')

    funcao = models.CharField(max_length=2, choices=Funcao.choices)

    def __str__(self):
        return f'{self.nome} [{self.funcao}]'

    class Meta:
        verbose_name_plural = 'Funcionários'

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

    class Meta:
        verbose_name_plural = 'Estudantes'

class ItemEstoque(models.Model):
    nome = models.CharField(max_length=50)
    peso_gramas = models.IntegerField()

    def __str__(self):
        return f'{self.nome} [{self.peso_gramas} g]'

    class Meta:
        verbose_name_plural = 'Itens no Estoque'
    
class Cardapio(models.Model):
    prato_principal = models.ForeignKey(ItemEstoque, on_delete=models.CASCADE, related_name='prato_principal')
    acompanhamento = models.ForeignKey(ItemEstoque, on_delete=models.CASCADE, related_name='acompanhamento')
    sobremesa = models.ForeignKey(ItemEstoque, on_delete=models.CASCADE)

    nutricionista = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.prato_principal}-{self.acompanhamento}-{self.sobremesa}'

    class Meta:
        verbose_name_plural = 'Cardápios'

class Refeicao(models.Model):
    estudante = models.ManyToManyField(Estudante, blank=True)
    cardapio = models.ForeignKey(Cardapio, on_delete=models.CASCADE)
    data = models.DateField()

    class Periodo(models.TextChoices):
        ALMOCO = 'A', _('Almoço')
        JANTAR = 'J', _('Jantar')

    periodo = models.CharField(max_length=1, choices=Periodo.choices)


    def __str__(self):
        return f'Refeição [{self.data}] > {self.cardapio}'
    
    class Meta:
        verbose_name_plural = 'Refeições'