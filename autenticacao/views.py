from django.shortcuts import render


# Create your views here.
def cadastrar(request):
    return render(request, 'cadastrar.html')


def logar(request):
    return render(request, 'logar.html')
