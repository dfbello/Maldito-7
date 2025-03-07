# Maldito 7

Un juego donde el lanzamiento de los dados determina al ganador, con algunos pasos extra. Perfecto para los adictos a las apuestas (es broma).

## Reglas
* Cada jugador tiene un tablero con números del 2 al 12 inclusive, excluyendo el número siete. El objetivo es marcar todos los números en tu tablero. El primer jugador en lograrlo es el ganador.
* El jugador inicial se determina lanzando un solo dado.
* En su turno, el jugador presiona `ENTER` para lanzar los dados. Llamaremos a la suma de los dados `tirada`. Cuando `tirada` no está marcada en el tablero del jugador actual, se marca.
* Cuando el jugador ya ha marcado el valor de `tirada`, el turno pasa al siguiente jugador que no haya marcado ese valor en su tablero.
* Si `tirada` es igual a 7, el jugador añade una cantidad de dinero predefinida al bote del premio.

## Ejecución
Con el código fuente en un directorio de tu elección, ejecuta en la terminal:
```bash
python main.py
```

### Desarrollo futuro
* Reiniciar el juego después de que haya un ganador.
* Tal vez algunos identificadores de color para los jugadores.
* Algo relacionado con la actualización de la terminal en lugar de imprimir nuevas líneas.
