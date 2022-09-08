from django.db import models

# Create your models here.

#Criação do banco de dados do PI, dos mais simples aos mais avançados
class Bairro(models.Model):
    bairro = models.CharField(max_length=40)

    def __str__(self):
        return self.bairro

class Tema(models.Model):
    tema = models.CharField(max_length=20)

    def __str__(self):
        return self.tema

class Cliente(models.Model):
    nome = models.CharField(max_length=75)
    numero = models.IntegerField()
    logradouro = models.CharField(max_length=150)
    telefone = models.CharField(max_length=15)
    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Aluguel(models.Model):
    valor = models.IntegerField()
    idade = models.IntegerField()
    entrega = models.DateField()
    recebimento = models.DateField()
    data_festa = models.DateField()
    especificacoes = models.CharField(max_length=500)
    aniversariante = models.CharField(max_length=100)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

