"""
Programação Orientada a Objetos

Composição
Composição ocorre quando uma classe compõe ou é composta por uma ou mais classes.

"""
object
class Carta(object):
    def __init__(self, naipe, valor) -> None:
        self._naipe = naipe
        self._valor = valor

    def __repr__(self) -> str:
        return f"{self._valor}{self._naipe}"
    
    def __str__(self) -> str:
        return f"{self._valor}{self._naipe}"

class Baralho:
    
    def __init__(self) -> None:
        self._lista_de_cartas = []

        self._valores = [
            "2", "3", "4", "5", "6", "7", "8", "9", "10",
            "J", "Q", "K", "A"
        ]

        self._naipes = {
            "\u2660", "\u2665", "\u2666", "\u2663"
        }

        self._construir()

    def __repr__(self) -> str:
        return ", ".join([str(carta) for carta in self._lista_de_cartas])

    def _construir(self):
        for valor in self._valores:
            for naipe in self._naipes:
                self._lista_de_cartas.append(Carta(naipe, valor))

if __name__ == "__main__":
    baralho = Baralho()
    print(baralho)