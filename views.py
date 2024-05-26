from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout, get_user_model
from django.urls import reverse_lazy

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autentica o usuário utilizando o método authenticate do Django
        user = authenticate(request=request, username=username, password=password)

        # Se o usuário for autenticado
        if user is not None:
            # **Remove a linha que faz o login do usuário:**
            # login(request, user)

            # Redireciona para a página inicial após o login bem-sucedido
            return redirect('home')
        else:
            # Login falhou
            mensagem = "Usuário ou senha inválidos."
            context = {'mensagem': mensagem}
            return render(request, 'login.html', context)

    return render(request, 'login.html')

def logout_view(request):
  if request.method == 'POST':
    logout(request)
    return redirect('login')  # Redireciona para a rota de login
  else:
    # Exibir mensagem de erro (opcional)
    return render(request, 'error.html')


def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    acao = request.POST.get('acao', 'salvar')
    acao_cliente = request.POST.get('acao_cliente', False)
    gravou = False

    if acao == 'salvar' and not acao_cliente:
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.documento = request.POST.get('documento')
        novo_usuario.titulo_eleitor = request.POST.get('titulo_eleitor')
        novo_usuario.telefone = request.POST.get('telefone')
        novo_usuario.email = request.POST.get('email')
        novo_usuario.endereco = request.POST.get('endereco')
        estado_civil_selecionado = request.POST.get('estado_civil')
        novo_usuario.estado_civil = estado_civil_selecionado
        tipo_servico_selecionado = None
        if request.POST.get('tipo_servico1'):
            tipo_servico_selecionado = request.POST.get('tipo_servico1')
        elif request.POST.get('tipo_servico2'):
            tipo_servico_selecionado = request.POST.get('tipo_servico2')
        elif request.POST.get('tipo_servico3'):
            tipo_servico_selecionado = request.POST.get('tipo_servico3')
        novo_usuario.tipo_servico = tipo_servico_selecionado
        novo_usuario.senha_gov = request.POST.get('senha_gov')
        novo_usuario.info_adicionais = request.POST.get('info_adicionais')
        if novo_usuario.nome is not None and novo_usuario.nome !="":
            novo_usuario.save()
            #gravou = True  
            #mensagem = "Usuário salvo com sucesso!"
        #if gravou == False:
            #mensagem = "Listando clientes!"

    usuarios = Usuario.objects.all().order_by('nome')

    context = {
        'usuarios': usuarios,
        #'mensagem': mensagem
    }

    return render(request, 'usuarios/usuarios.html', context)

from django.shortcuts import redirect
from .models import Usuario

def editar_cliente(request, id_usuario):
    usuario = Usuario.objects.get(pk=id_usuario)

    if request.method == 'POST':
        # Atualizar os campos do cliente com os dados do formulário
        usuario.nome = request.POST.get('nome')
        usuario.documento = request.POST.get('documento')
        usuario.titulo_eleitor = request.POST.get('titulo_eleitor')
        usuario.telefone = request.POST.get('telefone')
        usuario.email = request.POST.get('email')
        usuario.endereco = request.POST.get('endereco')
        estado_civil_selecionado = request.POST.get('estado_civil')
        usuario.estado_civil = estado_civil_selecionado
        tipo_servico_selecionado = None
        if request.POST.get('tipo_servico1'):
            tipo_servico_selecionado = request.POST.get('tipo_servico1') 
        elif request.POST.get('tipo_servico2'):
            tipo_servico_selecionado = request.POST.get('tipo_servico2')
        elif request.POST.get('tipo_servico3'):
            tipo_servico_selecionado = request.POST.get('tipo_servico3')
        usuario.tipo_servico = tipo_servico_selecionado
        usuario.senha_gov = request.POST.get('senha_gov')
        usuario.info_adicionais = request.POST.get('info_adicionais')
        if usuario.nome is not None and usuario.nome !="":
            usuario.save()

        # Redirecionar para a lista de clientes após a edição
        return redirect('listagem_usuarios')

    # Pré-popular o formulário com os dados do cliente para edição
    context = {
        'usuario': usuario
    }
    return render(request, 'usuarios/editar.html', context)

