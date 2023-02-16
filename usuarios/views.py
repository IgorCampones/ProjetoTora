from django.shortcuts import render
from django.http import HttpResponse
from .models import Colaborador
from django.shortcuts import redirect

def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})

def valida_cadastro(request):
    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    tipo_acesso = request.POST.get('tipo_acesso')
    equipe = request.POST.get('equipe')

    colaborador = Colaborador.objects.filter(cpf = cpf)

#Verifica se a pessoa digitou espaços em branco
    if len(nome.strip()) == 0 or len(cpf.strip()) == 0 or len(tipo_acesso.strip()) == 0 or len(equipe.strip()) == 0:
        return redirect('/usuarios/cadastro/?status=1')

#Verifica a quantidade de números no cpf
    if len(cpf) < 11:
        return redirect('/usuarios/cadastro/?status=2')

#Verificar o cpf se já existe
    if len(colaborador) > 0:
        return redirect('/usuarios/cadastro/?status=3')

    try:
        colaborador = Colaborador(nomecolaborador = nome, cpf = cpf, tipo_acesso = tipo_acesso, equipe = equipe)
        colaborador.save()

        return redirect('/usuarios/cadastro/?status=0')
    
    except:
        return redirect('/usuarios/cadastro/?status=4')


def valida_login(request):

    cpf = request.POST.get('cpf')

    colaborador = Colaborador.objects.filter(cpf = cpf)

    if len(colaborador) == 0:
        return redirect('/usuarios/login/?status=1')
    elif len(colaborador) > 0:
        request.session['colaborador'] = colaborador[0].id
        return redirect('/usuarios/home/')

def home(request):
    if request.session.get('colaborador'):
        colaborador = Colaborador.objects.get(id = request.session['colaborador']).nomecolaborador
        return render(request, 'home.html', {'colaborador_logado': request.session.get('colaborador')})
    else:
        return redirect('/usuarios/login/?status=2')

def sair(request):
    request.session.flush()
    return redirect('/usuarios/login/')

def erro404(request, exception):
    return render(request, 'page404.html')