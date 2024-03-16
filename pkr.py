import random


class Carta:
    def __init__(self, valor, palo, mostrando=True):
        self.valor = valor
        self.palo = palo
        self.mostrando = mostrando

    def __repr__(self):
        nombre_valor = ""
        nombre_palo = ""
        if self.mostrando:
            if self.valor == 0:
                nombre_valor = "Dos"
            elif self.valor == 1:
                nombre_valor = "Tres"
            elif self.valor == 2:
                nombre_valor = "Cuatro"
            elif self.valor == 3:
                nombre_valor = "Cinco"
            elif self.valor == 4:
                nombre_valor = "Seis"
            elif self.valor == 5:
                nombre_valor = "Siete"
            elif self.valor == 6:
                nombre_valor = "Ocho"
            elif self.valor == 7:
                nombre_valor = "Nueve"
            elif self.valor == 8:
                nombre_valor = "Diez"
            elif self.valor == 9:
                nombre_valor = "Jota"
            elif self.valor == 10:
                nombre_valor = "Reina"
            elif self.valor == 11:
                nombre_valor = "Rey"
            elif self.valor == 12:
                nombre_valor = "As"
            if self.palo == 0:
                nombre_palo = "Diamantes"
            elif self.palo == 1:
                nombre_palo = "Tréboles"
            elif self.palo == 2:
                nombre_palo = "Corazones"
            elif self.palo == 3:
                nombre_palo = "Espadas"
            return nombre_valor + " de " + nombre_palo
        else:
            return "[CARTA]"


class Baraja:
    def __init__(self):
        self.cartas = []
        for valor in range(13):
            for palo in range(4):
                self.cartas.append(Carta(valor, palo))

    def mezclar(self):
        random.shuffle(self.cartas)

    def repartir_mano(self, num_cartas):
        mano = []
        for _ in range(num_cartas):
            mano.append(self.cartas.pop())
        return mano


def evaluar_mano(mano):
    valores = [carta.valor for carta in mano]
    palos = [carta.palo for carta in mano]

    valores.sort(reverse=True)  # Ordenar los valores de las cartas de mayor a menor

    # Verificar si hay un royal flush
    if valores == [12, 11, 10, 9, 8] and len(set(palos)) == 1:
        return "Royal Flush", valores

    # Verificar si hay un straight flush
    if len(set(palos)) == 1 and valores[0] - valores[-1] == 4 and len(set(valores)) == 5:
        return "Straight Flush", valores

    # Verificar si hay un four of a kind
    for valor in set(valores):
        if valores.count(valor) == 4:
            return "Four of a Kind", [valor]

    # Verificar si hay un full house
    if len(set(valores)) == 2 and (valores.count(valores[0]) == 3 or valores.count(valores[0]) == 2):
        return "Full House", [valores[0], valores[-1]]

    # Verificar si hay un flush
    if len(set(palos)) == 1:
        return "Flush", valores

    # Verificar si hay un straight
    if valores[0] - valores[-1] == 4 and len(set(valores)) == 5:
        return "Straight", valores

    # Verificar si hay un three of a kind
    for valor in set(valores):
        if valores.count(valor) == 3:
            return "Three of a Kind", [valor]

    # Verificar si hay un two pair
    pares = [valor for valor in set(valores) if valores.count(valor) == 2]
    if len(pares) == 2:
        return "Two Pair", sorted(pares, reverse=True) + [valor for valor in valores if valor not in pares]

    # Verificar si hay un pair
    for valor in set(valores):
        if valores.count(valor) == 2:
            return "Pair", [valor] + [val for val in valores if val != valor]

    # Si no se cumple ninguna de las condiciones anteriores, la mejor mano es High Card
    return "High Card", valores


# Ejemplo de uso:
def main():
    baraja = Baraja()
    baraja.mezclar()

    # Crear jugadores
    jugadores = [f"Jugador {i}" for i in range(1, 5)]
    manos_jugadores = {jugador: baraja.repartir_mano(2) for jugador in jugadores}

    # Repartir las cartas comunitarias ("el flop")
    flop = baraja.repartir_mano(3)

    print("Cartas comunitarias (el flop):")
    for carta in flop:
        print(carta)

    # Mostrar las manos de cada jugador y su mejor mano
    for jugador, mano in manos_jugadores.items():
        print(f"{jugador}:")
        print("Cartas en mano:")
        for carta in mano:
            print(carta)
        mejor_mano, valores_mano = evaluar_mano(mano + flop)
        print("Mejor mano:", mejor_mano)
        print("Valores de la mano:", valores_mano)
        print()


if __name__ == "__main__":
    main()
