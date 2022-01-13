from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from plataforma.models import Imovel, Cidade


# Create your views here.
@login_required(login_url='/auth/logar/')
def home(request):
    # consulta todas as Cidades cadastradas, para list cidades do formulário
    cidades = Cidade.objects.all()
    # captura os dados passados no formulário de filtro
    preco_minimo = request.GET.get('preco_minimo')
    preco_maximo = request.GET.get('preco_maximo')
    cidade = request.GET.get('cidade')
    tipo = request.GET.getlist('tipo')
    if preco_minimo or preco_maximo or cidade or tipo:
        if not preco_minimo:
            preco_minimo = 0
        if not preco_maximo:
            preco_maximo = 999999999
        if not tipo:
            tipo = ['A', 'C']
        if not cidade:
            cidade = cidades
        # consulta no Banco de Dados os Imóveis conforme parâmetros do filtro
        imoveis = Imovel.objects.filter(valor__gte=preco_minimo) \
            .filter(valor__lte=preco_maximo) \
            .filter(tipo_imovel__in=tipo) \
            .filter(cidade__in=cidade)
    else:
        # consulta no Banco de Dados todos os Imóveis cadastrados
        imoveis = Imovel.objects.all()
    return render(request, 'home.html',
                  {'imoveis': imoveis, 'cidades': cidades})


def imovel(request, id):
    # consulta no Banco de Dados o Imóvel conforme parâmetro recebido
    imovel = get_object_or_404(Imovel, id=id)
    # consulta Imóveis da mesma cidade e tipo como sugestões ao Usuário
    sugestoes = Imovel.objects.filter(cidade=imovel.cidade).filter(tipo_imovel=imovel.tipo_imovel).exclude(id=id)[:2]
    return render(request, 'imovel.html',
                  {'imovel': imovel, 'sugestoes': sugestoes, 'id': id})
