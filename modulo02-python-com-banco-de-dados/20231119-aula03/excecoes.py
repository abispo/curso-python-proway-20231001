
class SaldoInsuficienteError(Exception):

    def __init__(self) -> None:
        super().__init__("Não existe saldo suficiente para a operação.")

class ValorInvalidoParaDeposito(Exception):
    
    def __init__(self) -> None:
        super().__init__(
            "Não é possível depositar valores menores ou iguais a zero."
        )

class ContaInvestimentoBloqueadaParaTransferencia(Exception):

    def __init__(self, conta) -> None:
        super().__init__(
            f"A conta '{conta.nome}' ainda está bloqueada por {conta.dias_de_bloqueio} dias."
        )