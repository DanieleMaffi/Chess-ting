import pieces
import boardLogic
import os

board = boardLogic.Board()

print(board)

while(1):


    x, y = input("Select the piece you want to move: ").split()
    new_x, new_y = input("Select the new position: ").split()

    result = board.move_piece(x, int(y), new_x, int(new_y))

    #clear console
    os.system('cls' if os.name == 'nt' else 'clear')

    print(result)
    print(f"It's {board.turn}'s turn")
    print(board)
