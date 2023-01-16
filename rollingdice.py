import random
from playerbomb import playerCount, playerChar
from animation import display, rollingDiceAnimation, clear, winnings
from bombandbooster import bombs, boosters, newpositions
import positioning

#this file is used for the dice rolls, booster and bomb outputs

position = {'A': 1, 'B': 1,'C': 1, 'D': 1 }
position_real = dict(list(position.items())[:playerCount])

def rollingplayer(playerChar):
    invalidInput = True 
    while invalidInput == True:
        roll = input(f'Player {playerChar} turn, type r to roll, type e to end the game: ')
        if roll =='e':
            print(f'Player {playerChar} ends the game')
            exit()
        if roll=='r':
            rollingDiceAnimation(display)
            steps = random.randint(1, 6)
            print(display[steps-1])
            print(f'{playerChar} roll ', steps, '!')
            position_real[playerChar] += steps
            if position_real[playerChar]==100:
                winnings(playerChar)
                positioning.placing(position_real) 
                exit()
            if position_real[playerChar]>100:
                position_real[playerChar]-= steps
                print (f'You rolled too high, you only need {100-position_real[playerChar]} more step(s)')
            for i in position_real:
                if i!=playerChar:
                    if position_real[i]==position_real[playerChar]:
                        print(f'Oh noo, you got kicked by player {i}, 1 step backward')
                        position_real[playerChar]-=1
            bomb,booster=0,0
            if position_real[playerChar] in bombs:
                bombs.pop(bombs.index(position_real[playerChar]))
                newpositions[100-position_real[playerChar]] = position_real[playerChar]
                bomb += (random.randint(15, 30))
                if bomb>position_real[playerChar]:
                    bomb = position_real[playerChar]-1
                print (f'Ohh no you step on a bomb, {bomb} steps backward')
                bomb *=-1
            if position_real[playerChar] in boosters:
                booster+=random.randint(15,30)
                while position_real[playerChar] + booster > 98:
                    booster = 0
                    booster+=random.randint(1,10)
                print (f'Nice, you got a booster, {booster} steps forward')
            position_real[playerChar] += booster + bomb
            invalidInput = False
        else:
            print('Invalid input try again')

            
def play():
    for i in range(1, playerCount+1):
        rollingplayer(playerChar[i])
        if i==playerCount:
            positioning.placing(position_real) 
            play()
        
play()
