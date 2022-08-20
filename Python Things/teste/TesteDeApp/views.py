from cgitb import html
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def TelaTeste(request):
    treco = "<html><body><h1>Ola mundo!</h1></body></html>"
    return HttpResponse(treco)