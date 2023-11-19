"""
Programação Orientada a Objetos

Herança
Herança acontece quando uma classe(classe filha ou subclasse) herda atributos e métodos de uma outra classe(classe mãe ou superclasse)
"""

from excecoes import (
    SaldoInsuficienteError,
    ValorInvalidoParaDeposito,
    ContaInvestimentoBloqueadaParaTransferencia
)

class ContaFinanceira:

    def __init__(self, nome, saldo=0) -> None:
        self._nome = nome
        self._saldo = saldo

    def exibir_saldo(self):
        return f"O saldo atual da conta {self._nome} é de R${self._saldo:.2f}."
    
    def sacar(self, valor):
        # A linha abaixo lança uma exceção NotImplementedError. Essa exceção será lançada caso esse método seja chamado. Ou seja, as classes filhas devem implementar esse método caso não queiram receber esse erro
        raise NotImplementedError
    
    def depositar(self, valor: float):
        if valor > 0:
            self._saldo += valor
        else:
            raise ValorInvalidoParaDeposito()
        
    @property
    def nome(self):
        return self._nome
    
    def transferir(self, valor: float, conta):
        saque = self.sacar(valor)
        conta.depositar(saque)
    

class ContaCorrente(ContaFinanceira):

    def sacar(self, valor: float):
        if valor <= self._saldo:
            self._saldo -= valor
            return valor
        else:
            raise SaldoInsuficienteError()


class ContaInvestimento(ContaFinanceira):

    def __init__(self, nome, saldo=0, taxa=0.01, dias_de_bloqueio=30) -> None:
        self._taxa = taxa
        self._dias_de_bloqueio = dias_de_bloqueio
        
        # Podemos chamar um métoda da classe mãe de onde estamos herdando. A função built-in super() permite que façamos isso.
        # No caso abaixo, depois de termos criado os atributos _taxa e _dias_de_bloqueio, chamamos o método construtor da nossa classe mãe para criar os atributos restantes (_nome, _saldo)
        super().__init__(nome, saldo)

    def render(self):
        self._saldo = self._saldo + (self._saldo * self._taxa)

    def depositar(self, valor):
        super().depositar(valor)
        self._dias_de_bloqueio = 30

    def transferir(self, valor: float, conta: ContaFinanceira):
        if self._dias_de_bloqueio == 0:
            super().transferir(valor, conta)
        else:
            raise ContaInvestimentoBloqueadaParaTransferencia(self)
    
    @property
    def dias_de_bloqueio(self):
        return self._dias_de_bloqueio
        
if __name__ == "__main__":

    conta_corrente_itau = ContaCorrente(
        "Conta Corrente Itaú", 1000
    )
    conta_corrente_viacredi = ContaCorrente(
        "Conta Corrente Viacredi", 0
    )

    conta_cdb_caixa = ContaInvestimento(
        "CDB 30 dias Caixa", 100
    )

    print(conta_corrente_itau.exibir_saldo())
    print(conta_cdb_caixa.exibir_saldo())
    conta_cdb_caixa.transferir(50, conta_corrente_viacredi)
