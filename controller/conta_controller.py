from model.database import Database

class ContaController:
    def __init__(self):
        self.db = Database()

    def adicionar_conta(self, nome, tipo):
        if not nome.strip():
            raise ValueError("Nome da conta não pode ser vazio.")
        self.db.adicionar_conta(nome, tipo)

    def listar_contas(self):
        return self.db.listar_contas()

    def remover_conta(self, conta_id):
        self.db.remover_conta(conta_id)

    def saldo_conta(self, conta_id):
        return self.db.saldo_conta(conta_id)
