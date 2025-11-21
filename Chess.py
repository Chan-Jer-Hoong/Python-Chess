# imports
from enum import Enum
import itertools

# Enums
class File(Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6
    H = 7

class Rank(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8

class Piece(Enum):
    PAWN = 0
    ROOK = 1
    KNIGHT = 2
    BISHOP = 3
    QUEEN = 4
    KING = 5

class PieceInfo(Enum):
    PIECE = 0
    MOVED = 1
    COLOUR = 2

# Variables
chessboard = {}
square = "[ ]"
empty_square = " "
piece_moved = 0
empty_piece_colour = " "
CHESS_PIECE = ["p","r","k","b","Q","K"]
FILE_LETTER = ["a","b","c","d","e","f","g","h"]
RANK_NUM = [1,2,3,4,5,6,7,8]
BLACK_PIECE = "black"
WHITE_PIECE = "white"

# Functions
def init_chessboard(board : dict):
    # Temporary dictionary used to update the main dictionary with the new key:value pair
    temp_dict = {}

    for rank in RANK_NUM:
        for file in FILE_LETTER:
            temp_dict[file + str(rank)] = [square, piece_moved, empty_piece_colour]

    board.update(temp_dict)

def init_pieces(board : dict):
    for pawn_piece in FILE_LETTER:
        # White Pawn
        board[pawn_piece + str(Rank.TWO.value)][PieceInfo.PIECE.value] = insert_piece(square, CHESS_PIECE[Piece.PAWN.value], empty_square)
        board[pawn_piece + str(Rank.TWO.value)][PieceInfo.COLOUR.value] = WHITE_PIECE
        # Black Pawn
        board[pawn_piece + str(Rank.SEVEN.value)][PieceInfo.PIECE.value] = insert_piece(square, CHESS_PIECE[Piece.PAWN.value], empty_square)
        board[pawn_piece + str(Rank.SEVEN.value)][PieceInfo.COLOUR.value] = BLACK_PIECE
    
    for piece in board:
        # Rooks
        if piece == "a1" or piece == "h1":
            board[piece][PieceInfo.PIECE.value] = insert_piece(square, CHESS_PIECE[Piece.ROOK.value], empty_square)
            board[piece][PieceInfo.COLOUR.value] = WHITE_PIECE
        elif piece == "a8" or piece == "h8":
            board[piece][PieceInfo.PIECE.value] = insert_piece(square, CHESS_PIECE[Piece.ROOK.value], empty_square)
            board[piece][PieceInfo.COLOUR.value] = BLACK_PIECE
        # Knights
        elif piece == "b1" or piece == "g1":
            board[piece][PieceInfo.PIECE.value] = insert_piece(square, CHESS_PIECE[Piece.KNIGHT.value], empty_square)
            board[piece][PieceInfo.COLOUR.value] = WHITE_PIECE
        elif piece == "b8" or piece == "g8":
            board[piece][PieceInfo.PIECE.value] = insert_piece(square, CHESS_PIECE[Piece.KNIGHT.value], empty_square)
            board[piece][PieceInfo.COLOUR.value] = BLACK_PIECE
        # Bishops
        elif piece == "c1" or piece == "f1":
            board[piece][PieceInfo.PIECE.value] = insert_piece(square, CHESS_PIECE[Piece.BISHOP.value], empty_square)
            board[piece][PieceInfo.COLOUR.value] = WHITE_PIECE
        elif piece == "c8" or piece == "f8":
            board[piece][PieceInfo.PIECE.value] = insert_piece(square, CHESS_PIECE[Piece.BISHOP.value], empty_square)
            board[piece][PieceInfo.COLOUR.value] = BLACK_PIECE
        # Queens
        elif piece == "d1":
            board[piece][PieceInfo.PIECE.value] = insert_piece(square, CHESS_PIECE[Piece.QUEEN.value], empty_square)
            board[piece][PieceInfo.COLOUR.value] = WHITE_PIECE
        elif piece == "d8":
            board[piece][PieceInfo.PIECE.value] = insert_piece(square, CHESS_PIECE[Piece.QUEEN.value], empty_square)
            board[piece][PieceInfo.COLOUR.value] = BLACK_PIECE
        # Kings
        elif piece == "e1":
            board[piece][PieceInfo.PIECE.value] = insert_piece(square, CHESS_PIECE[Piece.KING.value], empty_square)
            board[piece][PieceInfo.COLOUR.value] = WHITE_PIECE
        elif piece == "e8":
            board[piece][PieceInfo.PIECE.value] = insert_piece(square, CHESS_PIECE[Piece.KING.value], empty_square)
            board[piece][PieceInfo.COLOUR.value] = BLACK_PIECE

# og_string is the original string, insert_string is the string to be placed, target_char is the specific character we want to target
def insert_piece(og_string : str, insert_string : str, target_char : str) -> str:
    # Get the index of the target character. In our case its the space left in between the square brackets
    insert_index = og_string.find(target_char)

    # Turn the string into a list for easier insertion of the new string
    string_to_list = list(og_string)

    # Insert the new string into the target character's index in the list
    string_to_list[insert_index] = insert_string

    # After insertion, turn the list back into a string by using the join method
    new_string = "".join(string_to_list)

    return new_string

def get_piece_from_square(board : dict, piece_start_pos : str) -> str:
    # save the piece before removing it
    square_and_piece = board[piece_start_pos][PieceInfo.PIECE.value]

    # Remove the square brackets from the piece by finding the index of the starting square bracket and getting the piece by adding 1
    piece_index = square_and_piece.find("[") + 1

    # Change the string into a list for easier indexing
    piece_list = list(square_and_piece)

    # Get the piece using the list index and saving it
    piece = piece_list[piece_index]

    return piece

def move_piece(player : str, board : dict, piece_start_pos : str, piece_end_pos : str):
    # Getting the piece within the square
    cur_piece = get_piece_from_square(board, piece_start_pos)

    # Saving the piece colour information
    prev_colour = board[piece_start_pos][PieceInfo.COLOUR.value]

    # Remove the piece from its original position and its information
    board[piece_start_pos][PieceInfo.PIECE.value] = square
    # Remove the colour information from piece
    board[piece_start_pos][PieceInfo.COLOUR.value] = empty_piece_colour

    # Add the piece into its new position and check if the square is empty
    if board[piece_end_pos][PieceInfo.PIECE.value] == square:
        # insert the piece to the new square
        board[piece_end_pos][PieceInfo.PIECE.value] = insert_piece(board[piece_end_pos][PieceInfo.PIECE.value], cur_piece, empty_square)
        # update colour
        board[piece_end_pos][PieceInfo.COLOUR.value] = prev_colour
        print("\n" + player + " moved their piece!")
    # If the square is not empty
    else:
        board[piece_start_pos][PieceInfo.PIECE.value] = insert_piece(board[piece_start_pos][PieceInfo.PIECE.value], cur_piece, empty_square)
        board[piece_end_pos][PieceInfo.COLOUR.value] = prev_colour
        print("\n!! This spot is occupied, please choose a different spot !!")
    
# Before moving a piece, check to see if it is a valid move
def check_valid_move(board : dict, cur_piece : str, piece_start_pos : str, piece_end_pos : str, piece_move : int) -> bool:
    # Changing the piece position coordinates into a list to better separate the string
    start_pos_list = list(piece_start_pos)
    end_pos_list = list(piece_end_pos)

    # Grabbing the rank after splitting the string into characters
    start_rank_val = start_pos_list[1]
    end_rank_val = end_pos_list[1]

    # Grabbing the file after splitting the string into characters
    start_file = start_pos_list[0]
    end_file = end_pos_list[0]

    # Changing the rank into an int for calculation
    start_rank = int(start_rank_val)
    end_rank = int(end_rank_val)

    # extracts the piece from its square brackets
    cur_player_piece = get_piece_from_square(board, cur_piece)
    
    # Main section that checks and validates the pieces movement
    if cur_player_piece == CHESS_PIECE[Piece.PAWN.value]:
        if board[piece_start_pos][PieceInfo.COLOUR.value] == WHITE_PIECE and (end_rank - start_rank) == 1 and start_file == end_file:
            print("white pawn moving")
            return True
        elif board[piece_start_pos][PieceInfo.COLOUR.value] == BLACK_PIECE and (start_rank - end_rank) == 1 and start_file == end_file:
            print("black pawn moving")
            return True
        else:
            # Debug print
            print("piece start pos:", board[piece_start_pos][PieceInfo.PIECE.value], "\n", "piece end pos:", board[piece_end_pos][PieceInfo.PIECE.value], "\n" ,"piece color:", board[piece_start_pos][PieceInfo.COLOUR.value], "\n" ,"black piece rank after subtraction:", start_rank - end_rank, "\n" ,"white piece rank after subtraction:", end_rank - start_rank)
            print("can't move there")
            return False
    elif cur_player_piece == CHESS_PIECE[Piece.ROOK.value]:
        # If the rook is moving down the column
        if start_file == end_file:
            # Add 1 to start rank so it does not count the rook's original position, add 1 to end rank to ensure it counts the last spot (if a6 is chosen, it will go to a5 and stop)
            for path in range(start_rank + 1, end_rank + 1):
                # Debug statement
                #print(start_file + str(path), ":", board[start_file + str(path)][PieceInfo.PIECE.value])
                #print(path, "=", end_rank)
                if board[start_file + str(path)][PieceInfo.PIECE.value] != square:
                    return False
            return True
        # If the rook is moving side to side in the row
        elif start_file != end_file and start_rank == end_rank:
            for path in range(FILE_LETTER.index(start_file) + 1, FILE_LETTER.index(end_file) + 1):
                if board[FILE_LETTER[path] + str(start_rank)][PieceInfo.PIECE.value] != square:
                    return False
            return True
        # Means the player is moving the rook diagonally
        else:
            # Debug print
            print("piece start pos:", board[piece_start_pos][PieceInfo.PIECE.value], "\n", "piece end pos:", board[piece_end_pos][PieceInfo.PIECE.value], "\n" ,"piece color:", board[piece_start_pos][PieceInfo.COLOUR.value], "\n" ,"black piece rank after subtraction:", start_rank - end_rank, "\n" ,"white piece rank after subtraction:", end_rank - start_rank)
            print("can't move there")
            return False
    elif cur_player_piece == CHESS_PIECE[Piece.KNIGHT.value]:
        ''' Not to brag, but somehow successfully implemented one of the more complicated chess piece on the first try '''
        if end_rank == start_rank + 2 and (end_file == FILE_LETTER[FILE_LETTER.index(start_file) + 1] or end_file == FILE_LETTER[FILE_LETTER.index(start_file) - 1]):
            return True
        elif end_rank == start_rank - 2 and (end_file == FILE_LETTER[FILE_LETTER.index(start_file) + 1] or end_file == FILE_LETTER[FILE_LETTER.index(start_file) - 1]):
            return True
        elif end_file == FILE_LETTER[FILE_LETTER.index(start_file) + 2] and (end_rank == start_rank + 1 or end_rank == start_rank - 1):
            return True
        elif end_file == FILE_LETTER[FILE_LETTER.index(start_file) - 2] and (end_rank == start_rank + 1 or end_rank == start_rank - 1):
            return True
        else:
            # Debug print
            print("piece start pos:", board[piece_start_pos][PieceInfo.PIECE.value], "\n", "piece end pos:", board[piece_end_pos][PieceInfo.PIECE.value], "\n" ,"piece color:", board[piece_start_pos][PieceInfo.COLOUR.value], "\n" ,"black piece rank after subtraction:", start_rank - end_rank, "\n" ,"white piece rank after subtraction:", end_rank - start_rank)
            print("can't move there")
            return False
    elif cur_player_piece == CHESS_PIECE[Piece.BISHOP.value]:
        # Going Down
        if start_rank < end_rank: # Doubles as checking if the piece is moving down the same rank
            print("going down")
            # Left
            if FILE_LETTER.index(start_file) > FILE_LETTER.index(end_file):
                print("entered left")
                # Checks to see if the given file is the same as the expected file from the list, if not that means it isn't moving correctly
                if end_file == FILE_LETTER[FILE_LETTER.index(start_file) - (end_rank - start_rank)]:
                    # Going left requires reverse indexing for the file, so negative steps are used but since its going down, rank stays positive
                    for file, rank in zip(range(FILE_LETTER.index(start_file) - 1, FILE_LETTER.index(end_file) - 1, -1), range(start_rank + 1, end_rank + 1)):
                        if board[FILE_LETTER[file] + str(rank)][PieceInfo.PIECE.value] != square:
                            print("failed at:", FILE_LETTER[file] + str(rank))
                            return False
                    return True
                else:
                    print("It isn't going diagonal")
                    return False
            # Right
            elif FILE_LETTER.index(start_file) < FILE_LETTER.index(end_file):
                print("entered right")
                if end_file == FILE_LETTER[FILE_LETTER.index(start_file) + (end_rank - start_rank)]:
                    for file, rank in zip(range(FILE_LETTER.index(start_file) + 1, FILE_LETTER.index(end_file) + 1), range(start_rank + 1, end_rank + 1)):
                        if board[FILE_LETTER[file] + str(rank)][PieceInfo.PIECE.value] != square:
                            print("failed at:", FILE_LETTER[file] + str(rank))
                            return False
                    return True
                else:
                    print("It isn't going diagonal")
                    return False
            else:
                # Debug print
                print("piece start pos:", board[piece_start_pos][PieceInfo.PIECE.value], "\n", "piece end pos:", board[piece_end_pos][PieceInfo.PIECE.value], "\n" ,"piece color:", board[piece_start_pos][PieceInfo.COLOUR.value], "\n" ,"black piece rank after subtraction:", start_rank - end_rank, "\n" ,"white piece rank after subtraction:", end_rank - start_rank)
                print("can't move there")
                return False
        '''
        # Going Down
        if end_rank > start_rank:
            # Right
            if end_file == FILE_LETTER[FILE_LETTER.index(start_file) + (end_rank - start_rank)]:
                return True
            # Left
            elif end_file == FILE_LETTER[FILE_LETTER.index(start_file) - (end_rank - start_rank)]:
                return True
            else:
                # Debug print
                print("piece start pos:", board[piece_start_pos][PieceInfo.PIECE.value], "\n", "piece end pos:", board[piece_end_pos][PieceInfo.PIECE.value], "\n" ,"piece color:", board[piece_start_pos][PieceInfo.COLOUR.value], "\n" ,"black piece rank after subtraction:", start_rank - end_rank, "\n" ,"white piece rank after subtraction:", end_rank - start_rank)
                print("can't move there")
                return False
        # Going up
        elif end_rank < start_rank:
            # Right
            if end_file == FILE_LETTER[FILE_LETTER.index(start_file) + (start_rank - end_rank)]:
                return True
            # Left
            elif end_file == FILE_LETTER[FILE_LETTER.index(start_file) - (start_rank - end_rank)]:
                return True
            else:
                # Debug print
                print("piece start pos:", board[piece_start_pos][PieceInfo.PIECE.value], "\n", "piece end pos:", board[piece_end_pos][PieceInfo.PIECE.value], "\n" ,"piece color:", board[piece_start_pos][PieceInfo.COLOUR.value], "\n" ,"black piece rank after subtraction:", start_rank - end_rank, "\n" ,"white piece rank after subtraction:", end_rank - start_rank)
                print("can't move there")
                return False
        # Anything else
        else:
            # Debug print
            print("piece start pos:", board[piece_start_pos][PieceInfo.PIECE.value], "\n", "piece end pos:", board[piece_end_pos][PieceInfo.PIECE.value], "\n" ,"piece color:", board[piece_start_pos][PieceInfo.COLOUR.value], "\n" ,"black piece rank after subtraction:", start_rank - end_rank, "\n" ,"white piece rank after subtraction:", end_rank - start_rank)
            print("can't move there")
            return False
        '''
    elif cur_player_piece == CHESS_PIECE[Piece.QUEEN.value]:
        pass
    elif cur_player_piece == CHESS_PIECE[Piece.KING.value]:
        pass
    else:
        print("\ninvalid piece --> ", cur_player_piece)

def display_UI(board : dict):
    # Stores the index of the current square the iteration is on
    cur_square = 0

    # Keeps track of which rank the current iteration is on
    cur_rank = 0

    # prints out the row letters for better reading
    for file in FILE_LETTER:
        print("  ", file, end="")

    for square in board:
        # If the current square is divisible by 8, then we drop to the next row
        if cur_square % 8 == 0:
            print() # Prints a new line
            print(RANK_NUM[cur_rank], end=" ") # everytime it goes into a new row, print out the rank number first
            cur_rank += 1 # increment the current rank number by 1

        print(board[square][PieceInfo.PIECE.value], end=" ")
        #print(square, end=" ")
        #print(board)

        cur_square += 1

# Main
def main():
    game_continue = True

    init_chessboard(chessboard)
    init_pieces(chessboard)
    display_UI(chessboard)

    while(game_continue):
        user_piece = str(input("\nchoose your piece: "))

        # Stops program
        if user_piece == "1":
            game_continue = False

        # Check to see if user input is correct and matching any of the keys in the dict
        if user_piece in chessboard:
            # Check to see if the player had chosen a spot that doesn't have a piece on it
            if chessboard[user_piece][PieceInfo.PIECE.value] == square:
                display_UI(chessboard)
                print("\nThere is no piece in that spot, please choose again.")
            else:
                user_decision = str(input("\nwhere does the piece go: "))
                # Check to see if user input is correct and matching any of the keys in the dict
                if user_decision in chessboard:
                    # Checks if the piece chosen does its correct chess movement or not
                    if check_valid_move(chessboard, user_piece, user_piece, user_decision, 1):
                        move_piece("player1", chessboard, user_piece, user_decision)
                        display_UI(chessboard)
                    else:
                        display_UI(chessboard)
                        print("\nInvalid move, please choose a valid spot for the piece.")
                else:
                    display_UI(chessboard)
                    print("\nInvalid input, please choose a valid square to put the piece on")
        else:
            display_UI(chessboard)
            print("\nInvalid input, please choose an existing piece from a valid square")

main()