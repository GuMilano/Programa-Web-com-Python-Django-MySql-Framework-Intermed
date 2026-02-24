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
            form.send_email()
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