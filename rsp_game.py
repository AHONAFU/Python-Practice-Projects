import random

print("Rock = r \n  Paper = p \n Scissors = s")
def game():
    moves = ["Rock", "Paper", "Scissors"]

    ran_moves = random.choice(moves)
    user_move = str(input("Make your move: "))

    if user_move == "r":
        user_move = moves[0]
    if user_move == "p":
        user_move = moves[1]
    if user_move == "s":
        user_move = moves[2]

    if user_move == ran_moves:
        print(ran_moves)
        print("### TIE  ###")
        game()
    elif user_move == moves[0] and ran_moves == moves[1]:
        print(ran_moves)
        print("\n Computer won!!")
        choices()
    elif user_move == moves[0] and ran_moves == moves[2]:
        print(ran_moves)
        print("\n Human won!!")
        choices()
    elif user_move == moves[1] and ran_moves == moves[2]:
        print(ran_moves)
        print("\n Computer won!!")
        choices()


    elif user_move == moves[1] and ran_moves == moves[0]:
        print(ran_moves)
        print("\n Human won!!")
        choices()
    elif user_move == moves[2] and ran_moves == moves[0]:
        print(ran_moves)
        print("\n Computer won!!")
        choices()
    elif user_move == moves[2] and ran_moves == moves[1]:
        print(ran_moves)
        print("\n Human won!!")
        choices()

    else:
        print("Could not understand the command. Try again")
        game()

def choices():
    choice = str(input("Would you like to play again?: "))
    if choice == "yes":
        game()
    elif choice == "no":
        print("Bye!")
        exit()
    else:
        choices()

game()

# rock-paper
# rock-sissor
# paper-scissor