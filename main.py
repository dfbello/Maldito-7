from match import Match
from player import Player
from dice import Dice

def set_up_match(dev_mode=False, auto_mode=False): # Auto mode and dev mode have to be mutually exclusive if one is active
    print("\n🔧 Configuración de la partida 🔧\n")

    # Set up the initial bet
    while True:
        try:
            initial_bet = int(input("Ingrese el cace inicial [500,): "))
            if initial_bet >= 500:
                break
        except ValueError:
            pass
        print("❌ Entrada inválida. Intente nuevamente.")

    # Set up the cace
    while True:
        try:
            cace = int(input("Ingrese el cace por sacar 7 [100,): "))
            if cace >= 100:
                break
        except ValueError:
            pass
        print("❌ Entrada inválida. Intente nuevamente.")
    
    # Set up the number of players
    while True:
        try:
            player_num = int(input("Ingrese el número de jugadores: "))
            if player_num > 1:
                break
        except ValueError:
            pass
        print("❌ Entrada inválida. Intente nuevamente.")

    # Set player names
    players = []
    for i in range(player_num):
        name = input(f"Ingrese el nombre del jugador {i + 1}: ")
        players.append(Player(name))

    # Set up the match
    dice = Dice(dev=dev_mode)
    match = Match(players, initial_bet, cace, dice, auto_mode=auto_mode)

    return match

def main_menu():
    print("\n🔹 Menú Principal 🔹")
    opcion = None
    while not opcion:
        print("1. Iniciar nueva partida")
        print("2. Salir")
        print("3. Help")
        opcion = input("Seleccione una opción: ")

        try: 
            if int(opcion) in [-1,0,1,2,3]:
                break
        except ValueError:
            print("❌ Opción inválida. Intente nuevamente.")
            opcion = None    
        else:
            print("❌ Opción inválida. Intente nuevamente.")
            opcion = None

    opcion = int(opcion)
    if opcion == 1:
        match = set_up_match()
        while match.in_play:
            match.play()
    elif opcion == -1:
        match = set_up_match(dev_mode=True)
        while match.in_play:
            match.play()
    elif opcion == 0:
        match = set_up_match(auto_mode=True)
        while match.in_play:
            match.play()
    elif opcion == 2:
        print("👋 ¡Gracias por jugar! Hasta luego.")
    elif opcion == 3:
        print("-1 : dev_mode = True, 0 : auto_mode = True")
        main_menu()

if __name__ == "__main__":
    main_menu()