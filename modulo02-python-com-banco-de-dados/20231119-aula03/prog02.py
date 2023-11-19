"""
Programação Orientada a Objetos

Encapsulamento
É o processo onde "escondemos" informações internas do objeto, e definimos as "interfaces" públicas, onde o usuário poderá acessar e manipular o estado do objeto
"""

class ContaBancaria:
    
    def __init__(self, nome, saldo=0) -> None:
        # Em Python, não temos a diferenciação de membros privados, protegidos e públicos como em outras linguagens, como Java, C#, etc. Quando queremos indicar que um atributo ou um método de uma classe deve ser tratado como privado, colocamos um underline '_' na frente. Assim sendo, esse atributo ou método não poderá ser chamado diretamente
        self._nome = nome
        self._saldo = saldo

    # Em alguns casos, podemos querer criar métodos de acesso e alteração dos atributos privados, chamados de métodos getters e setters. Podemos seguir esse mesmo padrão no Python, sem problemas. Porém o Python tem um decorador especial para tratar desses casos, que é o decorador @property. Lembrando que um decorador (ou decorator) é uma função que altera o comportamento de outra função
    # def get_nome(self):
    #     return self._nome
    
    # def set_nome(self, novo_nome):
    #     self._nome = novo_nome

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    def exibir_saldo(self):
        return self._saldo
    
    def depositar(self, valor):
        # self._saldo = self._saldo + valor
        self._saldo += valor

    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            return valor
        else:
            raise Exception("Valor disponível é menor do que o valor solicitado!")

if __name__ == "__main__":

    conta_corrente_caixa = ContaBancaria(
        "Conta Corrente Caixa", 100
    )
    
    while True:

        try:
            texto = """
        Escolha uma opção
        0   - SAIR
        1   - EXIBIR SALDO
        2   - FAZER DEPÓSITO
        3   - REALIZAR SAQUE"""
            
            print(texto)
            opcao = int(input("Informe a opção: "))

            match opcao:
                case 0:
                    break

                case 1:
                    # Apesar da linha abaixo ser executada sem problemas pelo Python, temos aqui uma quebra do conceito de encapsulamento, pois estamos acessando diretamente um atributo da classe que foi definido como sendo privado. Nesse caso, ao invés de fazermos isso, precisamos chamar o método público exibir_saldo, que acessa o valor do atributo _saldo e retorna.
                    # saldo = conta_corrente_caixa._saldo
                    saldo = conta_corrente_caixa.exibir_saldo()
                    print(f"O seu saldo atual é de R${saldo:.2f}")

                case 2:
                    # Na linha abaixo estamos cometendo o mesmo erro que na opção anterior, ou seja, acessando e alterando diretamente o valor de um atributo privado. Devemos chamar o método depositar()
                    # conta_corrente_caixa._saldo += valor
                    valor = float(input("Informe o valor do depósito: "))
                    conta_corrente_caixa.depositar(valor)

                case 3:
                    valor = float(input("Informe o valor do saque: "))
                    conta_corrente_caixa.sacar(valor)

                case _:
                    print("OPÇÃO DESCONHECIDA")
                    print('-'*50)

        except Exception as exc:
            print(f"Erro ao realizar a operação: {exc}")