import sqlite3
import os

# DB_PATH = os.path.join(os.path.dirname(__file__), '../Documents/Database DB Browser/sistema_contabil.db')
DB_PATH = r'C:\Users\LENOVO-TP\Documents\Database DB Browser\sistema_contabil.db'

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.conn.row_factory = sqlite3.Row
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                tipo TEXT NOT NULL CHECK(tipo IN ('Ativo', 'Passivo'))
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transacoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                conta_id INTEGER NOT NULL,
                data TEXT NOT NULL,
                descricao TEXT NOT NULL,
                valor REAL NOT NULL,
                tipo TEXT NOT NULL CHECK(tipo IN ('Entrada', 'Saída')),
                FOREIGN KEY(conta_id) REFERENCES contas(id) ON DELETE CASCADE
            )
        ''')
        self.conn.commit()

    # Contas
    def adicionar_conta(self, nome, tipo):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO contas (nome, tipo) VALUES (?, ?)", (nome, tipo))
        self.conn.commit()

    def listar_contas(self):
        return self.conn.execute("SELECT * FROM contas").fetchall()

    def remover_conta(self, conta_id):
        self.conn.execute("DELETE FROM contas WHERE id = ?", (conta_id,))
        self.conn.commit()

    # Transações
    def adicionar_transacao(self, conta_id, data, descricao, valor, tipo):
        self.conn.execute(
            "INSERT INTO transacoes (conta_id, data, descricao, valor, tipo) VALUES (?, ?, ?, ?, ?)",
            (conta_id, data, descricao, valor, tipo)
        )
        self.conn.commit()

    def listar_transacoes(self, conta_id=None):
        if conta_id:
            return self.conn.execute("SELECT * FROM transacoes WHERE conta_id = ?", (conta_id,)).fetchall()
        return self.conn.execute("SELECT * FROM transacoes").fetchall()

    def remover_transacao(self, transacao_id):
        self.conn.execute("DELETE FROM transacoes WHERE id = ?", (transacao_id,))
        self.conn.commit()

    def saldo_conta(self, conta_id):
        entradas = self.conn.execute(
            "SELECT SUM(valor) FROM transacoes WHERE conta_id = ? AND tipo = 'Entrada'",
            (conta_id,)
        ).fetchone()[0] or 0
        saidas = self.conn.execute(
            "SELECT SUM(valor) FROM transacoes WHERE conta_id = ? AND tipo = 'Saída'",
            (conta_id,)
        ).fetchone()[0] or 0
        return entradas - saidas
