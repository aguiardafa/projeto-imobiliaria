from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.
def cadastrar(request):
    if request.method == "GET":
        return render(request, 'cadastrar.html')
    elif request.method == "POST":
        # captura os dados passados no formulário
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        # validação básica
        if len(username.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0:
            return redirect('/auth/cadastrar')
        # consulta no Módulo Admin se existe usuário com o username passado
        user = User.objects.filter(username=username)
        if user.exists():
            return redirect('/auth/cadastrar')
        # cadastrar usuário no Banco de Dados
        try:
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=senha)
            user.save()
            return redirect('/auth/logar')
        except:
            return redirect('/auth/cadastrar')


def logar(request):
    return render(request, 'logar.html')
