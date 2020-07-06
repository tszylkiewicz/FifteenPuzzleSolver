from Base import *
from Direction import *
from time import time
from math import ceil

class AStar:

    frontier = {}
    explored = {}

    def __init__(self, start, target, strategy):
        self.target = target
        self.strategy = strategy
        self.start = Base(None, start, Direction(5), 0)
        self.maxDepth = 0
        self.rows = len(start)
        self.columns = len(start[0])
        if(self.start.state != self.target):
            if(self.strategy == 'manh'):
                distance = self.Manhattan(self.start.state)
            elif(self.strategy == 'hamm'):
                distance = self.Hamming(self.start.state)        
            self.frontier.setdefault(distance, []).append(self.start.state)
            self.explored[str(self.start.state)] = self.start     

    def Manhattan(self, state):     
        distance = 0
        for x in state:
            for y in x:                
                if(y != 0):
                    temp = y % self.columns
                    if(temp == 0):
                        temp = self.columns
                    distance += abs((state.index(x) + 1) - ceil(y / self.rows)) + abs((x.index(y) + 1) - temp)
        return distance 

    def Hamming(self, state):
        distance = 0
        for x in state:
            for y in x:                
                if(y != 0):
                    temp = y % self.columns
                    if(temp == 0):
                        temp = self.columns
                    if(((state.index(x) + 1) != ceil(y / self.rows)) or ((x.index(y) + 1) != temp)):
                        distance += 1
        return distance

    def solve(self):
        startTime = time()
        while(len(self.frontier) > 0):
            closest = min(self.frontier)
            currentState = self.frontier[closest].pop(0)
            if(len(self.frontier[closest]) == 0):
                del(self.frontier[closest])
            currentStateString = currentState.__str__()
            currentState = self.explored[currentStateString]
            moves = currentState.getValidMoves()
            for move in moves:
                newArray = currentState.move(move)  
                newCost = currentState.pathCost + 1
                newMove = move
                newState = Base(currentState, newArray, newMove, newCost)
                newStateString = newArray.__str__()
                if(newStateString not in self.explored):
                    self.explored[newStateString] = newState    
                    if(newCost > self.maxDepth):
                        self.maxDepth = newCost
                    if(newArray == self.target):
                        solvingTime = time() - startTime
                        solved = round(solvingTime, 3)
                        path = newState.getPath()
                        explored = (len(self.explored) + 1)
                        frontier = len(self.explored) - len(self.frontier)
                        return path, explored, frontier, self.maxDepth, solved
                    if(self.strategy == 'manh'):
                        distance = self.Manhattan(newArray)
                    elif(self.strategy == 'hamm'):
                        distance = self.Hamming(newArray)
                    if(distance not in self.frontier):
                        self.frontier.setdefault(distance, []).append(newArray)
                    else:
                        self.frontier[distance].append(newArray)