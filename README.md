# Notakto

Notakto is an impartial combinatorial game similar to tic-tac-toe in that they are played on the same board.

Rules:

1. Both player's moves are represented with 'X'
2. This version is played on a 5x5 tic-tac-toe board
3. If you create 5 X's in a row (horizontely, verticaly, diagonaly) on your turn, you lose
4. You can not skip a turn

This game was implemented with python's tkinter library. Each space that can be moved to is a button, so the overall board contains 25 buttons. There is also a label at the bottom that tracks the players turn and displays which player wins when they win.

A list is used to represent the game state. If a player clicks button 5, the lists 4th index is altered to show a move was made there

For the win condition, every possible win is checked. If the game state matches a possible win, the game is over.
