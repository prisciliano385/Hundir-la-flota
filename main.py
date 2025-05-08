import random
import utils

eslora_flotas = [2,2,2,3,3,4]

flota_jugador = []
flota_enemigo = []
lista_prueba = []

tablero_jugador = utils.crear_tablero()
tablero_enemigo = utils.crear_tablero()
tablero_visible_jugador = utils.crear_tablero()

vidas_jugador = 5
vidas_enemigo = 5

for eslora in eslora_flotas:
    barco = {"eslora": eslora}
    utils.crear_barco(barco, flota_jugador, tablero_jugador)
    flota_jugador.append(barco["posiciones"])

for eslora in eslora_flotas:
    barco = {"eslora": eslora}
    utils.crear_barco_random(barco, flota_enemigo, tablero_enemigo)
    flota_enemigo.append(barco["posiciones"])
    # No podemos hacer .extend(barco["posiciones"]), dentro de utils.crear_barco()
    # se itera la lista flota_enemigo en dos bucles: una por posiciones_barco y
    # luego posiciones

# En posiciones_enemigas almacenaremos las posiciones en un set.
# Posteriormente, cuando un disparo acierte, se quitará del set
posiciones_enemigas = {tuple(par) for barco in flota_enemigo for par in barco}
posiciones_jugador = {tuple(par) for barco in flota_jugador for par in barco}

turno = True # Comienza el jugador

while vidas_jugador > 0 and vidas_enemigo > 0:
    # Turno jugador
    while turno:
        print("Tu turno:\t")
        iv = int(input("Introduce la coordenada vertical del disparo:\t"))
        ih = int(input("\nIntroduce la coordenada horizontal del disparo:\t"))
        casilla = [iv, ih]
        acierto = utils.disparar(casilla, tablero_enemigo, tablero_visible_jugador)
        if acierto:
            # remove da error si casilla no está en el set
            posiciones_enemigas.remove(tuple(casilla))
            if len(posiciones_enemigas) == 0:
                print("¡VICTORIA! Has eliminado la flota enemiga")
                break # Se ha
        if not acierto:
            vidas_jugador -= 1 # Perdemos vida
            turno = False
    if len(posiciones_enemigas) == 0:
        victoria = True # True si gana el jugador
        break
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

if victoria: print("¡VICTORIA! La US Navy ha mandado a pique a la IJN")
else: print("¡DERROTA! Asia para los japoneses")
    
        
        