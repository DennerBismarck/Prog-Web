"""DoceFestas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from PIDoceFestas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/', views.teste),

    path('index/', views.index, name="index"),

    #Urls para CRUD dos clientes
    path('cadastroCli/', views.CadastroCliente, name="cadastroCli"),
    path('tabelaCli/', views.TabelaCliente, name="tabelaCli"),
    path('editarCli/<int:id>', views.EditarCliente, name="editarcliente"),
    path('deletarCli/<int:id>', views.DeletarCliente, name="deletarcliente"),

    #Urls para CRUD dos alugueis
    path('cadastroAlu/', views.CadastroAluguel, name="cadastroAlu"),
    path('tabelaAlu/', views.TabelaAluguel, name="tabelaAlu"),
    path('editarAlu/<int:id>', views.EditarAluguel, name="editaraluguel"),
    path('deletarAlu/<int:id>', views.DeletarAluguel, name="deletaraluguel"),
]
