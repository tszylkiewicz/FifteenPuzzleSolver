from Base import *
from Direction import *
from time import *

class DFS:

    frontier = []
    explored = {}

    def __init__(self, start, target, strategy):
        self.target = target      
        self.start = Base(None, start, Direction(5), 0)
        self.strategy = strategy
        self.maxDepth = 19
        if(self.start.state != self.target):
            self.frontier.append(self.start.state)
            self.explored[str(self.start.state)] = self.start
            

    def solve(self):
        startTime = time()
        while(len(self.frontier) > 0):
            currentState = self.frontier.pop()  
            currentStateString = currentState.__str__() 
            currentState = self.explored[currentStateString]              
            if (currentState.pathCost <= self.maxDepth):
                moves = currentState.getOrderedMoves(self.strategy)
                moves.reverse()
                for move in moves:  
                    newArray = currentState.move(move)  
                    newCost = currentState.pathCost + 1
                    newMove = move
                    newState = Base(currentState, newArray, newMove, newCost)
                    newStateString = newArray.__str__()
                    if(newStateString not in self.explored):
                        self.frontier.append(newArray)
                        self.explored[newStateString] = newState
                        if(newArray == self.target):
                            solvingTime = time() - startTime
                            solved = round(solvingTime, 3)
                            path = newState.getPath()
                            explored = (len(self.explored) + 1)
                            frontier = len(self.explored) - len(self.frontier)
                            return path, explored, frontier, self.maxDepth, solved                               
                    if(newStateString in self.explored):
                        oldCost = self.explored[newStateString].pathCost                                       
                        if (newCost < oldCost):
                            if ((oldCost - newCost) >= 1):
                                self.frontier.append(newArray)       
        solvingTime = time() - startTime
        solved = round(solvingTime, 3)
        explored = (len(self.explored) + 1)
        frontier = len(self.explored) - len(self.frontier)
        return -1, explored, frontier, self.maxDepth + 1, solved

