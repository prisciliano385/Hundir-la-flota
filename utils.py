import numpy as np
import random

# Tamaño estándar del tablero
n = 10

def crear_tablero(n=10):
    """Función para crear tablero. Argumentos:
        - n(=10): lado del cuadrado.
        
        Return: Numpy array n x n lleno de '_'."""
    return np.full((n,n), '_')
# =============================================================================
# Crear flota JUGADOR
# =============================================================================
def _fijar_barco(barco: dict):
    """Fija los parámetros básicos de un barco. Argumentos:
        - barco (dict): solo necesita la key 'eslora'.
        
        Return:
            - heading (char): 'H' o 'V' (horizontal o vertical respectivamente).
            - popa (list, int): índices de la popa del barco."""
    
    print("\n")
    print(f"Fija la posición del siguiente barco. Eslora: {barco['eslora']}")

    heading = ''
    while not(heading in {'H', 'V'}):
        heading = input("\nIntroduce la orientación del barco. 'H' para"
                        " horizontal y 'V' para vertical:\t")
    
    print("\nIntroduce la popa del barco. Si la orientación es 'H' o 'V',"
          " la popa corresponde al extremo izquierdo/superior del barco, "
          "respectivamente.\n")
    while True:
        try:
            popa = input("Introduce las coordenadas vertical y horizontal de la popa"
                         " SEPARADAS por una coma:\t")
            popa = [int(index) for index in popa.split(",")]
            booleano1 = all(isinstance(index, int) for index in popa)
            booleano2 = all(0 <= index < n for index in popa)
            if booleano1 and booleano2:
                break
            elif booleano1 and not booleano2:
                print("\nIntroduce valores correctos. Los índices deben estar entre"
                      f" 0 y {n}.")
        except:
            print("\nIntroduce valores correctos. Los índices deben estar entre"
                  f"0 y {n}.")
    return heading, popa

def _posiciones_barco(barco: dict, popa: list):
    """Fija las posiciones de un barco. Argumentos:
        - barco (dict): keys del barco ('eslora', 'heading')
        - popa (list(int)): índices de la popa del barco"""
    longitud = barco["eslora"]
    barco["posiciones"] = [popa]
    if barco["heading"] == 'H':
        for i in range(1, longitud):
            barco["posiciones"].append([popa[0], popa[1] + i])
    elif barco["heading"] == 'V':
        for i in range(1, longitud):
            barco["posiciones"].append([popa[0] + i, popa[1]])
    

def _check_barco(barco: dict):
    """Comprobar que las posiciones de un barco están dentro del tablero.
    Argumentos:
        - barco(dict): keys ('eslora','heading','posiciones')
    Return:
        - booleano(bool): True si está dentro, False si no lo está"""    
    
    booleano = True # retorna True si el barco está dentro del tablero
    
    for elem in barco["posiciones"]:
        ix, iy = elem
        if (0 <= ix < n) and (0 <= iy < n):
            continue
        else:
            booleano = False # retorna False si el barco está fuera
            break
    
    return booleano
    
    
def _check_flota(barco:dict, flota: list):
    """Comprueba si un barco se solapa con los otros barcos de una flota.
    Debe ser llamada cada vez que un barco vaya a ser añadido a la flota.
    Argumentos:
        - barco(dict): keys ('posiciones')
        - flota (list(list)): una lista de listas. Cada una de las listas
        corresponde a las posiciones de un barco.
    Return:
        - booleano(bool): True si no se solapan, False si lo hacen"""
    
    # Creamos un set en el que almacenar las posiciones individuales de los
    # barcos de la flota
    posiciones_flota = {tuple(pair) for ship in flota for pair in ship}
    
    # Creamos otro set en el que almacenar las posiciones del barco candidato
    posiciones_barco = {tuple(elem) for elem in barco["posiciones"]}
    
    # Comprobar si ambos set tienen algún elemento en común. Si no es así,
    # el método isdisjoint() retorna True
    if posiciones_flota.isdisjoint(posiciones_barco): booleano = True
    else: booleano = False
    return booleano

def colocar_barco(barco: list, tablero):
    """Función para colocar un barco en el tablero. Argumentos:
        - tablero: tablero sobre el que marcar las posiciones del barco
        - barco (lista): lista con las posiciones del barco
        de cada componente del barco.
        Return:
            - Nada. Pero ALTERA el tablero."""
    for elem in barco:
        i, j = elem
        tablero[i, j] = 'O'

def crear_barco(barco: dict, flota: list, board):
    """Función que agrupa a las anteriores, crea un barco y lo marca en el
    tablero del jugador. Argumentos:
        - barco(dict): key('eslora').
        - flota(list): lista de listas, cada una con las posiciones de un
        barco.
        - board: tablero del jugador.
        Return: ninguno, pero altera el dict barco y el tablero"""
    
    # Obtener la orientación y la popa del barco:
    heading, popa = _fijar_barco(barco)
    
    # Guardar orientación en el diccionario del barco
    barco["heading"] = heading
    
    # Guardar posiciones del barco en el diciconario
    _posiciones_barco(barco, popa)
    
    # Asegurar que el barco creado está dentro del tablero y no se sobrepone
    # a otros barcos.
    while not(_check_barco(barco) and _check_flota(barco, flota)):
        heading, popa = _fijar_barco(barco)
        barco["heading"] = heading
        _posiciones_barco(barco, popa)
    
    # Añadir barco al tablero e imprimirlo
    colocar_barco(barco["posiciones"], board)
    print(board)


# =============================================================================
# Crear flota de barcos ordenador
# =============================================================================
def _fijar_barco_random(barco: dict):
    """Genera la orientación y la popa de un barco al azar. Argumentos:
        - barco(dict): key('eslora').
        Return:
            - heading('H' o 'V'), popa(lista de índices)"""
    # Escoger una orientación al azar
    heading = random.choice(['H','V'])
    
    # Escoger índices al azar
    iv = random.randrange(n)
    ih = random.randrange(n)
    
    # Repetir hasta que el barco quepa dentro del tablero
    if heading == 'H':
        while iv >= n - barco["eslora"]:
            iv = random.randrange(n)
    else:
        while ih >= n - barco["eslora"]:
            ih = random.randrange(n)
    popa = [iv, ih]
    
    return heading, popa

def crear_barco_random(barco: dict, flota: list, board):
    """Crea un barco al azar y lo coloca en el tablero del jugador. Argumentos:
        - barco(dict): key('eslora').
        - flota(list): lista de listas con las posiciones de los barcos de la
        flota.
        - board: tablero del jugador.
        Return: ninguno, pero modifica el diccionario barco y el tablero del jugador."""
    
    # Generar la orientación y la posición de la popa del barco.
    heading, popa = _fijar_barco_random(barco)
    barco["heading"] = heading
    
    # Generar posiciones del barco
    _posiciones_barco(barco, popa)
    
    # Comprobar que el barco esté dentro del tablero y que no se solape con otros
    # barcos de la flota
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
    """Función para seguir la cuenta de los disparos. Argumentos:
        - casilla(lista): blanco del disparo
        - tablero_enemigo: comprueba si en el blanco hay un barco o no.
        - tablero_visible(=None): si no es None, marcará los disparos del jugador
        en un tablero, sean aciertos o caigan en el agua. Si =None, no marcará
        los intentos de disparo en un tablero (está pensado para el jugador de
        la máquina).
        Return:
            - booleano: True si ha acertado, False si falla.
            - Altera el tablero visible."""
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