# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170425_2318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='pergunta',
            name='criada_por',
        ),
        migrations.RemoveField(
            model_name='resposta',
            name='criada_por',
        ),
        migrations.AlterField(
            model_name='tag',
            name='nome',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='Perfil',
        ),
    ]