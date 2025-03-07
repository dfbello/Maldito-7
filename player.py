class Player:
    def __init__(self, name="Jugador", current_loss=0):
        self.name = name
        self.board = list(range(2,7)) + list(range(8,13))
        self.current_loss = current_loss

