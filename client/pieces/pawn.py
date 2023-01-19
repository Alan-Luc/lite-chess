from piece import Piece

class Pawn(Piece):
    def __init__(self, color, typeOfPiece, pos):
        super().__init__(color, typeOfPiece, pos)
        self.pos = pos
        self.color = color

        #current position
        #new position
        #if new position is valid then current position = new pos

    def isMoveValid(self, newPos):
        #self.pos = (6, 1) (B, 2)
        startPos = {"b": 2, "w": 6}
        if self.color == "b":
            diff = newPos[0] - self.pos[0]
            if diff < 0:
                return False
            else:
                return 0


        if self.pos[0] == startPos[self.color]:
            if self.color == "b":
                return 0





    