def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 9)


def verificar_ganador(tablero):
    # Verifica filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != ' ':
            return tablero[i][0]
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != ' ':
            return tablero[0][i]

    # Verifica diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != ' ':
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != ' ':
        return tablero[0][2]

    return None


def juego():
    tablero = [[' ' for _ in range(3)] for _ in range(3)]
    jugador = 'X'

    while True:
        imprimir_tablero(tablero)
        fila = int(input(f"Jugador {jugador}, elige fila (0, 1, 2): "))
        columna = int(input(f"Jugador {jugador}, elige columna (0, 1, 2): "))

        if tablero[fila][columna] != ' ':
            print("Esa casilla ya está ocupada. Intenta de nuevo.")
            continue

        tablero[fila][columna] = jugador

        ganador = verificar_ganador(tablero)
        if ganador:
            imprimir_tablero(tablero)
            print(f"¡El jugador {ganador} ha ganado!")
            break

        if all(all(c != ' ' for c in fila) for fila in tablero):
            imprimir_tablero(tablero)
            print("¡Empate!")
            break

        jugador = 'O' if jugador == 'X' else 'X'


if __name__ == "__main__":
    juego()