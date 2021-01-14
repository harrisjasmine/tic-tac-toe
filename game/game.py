def draw_board(board):
    board_size = len(board)
    for row_idx, row in enumerate(board):
        for col_idx, value in enumerate(row):
            print(f"{value}", end ="")
            if col_idx != board_size - 1:
                print("|", end ="")
        print("")
        if row_idx != board_size - 1:
            print("_+"* (board_size - 1), end ="")
            print("_")        


def take_next_move(character, board, player_name):
    move = input(f"Your turn, {player_name}. Enter your next move with x,y coordinates: ")
    if move == "":
        print("PLEASE ENTER YOUR MOVE XY COORDINATES SEPARATED BY A COMMA.")
        return take_next_move(character, board, player_name)
    if is_move_a_digit(move) is False:
        print("PLEASE ENTER NUMERIC XY COORDINATES SEPARATED BY A COMMA")
        return take_next_move(character, board, player_name)
    row_idx, col_idx = clean_up_coordinates(move)
    if is_valid_move(row_idx, col_idx, board) is False:
        print("INCORRECT INPUT. PLEASE ENTER YOUR MOVE XY COORDINATES SEPARATED BY A COMMA.")
        return take_next_move(character, board, player_name)
    if board[row_idx][col_idx] != " ":
        print("MOVE ALREADY TAKEN ON THE BOARD. PLEASE RETRY.")
        return take_next_move(character, board, player_name)
    #add player move to board
    board[row_idx][col_idx] = character
    return character
    

def is_move_a_digit(move):
    for value in move:
        if value.isalpha():
            return False
    return True 


def clean_up_coordinates(move):
    coordinates = move.split(",")
    row_idx = coordinates[0]
    if len(coordinates) < 2:
        col_idx = None
    else:
        col_idx = coordinates[1]
    row_idx = coordinates[0].strip()
    col_idx = coordinates[1].strip()
    row_idx = int(row_idx)
    col_idx = int(col_idx)
    return row_idx, col_idx


# west = board[row_idx][col_idx - 1]
# north = board[row_idx - 1][col_idx]
# east = board[row_idx][col_idx + 1]
# south = board[row_idx + 1][col_idx]
# ascending diagonal = board[row_idx + 1][col_idx + 1]
# decending diagonal = board[row_idx + 1][col_idx - 1]


def check_if_player_won(board, character, player_name):
    board_size = len(board)
    #check going west to east
    for row_idx, row in enumerate(board):
        w2ematch = 0
        for col_idx, value in enumerate(row):
            if value == character:
                w2ematch += 1            
            if w2ematch == board_size:
                return f"winner is {player_name}" 
    #check going north to south
    for column in range(board_size):
        n2smatch = 0
        for row in range(board_size):
            if board[row][column] == character:
                n2smatch += 1
            if n2smatch == board_size:
                return f"winner is {player_name}"
    #check going descending diagonal
    ddiagmatch = 0
    for diagpos in range(board_size):
        if board[diagpos][diagpos] == character:
            ddiagmatch += 1
        if ddiagmatch == board_size:
            return f"winner is {player_name}"
    #check going in ascending diagonal
    adcolumn = board_size
    adiagmatch = 0
    for row in range(board_size):
        adcolumn -= 1
        if board[row][adcolumn] == character:
            adiagmatch += 1
        if adiagmatch == board_size:
            return f"winner is {player_name}"
    #determine draw
    drawmatch = 0
    for row_idx, row in enumerate(board):
        for col_idx, value in enumerate(row):
            if value != " ":
                drawmatch += 1
            if drawmatch == (board_size ** 2):
                return f"no winner, draw game"


def is_valid_move(row_idx, col_idx, board):
    return row_idx >= 0 and row_idx < len(board) and col_idx >= 0 and col_idx < len(board)


def clean_up_character(character):
    return character[0:1].upper()


#make function to make sure another person cannot take the same character or name


def retrieve_player_information(game_participants):
    players_dict = {}
    for participant in range(game_participants):
        player_no = participant + 1
        name = input(f"Player Number {player_no}, enter your name: ")
        character = input(f"Thanks {name}, enter your single character (i.e. X, O, P): ")
        character = clean_up_character(character)
        print(f"Wonderful {name}! You are player {player_no} with character {character}")
        players_dict[player_no] = {"name": name, "character": character}
    return players_dict


def run_game():
    board_size = int(input("Welcome to Tic Tac Toe! Please enter your desired tic tac toe board size: "))
    board = [[" " for yaxis in range(board_size)] for xaxis in range(board_size)]
    game_participants = 2
    players_dict = retrieve_player_information(game_participants)
    while True:
        for player_no in range(game_participants):
            player_no += 1
            player_name = players_dict[player_no]["name"]
            character = players_dict[player_no]["character"]
            draw_board(board)        
            character = take_next_move(character, board, player_name)
            player_winner = check_if_player_won(board, character, player_name)
            if player_winner != None:
                print(f"{player_winner}")
                draw_board(board)
                break


if __name__ == "__main__": 
    run_game()