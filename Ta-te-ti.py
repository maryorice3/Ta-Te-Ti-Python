def mostrar_tablero(tablero):
    print("Tablero:")
    for i in range(3):
        print(tablero[i][0], "|", tablero[i][1], "|", tablero[i][2])
        if i < 2:
            print("---------")

def verificar_ganador(tablero, jugador):
    # Comprobar filas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == jugador:
            return True

    # Comprobar columnas
    for j in range(3):
        if tablero[0][j] == tablero[1][j] == tablero[2][j] == jugador:
            return True

    # Comprobar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True

    return False

def jugar_tateti():
    tablero = [[' ' for _ in range(3)] for _ in range(3)]
    jugador_actual = 'X'

    while True:
        mostrar_tablero(tablero)
        print("Turno del jugador", jugador_actual)

        fila = int(input("Ingrese la fila (0, 1, 2): "))
        columna = int(input("Ingrese la columna (0, 1, 2): "))

        if tablero[fila][columna] != ' ':
            print("Esa casilla ya está ocupada. Intente nuevamente.")
            continue

        tablero[fila][columna] = jugador_actual

        if verificar_ganador(tablero, jugador_actual):
            mostrar_tablero(tablero)
            print("¡El jugador", jugador_actual, "ha ganado!")
            break

        if all(tablero[i][j] != ' ' for i in range(3) for j in range(3)):
            mostrar_tablero(tablero)
            print("El juego ha terminado en empate.")
            break

        jugador_actual = 'O' if jugador_actual == 'X' else 'X'
jugar_tateti()