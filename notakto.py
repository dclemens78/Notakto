# Author : Danny Clemens

# notakto.py


"""

This program uses tkinter to create a working 
game of notakto. Notakto is an impartial misere game that
is similar to tic tac toe, in that is played on a 3x3 board.
The key difference is that both players moves are represented with X, 
and if 3 X's occur in a row on your turn, you lose.


For this program, we will use a 5x5 board to make the game more fun.

"""


from tkinter import *


"""

Global Variables

GAME_STATE     : Tracks every move that has been made
Current_PLAYER : Tracks which player's turn it is

"""

CURRENT_PLAYER = "Player One"

GAME_STATE = ["-", "-", "-", "-", "-",
              "-", "-", "-", "-", "-",
              "-", "-", "-", "-", "-",
              "-", "-", "-", "-", "-",
              "-", "-", "-", "-", "-"]


def main():
    
    # The main window is created here
    root = Tk()
    root.title("Notakto!")

    # this method essentially creates the board
    button_container = create_buttons(root)

    root.mainloop()
    # closes the window


def button_clicked(button, game_state_idx, turn_label):
    """ this method is run when a button is clicked. This is the programs driver method. """
    global GAME_STATE

    # Puts a game piece (blue X) on the button that was clicked
    button.configure(state=DISABLED, text="X", font="bold")
    button.configure(disabledforeground="blue")

    
    # Add X to the correct index of GAME_STATE to show a move was made there
    GAME_STATE[game_state_idx] = "X"
    change_turn(turn_label)

    
    
    


def change_turn(turn_label):
    """ This method is responsible for changing the label at the bottom """
    
    global CURRENT_PLAYER
    CURRENT_PLAYER = "Player Two" if CURRENT_PLAYER == "Player One" else "Player One"

    
    if is_game_over() == True:
        turn_label.configure(text=f"{CURRENT_PLAYER} Wins!")
    else:
        turn_label.configure(text=f"{CURRENT_PLAYER}'s Turn")



def is_game_over():
    """ This method checks every possible win to see if the game has been won yet """

    # horizontel wins
    if GAME_STATE[0] == "X" and GAME_STATE[1] == "X" and GAME_STATE[2] == "X" and GAME_STATE[3] == "X" and GAME_STATE[4] == "X":
        return True
    elif GAME_STATE[5] == "X" and GAME_STATE[6] == "X" and GAME_STATE[7] == "X" and GAME_STATE[8] == "X" and GAME_STATE[9] == "X":
        return True
    elif GAME_STATE[10] == "X" and GAME_STATE[11] == "X" and GAME_STATE[12] == "X" and GAME_STATE[13] == "X" and GAME_STATE[14] == "X":
        return True
    elif GAME_STATE[15] == "X" and GAME_STATE[16] == "X" and GAME_STATE[17] == "X" and GAME_STATE[18] == "X" and GAME_STATE[19] == "X":
        return True
    elif GAME_STATE[20] == "X" and GAME_STATE[21] == "X" and GAME_STATE[22] == "X" and GAME_STATE[23] == "X" and GAME_STATE[24] == "X":
        return True



    # verticle wins
    if GAME_STATE[0] == "X" and GAME_STATE[5] == "X" and GAME_STATE[10] == "X" and GAME_STATE[15] == "X" and GAME_STATE[20] == "X":
        return True
    elif GAME_STATE[1] == "X" and GAME_STATE[6] == "X" and GAME_STATE[11] == "X" and GAME_STATE[16] == "X" and GAME_STATE[21] == "X":
        return True
    elif GAME_STATE[2] == "X" and GAME_STATE[7] == "X" and GAME_STATE[12] == "X" and GAME_STATE[17] == "X" and GAME_STATE[22] == "X":
        return True
    elif GAME_STATE[3] == "X" and GAME_STATE[8] == "X" and GAME_STATE[13] == "X" and GAME_STATE[18] == "X" and GAME_STATE[23] == "X":
        return True
    elif GAME_STATE[4] == "X" and GAME_STATE[9] == "X" and GAME_STATE[14] == "X" and GAME_STATE[19] == "X" and GAME_STATE[24] == "X":
        return True



    # diagnoal wins
    if GAME_STATE[0] == "X" and GAME_STATE[6] == "X" and GAME_STATE[12] == "X" and GAME_STATE[18] == "X" and GAME_STATE[24] == "X":
        return True
    elif GAME_STATE[4] == "X" and GAME_STATE[8] == "X" and GAME_STATE[12] == "X" and GAME_STATE[16] == "X" and GAME_STATE[20] == "X":
        return True
    

    return False


def create_buttons(root):

    ''' 

    Creates and displays each individual button 
    To avoid complicating the program, I manually
    created and displayed each button


    KEY (btn_0_0): 
        btn = button
        first 0 = row number
        second 0 = column number
        this is to help me when I grid them



    button_containter is used to store each button I create

    this is so that a specific button that is clicked changes
    
    '''

    turn_label = Label(root, text=f"{CURRENT_PLAYER}'s turn", font="Helvetica 14 bold", width=35, borderwidth=5)
    turn_label.grid(row=5, column=1, columnspan=3, padx=10, pady=10)


    button_container = []

    # First we create all 25 buttons

    # ROW 1

    btn_0_0 = Button(root, text="", padx=60, pady=40, command=lambda : button_clicked(button_container[0], 0, turn_label))
    button_container.append(btn_0_0)

    btn_0_1 = Button(root, text="", padx=60, pady=40, command=lambda : button_clicked(button_container[1], 1, turn_label))
    button_container.append(btn_0_1)

    btn_0_2 = Button(root, text="", padx=60, pady=40, command=lambda : button_clicked(button_container[2], 2, turn_label))
    button_container.append(btn_0_2)

    btn_0_3 = Button(root, text="", padx=60, pady=40, command=lambda : button_clicked(button_container[3], 3, turn_label))
    button_container.append(btn_0_3)

    btn_0_4 = Button(root, text="", padx=60, pady=40, command=lambda : button_clicked(button_container[4], 4, turn_label))
    button_container.append(btn_0_4)



    # ROW 2

    btn_1_0 = Button(root, text="", padx=60, pady=40, command=lambda : button_clicked(button_container[5], 5, turn_label))
    button_container.append(btn_1_0)

    btn_1_1 = Button(root, text="", padx=60, pady=40, command=lambda : button_clicked(button_container[6], 6, turn_label))
    button_container.append(btn_1_1)

    btn_1_2 = Button(root, text="", padx=60, pady=40, command=lambda : button_clicked(button_container[7], 7, turn_label))
    button_container.append(btn_1_2)

    btn_1_3 = Button(root, text="", padx=60, pady=40, command=lambda : button_clicked(button_container[8], 8, turn_label))
    button_container.append(btn_1_3)

    btn_1_4 = Button(root, text="", padx=60, pady=40, command=lambda : button_clicked(button_container[9], 9, turn_label))
    button_container.append(btn_1_4)



    # ROW 3

    btn_2_0 = Button(root, text="", padx=60, pady=40, command=lambda : button_clicked(button_container[10], 10, turn_label))
    button_container.append(btn_2_0)

    btn_2_1 = Button(root, text="", padx=60, pady=40, command=lambda : button_clicked(button_container[11], 11, turn_label))
    button_container.append(btn_2_1)

    btn_2_2 = Button(root, text="", padx=60, pady=40, command=lambda : button_clicked(button_container[12], 12, turn_label))
    button_container.append(btn_2_2)

    btn_2_3 = Button(root, text="", padx=60, pady=40, command=lambda : button_clicked(button_container[13], 13, turn_label))
    button_container.append(btn_2_3)

    btn_2_4 = Button(root, text="", padx=60, pady=40, command=lambda : button_clicked(button_container[14], 14, turn_label))
    button_container.append(btn_2_4)



    # ROW 4

    btn_3_0 = Button(root, text="", padx=60, pady=40, command=lambda : button_clicked(button_container[15], 15, turn_label))
    button_container.append(btn_3_0)

    btn_3_1 = Button(root, text="", padx=60, pady=40, command=lambda : button_clicked(button_container[16], 16, turn_label))
    button_container.append(btn_3_1)

    btn_3_2 = Button(root, text="", padx=60, pady=40, command=lambda : button_clicked(button_container[17], 17, turn_label))
    button_container.append(btn_3_2)

    btn_3_3 = Button(root, text="", padx=60, pady=40, command=lambda : button_clicked(button_container[18], 18, turn_label))
    button_container.append(btn_3_3)

    btn_3_4 = Button(root, text="", padx=60, pady=40, command=lambda : button_clicked(button_container[19], 19, turn_label))
    button_container.append(btn_3_4)



    # ROW 5

    btn_4_0 = Button(root, text="", padx=60, pady=40, command=lambda : button_clicked(button_container[20], 20, turn_label))
    button_container.append(btn_4_0)

    btn_4_1 = Button(root, text="", padx=60, pady=40, command=lambda : button_clicked(button_container[21], 21, turn_label))
    button_container.append(btn_4_1)

    btn_4_2 = Button(root, text="", padx=60, pady=40, command=lambda : button_clicked(button_container[22], 22, turn_label))
    button_container.append(btn_4_2)

    btn_4_3 = Button(root, text="", padx=60, pady=40, command=lambda : button_clicked(button_container[23], 23, turn_label))
    button_container.append(btn_4_3)

    btn_4_4 = Button(root, text="", padx=60, pady=40, command=lambda : button_clicked(button_container[24], 24, turn_label))
    button_container.append(btn_4_4)



    # We then grid each individual button onto the window
    # We do this row by row from top to bottom

    btn_0_0.grid(row=0, column=0)
    btn_0_1.grid(row=0, column=1)
    btn_0_2.grid(row=0, column=2)
    btn_0_3.grid(row=0, column=3)
    btn_0_4.grid(row=0, column=4)

    btn_1_0.grid(row=1, column=0)
    btn_1_1.grid(row=1, column=1)
    btn_1_2.grid(row=1, column=2)
    btn_1_3.grid(row=1, column=3)
    btn_1_4.grid(row=1, column=4)

    btn_2_0.grid(row=2, column=0)
    btn_2_1.grid(row=2, column=1)
    btn_2_2.grid(row=2, column=2)
    btn_2_3.grid(row=2, column=3)
    btn_2_4.grid(row=2, column=4)

    btn_3_0.grid(row=3, column=0)
    btn_3_1.grid(row=3, column=1)
    btn_3_2.grid(row=3, column=2)
    btn_3_3.grid(row=3, column=3)
    btn_3_4.grid(row=3, column=4)

    btn_4_0.grid(row=4, column=0)
    btn_4_1.grid(row=4, column=1)
    btn_4_2.grid(row=4, column=2)
    btn_4_3.grid(row=4, column=3)
    btn_4_4.grid(row=4, column=4)

    # Now the window should display a 5x5 board, each space being a button



if __name__ == "__main__":
    main()
