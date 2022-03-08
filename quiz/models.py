from django.db import models
from django.contrib.auth.models import User
import mistune

from .mixins import MixinCriacaoEAlteracao


class Pergunta(MixinCriacaoEAlteracao):
    titulo = models.CharField(max_length=100, blank=False)
    data_criacao = models.DateTimeField()
    data_atualizacao = models.DateTimeField(auto_now_add=True)


class Resposta(MixinCriacaoEAlteracao):
    pergunta = models.ForeignKey(Pergunta, related_name="respostas", on_delete=models.CASCADE)
    conteudo = models.TextField(blank=False)


    @property
    def parsed(self):
        return mistune.markdown(self.conteudo)

    def __str__(self):
        return "{}".format(self.conteudo)


class Comentario(MixinCriacaoEAlteracao):
    conteudo = models.CharField(max_length=200)
    pergunta = models.ForeignKey(Pergunta, related_name="comentarios", on_delete=models.CASCADE)

    def __str__(self):
        return self.conteudo


class RespostaUsuario(MixinCriacaoEAlteracao):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    resposta = models.ForeignKey(Resposta, related_name="resposta_usuario", on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, related_name="usuario", on_delete=models.CASCADE)