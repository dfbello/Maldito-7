# Maldito 7

Es un juego donde los jugadores lanzan dos dados de 6 caras, cada jugador tiene un tablero con 11 casillas enumeradas del 1 al 12 excluyendo el 7.

## Reglas
* El primer jugador es determinado por el desempate de un dado
* En un turno individual el jugador lanza los dados, el número que sale es cubierto por el jugador en su tablero, el jugador lanza los dados hasta que el número que salga ya esté cubierto por él, es turno del siguiente jugador que no tenga ese número en su tablero en orden anti-horario.
* Cuando un jugador lanza el número 7 debe añadir una cantidad previamente acordada a la bolsa de premio y pierde su turno.
* Gana el jugador que primero complete los números en su tablero.

## Estructura
**Dados:** Controlan la logica de los dados, existen un par de dados comunes para toda la partida.
**Jugador:** El jugador actual y su tablero son manejados en esta clase, puede llevar un contador de perdidas en la partida actual-
**Partida:** Controla el flujo de los turnos, la bolsa de premios.
**Config:** Controla la carga y uso de configuración
**Main:** Maneja el menú principal, selección de la configuración de la partida, y el loop principal.

### Configuración (Conservar última usada en un archivo para fácil reinicio de la partida)
1. Número de jugadores
1. Nombres de los jugadores
1. Apuesta inicial
1. Cace por 7
1. Color de los jugadores (Opcional)


