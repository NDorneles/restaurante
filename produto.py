# Nícolas Artifon Dorneles
# Funções para gerar a lista com os Itens.

from item import Item
from pedido import Pedido
from pagamento import Pagamento


def gera_lanches():
    lanches = []
    lanches.append(Item("LAN-001", "Hambuguer Tradicional", 25.99))
    lanches.append(Item("LAN-002", "Hambuguer Bacon", 30.99))
    lanches.append(Item("LAN-003", "Hambuguer da Casa", 32.99))
    lanches.append(Item("LAN-004", "Hambuguer Vegetariano", 26.99))

    return lanches


def gera_bebidas():
    bebidas = []
    bebidas.append(Item("BEB-001", "Refrigerante Lata", 5.99))
    bebidas.append(Item("BEB-002", "Água com Gás", 4.99))
    bebidas.append(Item("BEB-003", "Drinks 500ml", 19.99))
    bebidas.append(Item("BEB-004", "Quentão", 8.99))

    return bebidas


def gera_sobrems():
    sobrems = []
    sobrems.append(Item("SOB-001", "Pudim", 19.99))
    sobrems.append(Item("SOB-002", "Churros", 20.99))
    sobrems.append(Item("SOB-003", "Fatia de Torta", 15.99))
    sobrems.append(Item("SOB-004", "Brigadeiro", 8.99))

    return sobrems


def procura(label, produtos: Item) -> Item:
    for produto in produtos:
        if label == produto.nome_item:
            return produto


lanches = gera_lanches()

pedido = Pedido(lanches, Pagamento(15.99))

# print(pedido.valor_itens())


# a = procura("Hambuguer da Casa", gera_lanches())

# print(a.imprime_info())
