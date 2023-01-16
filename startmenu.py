from animation import howToPlay

#this file is used for outputting the menu at the start of a game

print("****** Welcome to Bombs & Boosters ******")
print("1. Play")
print("2. How to play?")

firstInput = int(input(""))
valid = [1, 2]

#check if the input is either 1 or 2, show invalid if not.
if firstInput not in valid:
    invalidInput = True
    while invalidInput == True:
        print("Invalid input")
        firstInput = int(input("Please input again: "))
        if firstInput not in valid:
            invalidInput = True
        else:
            invalidInput = False

if firstInput == 1:
    import playerbomb

if firstInput == 2:
    howToPlay()
    x = input("Press enter to continue")
    if x == "":
        import playerbomb

