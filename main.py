import random
import utils

# Esloras de los barcos con los que se va a jugar.
eslora_flotas = [2,2,2,3,3,4]

# Listas en las que almacenar listas con las posiciones de los barcos
flota_jugador = []
flota_enemigo = []

# Tableros:
tablero_jugador = utils.crear_tablero()
tablero_enemigo = utils.crear_tablero()
tablero_visible_jugador = utils.crear_tablero()

# Opcional: solo para ver los disparos que va haciendo el ordenador
tablero_visible_enemigo = utils.crear_tablero()

vidas_jugador = 5
vidas_enemigo = 5

# Crear los barcos y las flotas de ambos jugadores
for eslora in eslora_flotas:
    barco = {"eslora": eslora}
    utils.crear_barco(barco, flota_jugador, tablero_jugador)
    # Los barcos son diccionarios, solo haremos append con sus posiciones
    flota_jugador.append(barco["posiciones"])

for eslora in eslora_flotas:
    barco = {"eslora": eslora}
    utils.crear_barco_random(barco, flota_enemigo, tablero_enemigo)
    flota_enemigo.append(barco["posiciones"])

# En estos dos sets almacenamos las posiciones de los barcos de ambos jugadores.
# Posteriormente, cuando un disparo acierte, se quitará del set
posiciones_enemigas = {tuple(par) for barco in flota_enemigo for par in barco}
posiciones_jugador = {tuple(par) for barco in flota_jugador for par in barco}

# La variable turno sirve para decidir el turno del jugador.
# Si es True, será el turno del jugador y viceversa.
turno = random.choice([True, False])

while vidas_jugador > 0 and vidas_enemigo > 0:
    
    # Turno jugador
    while turno:
        print("Tu turno:\t")
        
        # Solicitar el input para las coordenadas del disparo.
        iv = int(input("Introduce la coordenada vertical del disparo:\t"))
        ih = int(input("\nIntroduce la coordenada horizontal del disparo:\t"))
        casilla = [iv, ih]
        
        acierto = utils.disparar(casilla, tablero_enemigo, tablero_visible_jugador)
        if acierto:
            # Tras acertar, eliminar la posición del set de barcos enemigo,
            # y comprobar si quedan barcos por hundir.
            posiciones_enemigas.remove(tuple(casilla))
            if len(posiciones_enemigas) == 0:
                print("¡VICTORIA! Has eliminado la flota enemiga")
                break # Terminar turno del jugador y...
        
        if not acierto:
            # Perder vida y ceder turno.
            vidas_jugador -= 1 # Perdemos vida
            turno = False
    if len(posiciones_enemigas) == 0:
        victoria = True # True si gana el jugador
        break # ... salir del bucle while
    
    # Turno enemigo
    while not turno:
        print("Turno rival:\n")
        iv = random.randrange(utils.n)
        ih = random.randrange(utils.n)
        casilla = [iv, ih]
        acierto = utils.disparar(casilla, tablero_jugador)
        if acierto:
            posiciones_jugador.remove(tuple(casilla))
            if len(posiciones_jugador) == 0:
                print("¡DERROTA! La Armada Imperial Japonesa ha vencido")
                break
        if not acierto:
            vidas_enemigo -= 1
            turno = True
    if len(posiciones_jugador) == 0:
        victoria = False
        break

# Resultado del juego
if victoria: print("¡VICTORIA! La US Navy ha mandado a pique a la Teikoku Kaigun")
else: print("¡DERROTA! La Esfera de Coprosperidad de la Gran Asia Oriental "
            "se extenderá a toda Asia.")