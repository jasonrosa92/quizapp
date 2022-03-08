from django.urls import path
from django.contrib import admin

from quiz import views

urlpatterns = [
    path(r'admin/', admin.site.urls),

    path(r'', views.perguntas_recentes, name="index"),
    path(r'perguntas/<id_pergunta>', views.respostas, name="detalhes"),
    path(r'perguntas/<id_pergunta>/excluir/', views.excluir_pergunta),
    path(r'perguntas/<id_pergunta>/detalhes/', views.detalhes_pergunta),
    path(r'perguntas/<id_pergunta>/edit/', views.editar_pergunta),
    path(r'perguntas/<id_pergunta>/responder/', views.responder),
    path(r'respostas/<id_resposta>/mais_util/', views.escolher_resposta),

]
