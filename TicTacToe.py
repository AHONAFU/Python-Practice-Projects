print("You are X")

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_still_going = True
winner = None
current_player = "X"

def play_game():
    display_board()

    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

    if winner == "X" or winner == "O":
        print("The winner is " + winner)
    elif winner == None:
        print("It's a Tie!")


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])





def handle_turn(player):
    print(player + "'s turn")
    position = input("Chose a number between 1-9: ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose position from 1-9: ")
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Try again")
    board[position] = player
    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonal()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():
    global game_still_going
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3:
        game_still_going = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row2:
        return board[6]

    return


def check_columns():
    global game_still_going
    col1 = board[0] == board[1] == board[2] != "-"
    col2 = board[3] == board[4] == board[5] != "-"
    col3 = board[6] == board[7] == board[8] != "-"

    if col1 or col2 or col3:
        game_still_going = False
    if col1:
        return board[0]
    elif col2:
        return board[3]
    elif col3:
        return board[6]
    return


def check_diagonal():
    global game_still_going
    dia1 = board[0] == board[4] == board[8] != "-"
    dia2 = board[6] == board[4] == board[2] != "-"

    if dia1 or dia2:
        game_still_going = False
    if dia1:
        return board[0]
    elif dia2:
        return board[6]

    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


play_game()

# board
# display bpoard
# play game
# handle turn
# position
# check lose
# check win
# check rows
# check colums
# check diaonals
# check tie
# flip player
