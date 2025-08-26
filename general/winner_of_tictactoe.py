BOARD_SIZE = 7

board = [['-' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# [['X', 'X', '-', 'X', 'X']
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
board[0][6] = "O"


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
    for j in range (BOARD_SIZE): # number of rows
        
        # let's now check if row j has all the elements equal to current_player
        flag = True
        for i in range(BOARD_SIZE): # number of columns
            if board[j][i] != current_player:
                flag = False
                break
        if flag == True: 
            # this means that row j has all the elements equal to current_player
            return True
            
   
    for k in range (BOARD_SIZE): # number of columns
        
        flag = True
        for l in range(BOARD_SIZE): # number of rows
            if board[l][k] != current_player:
                flag = False
                break
        if flag == True: 
            
            return True
    
    flag = True
    for k in range(BOARD_SIZE):

        if board[k][k] != current_player:
            flag = False
            break
        
    if flag == True:
        return True
    
    flag = True    
    for r in range(BOARD_SIZE):

        col = r
        row = BOARD_SIZE - 1 - r

        if board[BOARD_SIZE - 1 - r][r] != current_player:
            flag = False
            break

    if flag == True:
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

