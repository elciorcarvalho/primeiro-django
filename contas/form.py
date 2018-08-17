from django.forms import ModelForm  #Importa a classe ModelForm com os componentes para a funcionalidade
from .models import Transacao  #Importa o Model que usara o ModelForm


class TransacaoForm(ModelForm):
    #Meta classe para selecionar os campos do Model que irao ser atribuidos no form
    class Meta:
        model = Transacao
        fields = {'dt_trasacao', 'descricao', 'valor', 'observacoes', 'categoria'}
