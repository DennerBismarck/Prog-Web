from django.contrib import admin
from .models import Instrutor, Atividade, Telefone_Instrutor, Turma, Aluno, Matricula, Chamada
# Register your models here.

admin.site.register(Instrutor)
admin.site.register(Atividade)
admin.site.register(Telefone_Instrutor)
admin.site.register(Turma)
admin.site.register(Aluno)
admin.site.register(Matricula)
admin.site.register(Chamada)