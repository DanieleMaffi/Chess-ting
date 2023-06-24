import pieces

class Board:
    black_square = pieces.Piece('a', 1, 'black', 'square')
    white_square = pieces.Piece('a', 1, 'white', 'square')
    pawns = [
        pieces.Piece('a', 7, 'black', 'pawn'),
        pieces.Piece('b', 7, 'black', 'pawn'),
        pieces.Piece('c', 7, 'black', 'pawn'),
        pieces.Piece('d', 7, 'black', 'pawn'),
        pieces.Piece('e', 7, 'black', 'pawn'),
        pieces.Piece('f', 7, 'black', 'pawn'),
        pieces.Piece('g', 7, 'black', 'pawn'),
        pieces.Piece('h', 7, 'black', 'pawn'),
        pieces.Piece('a', 2, 'white', 'pawn'),
        pieces.Piece('b', 2, 'white', 'pawn'),
        pieces.Piece('c', 2, 'white', 'pawn'),
        pieces.Piece('d', 2, 'white', 'pawn'),
        pieces.Piece('e', 2, 'white', 'pawn'),
        pieces.Piece('f', 2, 'white', 'pawn'),
        pieces.Piece('g', 2, 'white', 'pawn'),
        pieces.Piece('h', 2, 'white', 'pawn'),
    ]
    knights = [
        pieces.Piece('b', 8, 'black', 'knight'),
        pieces.Piece('g', 8, 'black', 'knight'),
        pieces.Piece('b', 1, 'white', 'knight'),
        pieces.Piece('g', 1, 'white', 'knight'),
    ]
    bishops = [
        pieces.Piece('c', 8, 'black', 'bishop'),
        pieces.Piece('f', 8, 'black', 'bishop'),
        pieces.Piece('c', 1, 'white', 'bishop'),
        pieces.Piece('f', 1, 'white', 'bishop'),
    ]
    rooks = [
        pieces.Piece('a', 8, 'black', 'rook'),
        pieces.Piece('h', 8, 'black', 'rook'),
        pieces.Piece('a', 1, 'white', 'rook'),
        pieces.Piece('h', 1, 'white', 'rook'),
    ]
    kings = [
        pieces.Piece('e', 8, 'black', 'king'),
        pieces.Piece('e', 1, 'white', 'king'),
    ]
    queens = [
        pieces.Piece('d', 8, 'black', 'queen'),
        pieces.Piece('d', 1, 'white', 'queen'),
    ]
    lost_pieces = 0,
    board_string = ""
    letters = "     A      B      C      D      E      F      G      H\n"
    hor_lines = "  --------------------------------------------------------\n"
    ver_line = "|"


    def __init__(self):
        self.board_string =  self.letters + self.hor_lines

    def convert_letter(self, letter):
        match letter:
            case 'a': return 1
            case 'b': return 2
            case 'c': return 3
            case 'd': return 4
            case 'e': return 5
            case 'f': return 6
            case 'g': return 7
            case 'h': return 8

    def convert_number(self, number):
        match number:
            case 1: return 'a'
            case 2: return 'b'
            case 3: return 'c'
            case 4: return 'd'
            case 5: return 'e'
            case 6: return 'f'
            case 7: return 'g'
            case 8: return 'h'


    def check_position(self, x, y):
        x = self.convert_number(x)
        for pawn in self.pawns:
            if pawn.x == x and pawn.y == y:
                return pawn
            
        for knight in self.knights:
            if knight.x == x and knight.y == y:
                return knight

        for bishop in self.bishops:
            if bishop.x == x and bishop.y == y:
                return bishop

        for rook in self.rooks:
            if rook.x == x and rook.y == y:
                return rook

        for king in self.kings:
            if king.x == x and king.y == y:
                return king

        for queen in self.queens:
            if queen.x == x and queen.y == y:
                return queen
            
        x = self.convert_letter(x)
            
        if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):
            return 'black'
        elif (x % 2 == 1 and y % 2 == 0) or (x % 2 == 0 and y % 2 == 1):
            return 'white'

    def print_board(self):
        square_height = 3
        board_height = 8
        board_width = 8
        self.board_string =  self.letters + self.hor_lines

        for i in reversed(range(board_height)):
            for j in range(square_height):
                if j == 1:
                    self.board_string += str(i+1) + self.ver_line
                else:
                    self.board_string += ' ' + self.ver_line
                for k in range(board_width):

                    if type(self.check_position(k+1, i+1)) == str:
                        if self.check_position(k+1, i+1) == 'black':
                            match j:
                                case 0:
                                    self.board_string += self.black_square.type.upper_part
                                case 1:
                                    self.board_string += self.black_square.type.middle_part
                                case 2:
                                    self.board_string += self.black_square.type.lower_part
                        else:
                            match j:
                                case 0:
                                    self.board_string += self.white_square.type.upper_part
                                case 1:
                                    self.board_string += self.white_square.type.middle_part
                                case 2:
                                    self.board_string += self.white_square.type.lower_part                       

                    elif type(self.check_position(k+1, i+1).type) == pieces.Pawn:
                        match j:
                            case 0:
                                self.board_string += self.pawns[0].type.upper_part
                            case 1:
                                self.board_string += self.pawns[0].type.middle_part
                            case 2:
                                self.board_string += self.pawns[0].type.lower_part

                    elif type(self.check_position(k+1, i+1).type) == pieces.Knight:
                        match j:
                            case 0:
                                self.board_string += self.knights[0].type.upper_part
                            case 1:
                                self.board_string += self.knights[0].type.middle_part
                            case 2:
                                self.board_string += self.knights[0].type.lower_part
                    
                    elif type(self.check_position(k+1, i+1).type) == pieces.Bishop:
                        match j:
                            case 0:
                                self.board_string += self.bishops[0].type.upper_part
                            case 1:
                                self.board_string += self.bishops[0].type.middle_part
                            case 2:
                                self.board_string += self.bishops[0].type.lower_part

                    elif type(self.check_position(k+1, i+1).type) == pieces.Rook:
                        match j:
                            case 0:
                                self.board_string += self.rooks[0].type.upper_part
                            case 1:
                                self.board_string += self.rooks[0].type.middle_part
                            case 2:
                                self.board_string += self.rooks[0].type.lower_part
                    
                    elif type(self.check_position(k+1, i+1).type) == pieces.Queen:
                        match j:
                            case 0:
                                self.board_string += self.queens[0].type.upper_part
                            case 1:
                                self.board_string += self.queens[0].type.middle_part
                            case 2:
                                self.board_string += self.queens[0].type.lower_part
                    
                    elif type(self.check_position(k+1, i+1).type) == pieces.King:
                        match j:
                            case 0:
                                self.board_string += self.kings[0].type.upper_part
                            case 1:
                                self.board_string += self.kings[0].type.middle_part
                            case 2:
                                self.board_string += self.kings[0].type.lower_part

                if j == 1:
                    self.board_string += self.ver_line + str(i+1) + '\n'
                else:
                    self.board_string += self.ver_line + ' \n'
        self.board_string += self.hor_lines + self.letters

        print(self.board_string)




"""  A       B       C       D       E       F       G       H
  ------- ------- ------- ------- ------- ------- ------- -------
 | @___@ |  %~b  |  .@.  | \o*o/ | __+__ |  .@.  |  %~b  | @___@ |
8|  @@@  | `'dX  |  @@@  |  @@@  | `@@@' |  @@@  | `'dX  |  @@@  |8
 | d@@@b |  d@@b | ./A\. | d@@@b | d@@@b | ./A\. |  d@@b | d@@@b |
  ------- ------- ------- ------- ------- ------- ------- -------
 |   _   |   _   |   _   |   _   |   _   |   _   |   _   |   _   |
7|  (@)  |  (@)  |  (@)  |  (@)  |  (@)  |  (@)  |  (@)  |  (@)  |7
 |  d@b  |  d@b  |  d@b  |  d@b  |  d@b  |  d@b  |  d@b  |  d@b  |
  ------- ------- ------- ------- ------- ------- ------- -------
 |       | . . . |       | . . . |       | . . . |       | . . . |
6|       | . . . |       | . . . |       | . . . |       | . . . |6
 |       | . . . |       | . . . |       | . . . |       | . . . |
  ------- ------- ------- ------- ------- ------- ------- -------
 | . . . |       | . . . |       | . . . |       | . . . |       |
5| . . . |       | . . . |       | . . . |       | . . . |       |5
 | . . . |       | . . . |       | . . . |       | . . . |       |
  ------- ------- ------- ------- ------- ------- ------- -------
 |       | . . . |       | . . . |       | . . . |       | . . . |
4|       | . . . |       | . . . |       | . . . |       | . . . |4
 |       | . . . |       | . . . |       | . . . |       | . . . |
  ------- ------- ------- ------- ------- ------- ------- -------
 | . . . |       | . . . |       | . . . |       | . . . |       |
3| . . . |       | . . . |       | . . . |       | . . . |       |3
 | . . . |       | . . . |       | . . . |       | . . . |       |
  ------- ------- ------- ------- ------- ------- ------- -------
 |   _   |   _   |   _   |   _   |   _   |   _   |   _   |   _   |
2|  ( )  |  ( )  |  ( )  |  ( )  |  ( )  |  ( )  |  ( )  |  ( )  |2
 |  /_\  |  /_\  |  /_\  |  /_\  |  /_\  |  /_\  |  /_\  |  /_\  |
  ------- ------- ------- ------- ------- ------- ------- -------
 | [___] |  %~\  |  .O.  | \o^o/ | __+__ |  .O.  |  %~\  | [___] |
1|  [ ]  | `')(  |  \ /  |  [ ]  | `. .' |  \ /  | `')(  |  [ ]  |1
 | /___\ |  <__> |  /_\  | /___\ | /___\ |  /_\  |  <__> | /___\ |
  ------- ------- ------- ------- ------- ------- ------- -------
     A       B       C       D       E       F       G       H"""