from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QComboBox, QListWidget, QMessageBox
from controller.conta_controller import ContaController

class ContaView(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = ContaController()
        self.setWindowTitle("Gerenciar Contas")
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()

        self.input_nome = QLineEdit()
        self.input_nome.setPlaceholderText("Nome da conta")
        layout.addWidget(self.input_nome)

        self.combo_tipo = QComboBox()
        self.combo_tipo.addItems(["Ativo", "Passivo"])
        layout.addWidget(self.combo_tipo)

        btn_adicionar = QPushButton("Adicionar Conta")
        btn_adicionar.clicked.connect(self.adicionar_conta)
        layout.addWidget(btn_adicionar)

        self.lista_contas = QListWidget()
        layout.addWidget(self.lista_contas)

        btn_remover = QPushButton("Remover Conta")
        btn_remover.clicked.connect(self.remover_conta)
        layout.addWidget(btn_remover)

        self.setLayout(layout)
        self.atualizar_lista()

    def adicionar_conta(self):
        try:
            self.controller.adicionar_conta(self.input_nome.text(), self.combo_tipo.currentText())
            self.input_nome.clear()
            self.atualizar_lista()
        except ValueError as e:
            QMessageBox.warning(self, "Erro", str(e))

    def remover_conta(self):
        item = self.lista_contas.currentItem()
        if item:
            conta_id = int(item.data(1))
            self.controller.remover_conta(conta_id)
            self.atualizar_lista()

    def atualizar_lista(self):
        self.lista_contas.clear()
        for conta in self.controller.listar_contas():
            saldo = self.controller.saldo_conta(conta["id"])
            self.lista_contas.addItem(f"{conta['id']} - {conta['nome']} ({conta['tipo']}) | Saldo: {saldo:.2f}")
