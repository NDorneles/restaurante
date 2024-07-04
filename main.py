from item import Item
from produto import gera_lanches, gera_bebidas, gera_sobrems
from pedido import Pedido
from pagamento import Pagamento
from personaliza import Rotulos_Left, Opcoes, Botao

from PySide6.QtWidgets import QRadioButton, QListWidget, QTabWidget, QApplication, QMainWindow, QGridLayout, QWidget, QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from qt_material import apply_stylesheet


class JanelaPrincipal(QMainWindow):

    # Salva os itens do pedido atual
    produtos = []
    # Salca os pedidos feitos
    pedidos_feitos = []
    # Soma o valor dos itens
    soma_itens = 0
    # Contados de pedidos
    numero_pedido = 1

    def __init__(self):
        super().__init__()
        # Mantem o tamanho contante e não permite que o usário mude.
        self.setFixedSize(700, 500)
        self.setWindowTitle("APP")
        # Criar abas
        self.tab = QTabWidget()

        # Criar widget
        self.widget = QWidget()
        self.widget_2 = QWidget()
        self.widget_3 = QWidget()
        # Layout da 1ª página
        self.layout_1 = QGridLayout()

        # Estilo da fonte, geral para as aplicações
        font = QFont()
        font.setPixelSize(15)
        # Estilo da fonte para a lista em Cozinha
        font_2 = QFont()
        font_2.setPixelSize(11)

        # Aba 1
        # Lista de pedidos selecionados
        self.list_1 = QListWidget()
        self.list_1.setFixedWidth(275)
        self.list_1.setFixedHeight(400)

        # Rótulos da primeira página
        self.label_1 = Rotulos_Left()
        self.label_1.setText("Lanches")

        self.label_2 = Rotulos_Left()
        self.label_2.setText("Bebidas")

        self.label_3 = Rotulos_Left()
        self.label_3.setText("Sobremesas")

        self.label_4 = Rotulos_Left()
        self.label_4.setText("Opção de Pagamento")

        # Rótulo com a soma dos itens do pedido
        self.label_5 = QLabel()
        self.label_5.setFont(font)
        self.label_5.setFixedWidth(200)
        self.label_5.setAlignment(Qt.AlignRight)
        self.label_5.setText(f"R$ {self.soma_itens:.2f}")

        # Impressão do título no início da página
        self.label_6 = Rotulos_Left()
        self.label_6.setText(f"MENU")

        # ComboBox para a seleção dos lanches
        self.combo_1 = Opcoes()
        self.combo_1.activated.connect(self.evento_lanche)

        # ComboBox para a seleção das bebidas
        self.combo_2 = Opcoes()
        self.combo_2.activated.connect(self.evento_bebida)

        # ComboBox para a seleção das sobremesas
        self.combo_3 = Opcoes()
        self.combo_3.activated.connect(self.evento_sobrem)

        # ComboBox para a seleção da forma de pagamento
        self.combo_4 = Opcoes()

        # Botão para a conclusão do pedido
        self.botao_1 = Botao()
        self.botao_1.setText("FAZER PEDIDO")
        # Ação do Botão 1
        self.botao_1.clicked.connect(self.concluir_pedido)

        # Botão para deletar o último item da lista
        self.botao_2 = Botao()
        self.botao_2.setText("REMOVER ITEM")
        # Ação do Botão 1
        self.botao_2.clicked.connect(self.remover_item)

        # Adiciona os objetos no grid da página
        self.layout_1.addWidget(self.label_6, 0, 0, 1, 2)
        self.layout_1.addWidget(self.label_1, 1, 0, 1, 1)
        self.layout_1.addWidget(self.label_2, 2, 0, 1, 1)
        self.layout_1.addWidget(self.label_3, 3, 0, 1, 1)
        self.layout_1.addWidget(self.label_4, 5, 0, 1, 1)
        self.layout_1.addWidget(self.label_5, 6, 2, 1, 1)
        self.layout_1.addWidget(self.combo_1, 1, 1, 1, 1)
        self.layout_1.addWidget(self.combo_2, 2, 1, 1, 1)
        self.layout_1.addWidget(self.combo_3, 3, 1, 1, 1)
        self.layout_1.addWidget(self.combo_4, 5, 1, 1, 1)
        self.layout_1.addWidget(self.botao_1, 6, 0, 1, 1)
        self.layout_1.addWidget(self.botao_2, 6, 1, 1, 1)
        self.layout_1.addWidget(self.list_1, 0, 2, 5, 1)

        # Espaçamento vertical entre os itens
        self.layout_1.setVerticalSpacing(25)
        # Adiciona o estilo no Widget
        self.widget.setLayout(self.layout_1)
        # Adicona o widget na ABA
        self.tab.addTab(self.widget, "PEDIDO")

        # Aba 2
        # Criação do layout
        self.layout_2 = QGridLayout()

        # Lista para os pedidos realizados
        self.list_2 = QListWidget()
        self.list_2.setFixedWidth(210)
        self.list_2.setFixedHeight(350)
        self.list_2.setFont(font_2)

        # Lista para o filtro de pedidos
        self.list_3 = QListWidget()
        self.list_3.setFixedWidth(210)
        self.list_3.setFixedHeight(350)
        self.list_3.setFont(font_2)

        # Rótulo da página
        self.label_7 = Rotulos_Left()
        self.label_7.setText("Número do pedido:")

        # ComboBox com o número dos pedidos
        self.combo_5 = Opcoes()
        # ComboBox com o filtro dos pedidos
        self.combo_6 = Opcoes()
        self.combo_6.activated.connect(self.filtro_opcao)

        # Botão para a submissão da mudança dos status
        self.botao_3 = Botao()
        self.botao_3.setText("MUDAR STATUS")
        self.botao_3.clicked.connect(self.procura_pedido)

        # Seleção da opção ente os status
        self.option_1 = QRadioButton("PEDIDO")
        self.option_2 = QRadioButton("EM PREPARAÇÃO")
        self.option_3 = QRadioButton("ENTREGUE")

        # Adiciona os objetos no grid da página
        self.layout_2.addWidget(self.list_2, 1, 0, 5, 1)
        self.layout_2.addWidget(self.list_3, 1, 1, 5, 1)
        self.layout_2.addWidget(self.label_7, 0, 2, 1, 1)
        self.layout_2.addWidget(self.combo_5, 1, 2, 1, 1)
        self.layout_2.addWidget(self.combo_6, 0, 1, 1, 1)
        self.layout_2.addWidget(self.option_1, 2, 2, 1, 1)
        self.layout_2.addWidget(self.option_2, 3, 2, 1, 1)
        self.layout_2.addWidget(self.option_3, 4, 2, 1, 1)
        self.layout_2.addWidget(self.botao_3, 5, 2, 1, 1)

        # Espaçamento vertical entre os itens
        self.layout_2.setVerticalSpacing(45)
        # Adiciona o estilo no Widget
        self.widget_2.setLayout(self.layout_2)
        # Adicona o widget na ABA
        self.tab.addTab(self.widget_2, "COZINHA")

        # Aba 3
        # Criação do layout
        self.layout_3 = QGridLayout()

        # Rótulos da aba
        self.label_8 = Rotulos_Left()
        self.label_8.setText("Número de pedidos:")

        self.label_9 = Rotulos_Left()
        self.label_9.setText("Faturamento total:")

        self.label_10 = Rotulos_Left()
        self.label_10.setText("Produto:")

        # Rótulos com os resultados.
        self.label_11 = Rotulos_Left()
        self.label_11.setAlignment(Qt.AlignRight)
        self.label_11.setFont(font)
        self.label_11.setFixedWidth(150)
        self.label_12 = Rotulos_Left()
        self.label_12.setAlignment(Qt.AlignRight)
        self.label_13 = Rotulos_Left()
        self.label_13.setAlignment(Qt.AlignRight)

        # ComboBox com as opções dos itens vendidos
        self.combo_7 = Opcoes()
        self.combo_7.activated.connect(self.conta_itens)

        # Adiciona os objetos no grid da página
        self.layout_3.addWidget(self.label_8, 2, 0, 1, 1)
        self.layout_3.addWidget(self.label_9, 3, 0, 1, 1)
        self.layout_3.addWidget(self.label_10, 1, 0, 1, 1)
        self.layout_3.addWidget(self.label_11, 2, 1, 1, 1)
        self.layout_3.addWidget(self.label_12, 3, 1, 1, 1)
        self.layout_3.addWidget(self.combo_7, 0, 1,1, 1)
        self.layout_3.addWidget(self.label_13, 1, 1, 1, 1)

        # Espaçamento vertical entre os itens
        self.layout_3.setVerticalSpacing(50)
        self.layout_3.setHorizontalSpacing(20)
        # Adiciona o estilo no Widget
        self.widget_3.setLayout(self.layout_3)
        self.widget_3.setFixedHeight(300)
        self.widget_3.setFixedWidth(550)
        # Adicona o widget na ABA
        self.tab.addTab(self.widget_3, "GERÊNCIA")

        # Define a aba principal
        self.setCentralWidget(self.tab)
        # Exibe a janela
        self.show()

    # Funções específicas
    # Procura dentro das opções de Lanche
    def evento_lanche(self):
        lanche = self.procura_item(self.combo_1.currentText(), gera_lanches())
        # Salva os produtos
        self.produtos.append(lanche)
        self.list_1.addItem(lanche.imprime_info())
        # Após adicionar algo, soma os itens
        self.soma_lista()

    # Procura dentro das opções de Bebida
    def evento_bebida(self):
        bebidas = self.procura_item(self.combo_2.currentText(), gera_bebidas())
        # Salva os produtos
        self.produtos.append(bebidas)
        self.list_1.addItem(bebidas.imprime_info())
        # Após adicionar algo, soma os itens
        self.soma_lista()

    # Procura dentro das opções de Bebida
    def evento_sobrem(self):
        sobrems = self.procura_item(self.combo_3.currentText(), gera_sobrems())
        # Salva os produtos
        self.produtos.append(sobrems)
        self.list_1.addItem(sobrems.imprime_info())
        # Após adicionar algo, soma os itens
        self.soma_lista()

    # Procura pelo texto do nome do produto na lista e produtos para o retornar
    def procura_item(self, label, produtos: Item) -> Item:
        for produto in produtos:
            if label == produto.nome_item:
                return produto

    # Remove o último item da lista
    def remover_item(self):
        self.list_1.takeItem(len(self.produtos)-1)
        self.produtos.pop()
        # Atualiza a soma com os valores na lista
        self.soma_lista()

    # Soma os preço dos produtos na lista
    def soma_lista(self):
        self.soma_itens = 0
        for produto in self.produtos:
            self.soma_itens += produto.preco_item
        self.label_5.setText(f"R$ {self.soma_itens:.2f}")

    def concluir_pedido(self):
        # Cria no método de pagamento atual
        pagamento = Pagamento(self.combo_4.currentText())
        # Cria o pedido atual e define o número dele
        pedido = Pedido(self.produtos.copy(), pagamento)
        pedido.numero_pedido = self.numero_pedido
        # Adiciona à lista de pedido e atualiza o contador de pedidos do dia
        pedido.valor_pedido()
        # Aciona o pedido à lista de pedidos
        self.pedidos_feitos.append(pedido)
        # Atauliza o contador
        self.numero_pedido += 1

        # Adiciona o pedido na lista da cozinha
        self.list_2.addItem(pedido.imprime_info())
        self.combo_5.addItem(str(pedido.numero_pedido))

        # Adiciona o pedido ao contador da Gerência
        self.label_11.setText(str(len(self.pedidos_feitos)))

        # deleta as listas para o próximo pedido
        self.list_1.clear()
        self.produtos.clear()
        # Reatuliza a soma
        self.soma_lista()
        # Atualiza o contador da gerência.
        self.soma_pedidos()

    # Procura um pedido específico tendo como base o número e atualiza o estados de acordo com o RadioBox marcado.
    def procura_pedido(self):
        # Número do pedido
        search = int(self.combo_5.currentText())
        if self.option_1.isChecked():
            status = self.option_1.text()
        elif self.option_2.isChecked():
            status = self.option_2.text()
        elif self.option_3.isChecked():
            status = self.option_3.text()
        # Status do pedido é atualizado
        self.pedidos_feitos[search-1].status_pedido = status
        # Atualiza o texto impresso na list 2
        self.list_2.item(
            search-1).setText(self.pedidos_feitos[search-1].imprime_info())

    # Filtro de opção. Imprime na list 3 os pedidos que tem aquele status.
    def filtro_opcao(self):
        # Limpa o atual
        self.list_3.clear()
        # Valor atual do filtro
        filtro = self.combo_6.currentText()
        # Procura a informação
        for pedido in self.pedidos_feitos:
            if pedido.status_pedido == filtro:
                self.list_3.addItem(pedido.imprime_info())

    # Conta os números de um item específico pedido.
    def conta_itens(self):
        cont = 0
        item_atual = self.combo_7.currentText()
        for pedido in self.pedidos_feitos:
            for itens in pedido.itens_pedido:
                # Se o nome é igual, atualiza a coma
                if item_atual == itens.nome_item:
                    cont += 1
        self.label_13.setText(str(cont))

    # Soma total do valor dos pedidos feitos.
    def soma_pedidos(self):
        soma = 0
        for pedido in self.pedidos_feitos:
            soma += pedido.valor_itens
        self.label_12.setText(f"R$ {soma:.2f}")


if __name__ == "__main__":
    # Vetores de itens
    lanches = gera_lanches()
    bebidas = gera_bebidas()
    sobrems = gera_sobrems()
    # Listas vazias
    lanche = []
    bebida = []
    sobrem = []
    # Loop para inserir o nome dos itens as listas que vão as ComboBox
    for itens in range(0, 4):
        lanche.append(lanches[itens].nome_item)
        bebida.append(bebidas[itens].nome_item)
        sobrem.append(sobrems[itens].nome_item)
    # Início da aplicação

    extra = {

    # Button colors
    'primaryColor': '#FF7E00',
    'secondaryLightColor': '#ffffff',
    'primaryTextColor': '#ffffff',

    # Font
    'font_family': 'Roboto',
    'font_size': '8px'
    }
    app = QApplication()
    apply_stylesheet(app, theme='dark_amber.xml', extra=extra)
    janela = JanelaPrincipal()
    # Valores definidos para as ComboBox
    janela.combo_1.addItems(lanche)
    janela.combo_2.addItems(bebida)
    janela.combo_3.addItems(sobrem)
    janela.combo_4.addItems(["Crédito", "Débito"])
    janela.combo_6.addItems(["PEDIDO", "EM PREPARAÇÃO", "ENTREGUE"])
    janela.combo_7.addItems(lanche)
    janela.combo_7.addItems(bebida)
    janela.combo_7.addItems(sobrem)
    # Valores iniciais das labels da aba gerência
    janela.label_11.setText(str(0))
    janela.label_12.setText("R$ " + str(0)+".00")
    janela.label_13.setText(str(0))

    # Exibe a aplicação.
    janela.show()
    app.exec()
