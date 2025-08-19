
from dataclasses import dataclass

@dataclass
class Transacao:
    id: int
    conta_id: int
    data: str       # ISO date
    descricao: str
    tipo: str       # 'Entrada' ou 'Saída'
    valor: float
