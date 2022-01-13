from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from plataforma.models import Imovel


# Create your views here.
@login_required(login_url='/auth/logar/')
def home(request):
    # consulta no Banco de Dados todos os Imóveis cadastrados, através do Model Imovel em Models
    imoveis = Imovel.objects.all()
    return render(request, 'home.html', {'imoveis': imoveis})
