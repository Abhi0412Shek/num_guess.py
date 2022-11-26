# Importing random module.
import random
# Main game definition.
def game(count):
    # Number of times game has been run!
    count+=1
    # Score of the user.
    score=0
    while True:
        # Taking lower and upper range from the user.
        a=int(input("Enter lower range!"))
        b=int(input("Enter upper range!"))
        if a>b:
            print("Invalid range of numbers!")
        else:
            # Generating the random number, which has to be guessed.
            num=random.randint(a,b)
            for i in range (3):
                guess=int(input("Guess the number!"))
                if guess==num:
                    print("Woohoo! You got it correct.")
                    # For correct answer score increases by 1.
                    score+=1
                    break
                elif i==2:
                    if guess!=num:
                        print("Better luck next Time!")
                        pass
                else:
                    if guess>num:
                        print("Have one more try!")
                        print("Your guess was too high!")
                    else:
                        print("Have one more try!")
                        print("Your guess was too small!") 
            # Asking user to play again!
            cont=input("Enter \"Y\" to play again OR \"N\" to exit and get score!")
            if "Y"==cont.upper():
                pass
            else:
                print("Your Score =",score)
                if score<=count*2 and score>count+2:
                    print("Congrats!")
                    break
                else:
                    print("Better luck next time!")
                    break
# Main Program               
count=0
print("--------------------------------")
print("| WELCOME to GUESS THE NUMBER! |")
print("--------------------------------")
# Beggining the game!
game(count)
