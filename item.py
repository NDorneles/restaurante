# Nícolas Artifon Dorneles
# Classe Item
class Item:
    # Construtor
    def __init__(self, codigo_item, nome_item, preco_item):
        self._codigo_item = codigo_item
        self._nome_item = nome_item
        self._preco_item = preco_item

    # Getters
    @property
    def codigo_item(self):
        return self._codigo_item

    @property
    def nome_item(self):
        return self._nome_item

    @property
    def preco_item(self):
        return self._preco_item

    # Setter
    @codigo_item.setter
    def codigo_item(self, codigo_item):
        self._codigo_item = codigo_item

    @nome_item.setter
    def nome_item(self, nome_item):
        self._nome_item = nome_item

    @preco_item.setter
    def preco_item(self, preco_item):
        self._preco_item = preco_item

    # Impressão das informações
    def imprime_info(self):
        return f'{self.codigo_item} --- {self.nome_item} --- R$ {self.preco_item:.2f}'
