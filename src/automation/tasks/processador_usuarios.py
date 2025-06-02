from src.core.use_cases.cadastrar_usuario import CadastrarUsuario
from src.core.entities.usuario import Usuario

class ProcessadorUsuarios:
    def __init__(self, cadastrar_usuario: CadastrarUsuario):
        self.cadastrar_usuario = cadastrar_usuario

    def execute(self, usuarios: list[Usuario]):
        for usuario in usuarios:
            if(usuario.nome is None): return
            self.cadastrar_usuario.execute(usuario)