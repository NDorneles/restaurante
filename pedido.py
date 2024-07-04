# Nícolas Artifon Dorneles
# Classe Pedido

from item import Item
from pagamento import Pagamento

class Pedido:

    numero_pedido:int
    valor_itens:float
    
    #Construtor
    def __init__(self, itens_pedido, pagamento_pedido:Pagamento):
        self._status_pedido = "PEDIDO"
        self._itens_pedido = itens_pedido
        self._pagamento_pedido = pagamento_pedido

    # Getters
    @property
    def numero_pedido(self):
        return self._numero_pedido
    
    @property
    def status_pedido(self):
        return self._status_pedido

    @property
    def itens_pedido(self):
        return self._itens_pedido

    @property
    def pagamento_pedido(self):
        return self._pagamento_pedido
    
    @property
    def valor_itens(self):
        return self._valor_itens
    
    #Setter
    @numero_pedido.setter
    def numero_pedido(self, numero_pedido):
        self._numero_pedido = numero_pedido
    
    @status_pedido.setter
    def status_pedido(self, status_pedido):
        self._status_pedido = status_pedido
    
    @itens_pedido.setter
    def itens_pedido(self, itens_pedido):
        self._itens_pedido = itens_pedido

    @pagamento_pedido.setter
    def pagamento_pedido(self, pagamento_pedido):
        self._pagamento_pedido = pagamento_pedido
    
    #Calcula o valor total do pedido
    def valor_pedido(self):
        valor_itens = 0 
        for item in self.itens_pedido:
            valor_itens += item.preco_item
        self._valor_itens = valor_itens 

    #Imprime as informações do pedido
    def imprime_info(self):
        return f'Pedido: {self.numero_pedido} - Status: {self.status_pedido} - R$ {self.valor_itens:.2f}'