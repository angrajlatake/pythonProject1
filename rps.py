import random
print("let's play Rock, paper Scissors. Best of 3")
compscore = 0
playscore = 0
def score():
    print(str(compscore) + " Computer " + str(playscore) + " Player" )
def compwin():
    print("Computer wins this round.")



def playwin():
    print(" You won this round")



list = ['r', 's', 'p']
while compscore !=2 or playscore != 2:
    if compscore == 2:
        print("Computer has won the game. Better luck next time.")
        break
    elif playscore == 2:
        print("You beat the computer. Congratulations!")
        break

    choice = input("Choose 'r', 'p', 's'. ")
    comp = random.choice(list)
    print( comp + " vs " + choice)
    if comp == choice:
        print("It's a tie! Let try again")
        score()

    elif comp == 'r':
        if choice == 'p':
            playwin()
            playscore += 1
            score()
        elif choice == 's':
            compwin()
            compscore += 1
            score()

    elif comp == 'p':
        if choice == 's':
            playwin()
            playscore += 1
            score()
        elif choice == 'r':
            compwin()
            compscore += 1
            score()

    elif comp == 's':
        if choice == 'r':
            playwin()
            playscore += 1
            score()
        elif choice == 'p':
            compwin()
            compscore += 1
            score()