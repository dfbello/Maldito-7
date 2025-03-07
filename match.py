from dice import Dice
from player import Player

class Match:
    def __init__(self, players, initial_bet, cace=100, dice=Dice(), auto_mode=False):
        self.auto_mode = auto_mode
        self.players = players
        self.dice = dice
        self.current_player = 0 # Index of the current player
        self.in_play = True
        self.price = initial_bet * len(players)
        self.cace = cace
        
        for player in self.players:
            player.current_loss = -initial_bet

    def play(self):

        self.current_player = self.tie_break(self.players)

        while self.in_play:
            player = self.players[self.current_player]
            
            print(f"\n______________________________________________________\n")
            print(f"\n{player.name}, es tu turno.\n")
            print(f"\tNúmeros faltantes para ganar\n\t{player.board}\n")

            if not self.auto_mode:
                # Prompt the user to press Enter to roll the dice
                input("\tPresiona Enter para lanzar los dados...\n")

            # Roll the dice
            roll = self.dice.roll()
            print(f"\t{player.name} sacó 🎲 {roll}\n")

            if roll in player.board:
                player.board.remove(roll)
                if self.check_winner(player):
                    break
                print(f"\t{player.board}")
                print(f"\t¡Bien {player.name}! Te quedan {len(player.board)} número(s) para ganar.\n")
            elif roll == 7:
                print(f"\t💰 ¡Maldito 7! {player.name} agrega {self.cace} a la bolsa de premio. 💰 ({self.price})\n")
                self.price += self.cace
                player.current_loss -= self.cace
                self.current_player = (self.current_player + 1) % len(self.players)
                continue
            else:
                self.next_player(roll)
    

    def next_player(self, number):
        count = 0
        while number not in self.players[self.current_player].board and count < len(self.players):
            self.current_player = (self.current_player + 1) % len(self.players)
            count += 1

        # If no player has that number, next player's turn
        if count == len(self.players):
            self.current_player = (self.current_player + 1) % len(self.players)
            return
        
        self.players[self.current_player].board.remove(number)
        if self.check_winner(self.players[self.current_player]):
            return
        
        return

    def check_winner(self, player):
            if not player.board:
                print(f"\n¡🏆 {player.name} ha ganado 💰 {self.price}!\n")
                player.current_loss += self.price
                self.in_play = False
                self.match_recap()
                return True
            return False
    
    def match_recap(self):
        print(f"\n📝 Resumen de la partida 📝\n")

        # Sort players by current_loss in descending order
        sorted_players = sorted(self.players, key=lambda player: player.current_loss, reverse=True)

        # Players' current loss
        print(f"\t🪙 Pérdidas de los jugadores:")
        for player in sorted_players:
            print(f"\t\t{player.name}: {player.current_loss}")

        # Numbers of the board remaining for each player
        print(f"\n\t📋 Tablero de los jugadores:")
        for player in sorted_players:
            print(f"\t\t{player.name}: {player.board}")

        return
    
    def tie_break(self, players):
        
        if len(players) == 1:
            return self.players.index(*players)
        
        print(f"\n🎲 ¡Desempate! 🎲")
        max_number = 0
        tied_players = []

        for player in players:
            print(f"\n______________________________________________________\n")
            print(f"\n{player.name}, es tu turno.\n")

            if not self.auto_mode:
                # Prompt the user to press Enter to roll the die
                input("\tPresiona Enter para lanzar el dado...\n")
            
            # Roll the die
            roll = self.dice.roll_single()
            print(f"\t{player.name} sacó 🎲 {roll}\n")

            if roll > max_number:
                max_number = roll
                tied_players = [player]
            elif roll == max_number:
                tied_players.append(player) 
        
        return self.tie_break(tied_players)
        
        

        

       
        
