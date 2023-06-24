class Square:
    upper_part =  "       "
    middle_part = "       "
    lower_part =  "       "

    def __init__(self, color):
        if color == 'white' or color == 'black':
            if color == 'white':
                self.upper_part =  " . . . "
                self.middle_part = " . . . "
                self.lower_part =  " . . . "
        else:
            raise ValueError("Color must be 'white' or 'black'")
        

class Pawn:
    upper_part =  "   _   "
    middle_part = "  (@)  "
    lower_part =  "  d@b  "
    first_move = True

    def __init__(self, color):
        if color == 'white' or color == 'black':
            if color == 'white':
                self.middle_part = "  ( )  "
                self.lower_part =  "  /_\  "
        else:
            raise ValueError("Color must be 'white' or 'black'")
        
class Knight:
    upper_part =  "  %~b  "
    middle_part = " `'dX  "
    lower_part =  "  d@@b "

    def __init__(self, color):
        if color == 'white' or color == 'black':
            if color == 'white':
                self.upper_part =  "  %~\  "
                self.middle_part = " `')(  "
                self.lower_part =  "  <__> "
        else:
            raise ValueError("Color must be 'white' or 'black'")  

class Rook:
    upper_part =  " @___@ "
    middle_part = "  @@@  "
    lower_part =  " d@@@b "

    def __init__(self, color):
        if color == 'white' or color == 'black':
            if color == 'white':
                self.upper_part =  " [___] "
                self.middle_part = "  [ ]  "
                self.lower_part =  " /___\ "
        else:
            raise ValueError("Color must be 'white' or 'black'")

class Bishop:
    upper_part =  "  .@.  "
    middle_part = "  @@@  "
    lower_part =  " ./A\. "

    def __init__(self, color):
        if color == 'white' or color == 'black':
            if color == 'white':
                self.upper_part =  "  .O.  "
                self.middle_part = "  \ /  "
                self.lower_part =  "  /_\  "
        else:
            raise ValueError("Color must be 'white' or 'black'")

class Queen:
    upper_part =  " \o*o/ "
    middle_part = "  @@@  "
    lower_part =  " d@@@b "

    def __init__(self, color):
        if color == 'white' or color == 'black':
            if color == 'white':
                self.upper_part =  " \o^o/ "
                self.middle_part = "  [ ]  "
                self.lower_part =  " /___\ "
        else:
            raise ValueError("Color must be 'white' or 'black'")      

class King:
    upper_part =  " __+__ "
    middle_part = " `@@@' "
    lower_part =  " d@@@b "

    def __init__(self, color):
        if color == 'white' or color == 'black':
            if color == 'white':
                self.upper_part =  " __+__ "
                self.middle_part = " `. .' "
                self.lower_part =  " /___\ "
        else:
            raise ValueError("Color must be 'white' or 'black'")

class Piece:
    x = None
    y = None
    color = None
    type = None

    def __init__(self, x, y, color, type, position):
        if (x == 'a' or x == 'b' or x == 'c' or x == 'd' or x == 'e' or 
            x == 'f' or x == 'g' or x == 'h'):
            self.x = x
        else:
            raise ValueError("Invalid horizontal position")
        
        if color == 'white' or color == 'black':
            self.color = color
        else: raise ValueError("Invalid color")
        
        if y >= 1 and y <= 8:
            self.y = y
        else:
            raise ValueError("Invalid vertical position")
        
        if type == 'pawn' or type == 'rook' or type == 'knight' or type == 'bishop' or type == 'queen' or type == 'king' or type == 'square':
            match type:
                case 'pawn':
                    self.type = Pawn(color)
                case 'rook':
                    self.type = Rook(color)
                case 'knight':
                    self.type = Knight(color)
                case 'bishop':
                    self.type = Bishop(color)
                case 'queen':
                    self.type = Queen(color)
                case 'king':
                    self.type = King(color)
                case 'square':
                    self.type = Square(color)
        else:
            raise ValueError("Type must be 'pawn', 'rook', 'knight', 'bishop', 'queen', 'king'")
        
        self.position = position