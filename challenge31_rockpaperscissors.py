import random

print("Let's play rock paper scissors!")
rounds = int(input("How many rounds would you like to play? You can play 3 to 10. "))

#defines score vals and sets them to 0
userScore = 0
compScore = 0

#runs this block of code for the integer put into the rounds var
for i in range(rounds):
    userAction = input("What will you play? (rock, paper, scissors) ")
    possibleActions = ["rock","paper","scissors"]
    #random choice of moves
    compAction = random.choice(possibleActions)
    print("You played", userAction+", I played",compAction+".")

    #all possible move combos
    if userAction == compAction:
        print("It's a draw!")
    elif userAction == "rock":
        if compAction == "scissors":
            print("Rock beats scissors! You win!")
            userScore += 1
        else:
            print("Paper covers rock! I win!")
            compScore += 1
    elif userAction == "paper":
        if compAction == "rock":
            print("Paper covers rock! You win!")
            userScore += 1
        else:
            print("Scissors cuts paper! I win!")
            compScore += 1
    elif userAction == "scissors":
        if compAction == "paper":
            print("Scissors cuts paper! You win!")
            userScore += 1
        else:
            print("Rock smashes scissors! I win!")
            compScore += 1

print("The final score is: you (", userScore,") to computer (",compScore,").")
           

    
    

