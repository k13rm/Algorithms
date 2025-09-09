BOARD_SIZE = 7

board = [['-' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# [['X', 'X', 'X', 'X', 'X']
#  ['-', '-', '-', '-', '-']
#  ['-', '-', '-', '-', '-']
#  ['-', '-', '-', '-', '-']
#  ['-', '-', '-', '-', '-']]

board[6][0] = "X"
board[5][1] = "X"
board[4][2] = "X"
board[3][3] = "X"
board[2][4] = "X"
board[1][5] = "X"
board[0][6] = "X"


# [(0,0), (0,1), (0,2), (0,3), (0,4)],
# current_player = "X"

# Goal (1): given the current player as input, return True, if all the numbers in row 0 are equal to the current player, otherwise, return False.

# Goal (2): given the current player as input, return True if all the numbers in at least one of rows is equal to the current player, otherwise, return False.

# Goal (3): given the current player as input, return True if all the numbers in at least one of the rows or one of the columns is equal to the current player, otherwise, return False.

# Goal (4): create a new function iswinner_short and make it such that it can do the exact same thing as the iswinner2 function, but with a maximum of 2 for loops.


def is_winner(current_player):

    count = 0   
    for i in range(BOARD_SIZE):
        if board[0][i] == current_player:
            # print(f"Row {j} has an {current_player} in column {i}")
            count += 1      
    
    if count == BOARD_SIZE:
        return True
    else:
        return False



def is_winner2(current_player):
    
    # The Flag Trick
    false2 = 0
    for j in range (BOARD_SIZE): # number of rows
        
        false1 = 0
        for i in range(BOARD_SIZE): # number of columns
            
            # check the row
            if board[j][i] != current_player:
                false1 += 1
            
            # check the column
            if board[i][j] != current_player:
                false1 += 1
            
            if false1 == 2:
                break

            if false1 < 2: 
                return True

        if board[j][j] != current_player:
                false2 += 1
            
        if board[BOARD_SIZE - 1 - j][j] != current_player:
                false2 += 1

    if false2 < 2: 
        return True
            
    
    return False


# (BOARD_SIZE - 1 - 0, 0) ( , r)
# (BOARD_SIZE - 1 - 1, 1)
# (BOARD_SIZE - 1 - 2, 2)
# (BOARD_SIZE - 1 - 3, 3)
# ....
# (0, BOARD_SIZE - 1)

    

print(is_winner2("X"))


        # [0, BOARD_SIZE - 1]

