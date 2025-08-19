
from dataclasses import dataclass

@dataclass
class Conta:
    id: int
    nome: str
    tipo: str  # 'Ativo' ou 'Passivo'
