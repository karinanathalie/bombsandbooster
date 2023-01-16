import board
from playerbomb import bomblist
import random
bombs= bomblist
newpositions= board.positions.copy()
boosterchoice= [i for i in range(100)]

#this file replaces the positions in the board with the bomb inputs and boosters

for i in bombs :
    newpositions[100-i] = '⦿'
    boosterchoice.remove(i)
board.process(newpositions)
if 99 in newpositions:
    boosterchoice.remove(99)
if 98 in newpositions:
    boosterchoice.remove(98)
boosters = (random.choices(boosterchoice,k=8))

