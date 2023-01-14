class Piece:
    def __init__(self, color, type_of_piece, pos):
        self.color = color
        self.type_of_piece = type_of_piece
        self.pos = pos

    def move(self, newPos, is_valid):
        if is_valid:
            self.pos = newPos
