from django import forms
from django.db import models

class ContactForm(forms.Form):
    estudante = models.ManyToManyField(Estudante, blank=True)
    cardapio = models.ForeignKey(Cardapio, on_delete=models.CASCADE)
    data = models.DateField()

    class Periodo(models.TextChoices):
        ALMOCO = 'A', _('Almoço')
        JANTAR = 'J', _('Jantar')

    periodo = models.CharField(max_length=1, choices=Periodo.choices)

    