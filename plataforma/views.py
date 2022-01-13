from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.
@login_required(login_url='/auth/logar/')
def home(request):
    return HttpResponse('Estamos na Home da Plataforma')
