from bombandbooster import boosters, bombs, newpositions
from board import positions
import board

#updating the positions of the player onto the board list
def placing(x):
    newposs = newpositions.copy()
    for i in x:
        a = positions.index(x[i])
        newposs[a]= i
    board.process(newposs)
