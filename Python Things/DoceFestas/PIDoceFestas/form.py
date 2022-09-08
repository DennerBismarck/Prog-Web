from django.forms import ModelForm
from PIDoceFestas.models import Cliente, Aluguel


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ["nome", "numero", "logradouro", "telefone", "bairro"]

class AluguelForm(ModelForm):
    class Meta:
        model = Aluguel
        fields = ["cliente", "tema", "aniversariante", "entrega", "recebimento", "data_festa", "idade", "valor", "especificacoes"]
        
