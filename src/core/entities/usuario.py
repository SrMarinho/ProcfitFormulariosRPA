from dataclasses import dataclass
from typing import Optional

@dataclass
class Usuario:
    nome: str
    login: Optional[int] = None
    usuario: Optional[int] = None
    superior_imediato: Optional[int] = None
    entidade: Optional[int] = None
    perfil_usuario_copia: Optional[int] = None
    empresa_lancamento: Optional[int] = None