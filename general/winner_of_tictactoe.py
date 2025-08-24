BOARD_SIZE = 7

board = [['-' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# [['X', 'X', '-', 'X', 'X']
#  ['-', '-', '-', '-', '-']
#  ['-', '-', '-', '-', '-']
#  ['-', '-', '-', '-', '-']
#  ['-', '-', '-', '-', '-']]

board[4][0] = "X"
board[4][1] = "X"
board[4][2] = "X"
board[4][3] = "X"
board[4][4] = "X"
board[4][5] = "X"
board[4][6] = "X"


# [(0,0), (0,1), (0,2), (0,3), (0,4)],
# current_player = "X"

# Goal (1): given the current player as input, return True, if all the numbers in row 0 are equal to the current player, otherwise, return False.

# Goal (2): given the current player as input, return True if all the numbers in at least one of rows is equal to the current player, otherwise, return False.

# Goal (3): given the current player as input, return True if all the numbers in at least one of the rows or one of the columns is equal to the current player, otherwise, return False.

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
    
    return False


    

print(is_winner2("X"))


        # [0, BOARD_SIZE - 1]

