# Tictactoe Mini Project (Medium)
"""

## Instructions

1) Create a list of board. This list should contain 3 list that has 3 empty spaces inside it to represent 3x3 board.
2) Create a board printing function which parses board and prints out tictactoe layout.
3) Create a move function which takes x,y cooridantes and replace board list with given mark if its not occupied.
4) Take names for player and randomly select who starting. Starter takes mark "x".
5) Create a turn counter with 0 and a loop with each turn increasing it to 1 until the limit 9.
6) Each turn player makes a move and replace an empty tile with their designated marks.
7) Craate a checkwin function where it looks board for 8 possible win moves. 3 horizontal, 3 vertical, 2 diagonal same marks.
8) After the end of each turn board state checked for win.
9) After 9 turns if no winner call it draw.

      |     |     
   -  |  -  |  -  
 _____|_____|_____
      |     |     
   -  |  -  |  -  
 _____|_____|_____
      |     |     
   -  |  -  |  -  
      |     |     


## Needed Skills:
- Input
- Conditionals
- Complex Lists
- While
- Functions
- Flags
"""

import random


def print_board(current_board):
  print("-----" + "|" + "-----" + "|" + "-----")
  #   -  |  -  |  -
  for k in range(3):
    print("  " + current_board[k][0] + "  " + "|" + "  " +
          current_board[k][1] + "  " + "|" + "  " + current_board[k][2] + "  ")

    print("-----" + "|" + "-----" + "|" + "-----")


# input("Where do you want to place your 'O' ")

# 3) Create a move function which takes x,y cooridantes and replace board list with given mark if its not occupied.



def move(current_board, x, y, mark):
  while current_board[y][x] != '-':
    print("You cannot use that there")
    coord = input("Give x and y:")
    x = int(coord[0])
    y = int(coord[1])
  current_board[y][x] = mark
  return current_board


# 7) Create a checkwin function where it looks board for 8 possible win moves. 3 horizontal, 3 vertical, 2 diagonal with the same marks.
def check_winner(current_board):
  print("Checking the winner...")
  if (current_board[0][2] == current_board[1][2]) and (
      current_board[0][2]
      == current_board[2][2]) and current_board[0][2] != "-":
    print("We have a winner!")
    return True
  elif (current_board[0][1] == current_board[1][1]) and (
      current_board[0][1]
      == current_board[2][1]) and current_board[0][1] != "-":
    print("We have a winner!")
    return True
  elif (current_board[0][0] == current_board[1][0]) and (
      current_board[0][0]
      == current_board[2][0]) and current_board[0][0] != "-":
    print("We have a winner!")
    return True
  elif (current_board[0][0] == current_board[0][1]) and (
      current_board[0][0]
      == current_board[0][2]) and current_board[0][0] != "-":
    print("We have a winner!")
    return True
  elif (current_board[1][0] == current_board[1][1]) and (
      current_board[1][0]
      == current_board[1][2]) and current_board[1][0] != "-":
    print("We have a winner!")
    return True
  elif (current_board[2][0] == current_board[2][1]) and (
      current_board[2][0]
      == current_board[2][2]) and current_board[2][0] != "-":
    print("We have a winner!")
    return True
  elif (current_board[0][0] == current_board[1][1]) and (
      current_board[0][0]
      == current_board[2][2]) and current_board[0][0] != "-":
    print("We have a winner!")
    return True
  elif (current_board[2][0] == current_board[1][1]) and (
      current_board[0][0]
      == current_board[0][2]) and current_board[0][0] != "-":
    print("We have a winner!")
    return True
  return False


# 3 Horizontal
#"02, 12, 22"  "01, 11, 21"  "00, 10, 20"
# 3 Vertical
#"00, 01, 02"  "10, 11, 12"  "20, 21, 22"
# 2 Diagonal
#"00, 11, 22"  "20, 11, 02"
"""
      |     |     
   00 |  10 |  20  
 _____|_____|_____
      |     |     
  01  | 11  |  21  
 _____|_____|_____
      |     |     
  02  | 12  |  22  
      |     |     
"""


def tic_tac_toe():

  board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

  current_player_id = random.randint(0, 1)

  names = ["Kerem", "Rıdvan"]

  marks = ["X", "O"]

  win = False

  for i in range(9):
    print("Player-", names[current_player_id], "is playing with mark ",
          marks[current_player_id])
    coord = input("Give x and y:")
    x_coord = int(coord[0])
    y_coord = int(coord[1])

    # HW: Check why the winner is not displayed and game is not finished
    board = move(board, x_coord, y_coord, marks[current_player_id])
    win = check_winner(board)
    print_board(board)
    if win == True:
      break
    if current_player_id == 0:
      current_player_id = 1
    elif current_player_id == 1:
      current_player_id = 0

  # p1_name = "Kerem"  #input("What is P1's me/nickname?")
  # p2_name = "Rıdvan"  #input("What is P2's name/nickname?")
  # names = [p1_name, p2_name]

  # player = random.randint(1, 2)

  # win = False  #check_winner(board) # True/False

  # m = "O"
  # m2 = "X"

  # while not win:
  #   print("Player-n is playing!")
  #   coord = input("Give x and y:")
  #   x_coord = int(coord[0])
  #   y_coord = int(coord[1])

  #   board = move(board, x_coord, y_coord, m)
  #   win = check_winner(board)
  #   print_board(board)


tic_tac_toe()

# Try to solve the occupied place problem

# REMAINDERS
# Functions: In order to define a function you need to use 'def' keyword
# Functions: you need to use '()' for arguments

