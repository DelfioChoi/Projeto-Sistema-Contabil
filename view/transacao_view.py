from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QComboBox, QListWidget, QMessageBox
from PyQt5.QtCore import QDate
from controller.transacao_controller import TransacaoController
from controller.conta_controller import ContaController

class TransacaoView(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = TransacaoController()
        self.conta_controller = ContaController()
        self.setWindowTitle("Gerenciar Transações")
        self.setGeometry(350, 350, 500, 400)

        layout = QVBoxLayout()

        self.combo_conta = QComboBox()
        self.atualizar_contas()
        layout.addWidget(self.combo_conta)

        self.input_data = QLineEdit(QDate.currentDate().toString("yyyy-MM-dd"))
        layout.addWidget(self.input_data)

        self.input_descricao = QLineEdit()
        self.input_descricao.setPlaceholderText("Descrição")
        layout.addWidget(self.input_descricao)

        self.input_valor = QLineEdit()
        self.input_valor.setPlaceholderText("Valor")
        layout.addWidget(self.input_valor)

        self.combo_tipo = QComboBox()
        self.combo_tipo.addItems(["Entrada", "Saída"])
        layout.addWidget(self.combo_tipo)

        btn_adicionar = QPushButton("Adicionar Transação")
        btn_adicionar.clicked.connect(self.adicionar_transacao)
        layout.addWidget(btn_adicionar)

        self.lista_transacoes = QListWidget()
        layout.addWidget(self.lista_transacoes)

        btn_remover = QPushButton("Remover Transação")
        btn_remover.clicked.connect(self.remover_transacao)
        layout.addWidget(btn_remover)

        self.setLayout(layout)
        self.atualizar_lista()

    def atualizar_contas(self):
        self.combo_conta.clear()
        for conta in self.conta_controller.listar_contas():
            self.combo_conta.addItem(f"{conta['id']} - {conta['nome']}", conta["id"])

    def adicionar_transacao(self):
        try:
            conta_id = self.combo_conta.currentData()
            self.controller.adicionar_transacao(
                conta_id,
                self.input_data.text(),
                self.input_descricao.text(),
                float(self.input_valor.text()),
                self.combo_tipo.currentText()
            )
            self.input_descricao.clear()
            self.input_valor.clear()
            self.atualizar_lista()
        except ValueError as e:
            QMessageBox.warning(self, "Erro", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Erro inesperado", str(e))

    def remover_transacao(self):
        item = self.lista_transacoes.currentItem()
        if item:
            transacao_id = int(item.data(1))
            self.controller.remover_transacao(transacao_id)
            self.atualizar_lista()

    def atualizar_lista(self):
        self.lista_transacoes.clear()
        for transacao in self.controller.listar_transacoes():
            self.lista_transacoes.addItem(
                f"{transacao['id']} - Conta: {transacao['conta_id']} | {transacao['data']} | {transacao['descricao']} | {transacao['valor']:.2f} ({transacao['tipo']})"
            )
