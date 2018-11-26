from Direction import *
import copy

class Base:

    def __init__(self, parent, state, move, pathCost):
        self.parent = parent       
        self.state = state
        self.lastMove = move
        self.pathCost = pathCost

    def move(self, move):
        x, y = self.getBlankPosition()
        array = copy.deepcopy(self.state)
        if(move == Direction(1)):
            array[x][y], array[x - 1][y] = array[x - 1][y], array[x][y]
        if(move == Direction(2)):
            array[x][y], array[x + 1][y] = array[x + 1][y], array[x][y]
        if(move == Direction(3)):
            array[x][y - 1], array[x][y] = array[x][y], array[x][y - 1]
        if(move == Direction(4)):
            array[x][y + 1], array[x][y] = array[x][y], array[x][y + 1]           
        return array

    def getBlankPosition(self):
            for x in self.state:
                if(0 in x):
                    posx = self.state.index(x)
                    posy = x.index(0)
                    return posx, posy

    def getValidMoves(self):
        x, y = self.getBlankPosition()
        rows = len(self.state)
        cols = len(self.state[0])
        moves = []
        if(x > 0):
            moves.append(Direction(1))
        if(x < rows - 1):
            moves.append(Direction(2))
        if(y > 0):
            moves.append(Direction(3))
        if(y < cols - 1):
            moves.append(Direction(4))
        return moves

    def getOrderedMoves(self, strategy):
        moves = self.getValidMoves()
        ordered = []
        for sign in strategy:
            for move in moves:
                if(sign == str(move)):
                    ordered.append(move)
        return ordered

    def getPath(self):
        path = ''
        if(self.parent == None):
            return path
        path += self.parent.getPath() + str(self.lastMove)
        return path


