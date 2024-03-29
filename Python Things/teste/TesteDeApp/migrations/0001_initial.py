# Generated by Django 4.0.5 on 2022-08-04 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('codmatricula', models.IntegerField(primary_key=True, serialize=False)),
                ('datamatricula', models.DateField()),
                ('nome', models.CharField(max_length=45)),
                ('endereco', models.TextField(null=True)),
                ('telefone', models.IntegerField(null=True)),
                ('datanascimento', models.DateField(null=True)),
                ('altura', models.FloatField(null=True)),
                ('peso', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Instrutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rg', models.IntegerField()),
                ('nome', models.CharField(max_length=45)),
                ('nascimento', models.DateField()),
                ('titulacao', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.TimeField()),
                ('duracap', models.IntegerField()),
                ('dataInicio', models.DateField()),
                ('dataFim', models.DateField()),
                ('atividade_idatividade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TesteDeApp.atividade')),
                ('instrutor_idinstrutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TesteDeApp.instrutor')),
            ],
        ),
        migrations.CreateModel(
            name='Telefone_Instrutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=45, null=True)),
                ('instrutor_idinstrutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TesteDeApp.instrutor')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aluno_codmatricula', models.ManyToManyField(to='TesteDeApp.aluno')),
                ('turma_idturma', models.ManyToManyField(to='TesteDeApp.turma')),
            ],
        ),
        migrations.CreateModel(
            name='Chamada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('presente', models.BooleanField()),
                ('matricula_aluno_codmatricula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TesteDeApp.matricula')),
                ('matricula_turma_idturma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TesteDeApp.turma')),
            ],
        ),
    ]
