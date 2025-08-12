BOARD_SIZE = 7

board = [['-' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# [['X', 'X', 'X', 'X', 'X']
#  ['-', '-', '-', '-', '-']
#  ['-', '-', '-', '-', '-']
#  ['-', '-', '-', '-', '-']
#  ['-', '-', '-', '-', '-']]

board[0][0] = "X"
board[0][1] = "X"
board[0][2] = "X"
board[0][3] = "X"
board[0][4] = "X"
board[0][5] = "X"
board[0][6] = "X"


# [(0,0), (0,1), (0,2), (0,3), (0,4)],
# current_player = "X"

# Goal (1): given the current player as input, return True, if all the numbers in row 0 are equal to the current player, otherwise, return False.

# Goal (2): given the current player as input, return True if all the numbers in at least one of rows is equal to the current player, otherwise, return False.

def is_winner(current_player):

    for j in range(BOARD_SIZE):

        count = 0   
        for i in range(BOARD_SIZE):
            if board[j][i] == current_player:
                # print(f"Row {j} has an {current_player} in column {i}")
                count += 1      
        
        if count == BOARD_SIZE:
            return True
        else:
            return False


    
print(is_winner("X"))


        # [0, BOARD_SIZE - 1]

