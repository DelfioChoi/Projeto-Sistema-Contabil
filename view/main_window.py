from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
from view.conta_view import ContaView
from view.transacao_view import TransacaoView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema Contábil Simples (SQLite)")
        self.setGeometry(200, 200, 400, 200)

        layout = QVBoxLayout()

        btn_contas = QPushButton("Gerenciar Contas")
        btn_contas.clicked.connect(self.abrir_contas)
        layout.addWidget(btn_contas)

        btn_transacoes = QPushButton("Gerenciar Transações")
        btn_transacoes.clicked.connect(self.abrir_transacoes)
        layout.addWidget(btn_transacoes)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def abrir_contas(self):
        self.conta_view = ContaView()
        self.conta_view.show()

    def abrir_transacoes(self):
        self.transacao_view = TransacaoView()
        self.transacao_view.show()
