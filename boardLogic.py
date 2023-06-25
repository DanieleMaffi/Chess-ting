import pieces

class Board:
    white_territory = []
    black_territory = []
    turn = 'white'
    black_square = pieces.Piece('a', 1, 'black', 'square', 0)
    white_square = pieces.Piece('a', 1, 'white', 'square', 1)
    pawns = [
        pieces.Piece('a', 7, 'black', 'pawn', 0),
        pieces.Piece('b', 7, 'black', 'pawn', 1),
        pieces.Piece('c', 7, 'black', 'pawn', 2),
        pieces.Piece('d', 7, 'black', 'pawn', 3),
        pieces.Piece('e', 7, 'black', 'pawn', 4),
        pieces.Piece('f', 7, 'black', 'pawn', 5),
        pieces.Piece('g', 7, 'black', 'pawn', 6),
        pieces.Piece('h', 7, 'black', 'pawn', 7),
        pieces.Piece('a', 2, 'white', 'pawn', 8),
        pieces.Piece('b', 2, 'white', 'pawn', 9),
        pieces.Piece('c', 2, 'white', 'pawn', 10),
        pieces.Piece('d', 2, 'white', 'pawn', 11),
        pieces.Piece('e', 2, 'white', 'pawn', 12),
        pieces.Piece('f', 2, 'white', 'pawn', 13),
        pieces.Piece('g', 2, 'white', 'pawn', 14),
        pieces.Piece('h', 2, 'white', 'pawn', 15),
    ]
    knights = [
        pieces.Piece('b', 8, 'black', 'knight', 0),
        pieces.Piece('g', 8, 'black', 'knight', 1),
        pieces.Piece('b', 1, 'white', 'knight', 2),
        pieces.Piece('g', 1, 'white', 'knight', 3),
    ]
    bishops = [
        pieces.Piece('c', 8, 'black', 'bishop', 0),
        pieces.Piece('f', 8, 'black', 'bishop', 1),
        pieces.Piece('c', 1, 'white', 'bishop', 2),
        pieces.Piece('f', 1, 'white', 'bishop', 3),
    ]
    rooks = [
        pieces.Piece('a', 8, 'black', 'rook', 0),
        pieces.Piece('h', 8, 'black', 'rook', 1),
        pieces.Piece('a', 1, 'white', 'rook', 2),
        pieces.Piece('h', 1, 'white', 'rook', 3),
    ]
    kings = [
        pieces.Piece('e', 8, 'black', 'king', 0),
        pieces.Piece('e', 1, 'white', 'king', 1),
    ]
    queens = [
        pieces.Piece('d', 8, 'black', 'queen', 0),
        pieces.Piece('d', 1, 'white', 'queen', 1),
    ]
    lost_pieces = 0,
    board_string = ""
    letters = "     A      B      C      D      E      F      G      H\n"
    hor_lines = "  --------------------------------------------------------\n"
    ver_line = "|"


    def __init__(self):
        self.board_string =  self.letters + self.hor_lines

    def swap_turns(self):
        if self.turn == 'white':
            self.turn = 'black'
        else:
            self.turn = 'white'

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

    def __str__(self):
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
                                self.board_string += self.pawns[self.check_position(k+1, i+1).position].type.upper_part
                            case 1:
                                self.board_string += self.pawns[self.check_position(k+1, i+1).position].type.middle_part
                            case 2:
                                self.board_string += self.pawns[self.check_position(k+1, i+1).position].type.lower_part

                    elif type(self.check_position(k+1, i+1).type) == pieces.Knight:
                        match j:
                            case 0:
                                self.board_string += self.knights[self.check_position(k+1, i+1).position].type.upper_part
                            case 1:
                                self.board_string += self.knights[self.check_position(k+1, i+1).position].type.middle_part
                            case 2:
                                self.board_string += self.knights[self.check_position(k+1, i+1).position].type.lower_part
                    
                    elif type(self.check_position(k+1, i+1).type) == pieces.Bishop:
                        match j:
                            case 0:
                                self.board_string += self.bishops[self.check_position(k+1, i+1).position].type.upper_part
                            case 1:
                                self.board_string += self.bishops[self.check_position(k+1, i+1).position].type.middle_part
                            case 2:
                                self.board_string += self.bishops[self.check_position(k+1, i+1).position].type.lower_part

                    elif type(self.check_position(k+1, i+1).type) == pieces.Rook:
                        match j:
                            case 0:
                                self.board_string += self.rooks[self.check_position(k+1, i+1).position].type.upper_part
                            case 1:
                                self.board_string += self.rooks[self.check_position(k+1, i+1).position].type.middle_part
                            case 2:
                                self.board_string += self.rooks[self.check_position(k+1, i+1).position].type.lower_part
                    
                    elif type(self.check_position(k+1, i+1).type) == pieces.Queen:
                        match j:
                            case 0:
                                self.board_string += self.queens[self.check_position(k+1, i+1).position].type.upper_part
                            case 1:
                                self.board_string += self.queens[self.check_position(k+1, i+1).position].type.middle_part
                            case 2:
                                self.board_string += self.queens[self.check_position(k+1, i+1).position].type.lower_part
                    
                    elif type(self.check_position(k+1, i+1).type) == pieces.King:
                        match j:
                            case 0:
                                self.board_string += self.kings[self.check_position(k+1, i+1).position].type.upper_part
                            case 1:
                                self.board_string += self.kings[self.check_position(k+1, i+1).position].type.middle_part
                            case 2:
                                self.board_string += self.kings[self.check_position(k+1, i+1).position].type.lower_part

                if j == 1:
                    self.board_string += self.ver_line + str(i+1) + '\n'
                else:
                    self.board_string += self.ver_line + ' \n'
        self.board_string += self.hor_lines + self.letters

        return self.board_string
    
    def available_moves(self, piece):
        available_moves = []
        x = self.convert_letter(piece.x)
        y = piece.y
        if type(piece.type) == pieces.Bishop:
            for i in range(1, 8):
                if x+i == 9 or y+i == 9: break
                available_moves.append([x+i, y+i])
                if type(self.check_position(x+i, y+i)) == pieces.Piece:
                    break
            for i in range(1, 8):
                if x-i == 0 or y+i == 9: break
                available_moves.append([x-i, y+i])
                if type(self.check_position(x-i, y+i)) == pieces.Piece:
                    break
            for i in range(1, 8):
                if x-i == 0 or y-i == 0: break
                available_moves.append([x-i, y-i])
                if type(self.check_position(x-i, y-i)) == pieces.Piece:
                    break
            for i in range(1, 8):
                if x+i == 9 or y-i == 0: break
                available_moves.append([x+i, y-i])
                if type(self.check_position(x+i, y-i)) == pieces.Piece:
                    break

        if type(piece.type) == pieces.Rook:
            for i in range(1, 8):
                if x+i == 9: break
                available_moves.append([x+i, y])
                if type(self.check_position(x+i, y)) == pieces.Piece:
                    break
            for i in range(1, 8):
                if x-i == 0: break
                available_moves.append([x-i, y])
                if type(self.check_position(x-i, y)) == pieces.Piece:
                    break
            for i in range(1, 8):
                if y-i == 0: break
                available_moves.append([x, y-i])
                if type(self.check_position(x, y-i)) == pieces.Piece:
                    break
            for i in range(1, 8):
                if y+i == 9: break
                available_moves.append([x, y+i])
                if type(self.check_position(x, y+i)) == pieces.Piece:
                    break

        if type(piece.type) == pieces.Queen:
            for i in range(1, 8):
                if x+i == 9: break
                available_moves.append([x+i, y])
                if type(self.check_position(x+i, y)) == pieces.Piece:
                    break
            for i in range(1, 8):
                if x-i == 0: break
                available_moves.append([x-i, y])
                if type(self.check_position(x-i, y)) == pieces.Piece:
                    break
            for i in range(1, 8):
                if y-i == 0: break
                available_moves.append([x, y-i])
                if type(self.check_position(x, y-i)) == pieces.Piece:
                    break
            for i in range(1, 8):
                if y+i == 9: break
                available_moves.append([x, y+i])   
                if type(self.check_position(x, y+i)) == pieces.Piece:
                    break
            for i in range(1, 8):
                if x+i == 9 or y+i == 9: break
                available_moves.append([x+i, y+i])
                if type(self.check_position(x+i, y+i)) == pieces.Piece:
                    break
            for i in range(1, 8):
                if x-i == 0 or y+i == 9: break
                available_moves.append([x-i, y+i])
                if type(self.check_position(x-i, y+i)) == pieces.Piece:
                    break
            for i in range(1, 8):
                if x-i == 0 or y-i == 0: break
                available_moves.append([x-i, y-i])
                if type(self.check_position(x-i, y-i)) == pieces.Piece:
                    break
            for i in range(1, 8):
                if x+i == 9 or y-i == 0: break
                available_moves.append([x+i, y-i])  
                if type(self.check_position(x+i, y-i)) == pieces.Piece:
                    break

        if type(piece.type) == pieces.King:
            if self.turn == "white":
                territory = self.black_territory
            else:
                territory = self.white_territory
            
            moves = [[x, y+1], [x, y-1], [x+1, y], [x-1, y], [x+1, y+1], [x-1, y-1], [x+1, y-1], [x-1, y+1]]
            to_remove = []
            for move in moves:
                if move in territory:
                    to_remove.append(move)
                    continue
                if move[0] < 1 or move[1] < 1 or move[0] > 8 or move[1] > 8:
                    to_remove.append(move)

            for move in to_remove:
                moves.remove(move)
                
            available_moves = moves

        return available_moves
    
    
    def update_territory(self, color):
        territory = []

        for pawn in self.pawns:
            if pawn.color == "white" and color == "white" and pawn.x != "dead":
                territory.append([self.convert_letter(pawn.x)+1, pawn.y+1])
                territory.append([self.convert_letter(pawn.x)-1, pawn.y+1])
        for pawn in self.pawns:
            if pawn.color == "black" and color == "black" and pawn.x != "dead":
                territory.append([self.convert_letter(pawn.x)+1, pawn.y-1])
                territory.append([self.convert_letter(pawn.x)-1, pawn.y-1])

        for knight in self.knights:
            if knight.color == color and knight.x != "dead":
                territory.append([self.convert_letter(knight.x)+1, knight.y+2])
                territory.append([self.convert_letter(knight.x)+1, knight.y-2])
                territory.append([self.convert_letter(knight.x)-1, knight.y-2])
                territory.append([self.convert_letter(knight.x)-1, knight.y+2])
                territory.append([self.convert_letter(knight.x)+2, knight.y+1])
                territory.append([self.convert_letter(knight.x)-2, knight.y-1])
                territory.append([self.convert_letter(knight.x)+2, knight.y-1])
                territory.append([self.convert_letter(knight.x)-2, knight.y+1])

        for bishop in self.bishops:
            if bishop.color == color and bishop.x != "dead":
                territory.extend(self.available_moves(bishop))

        for rook in self.rooks:
            if rook.color == color and rook.x != "dead":
                territory.extend(self.available_moves(rook))
        
        for queen in self.queens:
            if queen.color == color and queen.x != "dead":
                territory.extend(self.available_moves(queen))

        for king in self.kings:
            if king.color == color:
                territory.extend(self.available_moves(king))

        to_remove = []  
        for array in territory:
            if array == []:
                to_remove.append(array)
                continue
            if array[0] < 1 or array[1] < 1 or array[0] > 8 or array[1] > 8:
                to_remove.append(array)

        for array in to_remove:
                territory.remove(array)

        if color == 'white':
            self.white_territory = territory
        else:
            self.black_territory = territory
        return

    def is_check(self):
        king = self.kings[0] #black king
        if self.turn == "white":
            territory = self.black_territory
            king = self.kings[1]
        else:
            territory = self.white_territory

        if [self.convert_letter(king.x), king.y] in territory:
            available = self.available_moves(king)
            to_remove = []
            for move in available:
                if type(self.check_position(move[0], move[1])) != str:
                    if self.check_position(move[0], move[1]).color == self.turn:
                        to_remove.append(move)
            for move in to_remove:
                available.remove(move)
            if available == []:
                raise Exception("Check mate!")
            else:
                return True
        return False


    def check_block(self, x, y, new_x, new_y):
        if type(self.check_position(x, y).type)  == pieces.Pawn:
            pawn = self.check_position(x, y)
            if self.turn == 'white':
                if new_x == x and new_y > y and new_y <= y+2:
                    if not pawn.type.first_move and new_y == y+2: 
                        return False
                    if type(self.check_position(new_x, new_y)) == pieces.Piece:
                        return False
                    new_x = self.convert_number(new_x)
                    self.pawns[pawn.position].x = new_x
                    self.pawns[pawn.position].y = new_y
                    old_black = self.black_territory
                    old_white = self.white_territory
                    self.update_territory('black')
                    self.update_territory('white')
                    check = self.is_check()
                    self.pawns[pawn.position].x = self.convert_number(x)
                    self.pawns[pawn.position].y = y
                    self.white_territory = old_white
                    self.black_territory = old_black
                    return not check
            else:
                if new_x == x and new_y < y and new_y >= y-2:
                    if not pawn.type.first_move and new_y == y-2: 
                        return False
                    if type(self.check_position(new_x, new_y)) == pieces.Piece:
                        return False
                    new_x = self.convert_number(new_x)
                    self.pawns[pawn.position].x = new_x
                    self.pawns[pawn.position].y = new_y
                    old_black = self.black_territory
                    old_white = self.white_territory
                    self.update_territory('black')
                    self.update_territory('white')
                    check = self.is_check()
                    self.pawns[pawn.position].x = self.convert_number(x)
                    self.pawns[pawn.position].y = y
                    self.white_territory = old_white
                    self.black_territory = old_black
                    return not check
            return False
        
        if type(self.check_position(x, y).type)  == pieces.Knight:
                knight = self.check_position(x, y)
                new_pos = self.check_position(new_x, new_y)
                if ((new_x == x+1 or new_x == x-1) and (y+2 == new_y or y-2 == new_y)) or ((x+2 == new_x or x-2 == new_x) and (y+1 == new_y or y-1 == new_y)):
                    if type(new_pos) == pieces.Piece and new_pos.color == self.turn:
                        return False
                    new_x = self.convert_number(new_x)
                    self.knights[knight.position].x = new_x
                    self.knights[knight.position].y = new_y
                    old_black = self.black_territory
                    old_white = self.white_territory
                    self.update_territory('black')
                    self.update_territory('white')
                    check = self.is_check()
                    self.knights[knight.position].x = self.convert_number(x)
                    self.knights[knight.position].y = y
                    self.white_territory = old_white
                    self.black_territory = old_black
                    return not check
                return False
        
        if type(self.check_position(x, y).type)  == pieces.Bishop:
                bishop = self.check_position(x, y)
                new_pos = self.check_position(new_x, new_y)
                available_moves = self.available_moves(bishop)
                if ([new_x, new_y] in available_moves):
                    if type(new_pos) == pieces.Piece and new_pos.color == self.turn:
                        return False
                    new_x = self.convert_number(new_x)
                    self.bishops[bishop.position].x = new_x
                    self.bishops[bishop.position].y = new_y
                    old_black = self.black_territory
                    old_white = self.white_territory
                    self.update_territory('black')
                    self.update_territory('white')
                    check = self.is_check()
                    self.bishops[bishop.position].x = self.convert_number(x)
                    self.bishops[bishop.position].y = y
                    self.white_territory = old_white
                    self.black_territory = old_black
                    return not check
                return False
        
        if type(self.check_position(x, y).type)  == pieces.Rook:
                rook = self.check_position(x, y)
                new_pos = self.check_position(new_x, new_y)
                available_moves = self.available_moves(rook)
                
                if ([new_x, new_y] in available_moves):
                    if type(new_pos) == pieces.Piece and new_pos.color == self.turn:
                        return False
                    new_x = self.convert_number(new_x)
                    self.rooks[rook.position].x = new_x
                    self.rooks[rook.position].y = new_y
                    old_black = self.black_territory
                    old_white = self.white_territory
                    self.update_territory('black')
                    self.update_territory('white')
                    check = self.is_check()
                    self.rooks[rook.position].x = self.convert_number(x)
                    self.rooks[rook.position].y = y
                    self.white_territory = old_white
                    self.black_territory = old_black
                    return not check
                return False
        
        if type(self.check_position(x, y).type)  == pieces.Queen:
                queen = self.check_position(x, y)
                new_pos = self.check_position(new_x, new_y)
                available_moves = self.available_moves(queen)
                if ([new_x, new_y] in available_moves):
                    if type(new_pos) == pieces.Piece and new_pos.color == self.turn:
                        return False
                    new_x = self.convert_number(new_x)
                    self.queens[queen.position].x = new_x
                    self.queens[queen.position].y = new_y
                    old_black = self.black_territory
                    old_white = self.white_territory
                    self.update_territory('black')
                    self.update_territory('white')
                    check = self.is_check()
                    self.queens[queen.position].x = self.convert_number(x)
                    self.queens[queen.position].y = y
                    self.white_territory = old_white
                    self.black_territory = old_black
                    return not check
                return False


    def move_piece(self, x, y, new_x, new_y):
        x = self.convert_letter(x)
        new_x = self.convert_letter(new_x)

        if type(self.check_position(x, y))  == str:
            return "There is no piece at that position\n"
        
        if self.turn == 'white' and self.check_position(x, y).color == 'black':
            return "You cannot move black's pieces\n"
        
        if self.turn == 'black' and self.check_position(x, y).color == 'white':
            return "You cannot move white's pieces\n"
        
        if self.is_check() and type(self.check_position(x, y).type) != pieces.King:
            if not self.check_block(x, y, new_x, new_y):
                return "You have to move the king first or block the check\n"
            
        if not self.check_block(x, y, new_x, new_y) and type(self.check_position(x, y).type) != pieces.King:
            return "You cannot move that piece!\n"
        
        if type(self.check_position(x, y).type)  == pieces.Pawn:
            pawn = self.check_position(x, y)
            if self.turn == 'white':
                if new_x == x and new_y > y and new_y <= y+2:
                    if not pawn.type.first_move and new_y == y+2: 
                        return "You can't move a pawn two squares two times\n"
                    if type(self.check_position(new_x, new_y)) == pieces.Piece:
                        return "There is already a piece at that position\n"
                    new_x = self.convert_number(new_x)
                    self.pawns[pawn.position].x = new_x
                    self.pawns[pawn.position].y = new_y
                    self.pawns[pawn.position].type.first_move = False
                    self.update_territory(self.turn)
                    self.swap_turns()
                    self.is_check()
                    return "You moved a pawn\n"
                elif (x+1 == new_x or x-1 == new_x) and y+1 == new_y and type(self.check_position(new_x, new_y)) == pieces.Piece:
                    new_pos = self.check_position(new_x, new_y)
                    new_x = self.convert_number(new_x)
                    self.pawns[pawn.position].x = new_x
                    self.pawns[pawn.position].y = new_y
                    if type(new_pos) != str:
                        new_pos.x = 'dead'
                        new_pos.y = 0
                    self.update_territory(self.turn)
                    self.swap_turns()
                    self.is_check()
                    return "Got it\n"
            else:
                if new_x == x and new_y < y and new_y >= y-2:
                    if not pawn.type.first_move and new_y == y-2: 
                        return "You can't move a pawn two squares two times\n"
                    if type(self.check_position(new_x, new_y)) == pieces.Piece:
                        return "There is already a piece at that position\n"
                    new_x = self.convert_number(new_x)
                    self.pawns[pawn.position].x = new_x
                    self.pawns[pawn.position].y = new_y
                    self.pawns[pawn.position].type.first_move = False
                    self.update_territory(self.turn)
                    self.swap_turns()
                    self.is_check()
                    return "You moved a pawn\n"
                elif (x+1 == new_x or x-1 == new_x) and y-1 == new_y and type(self.check_position(new_x, new_y)) == pieces.Piece:
                    new_pos = self.check_position(new_x, new_y)
                    new_x = self.convert_number(new_x)
                    self.pawns[pawn.position].x = new_x
                    self.pawns[pawn.position].y = new_y
                    if type(new_pos) != str:
                        new_pos.x = 'dead'
                        new_pos.y = 0
                    self.update_territory(self.turn)
                    self.swap_turns()
                    self.is_check()
                    return "Got it\n"
            return "You can't move a pawn there\n"
        
        if type(self.check_position(x, y).type)  == pieces.Knight:
                knight = self.check_position(x, y)
                new_pos = self.check_position(new_x, new_y)
                if ((new_x == x+1 or new_x == x-1) and (y+2 == new_y or y-2 == new_y)) or ((x+2 == new_x or x-2 == new_x) and (y+1 == new_y or y-1 == new_y)):
                    if type(new_pos) == pieces.Piece and new_pos.color == self.turn:
                        return f"There is already a piece at that position\n"
                    new_x = self.convert_number(new_x)
                    self.knights[knight.position].x = new_x
                    self.knights[knight.position].y = new_y
                    if type(new_pos) != str:
                        new_pos.x = 'dead'
                        new_pos.y = 0
                    self.update_territory(self.turn)
                    self.swap_turns()
                    self.is_check()
                    return "You moved a horse\n"
                return "You can't move a horsy there\n"
        
        if type(self.check_position(x, y).type)  == pieces.Bishop:
                bishop = self.check_position(x, y)
                new_pos = self.check_position(new_x, new_y)
                available_moves = self.available_moves(bishop)
                if ([new_x, new_y] in available_moves):
                    if type(new_pos) == pieces.Piece and new_pos.color == self.turn:
                        return f"There is already a piece at that position\n"
                    new_x = self.convert_number(new_x)
                    self.bishops[bishop.position].x = new_x
                    self.bishops[bishop.position].y = new_y
                    if type(new_pos) != str:
                        new_pos.x = 'dead'
                        new_pos.y = 0
                    self.update_territory(self.turn)
                    self.swap_turns()
                    self.is_check()
                    return "You moved a bishop\n"
                return f"You can't move a bishop there\n"
        
        if type(self.check_position(x, y).type)  == pieces.Rook:
                rook = self.check_position(x, y)
                new_pos = self.check_position(new_x, new_y)
                available_moves = self.available_moves(rook)
                
                if ([new_x, new_y] in available_moves):
                    if type(new_pos) == pieces.Piece and new_pos.color == self.turn:
                        return f"There is already a piece at that position\n"
                    new_x = self.convert_number(new_x)
                    self.rooks[rook.position].x = new_x
                    self.rooks[rook.position].y = new_y
                    if type(new_pos) != str:
                        new_pos.x = 'dead'
                        new_pos.y = 0
                    self.update_territory(self.turn)
                    self.swap_turns()
                    self.is_check()
                    return "You moved a rook\n"
                return f"You can't move a rook there\n"
        
        if type(self.check_position(x, y).type)  == pieces.Queen:
                queen = self.check_position(x, y)
                new_pos = self.check_position(new_x, new_y)
                available_moves = self.available_moves(queen)
                if ([new_x, new_y] in available_moves):
                    if type(new_pos) == pieces.Piece and new_pos.color == self.turn:
                        return f"There is already a piece at that position\n"
                    new_x = self.convert_number(new_x)
                    self.queens[queen.position].x = new_x
                    self.queens[queen.position].y = new_y
                    if type(new_pos) != str:
                        new_pos.x = 'dead'
                        new_pos.y = 0
                    self.update_territory(self.turn)
                    self.swap_turns()
                    self.is_check()
                    return "You moved the queen\n"
                return f"You can't move the queen there\n"
        
        if type(self.check_position(x, y).type)  == pieces.King:
                king = self.check_position(x, y)
                new_pos = self.check_position(new_x, new_y)
                available_moves = self.available_moves(king)
                if ([new_x, new_y] in available_moves):
                    if type(new_pos) == pieces.Piece and new_pos.color == self.turn:
                        return f"There is already a piece at that position\n"
                    new_x = self.convert_number(new_x)
                    self.kings[king.position].x = new_x
                    self.kings[king.position].y = new_y
                    if type(new_pos) != str:
                        new_pos.x = 'dead'
                        new_pos.y = 0
                    self.update_territory(self.turn)
                    self.swap_turns()
                    self.is_check()
                    return "You moved the king\n"
                return f"You can't move the king there\n"