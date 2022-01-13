from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants


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
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos corretamente')
            return redirect('/auth/cadastrar')
        # consulta no Módulo Admin se existe usuário com o username passado
        user = User.objects.filter(username=username)
        if user.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usuário cadastrado com o username informado')
            return redirect('/auth/cadastrar')
        # cadastrar usuário no Banco de Dados
        try:
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=senha)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso')
            return redirect('/auth/logar')
        except:
            messages.add_message(request, constants.ERROR,
                                 'Erro interno inesperado! Tente novamente ou contate o Administrador do Sistema')
            return redirect('/auth/cadastrar')


def logar(request):
    return render(request, 'logar.html')
