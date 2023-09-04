import pieces
import boardLogic
import os
import sys

board = boardLogic.Board()

print(board)


while(1):
    while(True):
        try:
            x, y = input("Select the piece you want to move: ").split()
        except:
            print("Invalid piece, try again")
            continue
        break

    if x == 'exit':
        break

    while(True):
        try:
            new_x, new_y = input("Select the new position: ").split()
        except:
            print("Invalid position, try again")
            continue
        break

    if x == "O-O" or x == "O-O-O":
        result = board.castle(x)
    else: 
        result = board.move_piece(x, int(y), new_x, int(new_y))

    #clear console
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"It's {board.turn}'s turn")
    print(board)
    print(result)
