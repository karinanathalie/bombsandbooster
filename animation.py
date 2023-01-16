from os import system, name
from time import sleep
import random

#this file consists of all the animations and graphics used all over the game

def clear():
	# for windows(os.name is 'nt')
	if name == 'nt': 
		_ = system('cls') 
	# for mac and linux(os.name is 'posix')
	else: 
		_ = system('clear') 

#display of rolling dice
display = [
"""
----------
|        |
|   ()   |
|        |
----------
""",
"""
----------
| ()     |
|        |
|     () |
----------
""",
"""
----------
| ()     |
|   ()   |
|     () |
----------
""",
"""
----------
| ()  () |
|        |
| ()  () |
----------
""",
"""
----------
| ()  () |
|   ()   |
| ()  () |
----------
""",
"""
----------
| ()  () |
| ()  () |
| ()  () |
----------
"""
]

def rollingDiceAnimation(display):
  clear()
  for i in range(3):
    print(
    """
   ________            
  /\       \           
 /()\   ()  \          
/    \_______\         
\    /()     /         
 \()/   ()  /          
  \/_____()/
    """
    )
    sleep(0.4)
    clear()
    print(
    """
        _________  
       /()      /| 
      /    ()  / |  
     /______()/  |  
     |()     | ()/
     |       |  / 
     |_____()| /     
    """
  )
    sleep(0.4)
    clear()
  clear()

#display of how to play
def intro1():
  clear()
  print ("                      .----------------------------------   ")
  print ("                      | Boards&Boosters is a twist to   |   ")
  print ("                      | the popular game Snakes&Ladders |   ")
  print ("                     /.----------------------------------   ")
  print ("                O /                                         ")
  print ("               /|/                                          ")
  print ("                |\                                          ")
  print ("                | \                                         ")
  print ("       ^^^^^^^^^^^^^^^^^^^^^                                ")
  print ("                                                            ")

def intro2():
  clear()
  print ("                      .-----------------------------------------    ")
  print ("                      | First, You will have to choose how many |   ")
  print ("                      | players will be playing the game! The   |   ")
  print ("                      | number of players can be from 2 to 4.   |   ")
  print ("                     /.-----------------------------------------    ")
  print ("                O                                                    ")
  print ("               \|\/                                                  ")
  print ("                |\                                                   ")
  print ("                | |                                                  ")
  print ("       ^^^^^^^^^^^^^^^^^^^^^                                         ")
  print ("                                                                       ")

def intro3():
  clear()
  print ("                      .---------------------------------------   ")
  print ("                      | All the players can choose where they |   ")
  print ("                      | want to place the bombs. The bombs    |   ")
  print ("                      | will push you back a few places.      |   ")
  print ("                      /.--------------------------------------   ")
  print ("                O                                                 ")
  print ("               \|>                                                ")
  print ("                |\                                                ")
  print ("                | |                                               ")
  print ("       ^^^^^^^^^^^^^^^^^^^^^                                      ")
  print ("                                                                  ")

def intro4():
  clear()
  print ("                      .---------------------------------------    ")
  print ("                      | There are also randomly placed        |   ")
  print ("                      | boosters which will push you forward! |   ")
  print ("              !!!     /.--------------------------------------    ")
  print ("                O                                                   ")
  print ("               <|>                                                  ")
  print ("               / \                                                  ")
  print ("              /   |                                                 ")
  print ("       ^^^^^^^^^^^^^^^^^^^^^                                        ")
  print ("                                                                    ")

def intro5():
  clear()
  print ("                      .------------------------------------   ")
  print ("                      | The objective of the game is to    |  ")
  print ("                      | be the first one to reach the end! |  ")
  print ("                     /.------------------------------------   ")
  print ("                O /                                           ")
  print ("               <|/                                            ")
  print ("               / \                                            ")
  print ("              /   |                                           ")
  print ("       ^^^^^^^^^^^^^^^^^^^^^                                  ")
  print ("                                                              ")

def intro6():
  clear()
  print ("                      .------------------------------     ")
  print ("                      | You are excited, aren't you? |    ")
  print ("                      |   So, let's get started!     |    ")
  print ("                ^^   /.------------------------------     ")
  print ("                O__                                       ")
  print ("               /|                                         ")
  print ("               /\                                         ")
  print ("              /  \                                        ")
  print ("       ^^^^^^^^^^^^^^^^^^^^^                              ")
  print ("                                                           ")

def howToPlay():
  intro1()
  sleep(3)
  intro2()
  sleep(4)
  intro3()
  sleep(4)
  intro4()
  sleep(3)
  intro5()
  sleep(3)
  intro6()
  sleep(3)
  clear()

#display of winning screen
def winnings(x):
  clear()
  for i in range(2):
    print(
      f"""
            \   /                                         \   /      
             \O/                                           \O/       
              |    !!!! PLAYER {x} WINS THE GAME !!!!         |          
             / \                                           / \       
            /   \                                         /   \      
      """
      )
    sleep(1)
    clear()
    print(
      f"""
                                                           
              O                                             O       
            / | \    !!!! PLAYER {x} WINS THE GAME !!!!     / | \        
             / \                                           / \       
            /   \                                         /   \      
      """
      )
    sleep(1)
    clear()
  clear()
  print ("                                                              ")
  print ("                                                              ")
  print ("                                                              ")
  print ("   \   /                                         \   /        ")
  print ("    \O/                                           \O/         ")
  print (f"     |    !!!! PLAYER {x} WINS THE GAME !!!!       |          ")
  print ("    / \                                           / \         ")
  print ("   /   \                                         /   \        ")
  print ("                                                              ")
  print ("                                                              ")

