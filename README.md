# Hundir la flota:

Este proyecto implementa el clásico juego Hundir la Flota (Battleship) en Python, ejecutable desde el terminal (ejecutando el fichero *main.py*).

El jugador compite contra la máquina en un tablero de 10x10, colocando sus barcos manualmente y disparando por turnos hasta hundir toda la flota rival o quedarse sin vidas.

## Características:

- Juego por turnos: el jugador y la máquina alternan disparos.

- Colocación manual y aleatoria:

- El jugador coloca sus barcos indicando orientación y posición.

- La máquina coloca los suyos de forma aleatoria.

- Tableros separados para jugador y rival, con un tablero visible que muestra los aciertos (X) y los disparos al agua (A).

- Cada fallo resta una vida; si llegas a cero, pierdes la partida.

## Reglas del juego:

- El jugador coloca sus barcos uno a uno indicando:

    - Orientación (H = horizontal, V = vertical)

    - Coordenadas de la popa (esquina izquierda/superior del barco)

- El rival coloca sus barcos de forma aleatoria.

- En tu turno:

    - Introduce coordenadas vertical y horizontal para disparar: X = acierto, A = agua.

- Pierdes si te quedas sin vidas o si te hunden todos los barcos.

## Requerimientos:
- Numpy.
