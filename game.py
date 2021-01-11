
board_size = int(input("Please enter your desired tic tac toe board size:"))

def draw_board(board):
    for row_idx, row in enumerate(board):
        for col_idx, value in enumerate(row):
            print(f"{value}", end ="")
            if col_idx != board_size - 1:
                print("|", end ="")
        print("")
        if row_idx != board_size - 1:
            print("_+"* (board_size - 1), end ="")
            print("_")
        


def print_coordinates(board_size):
    for row_idx, row in enumerate(board):
        for col_idx, value in enumerate(row):
            if col
            print(f"{value}", end ="")
            if col_idx != board_size - 1:
                print("|", end ="")
        print("")
        if row_idx != board_size - 1:
            print("_+"* (board_size - 1), end ="")
            print("_")


def take_next_move(player_no, board):
    if player_no == 1:
        character = "X"
    if player_no == 2:
        character = "O" 
    move = input(f"Your Turn Player {player_no}! Your Character is {character}. Enter your next move with x,y coordinates:")
    coordinates = move.split(",")
    #need to create code to validate we received two ints separated by a comma
    row_idx = coordinates[0].strip()
    col_idx = coordinates[1].strip()
    row_idx = int(row_idx)
    col_idx = int(col_idx)
    if is_valid(row_idx, col_idx) is False:
        print("INCORRECT INPUT. PLEASE ENTER YOUR MOVE XY COORDINATES SEPARATED BY A COMMA.")
        return take_next_move(player_no, board)
    if board[row_idx][col_idx] != " ":
        print("MOVE ALREADY TAKEN ON THE BOARD. PLEASE RETRY.")
        return take_next_move(player_no, board)
    #add player move to board
    board[row_idx][col_idx] = character
    return character
    

# west = board[row_idx][col_idx - 1]
# north = board[row_idx - 1][col_idx]
# east = board[row_idx][col_idx + 1]
# south = board[row_idx + 1][col_idx]
# ascending diagonal = board[row_idx + 1][col_idx + 1]
# decending diagonal = board[row_idx + 1][col_idx - 1]


def check_if_player_won(board, character):
    #check going west to east
    for row_idx, row in enumerate(board):
        w2ematch = 0
        for col_idx, value in enumerate(row):
            if value == character:
                w2ematch += 1            
            if w2ematch == board_size:
                return f"winner is {character}" 
    #check going north to south
    for column in range(board_size):
        n2smatch = 0
        for row in range(board_size):
            if board[row][column] == character:
                n2smatch += 1
            if n2smatch == board_size:
                return f"winner is {character}"
    #check going descending diagonal
    ddiagmatch = 0
    for diagpos in range(board_size):
        if board[diagpos][diagpos] == character:
            ddiagmatch += 1
        if ddiagmatch == board_size:
            return f"winner is {character}"
    #check going in ascending diagonal
    adcolumn = board_size
    adiagmatch = 0
    for row in range(board_size):
        adcolumn -= 1
        if board[row][adcolumn] == character:
            adiagmatch += 1
        if adiagmatch == board_size:
            return f"winner is {character}"
    
    #determine draw
    drawmatch = 0
    for row_idx, row in enumerate(board):
        for col_idx, value in enumerate(row):
            if value != " ":
                drawmatch += 1
            if drawmatch == (board_size ** 2):
                return f"no winner, draw game"


def is_valid(row_idx, col_idx):
    return row_idx >= 0 and row_idx < board_size and col_idx >= 0 and col_idx < board_size


def run_game():
    board = [[" " for yaxis in range(board_size)] for xaxis in range(board_size)]
    for turn in range(board_size ** 2):
        player_no = turn % 2 + 1
        draw_board(board)        
        character = take_next_move(player_no, board)
        player_winner = check_if_player_won(board, character)
        if player_winner != None:
            print(f"{player_winner}")
            draw_board(board)
            break

if __name__ == "__main__": 
    run_game()