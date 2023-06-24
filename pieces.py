class Pawn:
    upper_part =  "   _   "
    middle_part = "  (@)  "
    lower_part =  "  d@b  "

    def __init__(self, color):
        if color == 'white' or color == 'black':
            if color == 'black':
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
            if color == 'black':
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
            if color == 'black':
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
            if color == 'black':
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
            if color == 'black':
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
            if color == 'black':
                self.upper_part =  " __+__ "
                self.middle_part = " `. .' "
                self.lower_part =  " /___\ "
        else:
            raise ValueError("Color must be 'white' or 'black'")

class Piece:
    hor_position = 'A'
    ver_position = 1
    color = "white"
    type = Pawn("white")

    def __init__(self, hor_position, ver_position, color, type):
        if hor_position == 'A' or hor_position == 'B' or hor_position == 'C' or hor_position == 'D' or hor_position == 'E' or hor_position == 'F' or hor_position == 'G' or hor_position == 'H' or hor_position == 'H':
            self.hor_position = hor_position
        else:
            raise ValueError("Invalid horizontal position")
        
        if ver_position >= 1 and ver_position <= 8:
            self.ver_position = ver_position
        else:
            raise ValueError("Invalid vertical position")
        
        if type == 'pawn' or type == 'rook' or type == 'knight' or type == 'bishop' or type == 'queen' or type == 'king':
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
        else:
            raise ValueError("Type must be 'pawn', 'rook', 'knight', 'bishop', 'queen', 'king'")