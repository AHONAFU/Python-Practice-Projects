import random

alu = random.randint(1, 20)
def num():
    global guess
    guess = int(input("Guess the number:  "))

    if guess < alu:
        print("Higher")
        num()
    elif guess > alu:
        print("Lower")
        num()
    elif guess == alu:
        print("###  You are the winner  ###")
        conv = str(alu)
        print(conv + " was the number")
        exit()
    else:
        print("Don't know what you are saying")

num()