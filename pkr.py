import random
import math

class Carta:
    def __init__(self, valor, palo, mostrando=True):
        self.valor = valor
        self.palo = palo
        self.mostrando = mostrando

    def __repr__(self):
        nombre_valor = ["Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve", "Diez", "Jota", "Reina", "Rey", "As"]
        nombre_palo = ["Diamantes", "Tréboles", "Corazones", "Espadas"]
        if self.mostrando:
            return f"{nombre_valor[self.valor]} de {nombre_palo[self.palo]}"
        else:
            return "[CARTA]"

class Baraja:
    def __init__(self):
        self.cartas = []
        self.nueva_baraja()

    def nueva_baraja(self):
        self.cartas = []
        for valor in range(13):
            for palo in range(4):
                self.cartas.append(Carta(valor, palo))
        random.shuffle(self.cartas)

    def repartir_mano(self, num_cartas):
        if not self.cartas:
            print("¡Se han agotado las cartas! Creando una nueva baraja...")
            self.nueva_baraja()
        mano = []
        for _ in range(num_cartas):
            mano.append(self.cartas.pop())
        return mano

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

    # Resto del código de evaluación de mano

    return "High Card", valores

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    if curDepth == targetDepth:
        return scores[nodeIndex]
    if maxTurn:
        return max(minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth))
    else:
        return min(minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth))

def obtener_mejor_mano(manos_jugadores, flop):
    scores = [valores_mano for _, valores_mano in manos_jugadores.values()]
    treeDepth = math.log(len(scores), 2)
    optimal_value = minimax(0, 0, True, scores, treeDepth)
    return optimal_value


# Ejemplo de uso:
def main():
    baraja = Baraja()
    baraja.mezclar()

    # Limitar a 3 rondas y 5 jugadores por ronda
    num_rondas = 3
    num_jugadores = 5

    # Iterar sobre cada ronda
    for ronda in range(num_rondas):
        print(f"Ronda {ronda + 1}:")
        print("---------")

        # Repartir las cartas comunitarias ("el flop")
        flop = baraja.repartir_mano(3)

        print("Cartas comunitarias (el flop):")
        for carta in flop:
            print(carta)

        # Repartir las manos de cada jugador
        manos_jugadores = {}

        # Verificar si hay suficientes cartas antes de repartir
        if len(baraja.cartas) >= num_jugadores * 2:
            jugadores = [f"Jugador {i}" for i in range(1, num_jugadores + 1)]
            manos_jugadores = {jugador: baraja.repartir_mano(2) for jugador in jugadores}
        else:
            print("No hay suficientes cartas en la baraja para repartir a todos los jugadores.")

        # Mostrar las manos de cada jugador y su mejor mano
        for jugador, mano in manos_jugadores.items():
            print(f"\n{jugador}:")
            print("Cartas en mano:")
            for carta in mano:
                print(carta)
            mejor_mano, valores_mano = evaluar_mano(mano + flop)
            print("Mejor mano:", mejor_mano)
            print("Valores de la mano:", valores_mano)

        print("\n---------\n")

if __name__ == "__main__":
    main()
