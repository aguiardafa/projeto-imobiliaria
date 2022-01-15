from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from plataforma.models import Imovel, Cidade, Visita


# Create your views here.
@login_required(login_url='/auth/logar/')
def home(request):
    # consulta todas as Cidades cadastradas, para list cidades do formulário
    cidades = Cidade.objects.all()
    # captura os dados passados no formulário de filtro
    preco_minimo = request.GET.get('preco_minimo')
    preco_maximo = request.GET.get('preco_maximo')
    cidade = request.GET.get('cidade')
    tipo_imovel = request.GET.getlist('tipo_imovel')
    tipo = request.GET.getlist('tipo')
    if preco_minimo or preco_maximo or cidade or tipo_imovel or tipo:
        if not preco_minimo:
            preco_minimo = 0
        if not preco_maximo:
            preco_maximo = 999999999
        if not tipo_imovel:
            tipo_imovel = ['A', 'C']
        if not tipo:
            tipo = ['A', 'V']
        if not cidade:
            cidade = cidades
        # consulta no Banco de Dados os Imóveis conforme parâmetros do filtro
        imoveis = Imovel.objects.filter(valor__gte=preco_minimo) \
            .filter(valor__lte=preco_maximo) \
            .filter(tipo_imovel__in=tipo_imovel) \
            .filter(tipo__in=tipo) \
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


def agendar_visitas(request):
    # captura os dados passados no formulário
    user = request.user
    dia = request.POST.get('dia')
    horario = request.POST.get('horario')
    id_imovel = request.POST.get('id_imovel')
    # cadastrar Visita no Banco de Dados
    visita = Visita(
        imovel_id=id_imovel,
        usuario=user,
        dia=dia,
        horario=horario
    )
    visita.save()
    return redirect('/agendamentos')


def agendamentos(request):
    # consulta no Banco de Dados as visitas do usuário que está acessando
    visitas = Visita.objects.filter(usuario=request.user)
    return render(request, "agendamentos.html", {'visitas': visitas, 'total_visitas': visitas.count()})


def cancelar_agendamento(request, id):
    # consulta no Banco de Dados o Imóvel conforme parâmetro recebido
    visitas = get_object_or_404(Visita, id=id)
    # atualiza status para cancelado e salva no Banco de Dados
    visitas.status = "C"
    visitas.save()
    return redirect('/agendamentos')
