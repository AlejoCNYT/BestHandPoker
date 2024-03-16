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
            nombres_valores = {0: "Dos", 1: "Tres", 2: "Cuatro", 3: "Cinco", 4: "Seis", 5: "Siete",
                               6: "Ocho", 7: "Nueve", 8: "Diez", 9: "Jota", 10: "Reina", 11: "Rey", 12: "As"}
            nombres_palos = {0: "Diamantes", 1: "Tréboles", 2: "Corazones", 3: "Espadas"}
            nombre_valor = nombres_valores[self.valor]
            nombre_palo = nombres_palos[self.palo]
            return f"{nombre_valor} de {nombre_palo}"
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

    # Verificar si hay un royal flush, straight flush, four of a kind, full house, flush, straight,
    # three of a kind, two pair, pair o high card
    # Implementa la lógica de evaluación de manos aquí...

    # Por simplicidad, aquí se devuelve siempre "High Card"
    return "High Card", valores

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []

def main():
    baraja = Baraja()
    baraja.mezclar()

    jugadores = [Jugador(f"Jugador {i}") for i in range(1, 6)]  # Creamos 5 jugadores en total

    # Repartir manos a cada jugador
    for jugador in jugadores:
        jugador.mano = baraja.repartir_mano(5)

    # Mostrar las manos de cada jugador y evaluarlas
    for jugador in jugadores:
        print(jugador.nombre + ":")
        for carta in jugador.mano:
            print(carta)
        mejor_mano, valores_mano = evaluar_mano(jugador.mano)
        print("Mejor mano:", mejor_mano)
        print("Valores de la mano:", valores_mano)
        print()

if __name__ == "__main__":
    main()
