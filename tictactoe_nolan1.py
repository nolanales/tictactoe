#!/usr/bin/env python
# coding: utf-8

# In[2]:


def create_empty_2d_array(rows, columns):
    # fus. to create 2D array of given row and column size, filled in with empty spaces
    empty_array = []
    for _ in range(rows):
        row = []
        for _ in range(columns):
            row.append(' ')
        
        empty_array.append(row)

    return empty_array

# Creating a 2D array with 3 rows and 3 columns
# empty_array = create_empty_2d_array(3, 3)
# print(empty_array)

def print_board(board):
    # fus. to print board based on 2D array board
    for i in board:
        print(" | ".join(i))
        # trying to make the dashes scale with the board size (so we can expand this to a bigger board)
        print("-" * (4 * len(i) - 1))
    
def is_board_full(board):
    # This fus. will return TRUE if all cells on the board are full. We can check this fus. after every turn
# It follows this logic:
#     for row in board:
#         for cell in row:
#             if cell == " ":
#                 return False
#    return True
    return all(cell != ' ' for row in board for cell in row)

    
def make_move(board, row, col, exesandos):
    # fus. will return true if the move executes correctly, or false if it does not
    # board is the 2D array of the board
    # row is the index of the row where the player chooses to play
    # col is the index of the column where the player chooses to play
    # exesandos is either "X", or "O", and is dependent on the player making the current move
    if board[row][col] == " ":
        board[row][col] = exesandos
        return True
    return False
    
def check_win(board, exesandos):
    # The Python all() fus. is pretty cool. It checks the condition to be true of each cell!
    # fus. to check if there is a win after every turn
    # will have to check each row, then each column, then each diagonal to meet all possible conditions
    
    # first up: checking rows
# The following logic is in place in the cleaned-up one line code below:
#     for row in board:
#         for cell in row:
#             if (cell == exesandos):
#                 return True
        for row in board:
            if all(cell == exesandos for cell in row):
                return True
    
    # next up: checking columns
        # len(board[0]) = the number of columns, since board[0] gives the array that makes up the first row
        # col = the index of each column, up to the amount of columns
# The following logic is in place in the cleaned-up one line code below:
#     for col in range(len(board[0])):
#         len(board) = the rows in the array
#         for row in range(len(board)):
#             if (board[row][col] == exesandos):
#                 return True
        for col in range(len(board[0])):
            if all(board[row][col] == exesandos for row in range(len(board))):
                return True    
    
    # finally: checking diagonals
    # first checking normal diagonal
    # basically checking (1,1),(2,2),(3,3)
    # for loop limited by the min of either the rows of columns, so that it accomidates diff. board sizes
# The following logic is in place in the cleaned-up one line code below:   
#     for i in range(min(len(board), len(board[0]))):
#         if (board[i][i] == exesandos):
#             return True
    # now checking the opposite diagonal
# The following logic is in place in the cleaned-up one line code below:
#     for i in range(min(len(board), len(board[0]))):
#         will check for board[first row][last column of the first row -1 - the index (starting at 0)]
#         if (board[i][len(board[0] - 1 - i)] == exesandos):
#             return True
        if all(board[i][i] == exesandos for i in range(min(len(board), len(board[0])))) or                 all(board[i][len(board[0]) - 1 - i] == exesandos for i in range(min(len(board), len(board[0])))):
            return True

        return False
    
def main():
    # get number of desired rows and columns
    rows = int(input("Please enter the desired number of rows: "))
    columns = int(input("Please enter the desired number of columns: "))
    
    # print board
    board = create_empty_2d_array(rows, columns)
    
    # set variables
    # the first player will be X, so we can set that now such that it is always first
    # set a bool to be false all game, until at the end it is set to true
    current_player = "X"
    game_over = False
    
    while game_over != True:
        # print the board using print_board fus.
        print_board(board)
        
        # for each move, change the current row and col
        # some weird indexing since python is 0 indexed
        row = int(input(f"Player {current_player}, enter row (0-{rows-1}): "))
        col = int(input(f"Player {current_player}, enter column (0-{columns-1}): "))
        
        # first, check if you just got a valid input! Again, weird python indexing here with row < rows!
        if 0 <= row < rows and 0 <= col < columns:
            # if the move is in bounds, 
            if make_move(board, row, col, current_player) == True:
                if check_win(board, current_player) == True:
                    print_board(board)
                    print(f"Player {current_player} wins!")
                    game_over = True
                elif is_board_full(board):
                    print_board(board)
                    print("It's a tie!")
                    game_over = True
                else:
                    # switch players
                    if current_player == "X":
                        current_player = "O"
                    else:
                        current_player = "X"
            else:
                print("Cell already taken. Try again.")
        else:
            print(f"Invalid input. Row and column must be in the range (0-{rows-1}) and (0-{cols-1}). Try again.")
                    
if __name__ == "__main__":
    main()


# 
