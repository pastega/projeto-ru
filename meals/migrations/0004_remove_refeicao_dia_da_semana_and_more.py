# Generated by Django 4.1.3 on 2022-11-22 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0003_alter_refeicao_estudante'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='refeicao',
            name='dia_da_semana',
        ),
        migrations.AlterField(
            model_name='refeicao',
            name='estudante',
            field=models.ManyToManyField(blank=True, to='meals.estudante'),
        ),
    ]
