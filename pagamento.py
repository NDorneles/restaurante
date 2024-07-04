# Nícolas Artifon Dorneles
# Classe Pagamento

class Pagamento:
    # Valor do pagamento inicial é zero
    _preco_pagar = 0
    
    # Construtor
    def __init__(self, forma_pagamento):
        self._forma_pagamento = forma_pagamento

    # Getters
    @property
    def preco_pagar(self):
        return self._preco_pagar

    @property
    def forma_pagamento(self):
        return self._forma_pagamento

    # Setter
    @preco_pagar.setter
    def preco_pagar(self, preco_pagar):
        self._preco_pagar = preco_pagar

    @forma_pagamento.setter
    def forma_pagamento(self, forma_pagamento):
        self._forma_pagamento = forma_pagamento

    def imprime_info(self):
        return f'Total {self.forma_pagamento}: R$ {self.preco_pagar}'
