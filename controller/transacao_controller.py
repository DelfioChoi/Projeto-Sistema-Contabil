from model.database import Database

class TransacaoController:
    def __init__(self):
        self.db = Database()

    def adicionar_transacao(self, conta_id, data, descricao, valor, tipo):
        if not descricao.strip():
            raise ValueError("Descrição não pode ser vazia.")
        if valor <= 0:
            raise ValueError("Valor deve ser positivo.")
        self.db.adicionar_transacao(conta_id, data, descricao, valor, tipo)

    def listar_transacoes(self, conta_id=None):
        return self.db.listar_transacoes(conta_id)

    def remover_transacao(self, transacao_id):
        self.db.remover_transacao(transacao_id)
