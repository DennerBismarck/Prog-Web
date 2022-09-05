from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#Def para testar se está tudo funcionando antes de começar o crud.
def teste(request):
    resposta = '<html><h1>Olá mundo</h1></html>'
    return HttpResponse(resposta)
    
def index(request):
    return render(request,"index.html")