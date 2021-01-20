import sqlite3


conn = sqlite3.connect('tictactoescore.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS scores (
            name text,
            wins integer
            )""")


def insert_scores(player_name):
    """
    Takes in a string containing winning player's name. If the name does not exist in the database, insert
    the name into the database with 1 win. Otherwise, update the wins associated with the name by 1.
    :param player_name: string containting name of winning player 
    """
    c.execute("""SELECT name FROM scores WHERE name=?""",(player_name,))
    result = c.fetchone()

    if result:
       with conn:
           c.execute("""UPDATE scores SET wins = wins+1 WHERE name =?""",(player_name,))

    else:
        with conn:
            c.execute("INSERT INTO scores VALUES (?, ?)", (player_name, 1))
    

def print_scoreboard():
    """
    Fetches the top 5 five scoring players from the database and displays them in descending order
    """
    print("***************************************")
    print("               SCOREBOARD              ")

    with conn:
            c.execute("SELECT * FROM scores ORDER BY wins DESC LIMIT 5")
            print(c.fetchall())
    print("***************************************")


def draw_board(board):
    """
    Takes in board, extracts size by the length of the board, and prints out tic-tac-toe board with
    boarder displaying coordinate instructions
    :param board: 2D array containing character values for moves or " " for empty space
    """
    board_size = len(board)
    print("0,0", end="")
    for _ in range(board_size):
        print("--", end="")
    print("> Y")
    print("| ")
    for row_idx, row in enumerate(board):
        for col_idx, value in enumerate(row):
            if col_idx == 0:
                print("|  ", end="")
            print(f"{value}", end ="")
            if col_idx != board_size - 1:
                print("|", end ="")
        print("")
        if row_idx != board_size - 1:
            print("|  ", end="")
            print("_+"* (board_size - 1), end ="")
            print("_")   
    print("V")
    print("X\n")      


def take_next_move(character, board, player_name):
    """
    Takes in string input from the user in the form of X,Y coordinates. Checks if move input is empty, has letters, has a comma, 
    exists on the board, is already already taken. If move input passes checks, assign character to corresponding space on board.
    :param character: 1 element string with character assigned for play 
    :param board: 2D array containing character values for moves or " " for empty space
    :param player_name: string with name of currentplayer
    """
    move = input(f"Your turn, {player_name} with character {character}. Enter your next move with x,y coordinates: ")
    #retry if empty string
    if move == "":
        print("PLEASE ENTER YOUR MOVE XY COORDINATES SEPARATED BY A COMMA.")
        return take_next_move(character, board, player_name)
    #retry if string contains letter
    if is_move_a_digit(move) is False:
        print("PLEASE ENTER NUMERIC XY COORDINATES SEPARATED BY A COMMA")
        return take_next_move(character, board, player_name)
    #retry if comma is not entered
    if "," not in move:
        print("PLEASE ENTER NUMERIC XY COORDINATES SEPARATED BY A COMMA")
        return take_next_move(character, board, player_name)
    row_idx, col_idx = clean_up_coordinates(move)
    #check if move exists on board
    if is_valid_move(row_idx, col_idx, board) is False:
        print("INPUT OUT OF BOUNDS. PLEASE ENTER YOUR MOVE XY COORDINATES SEPARATED BY A COMMA.")
        return take_next_move(character, board, player_name)
    #check if move is already taken
    if board[row_idx][col_idx] != " ":
        print("MOVE ALREADY TAKEN ON THE BOARD. PLEASE RETRY.")
        return take_next_move(character, board, player_name)
    #add player move to board
    board[row_idx][col_idx] = character
    

def is_move_a_digit(move):
    """
    Takes in string input and determines if the string contains alphabetic characters
    :param move: string 
    :return: True if input does not contain alphabetic characters, False if contains alphabetic characters. 
    """
    for value in move:
        if value.isalpha():
            return False
    return True 


def clean_up_coordinates(move):
    """
    Takes in coordinates in the forms, transforms into a list, cleans up white space. If empty string, set to -1 to flag
    as out of bounds. 
    :param move: string
    :return: x, y coordinates cleaned up to be used for input in take_move
    """
    coordinates = move.split(",")
    clean_coordinates = []
    for coordinate in coordinates:
        coordinate = coordinate.strip()
        if coordinate == "":
            # flag to catch as out of bounds
            coordinate = -1
        coordinate = int(coordinate)
        clean_coordinates.append(coordinate)
    return clean_coordinates[0], clean_coordinates[1]


# west = board[row_idx][col_idx - 1]
# north = board[row_idx - 1][col_idx]
# east = board[row_idx][col_idx + 1]
# south = board[row_idx + 1][col_idx]
# ascending diagonal = board[row_idx + 1][col_idx + 1]
# decending diagonal = board[row_idx + 1][col_idx - 1]


def check_if_player_won(board, character, player_name):
    """
    Checks if players has won the game
    :param character: 1 element string with character assigned for play 
    :param board: 2D array containing character values for moves or " " for empty space
    :param player_name: string with name of currentplayer
    :return: string declaring winner if player has won or draw if there is no declared winner
    """
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
    """
    Checks if the move the player entered exists within the bounds of the board
    :param row_idx: x coordinate
    :param col_idx: y coordinate
    :param board: 2D array containing character values for moves or " " for empty space
    """
    return row_idx >= 0 and row_idx < len(board) and col_idx >= 0 and col_idx < len(board)

 
def play_again():
    """
    Checks if player would like to play another game
    :return: True if 'y' or False if 'y' is not input
    """
    play = input("Would you like to play again? Enter yes or no: ")
    return play.lower().startswith('y')


def retrieve_player_information(game_participants):
    """
    Takes in player name at the start of the game and assigns player number and game character
    :param game_participants: Integer representing number of players
    :return: Dictionary with the key is the player number and the value is a dictionary 
    containing the name of player and their gameplay character.
    """
    character_set = ['X', 'O', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J', 'K', 'L', 'M', 'N']
    players_dict = {}
    for participant in range(game_participants):
        character = character_set[participant]
        player_no = participant + 1
        name = input(f"Player Number {player_no}, enter your name: ")
        players_dict[player_no] = {"name": name, "character": character} 
        print(f"Wonderful {name}! You are player {player_no} with character {character}")
    return players_dict


def comp_move(board):
    """
    Computer player
    :param board: 2D array containing character values for moves or " " for empty space
    """
    for row_idx, row in enumerate(board):
        for col_idx, value in enumerate(row):
            if board[row_idx][col_idx] == " ":
                board[row_idx][col_idx] = 'O'
                return 


def multiplayer_game():
    """
    Controller for multiplayer game
    """       
    board_size = int(input("Enter your tic tac toe board size as a single digit(ex. Enter 3 for 3x3): "))
    board = [[" " for yaxis in range(board_size)] for xaxis in range(board_size)]
    game_participants = int(input("How many players?: "))
    players_dict = retrieve_player_information(game_participants)
    gameplay = True
    while gameplay:
        for player_no in range(game_participants):
            player_no += 1
            player_name = players_dict[player_no]["name"]
            character = players_dict[player_no]["character"]
            draw_board(board)        
            take_next_move(character, board, player_name)
            player_winner = check_if_player_won(board, character, player_name)
            if player_winner != None:
                print(f"{player_winner}")
                draw_board(board)
                insert_scores(player_name)
                print_scoreboard()
                gameplay = False
                break


def computer_game():
    """
    Controller for computer gameplay
    """
    board_size = int(input("Enter your tic tac toe board size as a single digit(ex. Enter 3 for 3x3): "))
    board = [[" " for yaxis in range(board_size)] for xaxis in range(board_size)]
    game_participants = 1
    players_dict = retrieve_player_information(game_participants)
    gameplay = True
    player_name = players_dict[game_participants]["name"]
    player = players_dict[game_participants]["name"]
    while gameplay:
        if player == player_name:
            draw_board(board)        
            take_next_move("X", board, player_name)
            player_winner = check_if_player_won(board, "X", player_name)
            if player_winner != None:
                print(f"{player_winner}")
                draw_board(board)
                gameplay = False
            player = "computer"

        if player == "computer":    
            draw_board(board)
            print("Computer Move")        
            comp_move(board)
            player_winner = check_if_player_won(board, "O", "computer")
            if player_winner != None:
                print(f"{player_winner}")
                draw_board(board)
                gameplay = False
            player = player_name


def run_game():
    """
    Gameplay loop
    """
    print("Welcome to Tic Tac Toe! ", end="")
    reset_board = True
    while reset_board:
        gameplay = input("Enter 'multiplayer' or 'computer': ")
        if gameplay.lower().startswith('m'):
            multiplayer_game()
            if not play_again():
                reset_board = False
        if gameplay.lower().startswith('c'):
            computer_game()
            if not play_again():
                reset_board = False
            

if __name__ == "__main__": 
    run_game()