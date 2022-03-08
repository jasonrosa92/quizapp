from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Pergunta, Resposta, RespostaUsuario


def detalhes_pergunta(request, id_pergunta):
    pergunta = Pergunta.objects.get(pk=id_pergunta)

    return render(request, 'editar_pergunta.html', {"pergunta": pergunta})


def editar_pergunta(request, id_pergunta):
    novo_titulo = request.POST["titulo"]
    novo_conteudo = request.POST['conteudo']

    pergunta = Pergunta.objects.get(pk=id_pergunta)

    pergunta.titulo = novo_titulo
    pergunta.conteudo = novo_conteudo
    pergunta.save()

    return redirect('index')


def responder(request, id_pergunta):
    user_pk = request.user.pk
    pergunta = Pergunta.objects.get(pk=id_pergunta)
    respostas = Resposta.objects.filter(pergunta=id_pergunta)
    if request.method == 'POST':
        resposta = request.POST['resposta']

        #Resposta.objects.filter(pergunta=pergunta).update_or_create(conteudo=resposta)
        obj = RespostaUsuario.objects.create(
            respostas='id_resposta',
            pergunta='id_pergunta',
            usuario='user_pk',
        )
        obj.save()
        return redirect('index')

    response = {"pergunta": pergunta,
                "respostas": respostas}

    return render(request, 'listagem_respostas.html', response)


def perguntas_recentes(request):
    perguntas = Pergunta.objects.all()

    dados = {"perguntas": perguntas}

    return render(request, 'listagem_perguntas.html', dados)


def respostas(request, id_pergunta):
    pergunta = Pergunta.objects.get(pk=id_pergunta)
    respostas = Resposta.objects.filter(pergunta=id_pergunta)

    comentarios = pergunta.comentarios.all()

    dados = {'respostas': respostas,
             'pergunta': pergunta,
             }

    return render(request, "listagem_respostas.html", dados)


def excluir_pergunta(request, id_pergunta):
    pergunta = Pergunta.objects.get(pk=id_pergunta)
    pergunta.delete()

    return redirect('index')


def escolher_resposta(request, id_resposta):
    resposta = Resposta.objects.get(pk=id_resposta)
    resposta.mais_util = True
    resposta.save()

    return redirect('index')



