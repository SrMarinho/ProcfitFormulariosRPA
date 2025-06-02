from src.core.entities.funcionario import Funcionario
from src.core.use_cases.cadastras_funcionario import CadastrarFuncionario

class ProcessadorFuncionarios:
    def __init__(self, cadastrar_funcionario: CadastrarFuncionario):
        self.cadastrar_funcionario = cadastrar_funcionario

    def execute(self, funcionarios: list[Funcionario]):
        for funcionario in funcionarios:
            if(funcionario.nome is None): return
            self.cadastrar_funcionario.execute(funcionario)