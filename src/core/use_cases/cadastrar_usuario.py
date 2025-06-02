from src.core.entities.usuario import Usuario
from src.automation.pages.usuario_page import UsuarioPage
from src.utils.login import generate_possibles_logins

class CadastrarUsuario:
    def __init__(self, usuario_page: UsuarioPage):
        self.usuario_page = usuario_page

    def execute(self, usuario: Usuario):
        if not usuario.nome:
            return False

        login = self._encontrar_login_disponivel(usuario.nome)
        if not login:
            return False

        usuario.login = login

        if not self._validar_nome_unico(usuario.nome):
            return False

        if usuario.entidade and not self._validar_entidade(usuario.entidade):
            return False

        self._preencher_formulario(usuario)
        return True

    def _encontrar_login_disponivel(self, nome: str):
        self.usuario_page.clickOnSearchButton()
        self.usuario_page.moveFromNameToLogin()

        for login in reversed(generate_possibles_logins(nome)):
            self.usuario_page.writePossibleLogin(login)
            if not self.usuario_page.loginAlreadyUsed():
                self.usuario_page.clickOnCloseSearchButton()
                return login

        self.usuario_page.clickOnCloseSearchButton()
        return None

    def _validar_nome_unico(self, nome: str):
        self.usuario_page.clickOnSearchButton()
        self.usuario_page.seachByName(nome)
        is_unique = not self.usuario_page.searchByNameUserRegistered()
        self.usuario_page.clickOnCloseSearchButton()
        return is_unique

    def _validar_entidade(self, entidade: str):
        self.usuario_page.openSearchEntidade()
        self.usuario_page.searchEntidadeFillNomeEntidade(entidade)
        encontrada = self.usuario_page.entidadeFounded()
        self.usuario_page.clickOnCloseSearchButton()
        return encontrada

    def _preencher_formulario(self, usuario: Usuario):
        self.usuario_page.addRegister()
        self.usuario_page.fill_nome(usuario.nome)
        self.usuario_page.fill_login(usuario.login)

        if usuario.perfil_usuario_copia:
            self.usuario_page.fill_perfil_usuario_copia(usuario.perfil_usuario_copia)
            self.usuario_page.importar_perfil()

        self.usuario_page.resetar_senha()

        if usuario.empresa_lancamento:
            self.usuario_page.activateDetailEmpresasLancemento()
            self.usuario_page.fill_empresa_lancamento(usuario.empresa_lancamento)