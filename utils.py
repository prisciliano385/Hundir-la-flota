import numpy as np

n = 10

barco1 = {
        "tipo": "Acorazado",
        "clase": "Yamato",
        "eslora": 4,
        "heading": None,
        "posiciones": None,
        }

barco2 = {
        "tipo": "Crucero",
        "clase": "Mogami",
        "eslora": 3,
        "heading": None,
        "posiciones": None,
        }

barco3 = {
        "tipo": "Acorazado",
        "clase": "Nagato",
        "eslora": 4,
        "heading": None,
        "posiciones": None,
        }

# flota1 = [barco1]
flota2 = [barco1, barco2, barco3]

def crear_tablero(n=10):
    """Función para crear tablero. Argumentos:
        - n(=10): lado del cuadrado"""
    return np.full((n,n), '_')

def colocar_barco(tablero, barco: list):
    """Función para colocar un barco en el tablero. Argumentos:
        - tablero: tablero de juego
        - barco (lista): lista de [i, j] que contienen los índices
        de cada componente del barco
        
        OJO: el tablero introducido en el argumento se ve afectado"""
    for elem in barco:
        i, j = elem
        tablero[i, j] = 'O' # Si hiciésemos tablero[i,j] = ... afectaría a tablero fuera de la función

def disparar(casilla: list, tablero):
    assert len(casilla) == 2, f"{len(casilla)=} es distinta de 2"
    i, j = casilla
    if tablero[i, j] == 'O':
        print("¡Barco enemigo alcanzado!")
        tablero[i, j] = 'X'
    elif tablero[i, j] == '_':
        print("Disparo fallido.")
        tablero[i, j] = 'A'
    return tablero
# =============================================================================
# 
# =============================================================================
def _fijar_barco(barco: dict):
    print("\n")
    print(f"Barco: {barco['tipo']} {barco['clase']}. Eslora: {barco['eslora']}")

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
    
    assert len(barco["posiciones"]) == longitud, f"{longitud=} != longitud barco"
    f"{len(barco['posiciones'])=}"

def _check_barco(barco: dict):
    """Comprobar que las posiciones de un barco están dentro del tablero"""
    
    assert not barco["posiciones"] is None, f"{barco['posiciones']=}: no se ha definido la lista de posiciones del barco."
    assert barco["eslora"] == len(barco["posiciones"]), f"{barco['eslora']=} != longitud del barco"
    
    booleano = True
    
    for elem in barco["posiciones"]:
        ix, iy = elem
        if (0 <= ix < n) and (0 <= iy < n):
            continue
        else:
            booleano = False
            break
    
    return booleano
    
    
def _coincidir_barco(flota: list):
    posiciones = set()
    booleano = True
    for barco in flota:
        if not(barco["posiciones"] is None):
            new_list = [tuple(elem) for elem in barco["posiciones"]]
            new_set = set(new_list)
            if posiciones.isdisjoint(new_set):
                posiciones.update(new_set)
            else:
                booleano = False
        else:
            continue
    return booleano

# =============================================================================
# 
# =============================================================================

def _crear_flota(flota: list):
    board = crear_tablero()
    for barco in flota:
        heading, popa = _fijar_barco(barco)
        barco["heading"] = heading
        _posiciones_barco(barco, popa)
        print(f"{_check_barco(barco)=}")
        print(f"{_coincidir_barco(flota)=}")
        while not(_check_barco(barco) and _coincidir_barco(flota)):
            heading, popa = _fijar_barco(barco)
            barco["heading"] = heading
            _posiciones_barco(barco, popa)
        colocar_barco(board, barco["posiciones"])
        print(board)

