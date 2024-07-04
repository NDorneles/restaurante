# Nícolas Artifon Dorneles
# Classes herdadsa do Qt

from PySide6.QtWidgets import QComboBox, QLabel, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


class Rotulos_Left(QLabel):
    def __init__(self):
        super().__init__()

        font = QFont()
        font.setPixelSize(15)

        self.setFont(font)
        self.setFixedWidth(150)
        self.setAlignment(Qt.AlignLeft)


class Opcoes(QComboBox):
    def __init__(self):
        super().__init__()

        font = QFont()
        font.setPixelSize(13)
        #font.set

        self.setFont(font)
        self.setFixedSize(200, 50)


class Botao(QPushButton):
    def __init__(self):
        super().__init__()

        font = QFont()
        font.setPixelSize(15)

        self.setFont(font)
        self.setFixedSize(200, 30)
