from django.shortcuts import render
from django.contrib import messages

from .forms import ContatoForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        print(f"Post: {request.POST}")
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print("Mensagem Enviada")
            print("Nome: ", nome)
            print("Email: ", email)
            print("Assunto: ", assunto)
            print("Mensagem: ", mensagem)

            messages.success(request, 'Mensagem enviada com Sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar mensagem!')
    
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def produtos(request):
    return render(request, 'produtos.html')