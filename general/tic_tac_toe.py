import tkinter as tk


root = tk.Tk()

root.title("Tic Tac Toe")

for i in range(3): # [0, 1, 2]
    root.rowconfigure(i, weight=1)
    root.columnconfigure(i, weight=1)


# Front End: what the user sees
# Back  End: what the user does not see, and is important for the game logic

board = [
    ['-', '-', '-'], 
    ['-', '-', '-'], 
    ['-', '-', '-']
]

message_label = tk.Label(root, text=f"", font=('Arial', 16))
message_label.grid(row=3, column=0, columnspan=3)

current_player = "X"
message_label.config(text=f"Player X's turn")

all_buttons = []
for i in range(3): # rows
    row_buttons = []
    for j in range(3): # column
        button = tk.Button(root, text='-', width=5, height=2, font=('Arial', 24))
        # this makes sure when the button is clicked, it calls the button_click function with the correct row, column, and button
        button.config(command=lambda r=i, c=j, b=button: button_click(r, c, b))
        
        # this makes sure the button is placed in the correct row and column on the board
        button.grid(row=i, column=j, sticky='nsew')

        row_buttons.append(button)
    all_buttons.append(row_buttons)

def is_winner(current_player): # either X or O
    
    # for i in range(3):
    #     for j in range(3):
    #         if board[i][j] != current_player:

    if (board[0][0] == board[0][1]) and (board[0][1] == board[0][2]) and (board[0][0] == current_player):
        return True
    
    if (board[1][0] == board[1][1]) and (board[1][1] == board[1][2]) and (board[1][0] == current_player):
        return True
    
    if (board[2][0] == board[2][1]) and (board[2][1] == board[2][2]) and (board[2][0] == current_player):
        return True
    
    if (board[0][0] == board[1][0]) and (board[1][0] == board[2][0]) and (board[0][0] == current_player):
        return True    
    
    if (board[0][1] == board[1][1]) and (board[1][1] == board[2][1]) and (board[0][1] == current_player):
        return True    

    if (board[0][2] == board[1][2]) and (board[1][2] == board[2][2]) and (board[0][2] == current_player):
        return True

    if (board[0][0] == board[1][1]) and (board[1][1] == board[2][2]) and (board[0][0] == current_player):
        return True    

    if (board[0][2] == board[1][1]) and (board[1][1] == board[2][0]) and (board[0][2] == current_player):
        return True    
    
    return False


    # [ [(0,0), (0,1), (0,2)],] 
    #   [(1,0), (1,1), (1,2)],
    #   [(2,0), (2,1), (2,2)] ]
    
    # [ ['-', '-', '-'],] 
    #   ['-', '-', '-'],
    #   ['-', '-', '-'] ]

def button_click(row, col, button):
    
    global current_player

    if board[row][col] == '-':
        if current_player == "X":
            board[row][col] = "X"
            button.config(text="X")

            if is_winner("X"):
                message_label.config(text="Player X wins!")
                return

            current_player = "O"
            message_label.config(text="Player O's turn")
        else:
            board[row][col] = "O"
            button.config(text="O")
            if is_winner("O"):
                message_label.config(text="Player O wins!")
                return
            
            current_player = "X"
            message_label.config(text="Player X's turn")


reset_button = tk.Button(root, text="Reset", width=10, height=2, font=('Arial', 16))
reset_button.grid(row=4, column=0, columnspan=3)
reset_button.config(command=lambda: reset_board())

def reset_board():
    global current_player, board
    current_player = "X"
    message_label.config(text="Player X's turn")

    for i in range(3):
        for j in range(3):
            board[i][j] = '-'
            all_buttons[i][j].config(text='-')

root.mainloop()
