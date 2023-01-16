  
playerCounter = input("Input the number of players (2-4): ")

try:
    val = int(playerCounter)
except ValueError:
    print("Invalid input")
    playerCounter = input("Input the number of players (2-4): ")

validPlayers = [2, 3, 4]
playerCount = int(playerCounter)
#check if number of players input is valid
if playerCount not in validPlayers:
    invalidInput = True
    while invalidInput == True:
        print("Invalid input")
        playerCount = int(input("Please input again: "))
        if playerCount not in validPlayers:
            invalidInput = True
        else:
            invalidInput = False

import board
bomblist = []
numberOfBombs = {2: 3, 3: 2, 4: 2}
playerChar = {1: "A", 2: "B", 3: "C", 4: "D"}

#take the bomb input from the players, add them to a list and counter invalid inputs
for i in range(1, playerCount + 1):
    bombs = list(map(int, input(f"Player {playerChar[i]} place {numberOfBombs[playerCount]} bombs: ").split()))
    if len(bombs) != numberOfBombs[playerCount]:
        invalidInput = True
        while invalidInput == True:
            print("Invalid number of bombs")
            bombs = list(map(int, input(f"Player {playerChar[i]} place {numberOfBombs[playerCount]} bombs: ").split()))
            if len(bombs) != numberOfBombs[playerCount]:
                invalidInput = True
            else:
                invalidInput = False

    for j in bombs:
        if j in bomblist:
            print(f"{j} already has a bomb placed")
            invalidInput = True
            while invalidInput == True:
                bombs = list(map(int, input(f"Player {playerChar[i]} place {numberOfBombs[playerCount]} bombs: ").split()))
                invalidInput = False
                for j in bombs:
                    if j in bomblist:
                        print(f"{j} already has a bomb placed")
                        invalidInput = True
                if len(bombs) != numberOfBombs[playerCount]:
                    print("Invalid amount of bombs")
                    invalidInput = True

    for l in bombs:
        if l > 99 or l < 2:
            invalidInput = True
            while invalidInput == True:
                print("Invalid position")
                invalidInput = False
                bombs = list(map(int, input(f"Player {playerChar[i]} place {numberOfBombs[playerCount]} bombs: ").split()))
                for l in bombs:
                    if l > 99 or l < 2:
                        invalidInput = True
            
    for k in bombs:
        bomblist.append(k)
    
