from Base import *
from Direction import *
from queue import Queue
from time import *

class BFS:

    frontier = Queue()
    explored = {}

    def __init__(self, start, target, strategy):
        self.target = target
        self.start = Base(None, start, Direction(5), 0)
        self.strategy = strategy
        self.maxDepth = 0
        if(self.start.state != self.target):
            self.frontier.put(self.start.state)
            self.explored[str(self.start.state)] = self.start

    def solve(self):
        startTime = time()
        while(self.frontier.qsize() > 0):
            currentState = self.frontier.get()
            currentStateString = currentState.__str__() 
            currentState = self.explored[currentStateString]
            moves = currentState.getOrderedMoves(self.strategy)
            for move in moves:
                newArray = currentState.move(move)  
                newCost = currentState.pathCost + 1
                newMove = move
                newState = Base(currentState, newArray, newMove, newCost)
                newStateString = newArray.__str__()
                if(newStateString not in self.explored):
                    self.frontier.put(newArray)
                    self.explored[newStateString] = newState
                    if(newCost > self.maxDepth):
                        self.maxDepth = newCost
                    if(newArray == self.target):
                        solvingTime = time() - startTime
                        solved = round(solvingTime, 3)
                        path = newState.getPath()
                        explored = (len(self.explored) + 1)
                        frontier = len(self.explored) - self.frontier._qsize()
                        return path, explored, frontier, self.maxDepth, solved
        solvingTime = time() - startTime
        solved = round(solvingTime, 3)
        explored = (len(self.explored) + 1)
        frontier = len(self.explored) - len(self.frontier)
        return -1, explored, frontier, self.maxDepth + 1, solved