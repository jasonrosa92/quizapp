from django.urls import path
from django.contrib import admin

from quiz import views

urlpatterns = [
    path(r'^admin/', admin.site.urls),

    path(r'', views.perguntas_recentes, name="index"),
    path(r'perguntas/(?P<id_pergunta>[0-9]+)/', views.respostas, name="detalhes"),
    path(r'perguntas/(?P<id_pergunta>[0-9]+)/excluir/', views.excluir_pergunta),
    path(r'perguntas/(?P<id_pergunta>[0-9]+)/detalhes/', views.detalhes_pergunta),
    path(r'perguntas/(?P<id_pergunta>[0-9]+)/edit/', views.editar_pergunta),
    path(r'perguntas/(?P<id_pergunta>[0-9]+)/responder/', views.responder),
    path(r'respostas/(?P<id_resposta>[0-9]+)/mais_util/', views.escolher_resposta),

    path(r'tags/create/', views.criar_tag, name="criar_tag")
]
