import numpy as np
import random
n = 10
ontzi = {"eslora": 3}

def crear_tablero(n=10):
    """Función para crear tablero. Argumentos:
        - n(=10): lado del cuadrado"""
    return np.full((n,n), '_')
# =============================================================================
# Crear flota JUGADOR
# =============================================================================
def _fijar_barco(barco: dict):
    print("\n")
    print(f"Fija la posición del siguiente barco. Eslora: {barco['eslora']}")

    heading = ''
    while not(heading in {'H', 'V'}):
        heading = input("Introduce la orientación del barco. 'H' para"
                        " horizontal y 'V' para vertical:\t")
    print("\nIntroduce la popa del barco. Si la orientación es 'H' o 'V',"
          " la popa corresponde al extremo izquierdo/superior del barco, "
          "respectivamente.\n")
    
    i, j = -n, -n
    while not(0<= i < n):
        i = int(input("Introduce la coordenada vertical de la popa del barco:\t"))
    while not(0<= j < n):
        j = int(input("Introduce la coordenada horizontal de la popa del barco:\t"))
    
    return heading, [i, j]

def _posiciones_barco(barco: dict, popa: list):
    longitud = barco["eslora"]
    barco["posiciones"] = [popa]
    if barco["heading"] == 'H':
        for i in range(1, longitud):
            barco["posiciones"].append([popa[0], popa[1] + i])
    elif barco["heading"] == 'V':
        for i in range(1, longitud):
            barco["posiciones"].append([popa[0] + i, popa[1]])
    

def _check_barco(barco: dict):
    """Comprobar que las posiciones de un barco están dentro del tablero"""    
    
    booleano = True
    
    for elem in barco["posiciones"]:
        ix, iy = elem
        if (0 <= ix < n) and (0 <= iy < n):
            continue
        else:
            booleano = False
            break
    
    return booleano
    
    
def _check_flota(barco:dict, flota: list):

    posiciones_flota = {tuple(pair) for ship in flota for pair in ship}
    posiciones_barco = {tuple(elem) for elem in barco["posiciones"]}
    if posiciones_flota.isdisjoint(posiciones_barco): booleano = True
    else: booleano = False
    return booleano

def colocar_barco(barco: list, tablero):
    """Función para colocar un barco en el tablero. Argumentos:
        - tablero: tablero de juego
        - barco (lista): lista de [i, j] que contienen los índices
        de cada componente del barco
        
        OJO: el tablero introducido en el argumento se ve afectado"""
    for elem in barco:
        i, j = elem
        tablero[i, j] = 'O'

def crear_barco(barco: dict, flota: list, board):
    heading, popa = _fijar_barco(barco)
    barco["heading"] = heading
    _posiciones_barco(barco, popa)
    while not(_check_barco(barco) and _check_flota(barco, flota)):
        heading, popa = _fijar_barco(barco)
        barco["heading"] = heading
        _posiciones_barco(barco, popa)
    colocar_barco(barco["posiciones"], board)
    print(board)
# =============================================================================
# Crear flota de barcos ordenador
# =============================================================================
def _fijar_barco_random(barco: dict):
    
    heading = random.choice(['H','V'])
    
    iv = random.randrange(n)
    ih = random.randrange(n)
    if heading == 'H':
        while iv >= n - barco["eslora"]:
            iv = random.randrange(n)
    else:
        while ih >= n - barco["eslora"]:
            ih = random.randrange(n)
    popa = [iv, ih]
    
    return heading, popa

def crear_barco_random(barco, flota, board): # Esta función es casi igual
# que la otra
    heading, popa = _fijar_barco_random(barco)
    barco["heading"] = heading
    _posiciones_barco(barco, popa)
    while not(_check_barco(barco) and _check_flota(barco, flota)):
        heading, popa = _fijar_barco_random(barco)
        barco["heading"] = heading
        _posiciones_barco(barco, popa)
    colocar_barco(barco["posiciones"], board)
    print(board)
# =============================================================================
# 
# =============================================================================

def disparar(casilla: list, tablero_enemigo, tablero_visible=None):
    """Funciona! Tanto con tablero_visible (turno jugador) como
    sin él (turno enemigo)"""
    i, j = casilla
        
    if not (tablero_visible is None):
        if tablero_visible[i, j] not in {'A', 'X'}:
            if tablero_enemigo[i, j] == 'O':
                print("¡Barco enemigo alcanzado!")
                tablero_visible[i, j] = 'X'
                return True
            elif tablero_enemigo[i, j] == '_':
                print("Disparo fallido.")
                tablero_visible[i, j] = 'A'
                return False
        else:
            print("Has disparado a una casilla a la que ya has disparado, ¡CAZURRO!\n")
            return False
    else:
        if tablero_enemigo[i, j] == 'O':
            print("¡Barco enemigo alcanzado!")
            return True
        elif tablero_enemigo[i, j] == '_':
            print("Disparo fallido.")
            return False