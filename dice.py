import random
import re

class Dice:
    def __init__(self, dev=None): # dev = Developer mode
        self.dev = dev

    def roll(self):
        """Rolls two dice and returns their values."""
        
        if self.dev:
            while True:
                cin = input("🎲 Desea dados aleatorios? (1 Si / 0 No): ")
                try:
                    cin = int(cin)
                    break
                except ValueError:
                    print("Entrada inválida. Intente nuevamente")

            if cin:
                die1 = random.randint(1, 6)
                die2 = random.randint(1, 6)
                
            else:
                """Developer mode: allows choosing the values."""
                while True:
                    cin = input("🎲 Ingrese dos valores (1-6) separados por espacios: ")
                    
                    # Extract numbers
                    values = re.findall(r'\d+', cin)
                    
                    # Convert to int and evaluate
                    if len(values) == 2:
                        die1, die2 = map(int, values)
                        if 1 <= die1 <= 6 and 1 <= die2 <= 6:
                            break
                    else:
                        print("Entrada inválida. Ingrese dos números entre 1 y 6.")
        
        else:
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)

        return die1, die2

    def roll_single(self):
        """Rolls a single die (for tiebreakers)."""
        if self.dev:
            while True:
                cin = input("🎲 Desea dados aleatorios? (1 Si / 0 No): ")
                try:
                    cin = int(cin)
                    break
                except ValueError:
                    print("Entrada inválida. Intente nuevamente")

            if cin:
                die1 = random.randint(1, 6)
                
            else:
                """Developer mode: allows choosing the value."""
                while True:
                    cin = input("🎲 Ingrese un valor (1-6): ")
                    
                    # Extract numbers
                    value = re.findall(r'\d+', cin)
                    
                    # Convert to int and evaluate
                    if len(value) == 1:
                        die1 = int(value[0])
                        if 1 <= die1 <= 6:
                            break
                    else:
                        print("Entrada inválida. Ingrese un número entre 1 y 6.")
        
        else:
            die1 = random.randint(1, 6)

        return die1