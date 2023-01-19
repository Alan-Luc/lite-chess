from piece import Piece
from board import Board

class Pawn(Piece):
    def __init__(self, color, typeOfPiece, pos):
        super().__init__(color, typeOfPiece, pos)
        self.pos = pos
        self.color = color

    # TODO: en passant
    # and another elif for promotion


    def isMoveValid(self, newPos):
        # validity check for if move is within the board
        if newPos[0] > 7 or newPos[0] < 0:
            return False
        if newPos[1] > 7 or newPos[1] < 0:
            return False

        #self.pos = (6, 1) = (B, 2)
        startPos = {"b": 2, "w": 6}
        newRow = newPos[0]
        rowDiff = newPos[0] - self.pos[0]
        col = self.pos[1]
        validCol = (col-1, col, col+1)

        if self.color == "b":

            # for reg movement
            if rowDiff < 0:
                return False

            # at starting position
            if self.pos[0] == startPos[self.color]:
                if self.color == "b":
                    # black pawns can only move down
                    if rowDiff <= 2 and newPos[1] == col:
                        return True
                    else:
                        return False

            # also reg movement
            if rowDiff == 1:
                # move piece forward, not at starting postion
                if newPos[1] == col:
                    if Board[newPos[0]][newPos[1]] != "":
                         return False
                    else:
                        return True
                # pawn can move diagonally if it is capturing a piece
                if col == 0:
                    if newPos[1] in validCol[1:]:
                        if Board[newRow][validCol[1]] != "" or Board[newRow][validCol[2]] != "":
                            return True
                        else:
                            return False
                if col == 7:
                    if newPos[1] in validCol[:2]:
                        if Board[newRow][validCol[0]] != "" or Board[newRow][validCol[1]] != "":
                            return True
                        else:
                            return False

                if Board[newPos[0]][col-1] != "" or Board[newPos[0]][col+1] != "":
                     return True
                else:
                    return False




        elif self.color == "w":
            # for reg movement
            if rowDiff > 0:
                return False

            # at starting position
            if self.pos[0] == startPos[self.color]:
                if self.color == "w":
                    # black pawns can only move down
                    if rowDiff >= -2 and newPos[1] == col:
                        return True
                    else:
                        return False

            # also reg movement
            if rowDiff == -1:
                # move piece forward, not at starting postion
                if newPos[1] == col:
                    if Board[newPos[0]][newPos[1]] != "":
                         return False
                    else:
                        return True
                # pawn can move diagonally if it is capturing a piece
                if col == 0:
                    if newPos[1] in validCol[1:]:
                        if Board[newRow][validCol[1]] != "" or Board[newRow][validCol[2]] != "":
                            return True
                        else:
                            return False
                if col == 7:
                    if newPos[1] in validCol[:2]:
                        if Board[newRow][validCol[0]] != "" or Board[newRow][validCol[1]] != "":
                            return True
                        else:
                            return False

                if Board[newRow][col-1] != "" or Board[newRow][col+1] != "":
                     return True
                else:
                    return False
