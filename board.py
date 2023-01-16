from termcolor import colored

#this file is used for printing the board

colors = {"A": "yellow", "B": "white", "C": "blue", "D": "magenta", "⦿": "red"}
positions=[j for j in range(100,0,-1)]
def process(x):
    spaces = 5
    output = True
    for i in range (9):
        row = x[i*10:i*10+10] 
        if output==True:
            for c in row:
                if isinstance(c, str):
                    print(colored(f'{c: >{spaces}}', colors[c]),end = "")
                else:
                    print(f'{c: >{spaces}}',end="")
            output=False
        else:
            for d in row[::-1]:
                if isinstance(d, str):
                    print(colored(f'{d: >{spaces}}', colors[d]),end = "")
                else:
                    print(f'{d: >{spaces}}',end="")
            output = True
        print()
    for g in x[100:89:-1]:
        if isinstance(g, str):
            print(colored(f'{g: >{spaces}}', colors[g]),end = "")
        else: 
            print(f'{g: >{spaces}}',end="")
    print()

process(positions)
