# Maldito 7

A game where the roll of the dice determines the winner, with some extra steps. Perfect for my fellow gambling addicts (just jk). 

## Rules
* Each player has a board with numbers from 2 to 12 inclusive, excluding the number seven. The objective is to check all numbers in your board. First player to achive this is the winner.
* Starting player is determined by the roll of a single die
* In their turn the player presses `ENTER` to roll the dice, we will call the sum of the dice `roll`.  When `roll` is not checked in the current player's board, it gets checked.
* When the player has already checked the value of `roll`, the turn corresponds to the next player whose not checked the value of `roll` in their board.
* If `roll` equals to 7, the player adds a preset money quantity to the price pot.

## Execution
With the source code in a directory of your choice run:
```bash
python main.py
```

### Future development 
1. Restart game after winner 
1. Maybe some color identifiers for the players
1. Something regarding terminal redrawing instead of printing new lines

# Notes
* Game is in spanish so if you are an english speaker, i will make an english version soon enough.
