from match import Match
from player import Player
from dice import Dice

def set_up_match(dev_mode=False):
    print("🔧 Configuración de la partida 🔧")

    # Set up the number of players
    while True:
        try:
            player_num = int(input("Ingrese el número de jugadores: "))
            if player_num > 1:
                break
        except ValueError:
            pass
        print("❌ Entrada inválida. Intente nuevamente.")

    # Configurar nombres y colores de los jugadores
    players = []
    for i in range(player_num):
        name = input(f"Ingrese el nombre del jugador {i + 1}: ")
        players.append(Player(name))

    # Crear dados y partida
    dice = Dice(dev=dev_mode)
    match = Match(players, 1000, 100, dice)

    return match

def main_menu(dev_mode=False):
    print("\n🔹 Menú Principal 🔹")
    opcion = None
    while not opcion:
        print("1. Iniciar nueva partida")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        try: 
            if int(opcion) in [1,2]:
                break
        except ValueError:
            print("❌ Opción inválida. Intente nuevamente.")
            opcion = None    
        else:
            print("❌ Opción inválida. Intente nuevamente.")
            opcion = None

    if opcion == "1":
        match = set_up_match(dev_mode)
        while match.in_play:
            match.play()
    elif opcion == "2":
        print("👋 ¡Gracias por jugar! Hasta luego.")

if __name__ == "__main__":
    main_menu(dev_mode=False)