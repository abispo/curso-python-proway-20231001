"""
Programação Orientada a Objetos

Polimorfismo
Polimorfismo significa "muitos formas", ou seja, uma função ou método que pode ser chamado de diferentes maneiras ou possui diferentes comportamentos.

Dentro do Python existem alguns tipos de polimorfismos, como de função, de método, etc. No caso abaixo, o método calcular_salario() da classe mãe Funcionario, possui diferentes implementações nas classes filhas, apesar de sempre retornar um valor numérico.
"""

class Funcionario:

    def __init__(self, nome) -> None:
        self._nome = nome

    def calcular_salario(self):
        raise NotImplementedError
    
    @property
    def nome(self):
        return self._nome
    

class FuncionarioCLT(Funcionario):
    def __init__(self, nome, salario) -> None:
        self._salario = salario
        super().__init__(nome)

    def calcular_salario(self):
        return self._salario
    

class FuncionarioTerceirizado(Funcionario):

    def __init__(self, nome, valor_hora, qtd_horas) -> None:
        self._valor_hora = valor_hora
        self._qtd_horas = qtd_horas
        super().__init__(nome)

    def calcular_salario(self):
        return self._valor_hora * self._qtd_horas
    

class FuncionarioComissionado(Funcionario):

    def __init__(self, nome, valor_das_vendas, comissao) -> None:
        self._valor_das_vendas = valor_das_vendas
        self._comissao = comissao
        super().__init__(nome)

    def calcular_salario(self):
        return self._valor_das_vendas * (self._comissao / 100)
    
if __name__ == "__main__":

    jose = FuncionarioCLT("José", 2500)
    joao = FuncionarioTerceirizado("João", 120, 21)
    maria = FuncionarioComissionado("Maria", 80000, 5)

    for funcionario in [jose, joao, maria]:
        print(f"O funcionário {funcionario.nome} recebeu R$ {funcionario.calcular_salario():.2f}.")