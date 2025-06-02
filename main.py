from src.core.entities.usuario import Usuario
from src.automation.pages.usuario_page import UsuarioPage
from src.core.use_cases.cadastrar_usuario import CadastrarUsuario
from src.automation.tasks.processador_usuarios import ProcessadorUsuarios
from src.core.entities.colaborador import Colaborador

def main():
    usuario_page = UsuarioPage()
    cadastrar_usuario = CadastrarUsuario(usuario_page)
    task = ProcessadorUsuarios(cadastrar_usuario)

    colaboradores = Colaborador()

    usuarios = []
    for colaborador in colaboradores.getColaboradores():
        usuario = Usuario(
            nome=colaborador[5],
            perfil_usuario_copia=colaborador[7],
            empresa_lancamento=15
        )
        usuarios.append(usuario)
    
    task.execute(usuarios)
    print("Cadastro concluido")

if __name__ == "__main__":
    main()