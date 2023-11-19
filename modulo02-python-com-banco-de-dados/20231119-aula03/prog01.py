"""
Programação Orientada a Objetos

Classe, atributos e métodos
"""

# Utilizamos a palavra reservada 'class' para criar uma classe. Por padrão, os nomes das classes em Python devem seguir o padrão PascalCase
class Pokemon:
    
    # O método __init__ é chamado quando estamos instanciando uma classe. Apesar de não ser exatamente, podemos chamá-lo de método construtor, ou método inicializador da classe. Nesse método podemos passar os valores com que vamos passar inicialmente para os atributos da classe.
    def __init__(self, nome, tipo, vitalidade):

        # self é uma referência ao próprio objeto instanciado. No Python, devemos passar essa referência de maneira explícita, sempre como o primeiro argumento dos métodos
        self.nome = nome
        self.tipo = tipo
        self.vitalidade = vitalidade

    # Utilizamos o self para acessar os atributos ou os métodos do próprio objeto. Com isso, podemos ter métodos que alteram o estado do objeto.
    def atacar(self):
        print(f"O {self.nome} atacou!")

    def desviar(self):
        print(f"O {self.nome} desviou do Ataque!")

    def evoluir(self):
        print(f"O {self.nome} evoluiu!")

if __name__ == "__main__":
    pikachu = Pokemon("Pikachu", "Elétrico", 70)

    saida = f"""
    Pokemon: {pikachu.nome}
    Tipo: {pikachu.tipo}
    Vitalidade: {pikachu.vitalidade}
    """

    print(saida)

    pikachu.atacar()
    pikachu.desviar()
    pikachu.evoluir()

    bulbasauro = Pokemon("Bulbasauro", "Planta", 100)

    saida = f"""
    Pokemon: {bulbasauro.nome}
    Tipo: {bulbasauro.tipo}
    Vitalidade: {bulbasauro.vitalidade}
    """

    print(saida)

    bulbasauro.atacar()
    bulbasauro.desviar()
    bulbasauro.evoluir()

    class Pikachu(Pokemon):

        def __init__(self):
            super().__init__("Pikachu", "Elétrico", 70)

    class Bulbasauro(Pokemon):

        def __init__(self):
            super().__init__("Bulbasauro", "Planta", 100)

    pikachu2 = Pikachu()

    bulbasauro2 = Bulbasauro()
    bulbasauro2.atacar()
    bulbasauro2.evoluir()