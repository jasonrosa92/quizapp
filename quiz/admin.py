from django.contrib import admin
from .models import *


@admin.register(Pergunta)
class Pergunta(admin.ModelAdmin):
	list_display = ['titulo']


@admin.register(Resposta)
class Resposta(admin.ModelAdmin):
	pass


@admin.register(Comentario)
class Comentario(admin.ModelAdmin):
	pass