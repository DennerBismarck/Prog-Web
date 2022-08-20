from codecs import backslashreplace_errors
from django.db import models
# Create your models here.

#Tentativa de fazer a prova da 1M
#Primeiro as tabelas que não necessitam de foreign keys alheias.
class Instrutor(models.Model):
    rg = models.IntegerField()
    nome = models.CharField(max_length=45)
    nascimento = models.DateField()
    titulacao = models.IntegerField(null=True)

class Atividade(models.Model):
    nome = models.CharField(max_length=100)
#Agora tabelas que necessitam de uma das primary keys já criadas como foreign key.
class Telefone_Instrutor(models.Model):
    numero = models.IntegerField
    tipo = models.CharField(max_length=45, null=True)
    instrutor_idinstrutor = models.ForeignKey(Instrutor, on_delete=models.CASCADE)
#Agora a tabela Turma, pois era será utilizada para várias outras tabelas
class Turma(models.Model):
    horario = models.TimeField()
    duracap = models.IntegerField()
    dataInicio = models.DateField()
    dataFim = models.DateField()
    atividade_idatividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    instrutor_idinstrutor = models.ForeignKey(Instrutor, on_delete=models.CASCADE)

#Por fim, o resto das tabelas.
class Aluno(models.Model):
    codmatricula = models.IntegerField(primary_key=True)
    datamatricula = models.DateField()
    nome = models.CharField(max_length=45)
    endereco = models.TextField(null=True)
    telefone = models.IntegerField(null=True)
    datanascimento = models.DateField(null=True)
    altura = models.FloatField(null=True)
    peso = models.IntegerField(null=True)

class Matricula(models.Model):
    aluno_codmatricula = models.ManyToManyField(Aluno)
    turma_idturma = models.ManyToManyField(Turma)

class Chamada(models.Model):
    data = models.DateField()
    presente = models.BooleanField()
    matricula_aluno_codmatricula = models.ForeignKey(Matricula, on_delete=models.CASCADE)
    matricula_turma_idturma = models.ForeignKey(Turma, on_delete=models.CASCADE)