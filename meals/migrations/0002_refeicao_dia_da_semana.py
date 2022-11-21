# Generated by Django 4.1.3 on 2022-11-20 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='refeicao',
            name='dia_da_semana',
            field=models.CharField(choices=[('SEG', 'Segunda-feira'), ('TER', 'Terça-feira'), ('QUA', 'Quarta-feira'), ('QUI', 'Quinta-feira'), ('SEX', 'Sexta-feira'), ('SAB', 'Sábado'), ('DOM', 'Domingo')], default='SEG', max_length=3),
        ),
    ]
