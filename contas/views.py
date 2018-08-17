from django.shortcuts import render
from .models import Transacao
from .form import TransacaoForm
from django.http import HttpResponse  #Importa a Classe HttpResponse do pacote http
import datetime  #Importa a biblioteca datetime


def index(request):
    data = {}

    # Criamos um item no dicionario com a data e hora do SO
    data['now'] = datetime.datetime.now()

    # Criamos um item no dicionario que eh uma lista com 3 valores
    data['transacoes'] = ['t1', 't2', 't3']

    return render(request, 'contas/index.html', data)

def listagem(request):
    data = {}
    # .objects eh um manager para o Model (DB)
    # .all() eh um metodo que traz todos os dados do Model
    data['transacoes'] = Transacao.objects.all()

    return render(request, 'contas/listagem.html', data)


def nova_transacao(request):
    form = TransacaoForm(request.POST or None)  #Verifica se existem informacoes tipo POST para preencher os campos

    if form.is_valid():
        form.save()
        return listagem(request)

    #Fizemos a etapa de criar a colecao em um passo apenas
    return render(request, 'contas/form.html', {'form': form})
