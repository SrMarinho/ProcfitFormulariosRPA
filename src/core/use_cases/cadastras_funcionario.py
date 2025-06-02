from src.core.entities.funcionario import Funcionario
from src.automation.pages.funcionario_page import FuncionarioPage

class CadastrarFuncionario:
    def __init__(self, funcionario_page: FuncionarioPage):
        self.usuario_page = funcionario_page

    def execute(self, funcionario: Funcionario):
        #TODO passar o cadastro de funcionaro da estrutura anterior para a nova
        ...