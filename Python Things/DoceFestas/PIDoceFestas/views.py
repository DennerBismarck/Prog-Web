from django.http import HttpResponse
from django.shortcuts import render,redirect
from PIDoceFestas.form import ClienteForm, AluguelForm
from PIDoceFestas.models import Cliente, Aluguel
# Create your views here.

#Def para testar se está tudo funcionando antes de começar o crud.
def teste(request):
    resposta = '<html><h1>Olá mundo</h1></html>'
    return HttpResponse(resposta)

def index(request):
    return render(request,"index.html")

#CRUD dos clientes  
def CadastroCliente(request):
    formCliente = ClienteForm(request.POST or None)
    if formCliente.is_valid() :
        formCliente.save()
        return redirect("tabelaCli")    
    pacote = {"formCliente": formCliente}
    return render(request, "CadastroCliente.html", pacote)

def TabelaCliente(request):
    clientes = Cliente.objects.all()
    return render(request, "TabelaCliente.html", {"clientes": clientes})

def EditarCliente(request, id):
    cliente = Cliente.objects.get(pk=id)
    formCliente = ClienteForm(request.POST or None, instance=cliente)
    if formCliente.is_valid() :
        formCliente.save()
        return redirect("tabelaCli")    
    pacote = {"formCliente": formCliente}
    return render(request, "EditarCliente.html", pacote)

def DeletarCliente(request, id):
    cliente = Cliente.objects.get(pk=id)
    cliente.delete()
    return redirect("tabelaCli")

#CRUD dos alugueis
def CadastroAluguel(request):
    formAluguel = AluguelForm(request.POST or None)
    if formAluguel.is_valid() :
        formAluguel.save()
        return redirect("tabelaAlu")    
    pacote = {"formAluguel": formAluguel}
    return render(request, "CadastroAluguel.html", pacote)

def TabelaAluguel(request):
    alugueis = Aluguel.objects.all()
    return render(request, "TabelaAluguel.html", {"alugueis": alugueis})

def EditarAluguel(request, id):
    aluguel = Aluguel.objects.get(pk = id)
    formAluguel = AluguelForm(request.POST or None, instance=aluguel)
    if formAluguel.is_valid() :
        formAluguel.save()
        return redirect("tabelaAlu")    
    pacote = {"formAluguel": formAluguel}
    return render(request, "EditarAluguel.html", pacote)

def DeletarAluguel(request, id):
    aluguel = Aluguel.objects.get(pk=id)
    aluguel.delete()
    return redirect("tabelaAlu")
